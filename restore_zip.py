from pathlib import Path
import base64
import hashlib
import zipfile
import sys

ZIP_FILE = Path('uacos_v2_release.zip')
EXPECTED_SHA256 = '1e85f909075d6dbbeaf3d5e4556ff79a7254739664644ca60342fb5042a757f4'


def read_base64_payload():
    single = Path('uacos_v2_release.zip.b64')
    if single.exists():
        return single.read_text(encoding='utf-8')

    parts = sorted(Path('.').glob('uacos_v2_release.zip.b64.part*'))
    if parts:
        return ''.join(p.read_text(encoding='utf-8') for p in parts)

    print('ERROR: missing uacos_v2_release.zip.b64 or part files', file=sys.stderr)
    sys.exit(1)


def main():
    raw = read_base64_payload()
    compact = ''.join(raw.split())
    data = base64.b64decode(compact)
    ZIP_FILE.write_bytes(data)

    sha256 = hashlib.sha256(data).hexdigest()
    print('created:', ZIP_FILE)
    print('size:', ZIP_FILE.stat().st_size, 'bytes')
    print('sha256:', sha256)

    if sha256 != EXPECTED_SHA256:
        print('ERROR: SHA256 mismatch', file=sys.stderr)
        sys.exit(2)

    with zipfile.ZipFile(ZIP_FILE, 'r') as z:
        bad = z.testzip()
        if bad:
            print('ERROR: zip integrity failed at', bad, file=sys.stderr)
            sys.exit(3)
        print('zip_test: ok')
        print('file_count:', len(z.namelist()))

    print('restore: ok')


if __name__ == '__main__':
    main()
