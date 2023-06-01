import record
import speechToText
import textToSpeech

# 音声を録音
record.record()
# テキストに書き出し
text = speechToText.speechToText()
# テキストから読み上げ音声を生成し出力
textToSpeech.textToSpeech(text)