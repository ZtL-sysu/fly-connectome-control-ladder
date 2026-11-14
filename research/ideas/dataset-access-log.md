# Dataset / asset access log

- Official flyvis averaged connectome spec directly acquired in sources/flyvis/flyvis/connectome/fib25-fib19_v2.2.json, public GitHub source archive, no access request. Source code MIT per repository; data provenance/license must follow original source and paper attribution. This model is not individual MaleCNS.
- Official MovingEdge generation source directly acquired; procedural moving visual edges with direction labels from generator parameters, no approval required. Public task code and deterministic stimulus identities must be frozen before any run.
- Existing MaleCNS/CIFAR/digits prior tests are exposed historical evidence; no holdout claims may be recycled.
- Original natural optic-flow/Sintel data and pretrained models: direct sources/license to be verified by task21782; not declared accessible on the basis of documentation alone.
- No private/paid/restricted assets accepted. Full dataset access gate not yet passed.

## Direct Sintel access check — 2026-11-11

Official download/license pages were retrieved: https://sintel.is.tue.mpg.de/downloads and https://sintel.is.tue.mpg.de/license. Research use is noncommercial and the data may not be redistributed; this is publicly downloadable research data, not an unrestricted redistribution license. The flow labels for the official test set are withheld. Any autonomous confirmation must use a prospectively frozen, scene-disjoint split of the labelled training sequences; no benchmark test-submission claim.

Executed code-audit/inspect_public_sintel.py in local Conda ceg_snn_mi. The HTTPS archive returned byte ranges directly without login/approval. Parsed the 5,627,783,629-byte archive's central directory (8,753 entries, 23 training sequences) and downloaded one PNG and matching .flo from training scene alley_1. Both ZIP CRC checks passed; PNG dimensions436×1024 and flow dimensions436×1024×2 passed header/length checks. Actual transfer4,631,067bytes. Hashes, URL, ETag and range requests are in sources/sintel-access-sample/access-manifest.json.

This establishes direct access and two sample formats, not complete acquisition, full data integrity, rendering equivalence, trainability or experimental results. Scene alley_1 is engineering-exposed and may only be used in development/training. Do not put licensed sample data in paper/source deliverables. Sintel is naturalistic rendered imagery; do not describe it as real-world camera footage. Full flow adaptation and scene split remain unaccepted.

## Official pretrained flyvis models — actual acquisition

Executed code-audit/acquire_official_flyvis_models.py with Conda. The publisher's documented public download settings yielded results_pretrained_models.zip (3,417,042bytes), SHA25671c78d4070556a536b13b23ee3139cd2788aa2a9d07d430a223b4edead281db1, exactly matching the checksum in official flyvis source. Safely extracted353 archive entries /5,255,400 uncompressed bytes under sources/flyvis-pretrained-access/unpacked. Manifest saved in that folder's parent; no model loaded or executed.

The public model archive closes the previous access uncertainty; task-level recovery/inference remains to be tested. A pretrained-model acute rewiring experiment is a different estimand from a shared from-scratch architecture comparison. Match checkpoint, readout, state and stimulus mapping across each acute control. Never compare pretrained bio to from-scratch null and interpret the difference as an adjacency effect.
