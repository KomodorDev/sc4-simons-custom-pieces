"""Stage and fetch an installer ZIP using a private Dropbox App Folder."""
from __future__ import annotations

import argparse
from base64 import urlsafe_b64encode
from dataclasses import dataclass, field
from getpass import GetPassWarning, getpass
from hashlib import sha256
import http.client
import json
import math
import os
from pathlib import Path
import re
import secrets
import stat
import subprocess
import sys
import tempfile
import time
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import HTTPRedirectHandler, Request, build_opener
import warnings


DEFAULT_CREDENTIALS = Path.home() / ".config/scp/release-dropbox.json"
APP_KEY_ENV = "SCP_DROPBOX_APP_KEY"
REFRESH_TOKEN_ENV = "SCP_DROPBOX_REFRESH_TOKEN"
SCOPES = "files.metadata.read files.content.read"
TOKEN_URL = "https://api.dropboxapi.com/oauth2/token"
METADATA_URL = "https://api.dropboxapi.com/2/files/get_metadata"
DOWNLOAD_URL = "https://content.dropboxapi.com/2/files/download"
BLOCK_SIZE = 4 * 1024 * 1024
JSON_LIMIT = 64 * 1024
DIGEST = re.compile(r"[0-9a-f]{64}")
ARCHIVE_NAME = re.compile(r"[A-Za-z0-9][A-Za-z0-9._-]{0,199}\.zip")


class DropboxError(ValueError):
    """A sanitized transport or configuration error."""


class DropboxNotFound(DropboxError):
    """The expected file is absent from the app folder."""


class _RetryableDropboxError(DropboxError):
    def __init__(self, message, retry_after=5):
        super().__init__(message)
        self.retry_after = retry_after


class _NoRedirect(HTTPRedirectHandler):
    def redirect_request(self, req, fp, code, msg, headers, newurl):
        # Credentials and file downloads belong to the exact Dropbox endpoints.
        return None


_OPENER = build_opener(_NoRedirect())


def _opaque(value):
    return (isinstance(value, str) and bool(value) and value.isascii()
            and all("!" <= char <= "~" for char in value))


@dataclass(frozen=True)
class DropboxCredentials:
    app_key: str = field(repr=False)
    refresh_token: str = field(repr=False)

    def __post_init__(self):
        if (not isinstance(self.app_key, str) or re.fullmatch(r"[A-Za-z0-9_-]+", self.app_key) is None
                or not _opaque(self.refresh_token)):
            raise DropboxError("Dropbox app key or refresh token is missing or invalid.")


def _credentials_path(path):
    path = Path(path).expanduser().absolute()
    if path.is_symlink():
        raise DropboxError("The Dropbox credentials file must be a regular local file.")
    path = path.parent.resolve() / path.name
    cloud_roots = ((Path.home() / "Library/CloudStorage").resolve(), (Path.home() / "Dropbox").resolve())
    if any(path.is_relative_to(root) for root in cloud_roots) or any(
            (parent / ".git").exists() for parent in path.parents):
        raise DropboxError("Keep the Dropbox credentials file outside Git and synced folders.")
    return path


def load_local_credentials(path=DEFAULT_CREDENTIALS):
    path = _credentials_path(path)
    try:
        descriptor = os.open(path, os.O_RDONLY | getattr(os, "O_NOFOLLOW", 0) | getattr(os, "O_NONBLOCK", 0))
        with os.fdopen(descriptor, "rb") as stream:
            mode = os.fstat(stream.fileno()).st_mode
            if not stat.S_ISREG(mode) or (os.name != "nt" and mode & 0o077):
                raise DropboxError("Dropbox credentials need a regular file with permissions 0600.")
            value = _json_object(stream.read(JSON_LIMIT + 1))
    except OSError:
        raise DropboxError("Cannot read local Dropbox credentials. Run the authorize command first.") from None
    return DropboxCredentials(value.get("app_key"), value.get("refresh_token"))


def _runner_credentials():
    if not os.environ.get(APP_KEY_ENV) or not os.environ.get(REFRESH_TOKEN_ENV):
        raise DropboxError(f"Configure the protected GitHub environment secrets {APP_KEY_ENV} and {REFRESH_TOKEN_ENV}.")
    return DropboxCredentials(os.environ[APP_KEY_ENV], os.environ[REFRESH_TOKEN_ENV])


def _json_object(raw):
    if not raw or len(raw) > JSON_LIMIT:
        raise DropboxError("Dropbox metadata or credentials are missing or too large.")
    try:
        value = json.loads(raw)
    except (ValueError, UnicodeError):
        raise DropboxError("Dropbox metadata or credentials are invalid.") from None
    if not isinstance(value, dict):
        raise DropboxError("Dropbox metadata or credentials are invalid.")
    return value


