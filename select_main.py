# -*- coding: utf8 -*-
# Thurston_paired_comparison_method/select_main.py
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
    print("Welcome to サーストン一対比較法実験集計システムver2:2021,1,3")
    print("Thurston paired comparison method data processing software, TPCMDPS")
    print("made by kazuya yuda.")

def exit_all(): # 終了処理
    sys.exit()

def permutations_count(n , r):
    return math.factorial(n) // math.factorial(n - r)

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))

def initial_data_set(): # データ初期設定 
    data=[] # 統合的にデータを保持

    print("被験者情報を入力:",end=" ")
    data.append(input()) # 被験者の名前を格納

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
    for i in itertools.permutations(material, r=2):
        itertools_material.append(i)
    random.shuffle(itertools_material)
    return itertools_material

def confirmation(data): # パラメータ確認フェーズ
    print("パラメータを確認してください↓")
    caption = ["被験者","備考","試料数:","試料:","試行回数:"]
    for i in range(5):
        print(caption[i],end=' ')
        print(data[i])

def start(): # 実験開始処理
    print("実験を開始しますか? y,n:",end=" ")
    if input() == "y":
        print("実験開始します.")
        print("開始時間:")
        print(datetime.datetime.now())
        start_time = datetime.datetime.now()
        return start_time
    else:
        print("中断します,最初からやり直してください.")
        exit_all()
def process(itertools_material,main_data,count,i,option): # メインインターフェース
        print(itertools_material[i])
        print("%d回目 どちらの試料が選ばれましたか?:左 → 0 , 右 → 1 , 戻る→ r" % count)
        ans = input()
        if ans == "r" and i != 0 and option != "final":
            print("何回目に戻りますか?:",end=" ")
            count_val = input()
            if str.isalpha(count_val):
                print("数値を入力してください")
                l = process(itertools_material,main_data,count,i,option)
            else:
                count_change = int(count_val)
                if count_change <= 0:
                    print("0回目以下は存在し得ません.")
                    l = process(itertools_material,main_data,count,i,option)
                elif count_change >= count:
                    print("現在の回数より後へは戻れません.ファイナライズ画面で再度リクエストしてください.")
                    l = process(itertools_material,main_data,count,i,option)
                else:
                    i_change = count_change-1
                    l = process(itertools_material,main_data,count_change,i_change,option)
                    main_data[i_change]=l

                    if option == "final":
                        final_process(itertools_material,main_data,count,i,option)
                    else:
                        l = process(itertools_material,main_data,count,i,option)
        elif ans == "0" or ans == "1":
            l = list(itertools_material[i])
            l.append(ans)
        else:
            print("指定された数値を入力してください,1回目,ファイナライズ時は戻れません.")
            l = process(itertools_material,main_data,count,i,option)
        return l

def final_process(itertools_material,main_data,countneo,i,option): # ファイナライズ
    print("以上で終了です,本当に終了してもよろしいですか?y,n:",end=" ")
    ans = input()
    if ans == "n" and i != 0 and ans != "0":
        print("何回目に戻りますか?:",end=" ")
        count_val = input()
        if str.isalpha(count_val):
            print("数値を入力してください")
            l = process(itertools_material,main_data,count,i,option)
        else:
            count_change = int(count_val)
            if count_change <= 0:
                print("0回目以下は存在し得ません.")
                l = final_process(itertools_material,main_data,countneo,i,option)
            elif count_change >= countneo:
                print("現在の回数より後へは戻れません.指定された回数は存在しません.")
                l = final_process(itertools_material,main_data,countneo,i,option)
            else:
                option = "final"
                i_change = count_change-1
                l = process(itertools_material,main_data,count_change,i_change,option)
                main_data[i_change]=l
                l = final_process(itertools_material,main_data,countneo,i,option)
    else:
        print("終了処理を開始します.")
        print("※ 処理中はプログラムを中断しないでください")

    return main_data

def process_end(): # 終了時間記録
    end_time = datetime.datetime.now()
    return end_time

def result_export_process(data,integration_data,end_time): # CSV形式でエクスポート
    print(data[0:])
    print(integration_data[0:])
    Coulum = ['比較データ左','比較データ右','選択結果']
    df_info = pd.DataFrame(data)
    df_main = pd.DataFrame(integration_data,columns=Coulum)
    df_info.to_csv("%s%s%s_result_info.csv" % (data[0],"-",end_time))
    df_main.to_csv("%s%s%s_result_main.csv" % (data[0],"-",end_time))

def main(): # メインops
    welcome_mes() # welcomeメッセージ生成

    data = initial_data_set() # データ初期設定後dataへ格納

    material = material_get(data[2]) # 試料情報を格納する
    data.append(material[0:])

    N = int(data[2]) # 試料数取得

    try_num = permutations_count(N,2) # 試行回数取得(順列を計算)
    data.append(try_num)

    itertools_material = itertools_make_material(material) # 試料をシャッフル,取り出し

    confirmation(data) # パラメータ確認フェーズ

    # start
    data.append(start())
    
    main_data=[] # 一対比較の実験データ格納用
    
    option="none"
    for i in range(try_num): # 試行回数分イテレーション
        count = i + 1
        main_data.append(process(itertools_material,main_data,count,i,option))

    # finalaize開始
    option="final"
    main_data = final_process(itertools_material,main_data,try_num+1,i,option)
    integration_data = main_data

    # end
    end_time = process_end()
    data.append(end_time)

    # export
    result_export_process(data,integration_data,end_time)

if __name__ == "__main__":
    main()
