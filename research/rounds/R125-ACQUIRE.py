#!/usr/bin/env python3
"""R125 acquisition map -- READ-ONLY provenance record.

This module does NOT re-run any network request. It records the exact
URL -> local raw file mapping used for the R125 first-hand freeze, plus the
HTTP status / byte count observed at acquisition time.

All responses were fetched with curl -L and saved verbatim (no transform,
no retry-repair, no content substitution). Failed / negative endpoints are
preserved verbatim as negative evidence.

Scope: third-party public small text only. No dataset, weights, binaries,
credentials, or local absolute paths are present in raw/.
"""
from __future__ import annotations

# (local filename, url, observed_http_status, observed_bytes, note)
ACQUISITION = [
    ("biorxiv-v1-source.xml",
     "https://www.biorxiv.org/content/early/2026/06/12/2026.06.10.731214.source.xml",
     429, 17,
     "Official per-version JATS URL taken verbatim from the bioRxiv details API "
     "collection[version=1].jatsxml field (R124 frozen bytes). Cloudflare 1015."),
    ("biorxiv-v1-source2.xml",
     "https://www.biorxiv.org/content/biorxiv/early/2026/06/12/2026.06.10.731214.source.xml",
     429, 17,
     "Alternate /content/biorxiv/early/ path form for the same v1 JATS. Cloudflare 1015."),
    ("biorxiv-v1-full.xml",
     "https://www.biorxiv.org/content/10.64898/2026.06.10.731214v1.full.xml",
     429, 17,
     "DOI-form v1 full XML. Cloudflare 1015."),
    ("jats-v3.xml",
     "https://www.biorxiv.org/content/early/2026/06/23/2026.06.10.731214.source.xml",
     429, 17,
     "Official per-version JATS for version 3 (same URL is also published for "
     "version 4; see date-collision finding). Cloudflare 1015."),
    ("jats-v12.xml",
     "https://www.biorxiv.org/content/early/2026/10/16/2026.06.10.731214.source.xml",
     429, 17,
     "Official per-version JATS for version 12 (current). Cloudflare 1015."),
    ("epmc-fulltext.xml",
     "https://www.ebi.ac.uk/europepmc/webservices/rest/PPR1251441/fullTextXML",
     500, 150,
     "Europe PMC full-text endpoint. HTTP 500 body preserved verbatim. "
     "R124 frozen EPMC lite metadata says hasPDF=N / inEPMC=N / inPMC=N, "
     "so no full text is expected here; the 500 is structural, not a "
     "transient retry candidate."),
    ("epmc-fulltext-v2.xml",
     "https://www.ebi.ac.uk/europepmc/webservices/rest/PPR1251441/fullTextXML?format=xml",
     500, 150,
     "Same endpoint with explicit format parameter. HTTP 500 preserved verbatim."),
    ("epmc-core.json",
     "https://www.ebi.ac.uk/europepmc/webservices/rest/search?query=DOI:10.64898/2026.06.10.731214&resultType=core&format=json",
     200, 6367,
     "Europe PMC core record: full abstractText, licence, dates and "
     "fullTextUrlList. Third independent first-hand endpoint, distinct host "
     "from bioRxiv and Crossref."),
    ("connect-jats.xml",
     "https://connect.biorxiv.org/relate/content/181",
     200, 58714,
     "Auxiliary connect page. Byte-identical to R124's frozen copy "
     "(verified by R125-verify.py, group H); retained for completeness only, "
     "not counted as a new source."),
    ("wayback-cdx.json",
     "https://web.archive.org/cdx/search/cdx?url=biorxiv.org/content/10.64898/2026.06.10.731214v1&output=json&filter=statuscode:200&fl=timestamp,statuscode,digest&limit=5",
     200, 3,
     "Wayback CDX query scoped to the v1 URL with statuscode:200 filter. "
     "Body is the empty JSON array: zero qualifying snapshots at query time."),
    ("wayback-v1.html",
     "https://web.archive.org/web/2026/https://www.biorxiv.org/content/10.64898/2026.06.10.731214v1",
     404, 4657,
     "Wayback snapshot lookup. 404 page preserved verbatim."),
    ("api-jats.json",
     "https://api.biorxiv.org/jats/10.64898/2026.06.10.731214",
     404, 196,
     "Hypothesised api.biorxiv.org JATS endpoint; does not exist. 404 body "
     "preserved verbatim as a negative route result."),
    ("api-details-v1.json",
     "https://api.biorxiv.org/details/biorxiv/10.64898/2026.06.10.731214/1",
     200, 64741,
     "Version-selector probe. Byte-identical to R124's un-suffixed details "
     "response (group I), confirming /1 is NOT a version selector for this "
     "endpoint; R124's negative finding is independently reproduced."),
]

SCOPE_NOTE = (
    "R125 is a READONLY first-hand route-exhaustion acquisition addressing the "
    "open version-attribution evidence gap left by R124 post-review correction "
    "M3 (v1 page abstract has no local byte freeze) and R106 section 6 item R3. "
    "It is NOT a gate pass, NOT a scientific result, NOT a forward pass, and "
    "NOT a score change. No state / matrix / registry / manifest / gate config "
    "was written back. Classification and registration decisions remain with "
    "the designated gate owner (R120 G4/G5/G6/G7)."
)

TIMEPOINT_NOTE = (
    "HTTP 429 / 1015 is a host-specific, time-point-dependent rate limit, NOT "
    "a claim of permanent unavailability: R124 obtained HTTP 200 from "
    "api.biorxiv.org and connect.biorxiv.org, and reported an unsaved 200 / "
    "105400 B response from the v1 HTML page earlier on 2026-11-14. All "
    "negative results below are scoped to the R125 acquisition instant "
    "(2026-11-14 ~17:0x +0800) and the exact URL / host listed."
)
