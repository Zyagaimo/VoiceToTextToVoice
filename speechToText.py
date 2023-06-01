import openai

openai.api_key = 'XXXX'

def speechToText():
    audio_file= open("/home/user/Documents/hogehoge/VoiceToTextToVoice/rec.wav", "rb")
    transcript = openai.Audio.transcribe("whisper-1", audio_file)
    text = transcript.text
    return text