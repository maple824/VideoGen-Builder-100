from pathlib import Path


def get_project_root() -> Path:
    """Return the project root directory."""
    return Path(__file__).resolve().parents[1]


def main() -> None:
    project_root = get_project_root()

    print("VideoGen-Builder-100")
    print(f"Project root: {project_root}")
    print(f"Script file: {Path(__file__).resolve()}")


if __name__ == "__main__":
    main()