import os
import platform
import sys
from pathlib import Path


def main() -> None:
    project_root = Path(__file__).resolve().parents[1]

    print("VideoGen Builder 100 - 环境检查")
    print("-" * 40)
    print(f"Python 版本: {sys.version.split()[0]}")
    print(f"Python 可执行文件: {sys.executable}")
    print(f"操作系统: {platform.platform()}")
    print(f"当前工作目录: {Path.cwd()}")
    print(f"项目根目录: {project_root}")
    print(f"Conda 环境: {os.environ.get('CONDA_DEFAULT_ENV', '未检测到')}")


if __name__ == "__main__":
    main()