def _open(request, operation, timeout, *, allow_missing=False):
    try:
        return _OPENER.open(request, timeout=timeout)
    except HTTPError as error:
        with error:
            if allow_missing and error.code == 409:
                response = _json_object(error.read(JSON_LIMIT + 1))
                if str(response.get("error_summary", "")).startswith("path/not_found"):
                    return None
            if error.code == 429 or error.code >= 500:
                delay = error.headers.get("Retry-After", "")
                delay = int(delay) if re.fullmatch(r"[0-9]{1,6}", delay) else 5
                raise _RetryableDropboxError(f"Dropbox {operation} is temporarily unavailable (HTTP {error.code}).",
                                             max(1, delay)) from None
        raise DropboxError(f"Dropbox {operation} failed (HTTP {error.code}). Check the app and its authorization.") from None
    except (URLError, OSError, http.client.HTTPException):
        raise _RetryableDropboxError(f"Could not connect to Dropbox for {operation}.") from None


def _token(form):
    request = Request(TOKEN_URL, data=urlencode(form).encode("ascii"), method="POST",
                      headers={"Content-Type": "application/x-www-form-urlencoded"})
    with _open(request, "OAuth token exchange", 30) as response:
        result = _json_object(response.read(JSON_LIMIT + 1))
    # Dropbox can omit the refresh response scope. Our refresh request
    # explicitly asks the server to narrow the token to these two scopes.
    scoped_refresh = form.get("grant_type") == "refresh_token" and form.get("scope") == SCOPES
    if "scope" in result or not scoped_refresh:
        scope = result.get("scope")
        if not isinstance(scope, str) or set(scope.split()) != set(SCOPES.split()):
            raise DropboxError("Dropbox did not grant exactly the two installer read scopes.")
    return result


class DropboxClient:
    def __init__(self, credentials):
        self.credentials = credentials
        self._access_token = None
        self._expires_at = 0

    def refresh_access_token(self):
        result = _token({"grant_type": "refresh_token", "client_id": self.credentials.app_key,
                         "refresh_token": self.credentials.refresh_token, "scope": SCOPES})
        access = result.get("access_token")
        expires = result.get("expires_in")
        if isinstance(expires, str) and re.fullmatch(r"[0-9]{1,10}", expires):
            expires = int(expires)
        if not _opaque(access) or type(expires) is not int or not 0 < expires <= 9_999_999_999:
            raise DropboxError("Dropbox did not return a usable access token.")
        self._access_token = access
        self._expires_at = time.monotonic() + max(1, expires - 30)

    def _bearer(self):
        if self._access_token is None or time.monotonic() >= self._expires_at:
            self.refresh_access_token()
        return "Bearer " + self._access_token

    def get_metadata(self, path, *, timeout=30):
        request = Request(METADATA_URL, method="POST", headers={"Authorization": self._bearer(),
                                                               "Content-Type": "application/json"},
                          data=json.dumps({"path": path, "include_has_explicit_shared_members": True}).encode("ascii"))
        response = _open(request, "file metadata lookup", timeout, allow_missing=True)
        if response is not None:
            with response:
                return _json_object(response.read(JSON_LIMIT + 1))
        return None

    def download_revision(self, revision):
        request = Request(DOWNLOAD_URL, method="POST", headers={
            "Authorization": self._bearer(), "Dropbox-API-Arg": json.dumps({"path": f"rev:{revision}"}),
        })
        return _open(request, "file download", 60)


def _archive_path(name):
    if not isinstance(name, str) or ARCHIVE_NAME.fullmatch(name) is None:
        raise DropboxError("Use a single ZIP filename in the Dropbox App Folder.")
    return "/" + name


def _snapshot(metadata, name):
    if metadata.get(".tag", "file") != "file" or metadata.get("name") != name:
        raise DropboxError("Dropbox returned a different file than the expected installer ZIP.")
    if metadata.get("sharing_info") is not None or metadata.get("has_explicit_shared_members") is True:
        raise DropboxError("Dropbox reports this installer ZIP is shared. Use a private App Folder.")
    identity = metadata.get("id")
    revision = metadata.get("rev")
    size = metadata.get("size")
    digest = metadata.get("content_hash")
    if (not isinstance(identity, str) or not identity.startswith("id:")
            or not isinstance(revision, str) or re.fullmatch(r"[0-9a-f]{9,}", revision) is None
            or type(size) is not int or size <= 0 or not isinstance(digest, str) or DIGEST.fullmatch(digest) is None):
        raise DropboxError("Dropbox did not return the installer ZIP revision, size, and content hash.")
    return identity, revision, size, digest


