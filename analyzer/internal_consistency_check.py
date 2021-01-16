# -*- coding: utf8 -*-
# paired_comparison_method/internal_consistency_check.py
# made by kazuya yuda.

import pandas as pd
import csv
import subprocess
import re
import numpy as np
import sys
import datetime
from statistics import NormalDist
import math
import pylab

def welcome_mes(): # 起動時のメッセージ
    print("Welcome to 一対比較法内的整合性検定システムver3:2021,1,16")
    print("paired comparison method internal consistency software, PCIC")
    print("made by kazuya yuda.")

def import_npy():
    b=[0]*3
    return_code = subprocess.check_output(['ls','./internal_consistency_data/'])
    code = return_code.split(b"\n")
    for i in range(len(code)):
        stdout_txt = str(code[i]).replace("b","").replace('\'',"")
        if re.search("npy",stdout_txt):
            print(stdout_txt)
    print("一括で解析済みデータを読み込みますか？y,n:",end = " ")
    all_import_ans = input()
    if all_import_ans == "y":
        for i in range(len(code)):
            stdout_txt = str(code[i]).replace("b","").replace('\'',"")
            if re.search("npy",stdout_txt):
                filename = stdout_txt
                if filename == "npy":
                    print("npyファイルを指定してください。")
                    sys.exit()
                elif re.search("npy",filename):
                    pass
                else:
                    print("npyファイルを指定してください。")
                    sys.exit()
                print(filename,end=" ")
                print("を読み込みました.")
                b[i] = np.load('./internal_consistency_data/'+filename)
                print(b[i])
    return b

def get_info():
    filename = './../selector/data/' + 'setting_file_info.csv'
    print(filename,end=" ");print("を読み込みました.")
    csv_file = open(filename, "r", encoding="utf_8", errors="", newline="" )
    f = csv.reader(csv_file, delimiter=",", doublequote=True, lineterminator="\r\n", quotechar='"', skipinitialspace=True)
    header = next(f);info=[]
    for row in f: # データ読み込み
        info.append(row[1:])
    info = info[3][0].replace("[","").replace("]","").replace("\'","").replace(" ","").split(",")
    return info

def get_k(data):
    print(data.shape[1])
    return data.shape[1]

def get_n():
    path = './n.txt'
    with open(path) as f:
        s = f.read()
    if s == "":
        print("一致性の検定が完了していません。")
        sys.exit()
    else:
        return int(s)

def calculation_R(mean,k):
    print(mean[1])
    M_z1j = float(mean[1][0])
    R = [0] * k
    for i in range(k):
        M_zij = float(mean[1][i])
        R[i] = M_zij-(M_z1j)
    return R

def calculation_hatZ(mean,R,k):
    print(R)
    mapping = k-1
    hatZ_array = np.zeros((mapping,mapping))
    np.place(hatZ_array, hatZ_array == 0, 0.5)
    np.place(hatZ_array, hatZ_array == 1, 0.5)

    print(hatZ_array)
    M_z1j = float(mean[1][0])
    rock = 0
    for row in range(mapping):
        col=rock
        hatZ_array[row,col] = R[row+1]
    mapping=mapping-1
    for a in range(mapping):
        for b in range(mapping-a):
            col=a+1;row=a+b+1
            hatZ_array[row,col] = hatZ_array[row,col-1] - hatZ_array[a,a]
    print("hatZ")
    print(hatZ_array)
    return hatZ_array

def swap_p(p,k,mean):
    k=k-1;a_del=np.delete(p,0,0)
    p=np.delete(a_del,0,1)
    print("origin")
    print(p)

    swap_mapdata=[]
    mapdata_origin=get_info()
    mapdata_sorted=list(mean[0])
    for i in range(k+1):
        swap_mapdata.append(mapdata_origin.index(mapdata_sorted[i]))

    col_swap=p[:,swap_mapdata]
    col_swap=col_swap[swap_mapdata,:]
    print("swaped")
    print(col_swap)

    b_del=np.delete(col_swap,0,0)
    col_swap=np.delete(b_del,k,1)
    for row in range(k):
        for col in range(k-1-row):
            col=row+col+1
            col_swap[row,col]=0
    print("result")
    print(col_swap)
    return col_swap

def calculation_arcsin_P(array):
    print("def calculation_arcsin_P(array):")
    it = np.nditer(array, flags=['multi_index'])
    for x in it:
        array[it.multi_index[0],it.multi_index[1]] = math.sqrt(array[it.multi_index[0],it.multi_index[1]])
        array[it.multi_index[0],it.multi_index[1]] = math.asin(array[it.multi_index[0],it.multi_index[1]])
        array[it.multi_index[0],it.multi_index[1]] = math.degrees(array[it.multi_index[0],it.multi_index[1]])
    print(array)
    return array

def calculation_arcsin_hatP(array,k):
    print("def calculation_arcsin_hatP(array):")
    it = np.nditer(array, flags=['multi_index'])
    for x in it:
        array[it.multi_index[0],it.multi_index[1]] = math.sqrt(array[it.multi_index[0],it.multi_index[1]])
        array[it.multi_index[0],it.multi_index[1]] = math.asin(array[it.multi_index[0],it.multi_index[1]])
        array[it.multi_index[0],it.multi_index[1]] = math.degrees(array[it.multi_index[0],it.multi_index[1]])
    k=k-1
    for row in range(k):
        for col in range(k-1-row):
            col=row+col+1
            array[row,col]=0
    print(array)
    return array

def calculation_RSS(p_array,hatp_array):
    array =(p_array-hatp_array)**2
    print(array)
    return np.sum((p_array - hatp_array)**2)

def calculation_hatP(p_array,k):
    k = k-1
    print(k)
    for a in range(k):
        for b in range(k):
            # パラメータ指定がないと、標準正規分布(mu = 0およびsigma = 1)に自動補完される。
            p_array[a,b] = NormalDist().cdf(float(p_array[a,b]))
    print(p_array)
    return p_array

def main():
    welcome_mes()
    data=import_npy()
    mean=data[2]
    k=get_k(mean)
    n=get_n()
    R=calculation_R(mean,k)
    hatZ=calculation_hatZ(mean,R,k)
    p=swap_p(data[0],k,mean)
    hatP=calculation_hatP(hatZ,k)
    rss = calculation_RSS(calculation_arcsin_P(p),calculation_arcsin_hatP(hatP,k))
    print("カイ二乗値",end=" ")
    chi_2 = n * rss / 821
    print(chi_2)
    print("自由度f",end=" ")
    f = float((k-1) * (k-2)/2)
    print(f)


if __name__ == "__main__":
    main()



