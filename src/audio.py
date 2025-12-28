from pathlib import Path
import subprocess
from pydantic import AnyHttpUrl
import yt_dlp


# GTODO: make wav an environment variable for outtmpl and extension
# Also look into creating FFmpegConverAudioPP
def download_yt_video(url: AnyHttpUrl) -> Path:
    ydl_opts = {
        "format": "bestaudio/best",
        "postprocessors": [{"key": "FFmpegExtractAudio", "preferredcodec": "wav"}],
        "outtmpl": "bin/audio.tmp.%(ext)s",  # Try Path(./bin/audio.wav)
        "noplaylist": True,
        "quiet": True,
        "no_warnings": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url.encoded_string(), download=True)

        return Path(ydl.prepare_filename(info_dict)).with_suffix(".wav")


def convert_to_wav(src_path: Path, out_path: Path) -> None:
    if not src_path.exists():
        raise Exception(
            f"ERROR: Failed to convert to wav, source path {src_path} doesnt exit"
        )

    print(f"Converting {src_path} -> {out_path} with 16 kHz Sample Rate and Mono")

    process_cmd = [
        "ffmpeg",
        "-y",
        "-i",
        str(src_path),
        "-vn",
        "-acodec",
        "pcm_s16le",
        "-ar",
        "16000",
        "-ac",
        "1",
        str(out_path),
    ]

    result = subprocess.run(
        process_cmd,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    if result.returncode != 0:
        raise Exception(f"Failed to convert {str(src_path)} to wav file")