def _transfer(source, target=None, *, limit=None):
    """Hash normal SHA-256 and Dropbox's 4 MiB blocks in one streaming pass."""
    full_digest = sha256()
    dropbox_digest = sha256()
    block_digest = sha256()
    size = 0
    remaining = BLOCK_SIZE
    while chunk := source.read(remaining):
        size += len(chunk)
        if limit is not None and size > limit:
            raise DropboxError("Installer ZIP exceeds the expected byte count.")
        full_digest.update(chunk)
        block_digest.update(chunk)
        if target is not None:
            target.write(chunk)
        remaining -= len(chunk)
        if not remaining:
            dropbox_digest.update(block_digest.digest())
            block_digest = sha256()
            remaining = BLOCK_SIZE
    if remaining != BLOCK_SIZE:
        dropbox_digest.update(block_digest.digest())
    return size, full_digest.hexdigest(), dropbox_digest.hexdigest()


def _check_expected(sha256_digest, size):
    if sha256_digest is not None and (not isinstance(sha256_digest, str) or DIGEST.fullmatch(sha256_digest) is None):
        raise DropboxError("The expected installer SHA-256 must contain 64 lowercase hexadecimal digits.")
    if size is not None and (type(size) is not int or size <= 0):
        raise DropboxError("The expected installer size must be a positive byte count.")


def _proof(name, snapshot, actual):
    _, revision, size, content_hash = snapshot
    return {"filename": name, "sha256": actual[1], "bytes": size, "dropbox_content_hash": content_hash,
            "dropbox_path": _archive_path(name), "dropbox_revision": revision}


def validate_dropbox_directory(path):
    path = Path(path).expanduser().resolve()
    if not path.is_dir():
        raise DropboxError("Select the existing, private App Folder synced by Dropbox Desktop.")
    return path


def _new_file(destination):
    return tempfile.NamedTemporaryFile(dir=destination.parent, prefix=".~scp-", suffix=".tmp", delete=False)


def _place_archive(source, destination, sha256_digest, size, previous):
    if not source.is_file() or source.is_symlink():
        raise DropboxError("Choose a regular, verified installer ZIP.")
    temporary = _new_file(destination)
    try:
        with temporary, source.open("rb") as stream:
            actual = _transfer(stream, temporary, limit=size)
            if actual[0] <= 0 or (size is not None and actual[0] != size) or (
                    sha256_digest is not None and actual[1] != sha256_digest):
                raise DropboxError("The installer ZIP changed since it was verified.")
        if previous is not None and previous[2:] != (actual[0], actual[2]):
            raise DropboxError("A different installer ZIP already exists in the Dropbox App Folder.")
        try:
            # Publish only a complete file, atomically, without overwriting another run.
            os.link(temporary.name, destination)
        except FileExistsError:
            if not destination.is_file() or destination.is_symlink():
                raise DropboxError("The expected Dropbox ZIP path is not a regular file.") from None
            with destination.open("rb") as stream:
                if _transfer(stream, limit=actual[0]) != actual:
                    raise DropboxError("A different installer ZIP already exists in the Dropbox App Folder.") from None
        return actual
    finally:
        Path(temporary.name).unlink(missing_ok=True)


def sync_archive(source, dropbox_dir, *, timeout=300, credentials=None, sha256_digest=None, size=None):
    """Copy a verified archive and wait for the exact bytes to appear in Dropbox."""
    source = Path(source).expanduser()
    name = source.name
    path = _archive_path(name)
    _check_expected(sha256_digest, size)
    if not math.isfinite(timeout) or timeout <= 0:
        raise DropboxError("The Dropbox sync wait must be a positive, finite number of seconds.")
    folder = validate_dropbox_directory(dropbox_dir)
    client = DropboxClient(credentials or load_local_credentials())
    before = client.get_metadata(path)
    previous = None if before is None else _snapshot(before, name)
    actual = _place_archive(source, folder / name, sha256_digest, size, previous)
    deadline = time.monotonic() + timeout
    while (remaining := deadline - time.monotonic()) > 0:
        delay = 5
        try:
            metadata = client.get_metadata(path, timeout=min(30, remaining))
        except _RetryableDropboxError as error:
            delay = error.retry_after
        else:
            if metadata is not None:
                snapshot = _snapshot(metadata, name)
                if snapshot[2:] == (actual[0], actual[2]):
                    return _proof(name, snapshot, actual)
        time.sleep(min(delay, max(0, deadline - time.monotonic())))
    raise DropboxError(f"Dropbox did not confirm the complete {name} before the sync deadline. Check Dropbox Desktop.")


