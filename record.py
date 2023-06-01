# pyaudioというライブラリを使ってwavファイルを生成する
import pyaudio
import wave
# バッファサイズ（録音の遅延）
CHUNK = 2**10
FORMAT = pyaudio.paInt16
# 使用するマイクの本数
CHANNELS = 1
RATE = 44100
record_time = 5
output_path = "/home/user/Documents/hogehoge/VoiceToTextToVoice/rec.wav"

# インスタンス生成
p = pyaudio.PyAudio()
stream = p.open(format=FORMAT,
                channels=CHANNELS,
                rate=RATE,
                input=True,
                frames_per_buffer=CHUNK)

def record():
    print("録音を開始します...")
    # ここにバッファごとに録音された信号を追加していく
    frames = []
    for i in range(0,int(RATE/CHUNK * record_time)):
        data = stream.read(CHUNK)
        frames.append(data)
    print("録音終了")
    stream.stop_stream()
    stream.close()
    p.terminate()    

    wf = wave.open(output_path,'wb')
    wf.setnchannels(CHANNELS)
    wf.setsampwidth(p.get_sample_size(FORMAT))
    wf.setframerate(RATE)
    wf.writeframes(b''.join(frames))
    wf.close()



