from pathlib import Path
import voicevox_core
from voicevox_core import AccelerationMode, AudioQuery, VoicevoxCore
from playsound import playsound

SPEAKER_ID = 17

open_jtalk_dict_dir = './open_jtalk_dic_utf_8-1.11'
out = Path('output.wav')
acceleration_mode = AccelerationMode.AUTO

def textToSpeech(text) -> None:
    core = VoicevoxCore(
        acceleration_mode=acceleration_mode, open_jtalk_dict_dir=open_jtalk_dict_dir
    )
    core.load_model(SPEAKER_ID)
    audio_query = core.audio_query(text, SPEAKER_ID)
    wav = core.synthesis(audio_query, SPEAKER_ID)
    out.write_bytes(wav)
    playsound(out)