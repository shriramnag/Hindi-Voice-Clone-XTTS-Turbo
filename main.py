import os
from pydub import AudioSegment
from pydub.silence import split_on_silence
from app_config import get_model

def remove_silence(file_path):
    """ऑडियो से फालतू सन्नाटा हटाना - सुपर फ़ास्ट"""
    audio = AudioSegment.from_file(file_path)
    chunks = split_on_silence(audio, min_silence_len=400, silence_thresh=-45)
    clean_audio = AudioSegment.empty()
    for chunk in chunks:
        clean_audio += chunk
    clean_audio.export(file_path, format="wav")
    print("Silence removal done!")

def run_turbo_clone(model_type, text, voice_sample):
    out = "hindi_cloned_output.wav"
    
    # इंजन लोड करें
    engine = get_model(model_type)
    
    # आवाज़ जनरेशन
    engine.tts_to_file(
        text=text,
        speaker_wav=voice_sample,
        language="hi",
        file_path=out
    )
    
    # साइलेंस हटाना
    remove_silence(out)
    print(f"Success! Output saved as: {out}")

if __name__ == "__main__":
    # आप यहाँ "xtts_v2" या "tts_5" चुन सकते हैं
    run_turbo_clone("xtts_v2", "नमस्ते, आपकी आवाज़ सफलतापूर्वक क्लोन हो गई है।", "sample.wav")
  
