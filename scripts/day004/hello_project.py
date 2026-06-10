import sys

PROJECT_NAME = "VideoGen-Builder-100"
DAY = "Day004"
TOPIC = "Python project entry"
SCRIPT_NAME = "hello_project.py"

def build_message() -> str:
    """Build a small, readable status message for Day004."""
    lines = [
    f"Project: {PROJECT_NAME}",
    f"Day: {DAY}",
    f"Topic: {TOPIC}",
    f"Python: {sys.version.split()[0]}",
    f"Script: {SCRIPT_NAME}",
    "Status: OK",
    ]


    return "\n".join(lines)


def main() -> None:
    print(build_message())
    
if __name__ == "__main__":
    main()