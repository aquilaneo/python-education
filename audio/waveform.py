import numpy as np
import wave
import matplotlib.pyplot as plt

# WAVEファイル読み取り
wave_file = wave.open("s_s005.wav", "r")

# WAVEファイルの情報表示
print("チャンネル数:", wave_file.getnchannels())
print("量子化ビット数[Byte]:", wave_file.getsampwidth())
print("サンプリング周波数[Hz]:", wave_file.getframerate())
print("フレーム数:", wave_file.getnframes())

# WAVEファイルから全フレーム読み取って変数に
data = wave_file.readframes(wave_file.getnframes())

# 16ビット整数型でNumpy配列にする
x = np.frombuffer(data, dtype="int16")

# グラフ表示
plt.plot(x)
plt.show()

# WAVEファイルを閉じる
wave_file.close()
