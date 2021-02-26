import os
import matplotlib.pyplot as plt

fileName = "sample4.txt" # ファイル名を変数に置いておく

# ファイルの存在を確認
if os.path.exists(fileName):
    f = open(fileName) # ファイルを開く
    
    data = f.readlines() # 行ごとに区切ってリスト化
    averages = [] # 各月の平均
    count = 1 # 月の番号
    for month in data:
        # データ処理
        rawList = month.split(",")
        floatList = [float(raw) for raw in rawList]

        # 平均を求める
        average = sum(floatList) / len(floatList)
        averages.append(average)

        print(str(count) + "月", average) # 結果表示
        count += 1 # 月番号表示
else:
    print("File not found...")
