from pathlib import Path
import subprocess
from pydantic import AnyHttpUrl
import yt_dlp

from config import InputSource

def download_yt_video(url: AnyHttpUrl) -> Path:
    ydl_opts = {
        "format": "bestaudio/best",
        "postprocessors": [{"key": "FFmpegExtractAudio", "preferredcodec": "wav"}],
        "outtmpl": "bin/audio.tmp.%(ext)s",
        "noplaylist": True,
        "quiet": True,
        "no_warnings": True,
    }

    with yt_dlp.YoutubeDL(ydl_opts) as ydl:
        info_dict = ydl.extract_info(url.encoded_string(), download=True)

        return Path(ydl.prepare_filename(info_dict)).with_suffix(".wav")


def convert_to_wav(src_path: Path, out_path: Path, verbose=False) -> None:
    if not src_path.exists():
        raise Exception(
            f"ERROR: Failed to convert to wav, source path {src_path} doesnt exit"
        )

    if verbose:
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


def prepare_audio_file_for_whisper(input_src: InputSource, pre_whisper_path: Path):
    match input_src:
        case AnyHttpUrl() as url:
            print(f"🌐 Treating as YouTube: {url}")
            yt_download = download_yt_video(url)
            convert_to_wav(yt_download, pre_whisper_path)

            yt_download.unlink()
        case Path() as path:
            print(f"📁 Treating as Local File: {path}")
            convert_to_wav(path, pre_whisper_path)

    if not pre_whisper_path.exists():
        raise Exception(f"Pre whisper audio path does not exist: {pre_whisper_path}")
