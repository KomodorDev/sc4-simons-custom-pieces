"""Offline verification of the private Dropbox release transport."""
from __future__ import annotations

from base64 import urlsafe_b64encode
from contextlib import redirect_stdout
from hashlib import sha256
import io
import json
import os
from pathlib import Path
import stat
import subprocess
import sys
import tempfile
import unittest
from unittest.mock import Mock, patch
from urllib.error import HTTPError
from urllib.parse import parse_qs, urlparse


ROOT = Path(__file__).resolve().parents[1]
sys.path.insert(0, str(ROOT / "installer"))
import release_dropbox as dropbox


ARCHIVE = "SCP-Installer-Prebuilt-Review-windows-x64-123456789abc.zip"
DATA = b"synthetic installer ZIP bytes"
CREDENTIALS = dropbox.DropboxCredentials("fixture-key", "fixture-refresh-token")


def metadata(data=DATA, **changes):
    return {".tag": "file", "name": ARCHIVE, "id": "id:fixture", "rev": "0123456789abc",
            "size": len(data), "content_hash": sha256(sha256(data).digest()).hexdigest(), **changes}


class Response(io.BytesIO):
    def __init__(self, data=b"", headers=None):
        super().__init__(data)
        self.headers = headers or {}


class DropboxReleaseTests(unittest.TestCase):
    def setUp(self):
        temporary = tempfile.TemporaryDirectory()
        self.addCleanup(temporary.cleanup)
        self.directory = Path(temporary.name).resolve()

    def test_dropbox_digest_uses_exact_4_mib_blocks_and_empty_input(self):
        first = b"x" * dropbox.BLOCK_SIZE
        last = b"last part"
        data = first + last

        class ShortReads(io.BytesIO):
            def read(self, size=-1):
                return super().read(min(size, 83_019))

        expected = sha256(sha256(first).digest() + sha256(last).digest()).hexdigest()
        self.assertEqual(dropbox._transfer(ShortReads(data)), (len(data), sha256(data).hexdigest(), expected))
        self.assertEqual(dropbox._transfer(io.BytesIO()), (0, sha256(b"").hexdigest(), sha256(b"").hexdigest()))

    def test_pkce_authorizes_offline_read_scopes_and_keeps_credentials_private(self):
        destination = self.directory / "credentials.json"
        stream = io.StringIO()
        response = {"scope": dropbox.SCOPES, "refresh_token": CREDENTIALS.refresh_token}
        with patch.object(dropbox, "getpass", return_value="authorization-code"), \
                patch.object(dropbox._OPENER, "open", return_value=Response(json.dumps(response).encode())) as request, \
                redirect_stdout(stream):
            self.assertEqual(dropbox.authorize(CREDENTIALS.app_key, destination), destination)
        posted = request.call_args.args[0]
        data = parse_qs(posted.data.decode())
        self.assertEqual(posted.full_url, dropbox.TOKEN_URL)
        self.assertEqual(posted.get_method(), "POST")
        self.assertEqual(set(data), {"grant_type", "client_id", "code", "code_verifier"})
        url = stream.getvalue().splitlines()[-1]
        query = parse_qs(urlparse(url).query)
        self.assertEqual(query["code_challenge_method"], ["S256"])
        self.assertEqual(query["token_access_type"], ["offline"])
        self.assertEqual(query["scope"], [dropbox.SCOPES])
        challenge = urlsafe_b64encode(sha256(data["code_verifier"][0].encode()).digest()).decode().rstrip("=")
        self.assertEqual(query["code_challenge"], [challenge])
        self.assertNotIn(CREDENTIALS.refresh_token, stream.getvalue())
        self.assertNotIn("authorization-code", stream.getvalue())
        self.assertNotIn(CREDENTIALS.refresh_token, repr(CREDENTIALS))
        if os.name != "nt":
            self.assertEqual(stat.S_IMODE(destination.stat().st_mode), 0o600)
        self.assertEqual(dropbox.load_local_credentials(destination), CREDENTIALS)
        with self.assertRaisesRegex(dropbox.DropboxError, "already exists"):
            dropbox.authorize(CREDENTIALS.app_key, destination)

    def test_authorization_requires_the_reported_offline_code_scopes_before_saving_credentials(self):
        destination = self.directory / "credentials.json"
        for scopes in ({}, {"scope": dropbox.SCOPES + " files.content.write"}):
            response = {"refresh_token": CREDENTIALS.refresh_token, **scopes}
            with self.subTest(scopes=scopes), patch.object(dropbox, "getpass", return_value="authorization-code"), \
                    patch.object(dropbox._OPENER, "open", return_value=Response(json.dumps(response).encode())), \
                    redirect_stdout(io.StringIO()):
                with self.assertRaisesRegex(dropbox.DropboxError, "exactly the two"):
                    dropbox.authorize(CREDENTIALS.app_key, destination)
            self.assertFalse(destination.exists())

    def test_credential_file_cannot_be_in_git_or_group_readable(self):
        repo = self.directory / "repo"
        (repo / ".git").mkdir(parents=True)
        with self.assertRaisesRegex(dropbox.DropboxError, "outside Git"):
            dropbox.load_local_credentials(repo / "credentials.json")
        if os.name != "nt":
            path = self.directory / "credentials.json"
            path.write_text('{"app_key":"fixture-key","refresh_token":"fixture-refresh-token"}')
            path.chmod(0o640)
            with self.assertRaisesRegex(dropbox.DropboxError, "0600"):
                dropbox.load_local_credentials(path)

    def test_refresh_uses_app_key_without_secret_and_rejects_a_broader_access_token(self):
        client = dropbox.DropboxClient(CREDENTIALS)
        response = {"access_token": "fixture-access", "expires_in": 14400, "scope": dropbox.SCOPES}
        with patch.object(dropbox._OPENER, "open", return_value=Response(json.dumps(response).encode())) as request:
            self.assertIsNone(client.refresh_access_token())
        params = parse_qs(request.call_args.args[0].data.decode())
        self.assertEqual(params, {"grant_type": ["refresh_token"], "refresh_token": [CREDENTIALS.refresh_token],
                                  "client_id": [CREDENTIALS.app_key], "scope": [dropbox.SCOPES]})
        response["scope"] += " files.content.write"
        with patch.object(dropbox._OPENER, "open", return_value=Response(json.dumps(response).encode())):
            with self.assertRaisesRegex(dropbox.DropboxError, "exactly the two"):
                client.refresh_access_token()

    def test_explicitly_scoped_refresh_accepts_omitted_scope_and_string_expiration(self):
        client = dropbox.DropboxClient(CREDENTIALS)
        response = {"access_token": "fixture-access", "expires_in": "14400"}
        with patch.object(dropbox._OPENER, "open", return_value=Response(json.dumps(response).encode())) as request, \
                patch.object(dropbox.time, "monotonic", return_value=10):
            client.refresh_access_token()
        self.assertEqual(parse_qs(request.call_args.args[0].data.decode())["scope"], [dropbox.SCOPES])
        self.assertEqual(client._expires_at, 14_380)

    def test_refresh_refuses_invalid_expiration_and_reported_scope(self):
        client = dropbox.DropboxClient(CREDENTIALS)
        malformed = ({"expires_in": True}, {"expires_in": "14.5"}, {"expires_in": "0"}, {"scope": None})
        for fields in malformed:
            response = {"access_token": "fixture-access", "expires_in": 14400, **fields}
            with self.subTest(fields=fields), \
                    patch.object(dropbox._OPENER, "open", return_value=Response(json.dumps(response).encode())):
                with self.assertRaises(dropbox.DropboxError):
                    client.refresh_access_token()

    def test_metadata_missing_is_distinguished_from_a_sanitized_api_error(self):
        client = dropbox.DropboxClient(CREDENTIALS)
        client._access_token = "fixture-access"
        client._expires_at = float("inf")
        missing = HTTPError(dropbox.METADATA_URL, 409, "Conflict", {},
                            io.BytesIO(b'{"error_summary":"path/not_found/"}'))
        with patch.object(dropbox._OPENER, "open", side_effect=missing) as opener:
            self.assertIsNone(client.get_metadata("/" + ARCHIVE))
        posted = opener.call_args.args[0]
        self.assertEqual(json.loads(posted.data), {"path": "/" + ARCHIVE, "include_has_explicit_shared_members": True})
        self.assertEqual(posted.get_header("Authorization"), "Bearer fixture-access")
        failure = HTTPError(dropbox.METADATA_URL, 401, CREDENTIALS.refresh_token, {},
                            io.BytesIO(CREDENTIALS.refresh_token.encode()))
        with patch.object(dropbox._OPENER, "open", side_effect=failure):
            with self.assertRaisesRegex(dropbox.DropboxError, "HTTP 401") as raised:
                client.get_metadata("/" + ARCHIVE)
        self.assertNotIn(CREDENTIALS.refresh_token, str(raised.exception))

    def test_sync_waits_for_matching_remote_hash_and_size(self):
        source = self.directory / ARCHIVE
        source.write_bytes(DATA)
        folder = self.directory / "App Folder"
        folder.mkdir()
        client = Mock()
        client.get_metadata.side_effect = [None, metadata(b"wrong"), metadata()]
        with patch.object(dropbox, "DropboxClient", return_value=client), patch.object(dropbox.time, "sleep"):
            proof = dropbox.sync_archive(source, folder, credentials=CREDENTIALS,
                                         sha256_digest=sha256(DATA).hexdigest(), size=len(DATA))
        self.assertEqual((folder / ARCHIVE).read_bytes(), DATA)
        self.assertEqual(proof, {"filename": ARCHIVE, "bytes": len(DATA), "sha256": sha256(DATA).hexdigest(),
                                 "dropbox_path": "/" + ARCHIVE, "dropbox_revision": metadata()["rev"],
                                 "dropbox_content_hash": metadata()["content_hash"]})
        self.assertEqual(client.get_metadata.call_count, 3)
        self.assertEqual(list(folder.iterdir()), [folder / ARCHIVE])

    def test_sync_refuses_changed_source_and_unrelated_existing_remote_bytes(self):
        source = self.directory / ARCHIVE
        source.write_bytes(DATA)
        folder = self.directory / "App Folder"
        folder.mkdir()
        client = Mock()
        with patch.object(dropbox, "DropboxClient", return_value=client):
            client.get_metadata.return_value = None
            with self.assertRaisesRegex(dropbox.DropboxError, "changed since"):
                dropbox.sync_archive(source, folder, credentials=CREDENTIALS, sha256_digest="0" * 64)
            self.assertEqual(list(folder.iterdir()), [])
            client.get_metadata.return_value = metadata(b"unrelated")
            with self.assertRaisesRegex(dropbox.DropboxError, "already exists"):
                dropbox.sync_archive(source, folder, credentials=CREDENTIALS)
            self.assertEqual(list(folder.iterdir()), [])

    def test_sync_times_out_without_claiming_upload(self):
        source = self.directory / ARCHIVE
        source.write_bytes(DATA)
        folder = self.directory / "App Folder"
        folder.mkdir()
        client = Mock()
        client.get_metadata.return_value = None
        with patch.object(dropbox, "DropboxClient", return_value=client), \
                patch.object(dropbox.time, "monotonic", side_effect=[0, 1, 11, 11]), \
                patch.object(dropbox.time, "sleep"):
            with self.assertRaisesRegex(dropbox.DropboxError, "did not confirm"):
                dropbox.sync_archive(source, folder, timeout=10, credentials=CREDENTIALS)
        self.assertEqual((folder / ARCHIVE).read_bytes(), DATA)

    def test_download_pins_revision_and_streams_verified_payload(self):
        result = metadata()
        calls = [
            Response(json.dumps({"scope": dropbox.SCOPES, "access_token": "fixture-access", "expires_in": 14400}).encode()),
            Response(json.dumps(result).encode()),
            Response(DATA, {"Dropbox-API-Result": json.dumps(result)}),
            Response(json.dumps(result).encode()),
        ]
        target = self.directory / ARCHIVE
        with patch.object(dropbox._OPENER, "open", side_effect=calls) as opener:
            proof = dropbox.download_archive(ARCHIVE, target, credentials=CREDENTIALS)
        self.assertEqual(target.read_bytes(), DATA)
        self.assertEqual(proof["sha256"], sha256(DATA).hexdigest())
        self.assertEqual(proof["dropbox_revision"], result["rev"])
        request = opener.call_args_list[2].args[0]
        self.assertEqual(request.full_url, dropbox.DOWNLOAD_URL)
        self.assertEqual(request.get_method(), "POST")
        self.assertEqual(json.loads(request.get_header("Dropbox-api-arg")), {"path": "rev:" + result["rev"]})

    def test_download_refuses_missing_shared_changed_or_bad_bytes_without_destination(self):
        target = self.directory / ARCHIVE
        result = metadata()
        client = Mock()
        with patch.object(dropbox, "DropboxClient", return_value=client):
            client.get_metadata.return_value = None
            with self.assertRaises(dropbox.DropboxNotFound):
                dropbox.download_archive(ARCHIVE, target, credentials=CREDENTIALS)
            client.get_metadata.return_value = metadata(has_explicit_shared_members=True)
            with self.assertRaisesRegex(dropbox.DropboxError, "reports this installer ZIP is shared"):
                dropbox.download_archive(ARCHIVE, target, credentials=CREDENTIALS)
            client.get_metadata.return_value = result
            client.download_revision.return_value = Response(b"x" * len(DATA), {"Dropbox-API-Result": json.dumps(result)})
            with self.assertRaisesRegex(dropbox.DropboxError, "expected size or digest"):
                dropbox.download_archive(ARCHIVE, target, credentials=CREDENTIALS)
            client.get_metadata.side_effect = [result, metadata(rev="0123456789def")]
            client.download_revision.return_value = Response(DATA, {"Dropbox-API-Result": json.dumps(result)})
            with self.assertRaisesRegex(dropbox.DropboxError, "changed during download"):
                dropbox.download_archive(ARCHIVE, target, credentials=CREDENTIALS)
        self.assertEqual(list(self.directory.iterdir()), [])

    def test_runner_credentials_are_read_only_environment_values(self):
        with patch.dict(os.environ, {dropbox.APP_KEY_ENV: CREDENTIALS.app_key,
                                     dropbox.REFRESH_TOKEN_ENV: CREDENTIALS.refresh_token}, clear=True):
            self.assertEqual(dropbox._runner_credentials(), CREDENTIALS)
        with patch.dict(os.environ, {}, clear=True):
            with self.assertRaisesRegex(dropbox.DropboxError, "protected GitHub environment secrets"):
                dropbox._runner_credentials()

    def _github_response(self, data):
        return subprocess.CompletedProcess([], 0, json.dumps(data))

    def _github_environment(self, name, *, custom=True):
        return self._github_response({"name": name, "deployment_branch_policy": {
            "protected_branches": False, "custom_branch_policies": custom}})

    def test_github_secrets_verify_the_exact_environment_before_passing_values_over_stdin(self):
        for name, branch in (("scp-prebuilt-review", "dev"), ("scp-prebuilt-release", "main")):
            with self.subTest(environment=name):
                policy = self._github_response({"total_count": 1, "branch_policies": [
                    {"name": branch, "type": "branch"}]})
                done = subprocess.CompletedProcess([], 0)
                with patch.dict(os.environ, {dropbox.APP_KEY_ENV: CREDENTIALS.app_key,
                                             dropbox.REFRESH_TOKEN_ENV: CREDENTIALS.refresh_token,
                                             "GH_DEBUG": "api", "GH_HOST": "github.invalid"}), \
                        patch.object(dropbox.subprocess, "run", side_effect=[
                            self._github_environment(name), policy, done, done]) as run:
                    dropbox.install_github_secrets("owner/project", name, CREDENTIALS)
                checks, writes = run.call_args_list[:2], run.call_args_list[2:]
                endpoint = f"repos/owner/project/environments/{name}"
                self.assertEqual([call.args[0][-1] for call in checks],
                                 [endpoint, endpoint + "/deployment-branch-policies?per_page=100"])
                for call in checks:
                    self.assertEqual(call.args[0][:4], ["gh", "api", "--method", "GET"])
                    self.assertNotIn("input", call.kwargs)
                for call, secret, value in zip(writes, (dropbox.APP_KEY_ENV, dropbox.REFRESH_TOKEN_ENV),
                                               (CREDENTIALS.app_key, CREDENTIALS.refresh_token), strict=True):
                    self.assertEqual(call.args[0], ["gh", "secret", "set", secret, "--repo", "owner/project",
                                                    "--env", name])
                    self.assertEqual(call.kwargs["input"], value)
                    self.assertEqual(call.kwargs["stderr"], subprocess.DEVNULL)
                for call in run.call_args_list:
                    child = call.kwargs["env"]
                    self.assertEqual(child["GH_HOST"], "github.com")
                    self.assertFalse({dropbox.APP_KEY_ENV, dropbox.REFRESH_TOKEN_ENV, "GH_DEBUG"} & child.keys())

    def test_github_secrets_reject_other_environment_names_without_contacting_github(self):
        with patch.object(dropbox.subprocess, "run") as run:
            with self.assertRaisesRegex(dropbox.DropboxError, "scp-prebuilt-review or scp-prebuilt-release"):
                dropbox.install_github_secrets("owner/project", "protected", CREDENTIALS)
            run.assert_not_called()

    def test_github_secrets_stop_if_policy_is_unavailable_or_not_custom(self):
        name = "scp-prebuilt-review"
        for response in (subprocess.CompletedProcess([], 1), self._github_environment(name, custom=False)):
            with self.subTest(response=response), patch.object(dropbox.subprocess, "run", return_value=response) as run:
                with self.assertRaises(dropbox.DropboxError):
                    dropbox.install_github_secrets("owner/project", name, CREDENTIALS)
                self.assertEqual(run.call_count, 1)
                self.assertEqual(run.call_args.args[0][:2], ["gh", "api"])

    def test_github_secrets_reject_extra_branches_tags_and_unknown_rule_types_before_writing(self):
        name = "scp-prebuilt-review"
        cases = ([{"name": "main", "type": "branch"}],
                 [{"name": "dev", "type": "tag"}],
                 [{"name": "dev"}],
                 [{"name": "dev", "type": "branch"}, {"name": "*", "type": "tag"}])
        for policies in cases:
            rules = self._github_response({"total_count": len(policies), "branch_policies": policies})
            with self.subTest(policies=policies), patch.object(dropbox.subprocess, "run", side_effect=[
                    self._github_environment(name), rules]) as run:
                with self.assertRaisesRegex(dropbox.DropboxError, "only the dev branch and no tags"):
                    dropbox.install_github_secrets("owner/project", name, CREDENTIALS)
                self.assertEqual(run.call_count, 2)
                self.assertTrue(all(call.args[0][:2] == ["gh", "api"] for call in run.call_args_list))


if __name__ == "__main__":
    unittest.main()
