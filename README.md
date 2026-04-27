# UACOS v2 Release

This repository stores the UACOS v2 release archive as chunked base64 text so it can be restored even when binary artifact download fails.

## Restore ZIP

```powershell
git clone https://github.com/caotiensinh/uacos_v2.git
cd uacos_v2
python restore_zip.py
```

This creates:

```text
uacos_v2_release.zip
```

Expected file info:

```text
size_bytes: 145643
sha256: 1e85f909075d6dbbeaf3d5e4556ff79a7254739664644ca60342fb5042a757f4
zip_file_count: 135
```

## Extract and install on Windows

```powershell
Expand-Archive .\uacos_v2_release.zip -DestinationPath .\uacos_v2_release -Force
cd .\uacos_v2_release\uacos_phase15_v2_release
py -3.12 -m venv .venv
.venv\Scripts\activate
python -m pip install --upgrade pip
pip install -e .
uacos --help
```

## Quick smoke test

```powershell
$REPO="G:\My Drive\aimemory\uacos_test_repo"
New-Item -ItemType Directory -Force $REPO
uacos bootstrap --repo $REPO
uacos health --repo $REPO
```

## Contents

UACOS v2 includes Phase 0-15:

- local repo index
- context pack
- security/patch gate
- agent coordination
- adapter layer
- evidence hardening
- apply/rollback
- memory/regression brain
- dashboard
- packaging
- skill memory
- VSCode integration
- auto-learning
- semantic memory search
- autopilot orchestration
