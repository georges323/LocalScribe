import argparse
from pathlib import Path
import sys
from pydantic import AnyHttpUrl, ValidationError
from yt_dlp.utils import DownloadError

from audio import convert_to_wav, download_yt_video
from config import CLIConfig
from utils import check_dependencies


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("--input_src")

    args = vars(parser.parse_args())

    config = CLIConfig.model_validate(args)

    match config.input_src:
        case AnyHttpUrl() as url:
            print(f"🌐 Treating as YouTube: {url}")
            download_yt_video(url)
        case Path() as path:
            print(f"📁 Treating as Local File: {path}")
            convert_to_wav(path)


if __name__ == "__main__":
    check_dependencies()

    try:
        main()
    except ValidationError as e:
        print(f"ERROR: {e}")
    except DownloadError as e:
        print(f"ERROR yt_dlp: {e}")
    finally:
        sys.exit(1)
