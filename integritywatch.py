"""Small file-integrity manifest helpers."""
import hashlib

def digest(data, algorithm="sha256"):
    return hashlib.new(algorithm, data).hexdigest()

def compare(baseline, current):
    old, new = set(baseline), set(current)
    changed = sorted(k for k in old & new if baseline[k] != current[k])
    return {"added": sorted(new - old), "removed": sorted(old - new), "changed": changed}

def manifest(items):
    return {str(name): digest(data) for name, data in items}
