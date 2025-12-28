# LocalScribe - Local Video/Audio Transcription CLI

Built a privacy-preserving CLI tool to transcribe video and audio fully offline. This utilizes `FFmpeg` and OpenAI's `Whisper` locally.

## Install

Please follow FFmpeg's installation guide if you are not in a Linux machine.

```
sudo apt install ffmpeg

```

Once `FFmpeg` is installed clone this repository and run
```
```

```
uv sync
```

This should grab necessary dependencies such as `whisper`

Once done you can run

```
uv run src/main.py --input_src [INPUT_SRC] --ouput_src_dir [OUTPUT_SRC_DIRECTORY] --model [WHISPER_MODEL]
```

The output will be `.txt` file with a timestamp to whichever directory provided.




