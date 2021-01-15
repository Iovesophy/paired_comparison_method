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
import matplotlib.pyplot as plt
import pylab
from IPython import get_ipython
ipy = get_ipython()
if ipy is not None:
    ipy.run_line_magic('matplotlib', 'inline')

def welcome_mes(): # 起動時のメッセージ
    print("Welcome to 一対比較法z計算,尺度plotシステムver2:2021,1,3")
    print("paired comparison method z calculation and plot software, PCZPloter")
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
    return_code = subprocess.check_output(['ls','./../selector/data'])
    code = return_code.split(b"\n")
    for i in range(len(code)):
        stdout_txt = str(code[i]).replace("b","").replace('\'',"")
        if re.search("csv",stdout_txt) and stdout_txt != "sample_info.csv":
            print(stdout_txt)
    filename = './../selector/data/setting_file_info.csv'
    print(filename,end=" ")
    print("を読み込みました.")
    # info file　のインポート
    csv_file = open(filename, "r", encoding="utf_8", errors="", newline="" )
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
    if s == "":
        print("一致性の検定が完了していません。")
        sys.exit()
    else:
        return int(s)


def get_k(info):
    k = int(str(info[2]).replace("[","").replace("]","").replace("\'",""))
    return k

def conversion_p(array,n):
    conversion_array = array/n
    np.place(conversion_array, conversion_array == 0, 0.5)
    np.place(conversion_array, conversion_array == 1, 0.5)
    return conversion_array

def conversion_z(array):
    it = np.nditer(array, flags=['multi_index'])
    for x in it:
        # パラメータ指定がないと、標準正規分布(mu = 0およびsigma = 1)に自動補完される。
        #print(array[it.multi_index[0],it.multi_index[1]])
        #print(NormalDist().inv_cdf(array[it.multi_index[0],it.multi_index[1]]))
        array[it.multi_index[0],it.multi_index[1]] = NormalDist().inv_cdf(array[it.multi_index[0],it.multi_index[1]])
    print(array)
    return array

def sum_z(conversion_z_array):
    # 行和を計上し、平均を求め尺度値を算出する
    print(conversion_z_array)
    print(np.sum(conversion_z_array, axis=1))
    return np.sum(conversion_z_array, axis=1)

def mean_z(conversion_z_array):
    a_del = np.delete(conversion_z_array, 0, 0)
    b_del = np.delete(a_del, 0, 1)
    # 行和を計上し、平均を求め尺度値を算出する
    print(np.mean(b_del, axis=1))
    return np.mean(b_del, axis=1)

def plot_scale(k,labellist,mean_z_val):
    #配列を生成
    labellist = labellist[0].replace("[","").replace("]","").replace("\'","").replace(" ","").split(",")
    combine = sorted(zip(mean_z_val,labellist))
    print(combine)
    p,labellist = zip(*combine)
    p = list(p)
    labellist = list(labellist)

    y = [0]*k #y=0
    print(mean_z_val,labellist,p,y,k)

    #数直線
    fig,ax=plt.subplots(figsize=(15,15)) #画像サイズ
    fig.set_figheight(2.5) #高さ調整
    ax.tick_params(labelbottom=True, bottom=False) #x
    ax.tick_params(labelleft=False, left=False) #y
    ax.set_title('Psychological Scale') #タイトル

    #数値表示
    for i in range(int(k/2)):
        print(i)
        view_v = '{:.2f}'.format(p[2*i])
        ax.annotate(view_v,xy=(p[2*i],y[2*i]),xytext=(10, 20),textcoords='offset points',arrowprops=dict(arrowstyle="->"))

    for i in range(int(k/2)):
        print(i)
        view_v = '{:.2f}'.format(p[2*i+1])
        ax.annotate(view_v,xy=(p[2*i+1],y[2*i+1]),xytext=(10,-40),textcoords='offset points',arrowprops=dict(arrowstyle="->"))

    xmin, xmax= round(p[0])-.5,round(p[k-1])+.5 #数直線の最小値・最大値
    plt.tight_layout() #グラフの自動調整

    plt.subplots_adjust(left=0, right=1, bottom=0.2, top=0.8) #微調整

    markerlist = ['.','o','d','X','s','v','*','x','p','P','2']
    colorlist = ["r", "g", "b", "c", "m", "y", "#984ea3", "orange"]
    c_set = 0;m_set = 0
    for i_v in range(k):
        if m_set >= 10:
            m_set = 0
        elif c_set >= 8:
            c_set = 0
        else:
            pass
        plt.scatter(p[i_v],y[i_v], c=colorlist[c_set], s=100,marker=markerlist[m_set], label=labellist[i_v]) #size100
        c_set += 1;m_set += 1

    plt.hlines(y=0,xmin=xmin,xmax=xmax,colors='k',lw=0.8) #横軸
    #plt.vlines(x=np.arange(xmin,xmax+1,1),ymin=-0.2,ymax=0.2,colors='b') #目盛り線大
    #x=np.arange(xmin,xmax+1,1)
    #print(x)
    plt.vlines(x=np.arange(xmin,xmax,0.1),ymin=-0.1,ymax=0.1,colors='k',lw=1) #目盛り線小
    #x=np.arange(xmin,xmax,0.1)
    #print(x)

    plt.legend(loc='lower left') #ラベル
    line_width=0.1 #目盛り数値の刻み幅
    plt.xticks(np.arange(xmin,xmax+line_width,line_width)) #目盛り数値
    pylab.box(False) #枠を消す


    plt.show() #表示

def main():
    welcome_mes()
    material_import = import_csv(get_n())
    k = get_k(material_import[1])
    labellist = material_import[1][3]
    conversion_array = material_import[0]
    conversion_z_array = conversion_z(conversion_array)
    sum_z_val = sum_z(conversion_z_array)
    mean_z_val = mean_z(conversion_z_array)
    plot_scale(k,labellist,mean_z_val)

if __name__ == "__main__":
    main()
