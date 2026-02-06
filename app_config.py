import torch
from TTS.api import TTS

def get_model(model_name="xtts_v2"):
    device = "cuda" if torch.cuda.is_available() else "cpu"
    
    # मॉडल का चुनाव (दोनों फ्री हैं)
    if model_name == "tts_5":
        model_path = "tts_models/multilingual/multi-dataset/tts_5"
    else:
        model_path = "tts_models/multilingual/multi-dataset/xtts_v2"
        
    print(f"Loading {model_name} on {device} (Turbo Mode Enabled)...")
    return TTS(model_path).to(device)
  
