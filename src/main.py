import argparse
from pathlib import Path
import sys
from pydantic import ValidationError
from yt_dlp.utils import DownloadError

from audio import prepare_audio_file_for_whisper
from config import CLIConfig
from transcriber import transcribe
from utils import check_dependencies, write_to_file


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument(
        "--input_src",
        type=str,
        help="Youtube Link or absolute path of video/audio file of any type",
    )
    parser.add_argument(
        "--output_src",
        type=str,
        help="File path to where the transcription should be printed",
    )
    parser.add_argument("--model", type=str, help="Model size for Open AI's Whisper")
    parser.add_argument(
        "--verbose", type=bool, default=False, help="Get more indepth logs"
    )

    args = vars(parser.parse_args())

    config = CLIConfig.model_validate(args)

    # GTODO: Good candidate for env variable
    pre_whisper_audio_path = Path("bin/audio.wav")

    prepare_audio_file_for_whisper(config.input_src, pre_whisper_audio_path)

    print(f"Path of the wav file to feed to whisper: {pre_whisper_audio_path}")

    transcription = transcribe(pre_whisper_audio_path, config.model, config.verbose)

    write_to_file(config.output_src, transcription)

    pre_whisper_audio_path.unlink()

    sys.exit(1)


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
