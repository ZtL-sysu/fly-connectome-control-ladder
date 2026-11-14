#!/usr/bin/env python
"""R122 acquisition map for R106 §6 R4 first-hand freeze.

Pure data: maps each local raw file to the exact URL fetched on 2026-11-14.
No inference, no derived claims. The verifier must recompute from raw bytes.
"""
import os, hashlib, json

RAW = os.path.join(os.path.dirname(os.path.abspath(__file__)), "raw")

SOURCES = [
    {"file": "arxiv-2609.24565v1-abs.html",  "url": "https://arxiv.org/abs/2609.24565v1",       "kind": "abs_v1"},
    {"file": "arxiv-2609.24565v2-abs.html",  "url": "https://arxiv.org/abs/2609.24565v2",       "kind": "abs_v2"},
    {"file": "arxiv-2609.24565v1-html.html", "url": "https://arxiv.org/html/2609.24565v1",      "kind": "html_v1"},
    {"file": "arxiv-2609.24565v2-html.html", "url": "https://arxiv.org/html/2609.24565v2",      "kind": "html_v2"},
    {"file": "arxiv-2609.24565-api.xml",     "url": "https://export.arxiv.org/api/query?id_list=2609.24565", "kind": "atom_api"},
]


def sha256(path):
    h = hashlib.sha256()
    with open(path, "rb") as f:
        for chunk in iter(lambda: f.read(65536), b""):
            h.update(chunk)
    return h.hexdigest()


def build():
    out = []
    for s in SOURCES:
        p = os.path.join(RAW, s["file"])
        out.append({
            "file": s["file"], "url": s["url"], "kind": s["kind"],
            "bytes": os.path.getsize(p), "sha256": sha256(p),
        })
    return out


if __name__ == "__main__":
    print(json.dumps(build(), indent=2))
