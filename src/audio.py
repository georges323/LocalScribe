from pathlib import Path
import subprocess
from pydantic import AnyHttpUrl
import yt_dlp


def download_yt_video(url: AnyHttpUrl) -> None:
    ydl_opts = {
        "format": "bestaudio/best",
        "postprocessors": [{"key": "FFmpegExtractAudio", "preferredcodec": "wav"}],
        "outtmpl": "bin/audio.%(ext)s",  # Try Path(./bin/audio.wav)
        "noplaylist": True,
        "quiet": True,
        "no_warnings": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        ydl.download([url.encoded_string()])

        convert_to_wav(Path("./bin/audio.wav"))


def convert_to_wav(src_path: Path) -> None:
    print(f"Converting: {src_path} -> wav")

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
        "bin/audio.wav",
    ]

    result = subprocess.run(
        process_cmd,
        stdout=subprocess.DEVNULL,
        stderr=subprocess.DEVNULL,
    )

    if result.returncode != 0:
        raise Exception(f"Failed to convert {str(src_path)} to wav file")
