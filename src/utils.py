from datetime import datetime
import shutil
import sys

from pydantic import DirectoryPath


def check_dependencies() -> None:
    required_dependencies = ["ffmpeg", "ffprobe", "whisper"]

    missing = [tool for tool in required_dependencies if shutil.which(tool) is None]

    if len(missing):
        for tool in missing:
            print(f"Missing {tool}")

        sys.exit(1)


def write_to_file(output_path: DirectoryPath, content: str) -> None:
    timestamp = datetime.now().strftime("%Y%m%d%H%M%S")
    output_file_path = output_path.absolute().joinpath(f"output_{timestamp}.txt")

    with open(output_file_path, "w") as file:
        file.write(content)

        print(f"Successfully transcribed to: {output_file_path}")
