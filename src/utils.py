import shutil
import sys


def check_dependencies() -> None:
    required_dependencies = ["ffmpeg", "ffprobe"]

    missing = [tool for tool in required_dependencies if shutil.which(tool) is None]

    if len(missing):
        for tool in missing:
            print(f"Missing {tool}")

        sys.exit(1)
