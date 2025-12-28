from pathlib import Path
import torch
import whisper


def transcribe(audio_path: Path, model_name="base", verbose=False) -> str:
    if torch.backends.mps.is_available():
        device = "mps"
    else:
        device = "cpu"

    if verbose:
        print(f"Using '{model_name}' model")
    model = whisper.load_model(model_name, device)

    print("Transcribing...")
    result = model.transcribe(str(audio_path), fp16=False, verbose=verbose)

    return result["text"]
