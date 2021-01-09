# -*- coding: utf8 -*-
# paired_comparison_method/vote_aggregate.py
# made by kazuya yuda.

import math
import itertools
import pandas as pd
import csv
import subprocess
import re
import numpy as np
import datetime

def welcome_mes(): # 起動時のメッセージ
    print("Welcome to 一対比較法得票集計システムver2:2021,1,3")
    print("paired comparison method vote data aggregate software, PCVS")
    print("made by kazuya yuda.")

def import_csv(): # 試料読み込み
    material=[]
    info=[]

    # ファイル名確認
    return_code = subprocess.check_output(['ls','./../selector'])
    code = return_code.split(b"\n")
    for i in range(len(code)):
        stdout_txt = str(code[i]).replace("b","").replace('\'',"")
        if re.search("csv",stdout_txt) and stdout_txt != "sample_info.csv":
            print(stdout_txt)
    print("拡張子を含めて、解析したいmainデータファイル名を入力してください")
    filename = './../selector/' + input()
    print(filename,end=" ")
    print("を読み込みました.")
    print("集計開始してよろしいですか?y,n:", end=" ")
    ans = input()
    if ans == "n":
        print("終了します。")
    elif ans == "y":
        # main file のインポート
        csv_file = open(filename, "r", encoding="utf_8", errors="", newline="" )
        f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
        header = next(f)
        #print(header[1:]) # ヘッダーを出力
        for row in f: # データ読み込み
            #print(row[1:])
            material.append(row[1:])

        # info file　のインポート
        filename2 = filename.replace("main","info")
        csv_file = open(filename2, "r", encoding="utf_8", errors="", newline="" )
        f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
        header = next(f)
        #print(header[1:]) # ヘッダーを出力
        for row in f: # データ読み込み
            #print(row[1:])
            info.append(row[1:])
    else:
        pass

    # まとめる
    material_result=['','']
    material_result[0] = info
    material_result[1] = material

    return material_result

def get_k(info):
    k = int(str(info[2]).replace("[","").replace("]","").replace("\'",""))
    return k

def get_n(info):
    n = int(str(info[4]).replace("[","").replace("]","").replace("\'",""))
    return n

def get_uname(info):
    uname = str(info[0]).replace("[","").replace("]","").replace("\'","")
    return uname

def f_calculation(info):
    k = get_k(info)
    k_1 = k * (k-1) * (k-2)
    k_2 = (k-4) * (k-4)
    f = float(k_1/k_2)
    return f

def zeta_calculation(f,d,info):
    k = get_k(info)
    if k % 2 == 0:
        print("試料数k：偶数")
        v_1 = 24*d
        v_2 = (k^3) - (4*k)
        v_3 = float(v_1/v_2)
        zeta = 1 - v_3
    else:
        print("試料数k：奇数")
        v_1 = 24*d
        v_2 = (k^3) - (k)
        v_3 = float(v_1/v_2)
        zeta = 1 - v_3

    return zeta

def chi_2_0_caluculation(f,d,info):
    k = get_k(info)
    v_1 = k-4
    v_2 = k*(k-1)*(k-2)
    v_3 = float(v_2/24)
    chi_2_0 = float(8/v_1) * (float(v_3) - float(d) + 0.5) + float(f)
    return chi_2_0

def make_vote_list_and_calculation(info,material):
    # infoからk,n読み込み
    k = get_k(info)
    n = get_n(info)
    user_name = get_uname(info)

    # list 横軸作成
    vote_list = []
    for i in range(k+1):
        vote_list.append('')

    # list 縦軸作成
    vote_list_all = []
    for i in range(k+1):
        vote_list_all.append(vote_list)

    # 行列変換
    vote_list_all_np = np.array(vote_list_all,dtype=object)

    # 不要行 - 挿入(表示用)
    for i in range(k+1):
        vote_list_all_np[i][i] = '-'

    # 横軸iconより縦軸iconの方が大きい(表示用)
    vote_list_all_np[0][0] = 'i>j'

    # 提示試料情報抽出(表示用)
    get_icon = info[3]
    icon = get_icon[0].replace("[","").replace("]","").replace("\'","").replace("\"","").replace(" ","").split(',')

    # 提示試料情報セット(表示用)
    count = 0
    for send_icon in icon:
        vote_list_all_np[0][count+1] = send_icon
        vote_list_all_np[count+1][0] = send_icon
        count += 1

    # 得票挿入
    for i in range(n):
        selector = int(material[i][2])
        yoko = icon.index(str(material[i][selector]))
        selector2 = 0 if selector == 1 else 1
        tate = icon.index(str(material[i][selector2]))

        # add 1 point
        vote_list_all_np[yoko+1][tate+1] = 1

        # add 0 point
        vote_list_all_np[tate+1][yoko+1] = 0

    # 得票行列表示
    print("得票表")
    print(vote_list_all_np)

    now = datetime.datetime.now()
    print("viewファイルファイルを作成しますか？y,n:",end=" ")
    ans = input()
    if ans == "y":
        np.savetxt('./view_data/' + user_name + now.strftime('%Y%m%d_%H%M%S') + '.csv', vote_list_all_np, delimiter=',', fmt='%s')
        print("表示用ファイルが保存されました。")
    else:
        print("表示用ファイルは保存されませんでした。")

    # 計算用記号→0
    for i in range(k+1):
        vote_list_all_np[i][i] = 0

    # 計算用記号→0
    vote_list_all_np[0][0] = 0

    # 計算用提示試料情報→0
    count = 0
    for send_icon in icon:
        vote_list_all_np[0][count+1] = 0
        vote_list_all_np[count+1][0] = 0
        count += 1

    vote_sum = np.sum(vote_list_all_np, axis=1)

    print("得票 a_i：",end=" ")
    print(vote_sum)
    print("得票 Σa_i：",end=" ")
    print(np.sum(vote_sum))

    vote_calc_result = 0
    for i in range(k):
        vote_calc = vote_sum[i]*(vote_sum[i] - 1)
        vote_calc_result += vote_calc

    d = float(1/ 6) * float(k) * (float(k)-1.0) * (float(k)-2.0) - 0.5 * float(vote_calc_result)

    f = f_calculation(info)
    print("自由度f：",end=" ")
    print(f)

    zeta = zeta_calculation(f,d,info)
    print("一意性係数ζ ：",end=" ")
    print(zeta)

    chi_2_0 = chi_2_0_caluculation(f,d,info)
    print("カイ二乗値：",end=" ")
    print(chi_2_0)

    print("一巡三角形の個数は：",end=" ")
    print(d,end=" 個")
    print("ですが、一致性解析用ファイルを作成しますか？y,n:",end=" ")
    ans = input()
    if ans == "y":
        np.savetxt('./analyze_data/' + user_name + now.strftime('%Y%m%d_%H%M%S') + '.csv',vote_list_all_np, delimiter=',', fmt='%d')
        print("解析用ファイルが保存されました。")
    else:
        print("解析用ファイルは保存されませんでした。")

    return d

def main():
    welcome_mes()
    material = import_csv()
    info = material[0]
    main = material[1]

    d = make_vote_list_and_calculation(info,main)
    print("一巡三角形の個数：",end=" ")
    print(d)

    f = f_calculation(info)
    print("自由度f：",end=" ")
    print(f)

    zeta = zeta_calculation(f,d,info)
    print("一意性係数ζ ：",end=" ")
    print(zeta)

    chi_2_0 = chi_2_0_caluculation(f,d,info)
    print("カイ二乗値：",end=" ")
    print(chi_2_0)

if __name__ == "__main__":
    main()
