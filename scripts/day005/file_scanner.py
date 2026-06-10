from pathlib import Path


PROJECT_NAME = "VideoGen-Builder-100"
DAY = "Day005"
TOPIC = "pathlib and minimal file scan"
SCAN_DIR = Path("scripts/day004")


def get_project_root() -> Path:
    """Return the project root based on this script location."""
    return Path(__file__).resolve().parents[2]


def collect_files(scan_dir: Path) -> list[Path]:
    """Collect files directly under the scan directory."""
    files = []

    for path in scan_dir.iterdir():
        if path.is_file():
            files.append(path)

    return sorted(files)


def format_file_info(file_path: Path, project_root: Path) -> str:
    """Format one file as a readable report line."""
    relative_path = file_path.relative_to(project_root)
    suffix = file_path.suffix or "(no suffix)"

    return (
        f"- {relative_path.as_posix()} "
        f"| name: {file_path.name} "
        f"| suffix: {suffix}"
    )


def build_report() -> str:
    """Build a small report for the Day005 file scan."""
    project_root = get_project_root()
    scan_dir = project_root / SCAN_DIR

    lines = [
        f"Project: {PROJECT_NAME}",
        f"Day: {DAY}",
        f"Topic: {TOPIC}",
        f"Project root: {project_root}",
        f"Scan directory: {SCAN_DIR.as_posix()}",
    ]

    if not scan_dir.exists():
        lines.append("Status: scan directory not found.")
        return "\n".join(lines)

    if not scan_dir.is_dir():
        lines.append("Status: scan path is not a directory.")
        return "\n".join(lines)

    files = collect_files(scan_dir)

    lines.append(f"Files found: {len(files)}")

    if files:
        lines.append("File list:")
        for file_path in files:
            lines.append(format_file_info(file_path, project_root))
    else:
        lines.append("File list: (empty)")

    lines.append("Status: OK")

    return "\n".join(lines)


def main() -> None:
    print(build_report())


if __name__ == "__main__":
    main()