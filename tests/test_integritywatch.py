from integritywatch import compare, digest, manifest

def test_integrity():
    assert digest(b"abc") == "ba7816bf8f01cfea414140de5dae2223b00361a396177a9cb410ff61f20015ad"
    assert manifest([("a", b"x")])["a"]
    assert compare({"a": "1"}, {"a": "2", "b": "3"}) == {"added": ["b"], "removed": [], "changed": ["a"]}
