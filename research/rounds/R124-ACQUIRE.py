#!/usr/bin/env python3
"""R124 acquisition map.

READ-ONLY provenance record: this module does NOT re-run any network request.
It records the exact URL -> local raw file mapping used for the R124 first-hand
freeze, plus the observed HTTP status / byte count at acquisition time.

All raw files were fetched with curl and saved verbatim; no transformation,
no retry-repair, and no content substitution. Failed endpoints (HTTP 429
Cloudflare 1015) are preserved as-is as negative evidence.

Strict scope: third-party public small text only. No dataset, weights,
binaries, credentials, or local absolute paths are present in raw/.
"""
from __future__ import annotations

# (local filename, method, url, observed_http_status, observed_bytes, note)
ACQUISITION = [
    ("biorxiv-api-details.json", "curl GET",
     "https://api.biorxiv.org/details/biorxiv/10.64898/2026.06.10.731214",
     200, 64741,
     "bioRxiv official details API; collection has 12 version records, each with abstract/title/date/jatsxml"),
    ("biorxiv-api-v1-na.json", "curl GET",
     "https://api.biorxiv.org/details/biorxiv/10.64898/2026.06.10.731214/1",
     200, 64741,
     "The /1 suffix is NOT a version selector for this endpoint; response is byte-identical to details. Preserved as negative evidence."),
    ("crossref-work.json", "curl GET",
     "https://api.crossref.org/works/10.64898/2026.06.10.731214",
     200, 11160,
     "Crossref official work metadata, includes jats abstract"),
    ("europepmc-search.json", "curl GET",
     "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.64898/2026.06.10.731214&format=json",
     200, 841,
     "Europe PMC official search API, hitCount=1, PPR1251441"),
    ("connect-biorxiv-relate181.html", "curl GET",
     "https://connect.biorxiv.org/relate/content/181",
     200, 58714,
     "bioRxiv connect HTML; DOI string appears 30 times. Auxiliary, not used for abstract claims."),
    ("secondary-mirror-article.html", "curl GET",
     "https://aimedicalcompendium.com/article.cfm?id=253759",
     301, 265,
     "Bare-domain URL redirects to www. Preserved verbatim (301 body)."),
    ("secondary-mirror-article-followed.html", "curl GET -L",
     "https://aimedicalcompendium.com/article.cfm?id=253759",
     200, 37429,
     "Followed redirect. Second-hand mirror page; contains the size-matched/trained-ER abstract verbatim."),
    ("arxiv-2609.39248-abs.html", "curl GET -L",
     "https://arxiv.org/abs/2609.39248",
     200, 43328,
     "First-hand arXiv abs for R5 W8 Zenodo identifier correction"),
    ("arxiv-2610.13018-abs.html", "curl GET -L",
     "https://arxiv.org/abs/2610.13018",
     200, 42453,
     "First-hand arXiv abs for R5 W8 submission-date correction"),
    ("biorxiv-v1.html", "curl GET -L",
     "https://www.biorxiv.org/content/10.64898/2026.06.10.731214v1",
     429, 17,
     "Cloudflare error code 1015. An earlier exploratory probe of this exact URL returned HTTP 200 / 105400 B but was NOT saved to disk, so no local byte freeze exists for the v1 HTML page."),
    ("biorxiv-v1-retry.html", "curl GET -L",
     "https://www.biorxiv.org/content/10.64898/2026.06.10.731214v1?download=1",
     429, 17, "Cloudflare 1015; preserved as negative evidence"),
    ("biorxiv-v1-early-full.html", "curl GET -L",
     "https://www.biorxiv.org/content/biorxiv/early/2026/06/12/2026.06.10.731214v1.full",
     429, 17, "Cloudflare 1015; preserved as negative evidence"),
    ("biorxiv-v3.html", "curl GET -L",
     "https://www.biorxiv.org/content/10.64898/2026.06.10.731214v3",
     429, 17, "Cloudflare 1015; preserved as negative evidence"),
]

SCOPE_NOTE = (
    "R124 is a READONLY first-hand text acquisition for R106 section 6 items R3 and R5. "
    "It is NOT a gate pass, NOT a scientific result, NOT a forward pass, and NOT a score change. "
    "No state/matrix/registry/gate config was written. All classification and registration "
    "decisions remain with the designated gate owner (R120 G4/G5/G6/G7)."
)
