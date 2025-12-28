from pathlib import Path
import shutil
import sys


def check_dependencies() -> None:
    required_dependencies = ["ffmpeg", "ffprobe", "whisper"]

    missing = [tool for tool in required_dependencies if shutil.which(tool) is None]

    if len(missing):
        for tool in missing:
            print(f"Missing {tool}")

        sys.exit(1)


def write_to_file(output_path: Path, content: str) -> None:
    with open(str(output_path), "w") as file:
        file.write(content)
