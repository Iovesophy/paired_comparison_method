import time
import datetime
import math
import itertools
import sys
import random
import pandas as pd

print("Welcome to サーストン一対比較法実験集計システムver1")

data=[]

print("被験者情報を入力:",end=" ")
data.append(input())
print("備考:",end=" ")
data.append(input())
print("素材数を入力:",end=" ")
n = input()
if int(n) < 2:
    print("素材数が足りません")
    sys.exit()

data.append(int(n))

print("%s を設定しました" % n)
material=[]
for i in range(int(n)):
    count = i + 1
    print("素材%dの提示したい情報を入力:" % count , end=" ")
    material.append(input())

#print(material[0:])
data.append(material[0:])
N = int(n)
def permutations_count(n , r):
    return math.factorial(n) // math.factorial(n - r)

#print(permutations_count(N,2))
try_num = permutations_count(N,2)
data.append(try_num)
iter_material=[]
for i in itertools.permutations(material, r=2):
    iter_material.append(i)

#print(iter_material)
random.shuffle(iter_material)
print("パラメータ↓")
caption = ["被験者","備考","素材数:","素材:","試行回数:"]
for i in range(5):
    print(caption[i],end=' ')
    print(data[i])

print("実験を開始しますか?:y,n")
if input() == "y":
    print("実験開始")
    print("開始時間:")
    print(datetime.datetime.now())
    start_time = datetime.datetime.now()
    data.append(datetime.datetime.now())
else:
    print("中断します、最初からやり直してください")
    sys.exit()

main_data=[]
for i in range(try_num):
    count = i + 1
    print(iter_material[i])
    print("%d回目 どちらの素材が選ばれましたか?:左 → 0 , 右 → 1 , 戻る→ r" % count)
    ans = input()
    if ans == "r" and i != 0:
        print("何回目に戻りますか?:",end=" ")
        count_neo = int(input())
        if count_neo > count:
            print("存在しません")
            print(iter_material[i])
            print("%d回目 どちらの素材が選ばれましたか?:左 → 0 , 右 → 1 (破壊的記録)" % count)
            ans = input()
            l = list(iter_material[i])
            l.append(ans)
            main_data.append(l)
        else:
            box = count_neo-1
            print(iter_material[box])
            print("%d回目 どちらの素材が選ばれましたか?:左 → 0 , 右 → 1 (破壊的記録)" % count_neo)
            ans_neo = input()
            l = list(iter_material[count_neo])
            l.append(ans_neo)
            print(main_data[box])
            main_data[box]=l
            print(iter_material[i])
            print("%d回目 どちらの素材が選ばれましたか?:左 → 0 , 右 → 1 (破壊的記録)" % count)
            ans = input()
            l = list(iter_material[i])
            l.append(ans)
            main_data.append(l)
        
    elif ans == "0" or ans == "1":
        l = list(iter_material[i])
        l.append(ans)
        main_data.append(l)
    else:
        print("指定された数値を入力してください(初回は戻れません)")
        print(iter_material[i])
        print("%d回目 どちらの素材が選ばれましたか?:左 → 0 , 右 → 1 (破壊的記録)" % count)
        ans = input()
        l = list(iter_material[i])
        l.append(ans)
        main_data.append(l)

end_time = datetime.datetime.now()
data.append(end_time)

print(data[0:])
print(main_data[0:])
Coulum = ['比較データ左','比較データ右','選択結果']
df_info = pd.DataFrame(data)
df_main = pd.DataFrame(main_data,columns=Coulum)
df_info.to_csv("%s%s%s_result_info.csv" % (data[0],"-",end_time))
df_main.to_csv("%s%s%s_result_main.csv" % (data[0],"-",end_time))
