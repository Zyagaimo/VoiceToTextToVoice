# pyaudioというライブラリを使ってmp3ファイルを生成する
import pyaudio
import wave
# バッファサイズ（録音の遅延）
CHUNK = 2**10
FORMAT = pyaudio.paInt16
# 使用するマイクの本数
CHANNELS = 1
RATE = 44100
record_time = 10
output_path = "/home/user/Documents/hogehoge\rec.wav"