def download_archive(name, destination, *, sha256_digest=None, size=None, dropbox_content_hash=None, credentials=None):
    """Download a fixed revision and expose only its fully verified local file."""
    path = _archive_path(name)
    _check_expected(sha256_digest, size)
    if dropbox_content_hash is not None and (
            not isinstance(dropbox_content_hash, str) or DIGEST.fullmatch(dropbox_content_hash) is None):
        raise DropboxError("The expected Dropbox content hash must contain 64 lowercase hexadecimal digits.")
    destination = Path(destination)
    if destination.exists() or destination.is_symlink():
        raise DropboxError("Choose a new local path for the Dropbox installer ZIP.")
    client = DropboxClient(credentials or _runner_credentials())
    metadata = client.get_metadata(path)
    if metadata is None:
        raise DropboxNotFound(f"Dropbox App Folder does not contain the expected installer ZIP {name}.")
    snapshot = _snapshot(metadata, name)
    _, revision, expected_size, expected_content = snapshot
    if (size is not None and size != expected_size) or (
            dropbox_content_hash is not None and dropbox_content_hash != expected_content):
        raise DropboxError("Dropbox installer metadata differs from the expected size or content hash.")
    destination.parent.mkdir(parents=True, exist_ok=True)
    temporary = _new_file(destination)
    try:
        with temporary, client.download_revision(revision) as response:
            returned = _json_object(response.headers.get("Dropbox-API-Result", ""))
            if _snapshot(returned, name) != snapshot:
                raise DropboxError("Dropbox returned a different installer ZIP revision.")
            actual = _transfer(response, temporary, limit=expected_size)
        if actual[0] != expected_size or actual[2] != expected_content or (
                sha256_digest is not None and actual[1] != sha256_digest):
            raise DropboxError("Downloaded installer ZIP differs from its expected size or digest.")
        current = client.get_metadata(path)
        if current is None or _snapshot(current, name) != snapshot:
            raise DropboxError("The Dropbox installer filename changed during download.")
        os.link(temporary.name, destination)
        return _proof(name, snapshot, actual)
    except (http.client.HTTPException, URLError, TimeoutError):
        raise DropboxError("The Dropbox installer ZIP download ended before verification.") from None
    finally:
        Path(temporary.name).unlink(missing_ok=True)


def authorize(app_key, path=DEFAULT_CREDENTIALS):
    path = _credentials_path(path)
    if path.exists():
        raise DropboxError("The Dropbox credentials file already exists. Move it aside before authorizing again.")
    if not isinstance(app_key, str) or re.fullmatch(r"[A-Za-z0-9_-]+", app_key) is None:
        raise DropboxError("Enter the App key from the Dropbox Developer Console.")
    verifier = secrets.token_urlsafe(64)
    challenge = urlsafe_b64encode(sha256(verifier.encode("ascii")).digest()).decode("ascii").rstrip("=")
    query = urlencode({"client_id": app_key, "response_type": "code", "token_access_type": "offline",
                       "scope": SCOPES, "code_challenge": challenge, "code_challenge_method": "S256"})
    print("Open this Dropbox link, select Allow, then copy the authorization code.")
    print("https://www.dropbox.com/oauth2/authorize?" + query)
    with warnings.catch_warnings():
        warnings.simplefilter("error", GetPassWarning)
        try:
            code = getpass("Paste the Dropbox authorization code and press Return. ").strip()
        except (GetPassWarning, EOFError):
            raise DropboxError("Run authorization in an interactive terminal with hidden input.") from None
    if not _opaque(code):
        raise DropboxError("The Dropbox authorization code is missing or invalid.")
    result = _token({"grant_type": "authorization_code", "client_id": app_key, "code": code,
                     "code_verifier": verifier})
    credentials = DropboxCredentials(app_key, result.get("refresh_token"))
    path.parent.mkdir(parents=True, exist_ok=True, mode=0o700)
    temporary = tempfile.NamedTemporaryFile(dir=path.parent, prefix=".scp-credentials-", delete=False)
    try:
        with temporary:
            temporary.write(json.dumps({"app_key": credentials.app_key,
                                       "refresh_token": credentials.refresh_token}).encode("ascii"))
        os.chmod(temporary.name, 0o600)
        os.link(temporary.name, path)
    finally:
        Path(temporary.name).unlink(missing_ok=True)
    return path


