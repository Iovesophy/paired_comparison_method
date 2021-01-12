# -*- coding: utf8 -*-
# paired_comparison_method/z_calculation.py
# made by kazuya yuda.

import pandas as pd
import csv
import subprocess
import re
import numpy as np
import sys
import datetime
from statistics import NormalDist

def welcome_mes(): # 起動時のメッセージ
    print("Welcome to 一対比較法z計算システムver2:2021,1,3")
    print("paired comparison method z calculation software, PCZS")
    print("made by kazuya yuda.")

def import_csv(n): # 試料読み込み
    material=['','','']
    # ファイル名確認
    return_code = subprocess.check_output(['ls','./plot_data'])
    code = return_code.split(b"\n")
    for i in range(len(code)):
        stdout_txt = str(code[i]).replace("b","").replace('\'',"")
        if re.search("csv",stdout_txt):
            print(stdout_txt)
    print("拡張子を含めて、一致性確認済みの解析データファイル名を入力してください")
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
    if re.search("csv",filename) and filename != "":
        array = np.loadtxt('./plot_data/'+filename, delimiter=',')
        material[0] = conversion_p(array,n)
        print(material[0])
    elif filename == "csv":
        print("csvファイルを指定してください。")
        sys.exit()
    else:
        print("csvファイルを指定してください")
        sys.exit()

    info=[]
    return_code = subprocess.check_output(['ls','./../selector'])
    code = return_code.split(b"\n")
    for i in range(len(code)):
        stdout_txt = str(code[i]).replace("b","").replace('\'',"")
        if re.search("csv",stdout_txt) and stdout_txt != "sample_info.csv":
            print(stdout_txt)
    print("拡張子を含めて、現在解析中の関連mainデータファイル名を入力してください(実験基本情報をロードするため)")
    filename = './../selector/' + input()
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
    filename2 = filename.replace("main","info")
    csv_file = open(filename2, "r", encoding="utf_8", errors="", newline="" )
    f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
    header = next(f)
    for row in f: # データ読み込み
        info.append(row[1:])

    material[1] = info

    return material

def get_n():
    path = './n.txt'
    with open(path) as f:
        s = f.read()
    return int(s)

def get_k(info):
    k = int(str(info[2]).replace("[","").replace("]","").replace("\'",""))
    return k

def conversion_p(array,n):
    conversion_array = array/n
    np.place(conversion_array, conversion_array == 0, 0.5)
    return conversion_array

def conversion_z(array):
    it = np.nditer(array, flags=['multi_index'])
    for x in it:
    # パラメータ指定がないと、標準正規分布(mu = 0およびsigma = 1)に自動補完される。
        #print(array[it.multi_index[0],it.multi_index[1]])
        #print(NormalDist().inv_cdf(array[it.multi_index[0],it.multi_index[1]]))
        array[it.multi_index[0],it.multi_index[1]] = NormalDist().inv_cdf(array[it.multi_index[0],it.multi_index[1]])
    print(array)

def main():
    welcome_mes()
    material_import = import_csv(get_n())
    k = get_k(material_import[1])
    conversion_array = material_import[0]
    conversion_z(conversion_array)



if __name__ == "__main__":
    main()
