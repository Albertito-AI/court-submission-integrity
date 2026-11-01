"""Reproduce published fictional observations, not a legal-accuracy benchmark."""
from __future__ import annotations
import argparse
import hashlib
import json
from pathlib import Path
import sys

from court_integrity.engine import check_submission
from court_integrity.__main__ import load_package
from court_integrity.intake import extract_document, prepare_package

HERE = Path(__file__).resolve().parent
RECORD = HERE / "demo-observations.json"


def observations() -> dict:
    """Compute stable results from the checked-in fictional examples, offline."""
    result = {"record_schema": "1", "scope": "FICTIONAL_INTERNAL_DEMONSTRATION",
              "independent_evaluation": "NOT_PERFORMED", "cases": {}}
    for name in ("adverse", "matched", "unknown", "intake"):
        if name == "intake":
            library, _ = load_package(HERE / "intake_sources.json")
            package, manifest = prepare_package(
                extract_document(HERE / "intake_submission.txt"), library["sources"],
                jurisdiction="FICTIONAL")
            inputs = ("intake_submission.txt", "intake_sources.json")
        else:
            package, _ = load_package(HERE / f"{name}.json")
            inputs = (f"{name}.json",)
        report = check_submission(package)
        case = {"engine_version": report["engine_version"],
                "input_sha256": {p: hashlib.sha256((HERE / p).read_bytes()).hexdigest() for p in inputs},
                "package_digest": report["package_digest"],
                "status": report["overall_status"],
                "filing_decision": report["automatic_filing_decision"],
                "truth_certification": report["truth_certification"],
                "finding_counts": report["finding_counts"],
                "finding_codes": sorted({f["code"] for f in report["findings"]}),
                "citation_text_statuses": [row["text_status"] for row in report["citation_checks"]]}
        if name == "intake":
            case["citation_candidates"] = manifest["candidate_count"]
            case["citation_coverage"] = manifest["citation_coverage"]
        result["cases"][name] = case
    return result


def main(argv=None) -> int:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--check", action="store_true", help="compare with committed demo observations")
    args = parser.parse_args(argv)
    try:
        actual = observations()
        if args.check:
            saved = json.loads(RECORD.read_text(encoding="utf-8"))
            if saved != actual:
                print("Published fictional observations differ from current execution; review the change.", file=sys.stderr)
                return 1
            print("PASS: four fictional observations reproduced; no truth or court-readiness certification.")
        else:
            print(json.dumps(actual, ensure_ascii=False, sort_keys=True, indent=2))
    except (OSError, ValueError) as exc:
        print(f"Demo verification failed: {exc}", file=sys.stderr)
        return 2
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
