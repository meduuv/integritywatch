# IntegrityWatch

> Detect file changes against a known integrity baseline.

IntegrityWatch provides dependency-free helpers for creating deterministic SHA-256 file manifests and comparing later state against that baseline.

## Features

- Build SHA-256 integrity manifests
- Compare current files with a baseline
- Detect added files
- Detect removed files
- Detect changed files
- Produce deterministic results for automation
- Read-only analysis

## Workflow

```text
known-good files
       ↓
SHA-256 baseline
       ↓
current files
       ↓
comparison
       ↓
added / removed / changed
```

## Example

```python
from integritywatch import build_manifest, compare

baseline = build_manifest("./release")
current = build_manifest("./release")

changes = compare(baseline, current)
print(changes)
```

Check the source and tests for the exact supported API.

## Use cases

- Release verification
- Configuration monitoring
- Local forensic workflows
- Change detection
- Defensive automation

## Scope

IntegrityWatch performs local, read-only integrity analysis. It does not alter files or provide unauthorized access functionality.

## Development

```bash
python -m pytest
```

## License

MIT. See `LICENSE`.

## Author

Built by **Medu** · https://guns.lol/meduu