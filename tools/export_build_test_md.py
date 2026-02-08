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


def render_build_markdown(build, skills_idx, sets_idx, cp_idx):
    lines = []

    lines.append(f"# {build.get('name', 'Unnamed Build')}")
    lines.append("")
    lines.append(f"- ID: `{build.get('id', '')}`")
    meta = build.get("meta", {})
    if meta:
        lines.append(f"- Version: `{meta.get('version', '')}`")
        lines.append(f"- Author: `{meta.get('author', '')}`")
        lines.append(f"- Last updated: `{meta.get('last_updated', '')}`")
    lines.append("")

    lines.append("## Bars")
    lines.append("")
    bars = build.get("bars", {})
    for bar_name in ["front", "back"]:
        bar = bars.get(bar_name)
        if not bar:
            continue
        lines.append(f"### {bar_name.title()} Bar")
        lines.append("")
        weapon_type = bar.get("weapon_type", "")
        if weapon_type:
            lines.append(f"- Weapon type: `{weapon_type}`")
        lines.append("")
        lines.append("| Slot | Skill | Skill ID |")
        lines.append("|------|-------|----------|")
        slots = bar.get("slots", {})
        for slot_key in ["1", "2", "3", "4", "5", "ult"]:
            slot = slots.get(slot_key)
            if not slot:
                lines.append(f"| {slot_key} | *(empty)* | |")
                continue
            skill_id = slot.get("skill_id", "")
            skill = skills_idx.get(skill_id)
            skill_name = skill.get("name") if skill else "(unknown)"
            lines.append(f"| {slot_key} | {skill_name} | `{skill_id}` |")
        lines.append("")

    lines.append("## Gear")
    lines.append("")
    gear = build.get("gear", {})
    lines.append("| Slot | Set | Set ID | Notes |")
    lines.append("|------|-----|--------|-------|")
    for slot_name, gear_item in gear.items():
        if not gear_item:
            lines.append(f"| {slot_name} | *(empty)* | | |")
            continue
        set_id = gear_item.get("set_id", "")
        set_obj = sets_idx.get(set_id)
        set_name = set_obj.get("name") if set_obj else "(unknown)"
        notes = []
        weight = gear_item.get("weight")
        if weight:
            notes.append(f"weight: {weight}")
        weapon_type = gear_item.get("type")
        if weapon_type:
            notes.append(f"type: {weapon_type}")
        trait = gear_item.get("trait")
        if trait:
            notes.append(f"trait: {trait}")
        notes_str = ", ".join(notes)
        lines.append(f"| {slot_name} | {set_name} | `{set_id}` | {notes_str} |")
    lines.append("")

    lines.append("## Champion Points")
    lines.append("")
    cp = build.get("cp", {})
    for tree_name in ["warfare", "fitness", "craft"]:
        stars = cp.get(tree_name, [])
        lines.append(f"### {tree_name.title()} Tree")
        lines.append("")
        if not stars:
            lines.append("_No stars selected._")
            lines.append("")
            continue
        lines.append("| Star | Star ID |")
        lines.append("|------|---------|")
        for star_id in stars:
            star = cp_idx.get(star_id)
            star_name = star.get("name") if star else "(unknown)"
            lines.append(f"| {star_name} | `{star_id}` |")
        lines.append("")

    return "\n".join(lines)


def main():
    parser = argparse.ArgumentParser(
        description="Export a test ESO build JSON to Markdown."
    )
    parser.add_argument(
        "build_path",
        nargs="?",
        default=str(BUILDS_DIR / "test-dummy.json"),
        help="Path to build JSON (default: builds/test-dummy.json)",
    )
    parser.add_argument(
        "-o",
        "--output",
        default=str(BUILDS_DIR / "test-dummy.md"),
        help="Output Markdown path (default: builds/test-dummy.md)",
    )
    args = parser.parse_args()

    build_path = Path(args.build_path)
    output_path = Path(args.output)

    skills_data = load_json(DATA_DIR / "skills.json")
    effects_data = load_json(DATA_DIR / "effects.json")
    sets_data = load_json(DATA_DIR / "sets.json")
    cp_data = load_json(DATA_DIR / "cp-stars.json")

    skills_idx = index_by_id(skills_data.get("skills", []))
    sets_idx = index_by_id(sets_data.get("sets", []))
    cp_idx = index_by_id(cp_data.get("cp_stars", []))

    build = load_json(build_path)

    md = render_build_markdown(build, skills_idx, sets_idx, cp_idx)

    output_path.write_text(md, encoding="utf-8")
    print(f"[INFO] Wrote Markdown to {output_path}")

    sys.exit(0)


if __name__ == "__main__":
    main()
