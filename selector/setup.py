# -*- coding: utf8 -*-
# paired_comparison_method/select_main.py
# made by kazuya yuda.
import time
import datetime
import math
import itertools
import sys
import random
import pandas as pd
import csv

def welcome_mes(): # 起動時のメッセージ
    print("Welcome to 対比較法実験設定プログラムver2:2021,1,3")
    print("Paired comparison method data processing software, Setting mode")
    print("made by kazuya yuda.")

def exit_all(): # 終了処理
    sys.exit()

def process_end(): # 終了時間記録
    end_time = datetime.datetime.now()
    return end_time

def permutations_count(n , r):
    return math.factorial(n) // math.factorial(n - r)

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

def initial_data_set(): # データ初期設定 
    data=[] # 統合的にデータを保持

    print("設定ファイルを生成:",end=" ")
    data.append("setting_file") # 被験者の名前を格納

    print("備考:",end=" ")
    data.append(input()) # 被験者についての備考を格納

    print("試料数を入力:",end=" ")
    n = input()
    if int(n) < 2:
        print("試料数が足りません.")
        exit_all()
    data.append(int(n)) # 試料数を格納
    print("%s を設定しました" % n)
    return data

def material_get(n): # 試料読み込み
    material=[]
    print("試料情報をcsvから読み込みますか?y,n:", end=" ")
    if input() == n:
        for i in range(int(n)):
            count = i + 1
            print("試料%dの提示したい情報を入力:" % count , end=" ")
            material.append(input())
    else:
        csv_file = open("./sample_info.csv", "r", encoding="utf_8", errors="", newline="" )
        f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
        header = next(f)
        print(header) # ヘッダーを出力
        count = 0
        for row in f: # データ読み込み
            if count == int(n):
                break
            else:
                count += 1
                print(row)
                material.append(row[1])
    return material

def itertools_make_material(material): # 試行回数分一対比較用の比較試料生成
    itertools_material=[]
    for i in itertools.combinations(material, r=2):
        itertools_material.append(i)
    random.shuffle(itertools_material)
    return itertools_material

def confirmation(data): # パラメータ確認フェーズ
    print("パラメータを確認してください↓")
    caption = ["被験者","備考","試料数:","試料:","試行回数:"]
    for i in range(5):
        print(caption[i],end=' ')
        print(data[i])

def result_export_process(data,end_time): # CSV形式でエクスポート
    print(data[0:])
    df_info = pd.DataFrame(data)
    df_info.to_csv("./data/%s_info.csv" % (data[0]))

def main(): # メインops
    welcome_mes() # welcomeメッセージ生成

    data = initial_data_set() # データ初期設定後dataへ格納

    material = material_get(data[2]) # 試料情報を格納する
    data.append(material[0:])

    N = int(data[2]) # 試料数取得

    try_num = combinations_count(N,2) # 試行回数取得(組み合わせを計算)
    data.append(try_num)

    itertools_material = itertools_make_material(material) # 試料をシャッフル,取り出し

    confirmation(data) # パラメータ確認フェーズ

    # end
    end_time = process_end()
    data.append(end_time)

    # export
    result_export_process(data,end_time)

if __name__ == "__main__":
    main()
