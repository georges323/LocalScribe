# LocalScribe - Local Video/Audio Transcription CLI

Built a privacy-preserving CLI tool to transcribe video and audio fully offline. This utilizes `FFmpeg` and OpenAI's `Whisper` locally.

## Install

FFmpeg is required for this tool:

```
# on Ubuntu or Debian
sudo apt update && sudo apt install ffmpeg

# on MacOS using Homebrew (https://brew.sh/)
brew install ffmpeg

# on Windows using Chocolatey (https://chocolatey.org/)
choco install ffmpeg

# on Windows using Scoop (https://scoop.sh/)
scoop install ffmpeg

```
Once `FFmpeg` is installed clone this repository and run

``` 
uv sync
```

This should grab necessary dependencies such as `whisper`

## Running the CLI

```
uv run src/main.py --input_src [INPUT_SRC] --ouput_src_dir [OUTPUT_SRC_DIRECTORY] --model [WHISPER_MODEL]
```

Whisper model can be:
- `tiny`
- `base` (default)
- `small`
- `medium`
- `large`
- `turbo`

The output will be `.txt` file with a timestamp to whichever directory provided.




