"""Package only a verified staged build, instructions, and actual model preview."""
from pathlib import Path
import hashlib
import json
import zipfile

HERE = Path(__file__).resolve().parent
DIST = HERE / 'dist'


def main():
    manifest = json.loads((DIST / 'build-manifest.json').read_text())
    verification = json.loads((DIST / 'verification.json').read_text())
    dat = Path(manifest['output'])
    fingerprint = hashlib.sha256(dat.read_bytes()).hexdigest()
    assert fingerprint == manifest['sha256'] == verification['sha256']
    assert verification['static_checks_passed'] is True
    folder = dat.parent.name
    destination = DIST / 'HSR-over-diagonal-GHSR-NAM50-experimental.zip'
    members = {f'{folder}/{dat.name}': dat,
               'README.md': HERE / 'README.md',
               'model-preview.png': DIST / 'model-preview.png',
               'verification.json': DIST / 'verification.json'}
    with zipfile.ZipFile(destination, 'w', compression=zipfile.ZIP_DEFLATED, compresslevel=9) as archive:
        for name, source in members.items():
            assert source.is_file()
            if name == 'README.md':
                archive.writestr(name, source.read_text().replace('(dist/model-preview.png)', '(model-preview.png)'))
            else:
                archive.write(source, name)
    with zipfile.ZipFile(destination) as archive:
        assert archive.testzip() is None
        assert set(archive.namelist()) == set(members)
        assert hashlib.sha256(archive.read(f'{folder}/{dat.name}')).hexdigest() == fingerprint
    result = {'output': str(destination), 'bytes': destination.stat().st_size,
              'sha256': hashlib.sha256(destination.read_bytes()).hexdigest(),
              'dat_sha256': fingerprint, 'zip_integrity_checked': True,
              'installed': False}
    (DIST / 'package-verification.json').write_text(json.dumps(result, indent=2) + '\n')
    print(json.dumps(result, indent=2))


if __name__ == '__main__':
    main()
