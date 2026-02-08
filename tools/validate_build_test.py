import argparse
import json
import sys
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parents[1]
DATA_DIR = REPO_ROOT / "data"
BUILDS_DIR = REPO_ROOT / "builds"


def load_json(path: Path):
    try:
        with path.open("r", encoding="utf-8") as f:
            return json.load(f)
    except FileNotFoundError:
        print(f"[ERROR] File not found: {path}", file=sys.stderr)
        sys.exit(1)
    except json.JSONDecodeError as e:
        print(f"[ERROR] Invalid JSON in {path}: {e}", file=sys.stderr)
        sys.exit(1)


def index_by_id(items, id_key="id"):
    return {item[id_key]: item for item in items if id_key in item}


def validate_build_structure(build):
    errors = []

    required_top = ["id", "name", "bars", "gear", "cp"]
    for key in required_top:
        if key not in build:
            errors.append(f"Missing top-level key: {key}")

    bars = build.get("bars", {})
    for bar_name in ["front", "back"]:
        if bar_name not in bars:
            errors.append(f"Missing bar: {bar_name}")
            continue
        slots = bars[bar_name].get("slots")
        if not isinstance(slots, dict):
            errors.append(f"Bar '{bar_name}' slots must be an object with keys '1'-'5' and 'ult'")
            continue
        for slot_key in ["1", "2", "3", "4", "5", "ult"]:
            if slot_key not in slots:
                errors.append(f"Bar '{bar_name}' missing slot key: {slot_key}")

    cp = build.get("cp", {})
    for tree in ["warfare", "fitness", "craft"]:
        if tree not in cp:
            errors.append(f"CP tree missing: {tree}")

    return errors


def validate_references(build, skills_idx, sets_idx, cp_idx):
    errors = []

    # Bars -> skills
    bars = build.get("bars", {})
    for bar_name, bar_data in bars.items():
        slots = (bar_data or {}).get("slots", {})
        for slot_key, slot_value in slots.items():
            if not slot_value:
                continue
            skill_id = slot_value.get("skill_id")
            if not skill_id:
                errors.append(f"Bar '{bar_name}' slot '{slot_key}' missing skill_id")
                continue
            if skill_id not in skills_idx:
                errors.append(f"Bar '{bar_name}' slot '{slot_key}' references unknown skill_id: {skill_id}")

    # Gear -> sets
    gear = build.get("gear", {})
    for slot_name, gear_item in gear.items():
        if not gear_item:
            continue
        set_id = gear_item.get("set_id")
        if not set_id:
            errors.append(f"Gear slot '{slot_name}' missing set_id")
            continue
        if set_id not in sets_idx:
            errors.append(f"Gear slot '{slot_name}' references unknown set_id: {set_id}")

    # CP -> cp_stars
    cp = build.get("cp", {})
    for tree_name, star_ids in cp.items():
        for star_id in star_ids:
            if star_id not in cp_idx:
                errors.append(f"CP tree '{tree_name}' references unknown cp_star id: {star_id}")

    return errors


def main():
    parser = argparse.ArgumentParser(
        description="Validate a test ESO build JSON against Phase 1 data files."
    )
    parser.add_argument(
        "build_path",
        nargs="?",
        default=str(BUILDS_DIR / "test-dummy.json"),
        help="Path to build JSON (default: builds/test-dummy.json)",
    )
    args = parser.parse_args()

    build_path = Path(args.build_path)

    skills_data = load_json(DATA_DIR / "skills.json")
    effects_data = load_json(DATA_DIR / "effects.json")
    sets_data = load_json(DATA_DIR / "sets.json")
    cp_data = load_json(DATA_DIR / "cp-stars.json")

    skills_idx = index_by_id(skills_data.get("skills", []))
    sets_idx = index_by_id(sets_data.get("sets", []))
    cp_idx = index_by_id(cp_data.get("cp_stars", []))

    build = load_json(build_path)

    structure_errors = validate_build_structure(build)
    reference_errors = validate_references(build, skills_idx, sets_idx, cp_idx)

    all_errors = structure_errors + reference_errors

    result = {
        "build_id": build.get("id"),
        "build_name": build.get("name"),
        "status": "OK" if not all_errors else "ERROR",
        "error_count": len(all_errors),
        "errors": all_errors,
    }

    print(json.dumps(result, indent=2, ensure_ascii=False))

    if all_errors:
        sys.exit(1)
    sys.exit(0)


if __name__ == "__main__":
    main()