def _read_github_policy(endpoint, child_environment):
    try:
        result = subprocess.run(["gh", "api", "--method", "GET", "-H", "X-GitHub-Api-Version: 2026-03-10", endpoint],
                                text=True, env=child_environment, stdout=subprocess.PIPE, stderr=subprocess.DEVNULL,
                                timeout=30)
        if result.returncode:
            raise DropboxError("Could not verify the GitHub environment policy. Check gh authorization and Settings.")
        data = json.loads(result.stdout)
    except (OSError, subprocess.TimeoutExpired, json.JSONDecodeError):
        raise DropboxError("Could not verify the GitHub environment policy. Check gh authorization and Settings.") from None
    if not isinstance(data, dict):
        raise DropboxError("GitHub did not return a usable environment policy.")
    return data


def install_github_secrets(repository, environment, credentials):
    branches = {"scp-prebuilt-review": "dev", "scp-prebuilt-release": "main"}
    if re.fullmatch(r"[A-Za-z0-9_.-]+/[A-Za-z0-9_.-]+", repository) is None:
        raise DropboxError("Specify the GitHub owner/repository.")
    if environment not in branches:
        raise DropboxError("Use the scp-prebuilt-review or scp-prebuilt-release GitHub environment.")
    child_environment = {key: value for key, value in os.environ.items()
                         if key not in (APP_KEY_ENV, REFRESH_TOKEN_ENV, "GH_DEBUG")}
    child_environment.update(GH_HOST="github.com", GH_PROMPT_DISABLED="1")
    endpoint = f"repos/{repository}/environments/{environment}"
    details = _read_github_policy(endpoint, child_environment)
    policy = details.get("deployment_branch_policy")
    if (details.get("name") != environment or not isinstance(policy, dict)
            or policy.get("protected_branches") is not False or policy.get("custom_branch_policies") is not True):
        raise DropboxError("GitHub environment must use selected branches and tags before saving secrets.")
    rules = _read_github_policy(endpoint + "/deployment-branch-policies?per_page=100", child_environment)
    policies = rules.get("branch_policies")
    branch = branches[environment]
    if (type(rules.get("total_count")) is not int or rules["total_count"] != 1
            or not isinstance(policies, list) or len(policies) != 1 or not isinstance(policies[0], dict)
            or policies[0].get("name") != branch or policies[0].get("type") != "branch"):
        raise DropboxError(f"GitHub environment must allow only the {branch} branch and no tags before saving secrets.")
    for name, value in ((APP_KEY_ENV, credentials.app_key), (REFRESH_TOKEN_ENV, credentials.refresh_token)):
        result = subprocess.run(["gh", "secret", "set", name, "--repo", repository, "--env", environment],
                                input=value, text=True, env=child_environment,
                                stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
        if result.returncode:
            raise DropboxError(f"GitHub did not save {name}. Check the protected environment and gh authorization.")


def main(argv=None):
    parser = argparse.ArgumentParser(description=__doc__)
    commands = parser.add_subparsers(dest="command", required=True)
    auth = commands.add_parser("authorize", help="Create local credentials using Dropbox OAuth.")
    auth.add_argument("--app-key", required=True)
    auth.add_argument("--credentials", type=Path, default=DEFAULT_CREDENTIALS)
    github = commands.add_parser("github-secrets", help="Install the two protected GitHub environment secrets.")
    github.add_argument("--repository", required=True)
    github.add_argument("--environment", required=True)
    github.add_argument("--credentials", type=Path, default=DEFAULT_CREDENTIALS)
    fetch = commands.add_parser("download", help="Fetch one immutable installer ZIP revision on the runner.")
    fetch.add_argument("--name", required=True)
    fetch.add_argument("--destination", type=Path, required=True)
    fetch.add_argument("--sha256")
    fetch.add_argument("--size", type=int)
    fetch.add_argument("--dropbox-content-hash")
    options = parser.parse_args(argv)
    try:
        if options.command == "authorize":
            path = authorize(options.app_key, options.credentials)
            print(f"Saved private Dropbox credentials to {path}.")
        elif options.command == "github-secrets":
            install_github_secrets(options.repository, options.environment, load_local_credentials(options.credentials))
            print("Saved the two Dropbox secrets to the requested GitHub environment.")
        else:
            result = download_archive(options.name, options.destination, sha256_digest=options.sha256, size=options.size,
                                      dropbox_content_hash=options.dropbox_content_hash)
            print(json.dumps(result, sort_keys=True))
    except (DropboxError, OSError) as error:
        print(str(error), file=sys.stderr)
        return 1
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
