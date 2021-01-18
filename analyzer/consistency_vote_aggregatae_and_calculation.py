# -*- coding: utf8 -*-
# paired_comparison_method/consistencay_vote_aggregatae_and_calculation.py
# made by kazuya yuda.

import pandas as pd
import csv
import subprocess
import re
import numpy as np
import datetime
import sys
import datetime

def welcome_mes(): # 起動時のメッセージ
    print("Welcome to 一対比較法得票集計システムver2:2021,1,3")
    print("paired comparison method consistencay vote data aggregate software, PCCS")
    print("made by kazuya yuda.")

def import_csv(): # 試料読み込み
    material=[0]*3
    loop_ans = 0
    count = 0
    n = 1\0
    print("一括で解析済みデータを読み込みますか？y,n:",end = " ")
    all_import_ans = input()
    if all_import_ans == "y":
        # ファイル名確認
        return_code = subprocess.check_output(['ls','./analyze_data'])
        code = return_code.split(b"\n")
        for i in range(len(code)):
            stdout_txt = str(code[i]).replace("b","").replace('\'',"")
            if re.search("csv",stdout_txt):
                filename = stdout_txt
                if filename == "csv":
                    print("エラー:csvファイルを確認してください。")
                    sys.exit()
                elif re.search("csv",filename):
                    pass
                else:
                    print("エラー:csvファイルを確認してください。")
                    sys.exit()
                print(filename,end=" ")
                print("を読み込みました.")
                n += 1
                if count == 0 and filename != "":
                    material[0] = np.loadtxt('./analyze_data/'+filename, delimiter=',')
                    count += 1
                elif filename != "":
                    material[0] += np.loadtxt('./analyze_data/'+filename, delimiter=',')
                else:
                    pass
        if n <= 2:
            print("人数が足りません。")
            sys.exit()
        f = open('n.txt', 'w')
        f.write(str(n))
        f.close()
    elif all_import_ans == "":
        print("中断します。")
        sys.exit()
    else:
        while loop_ans < 2:
            # ファイル名確認
            return_code = subprocess.check_output(['ls','./analyze_data'])
            code = return_code.split(b"\n")
            for i in range(len(code)):
                stdout_txt = str(code[i]).replace("b","").replace('\'',"")
                if re.search("csv",stdout_txt):
                    print(stdout_txt)
            print("拡張子を含めて、一意性を確認済みの解析データファイル名を入力してください")
            filename = input()
            if filename == "csv":
                print("csvファイルを指定してください。")
                sys.exit()
            elif re.search("csv",filename):
                pass
            else:
                print("csvファイルを指定してください。")
                sys.exit()
            print(filename,end=" ")
            print("を読み込みました.")
            if count == 0 and filename != "":
                material[0] = np.loadtxt('./analyze_data/'+filename, delimiter=',')
                count += 1
            elif filename != "":
                material[0] += np.loadtxt('./analyze_data/'+filename, delimiter=',')
            else:
                pass
            print("読み込みを続けますか？y,n:",end=" ")
            ans = input()
            if ans == "n":
                loop_ans = 2
            else:
                n += 1
        if n <= 2:
            print("人数が足りません。")
            sys.exit()
        f = open('n.txt', 'w')
        f.write(str(n))
        f.close()

    info=[]
    return_code = subprocess.check_output(['ls','./../selector/data'])
    code = return_code.split(b"\n")
    for i in range(len(code)):
        stdout_txt = str(code[i]).replace("b","").replace('\'',"")
        if re.search("csv",stdout_txt) and stdout_txt != "sample_info.csv":
            print(stdout_txt)
    filename = './../selector/data/' + 'setting_file_info.csv'
    if filename == "csv":
        print("csvファイルを指定してください。")
        sys.exit()
    elif re.search("csv",filename):
        pass
    else:
        print("csvファイルを指定してください。")
        sys.exit()
    print(filename,end=" ")
    print("を読み込みました.")
    # info file　のインポート
    csv_file = open(filename, "r", encoding="utf_8", errors="", newline="" )
    f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
    header = next(f)
    for row in f: # データ読み込み
        info.append(row[1:])

    material[1] = info
    material[2] = n

    now = datetime.datetime.now()
    print("プロット用ファイルを作成しますか？y,n:",end=" ")
    ans = input()
    if ans == "y":
        np.savetxt('./plot_data/' + "plotdata" + "_calculation_" + now.strftime('%Y%m%d_%H%M%S') + '.csv',material[0], delimiter=',', fmt='%d')
        print("解析用ファイルが保存されました。")
    else:
        print("解析用ファイルは保存されませんでした。")

    return material

def get_k(info):
    k = int(str(info[2]).replace("[","").replace("]","").replace("\'",""))
    return k

def get_array_position():
    material_import = import_csv()
    k = get_k(material_import[1])
    n = int(material_import[2])
    material = material_import[0]
    count = 0
    sum_all = 0
    sum_2 = 0
    for a in range(k-1):
        count += 1
        for b in range(k-count):
            #print(a+1,a+b+2)
            sum_all += int(material[a+1,a+b+2])
            sum_2 += int(material[a+1,a+b+2])**2

    #print(material)
    #print(sum_all,sum_2)
    result=['','','','']
    result[0] = sum_all
    result[1] = sum_2
    result[2] = k
    result[3] = n
    return result

def sigma_calculation(sum_all,sum_2,k,n):
    v_1 = n*k*(n-1)*(k-1)
    v_2 = float(v_1/4)
    sigma_val = v_2 + sum_2 - (n*sum_all)
    return sigma_val

def consistency_u(sigma_val,k,n):
    v_1 = n*k*(n-1)*(k-1)
    u = float((8*sigma_val/v_1)-1)
    return u

def f_calculation(k,n):
    v_1 = n * (n-1) * k * (k-1)
    v_2 = 2*(n-2)** 2
    f = float(v_1/v_2)
    return f

def chi_2_0_caluculation(sigma_val,k,n):
    v_1 = float(4/(n-2))
    v_2 = n*(n-1)*(n-3)*k*(k-1)
    v_3 = 8*(n-2)
    chi_2_0 = v_1 * (sigma_val - float(v_2/v_3))
    return chi_2_0

def main():
    welcome_mes()
    material = get_array_position()
    sum_all = material[0]
    sum_2 = material[1]
    k = material[2]
    n = material[3]
    sigma_val=sigma_calculation(sum_all,sum_2,k,n)
    print("Σ値:",end=" ")
    print(sigma_val)
    print("一致性係数u:",end=" ")
    print(consistency_u(sigma_val,k,n))
    print("自由度f:",end=" ")
    print(f_calculation(k,n))
    print("カイ二乗値:",end="")
    print(chi_2_0_caluculation(sigma_val,k,n))

if __name__ == "__main__":
    main()
