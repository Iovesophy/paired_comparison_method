# 一対比較法における一意性の検定

# 環境
どの処理ソフトを使おうが、あまり影響はないと思いますが、今回はPython3系を利用。

# 一対比較法とは
一対比較法概要[^1]
>順位法では、感覚や好みの強さを測るのに、全ての試料を一度に評価して順位付けする必要があります。
試料数が多くなると、一度に順位付けすることが困難になることがあります。
そのような場合、２つの試料を対にして比較します。これを全ての対について行う方法が一対比較法です。

### 一対比較法における試験の主な種類

+ 一意性の係数
+ 一致性の係数
+ ブラッドレイの一対比較法
+ サーストンの一対比較法
+ シェフェの一対比較法

etc..

今回は一意性の係数を取り扱う
例えば３つの試料A、B、Cがある時、A>B、B>Cならば、A>Cであるはず。
では実際に、このようになっているかを検定する。

##　手法について

人間の好みや匙加減を測るときには、以下のような状況が生じる可能性がある。
例えば、A、B、Cの３つの試料の評価時に、実際に評価を行うとA=Cや、A>Cと評価されてしまい、一貫した評価がなされない状況が生じる。
このような３者間で順位がつけられない状態を一巡三角形と呼ぶ。

![循環三角.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/110060/e4ff347e-5ef4-7945-8e9a-a82df326eb35.png)

**A>B、B>CならA>Cなはずである、しかし時に、A<Cな場合がある。**

***

$$A>B>C$$

$$A>B,B>C,C<A$$
***
$$A>B>C>A$$

$$A>B,B>C,C>A$$

***

言い換えると、
**AはBより大きい(A>B),BはCより大きい(B>C)ならばAはCより大きい(A>C)はずである**、
（直観的に考えてもこうなると思います）

しかし時に、AはCより小さい(A<C)場合がある。

試料の数がn個あった時に、
3つずつ組み合わせて(A,B,C)
一巡三角形の数を数える場合、

$$d (一巡三角形数)$$

一巡三角形が生じる確率が十分に小さいなら、各試料間に順位をつけられる、
つまり、順位に一意性があったと考えてよい。

この検定法を一意性の検定という。

具体的には、

![好み.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/110060/fcda33d6-683d-a7b7-5b90-998a2e293056.png)


A ～ Fの6つの試料に対して、どちらがより好きかということを考えてみる。
図中の矢印は、A → Bは、AよりもBの方が好きなことを示すものとする。

### 表１
|  i>j  | $A_j$ | $B_j$ | $C_j$ | $D_j$ | $E_j$ | $F_j$ | $a_i$=計 |
| :---: | :---: | :---: | :---: | :---: | :---: | :---: | :---: |
| $A_i$ | - |   |   |   |   | 1 | $a_1=1$ |
| $B_i$ | 1 | - |   |   |   | 1 | $a_2=2$ |
| $C_i$ | 1 | 1 | - |   | 1 |   | $a_3=3$ |
| $D_i$ | 1 | 1 | 1 | - |   |   | $a_4=3$ |
| $E_i$ | 1 | 1 |   | 1 | - | 1 | $a_5=4$ |
| $F_i$ |   |   | 1 | 1 |   | - | $a_6=2$ |


また、表中の数値$1$は、例えば、1列目$A_j$、2行目$B_i$の1は$A_j$よりも$B_i$の方が好きなことを示すものとする。
この時、6つの試料間に好みの順位が存在すると考えてよいのか考えてみる。[^2] [^3]

(kは試料数)$k=6$の場合は、
$$d ≦ 1$$の時に、5％水準で試料間に有意な順位があるといえる。

$k=7$の場合は、$$d ≦ 3$$の時に、5％水準で試料間に有意な順位があるといえる。

また、$$k ≧ 8$$ の時は、カイ二乗検定を行うことにより統計的に有意な順位であるかを判定することができる。

ここで、この検定を行う際に注意しなければならない点であるが、

$$k = 5$$の時、一巡三角形の数（$d$）が0個の場合には一意性あるといえる。
ただし、１個以上の場合には一意性がないと判断できるが、検定の有意水準が通常の5%ではなく、12%水準での検定となる。

また、$$k ≦ 4$$の時は、$d = 0$であっても、有意に達しないということをまず認識しておかなければならない。
つまり、一巡三角形が０個であっても有意な順位があることにはならず、試料数が最低でも5個以上でないと検定結果を有効活用できないので注意が必要。

# 計算式

計算式を以下に示す[^2] [^3]
一巡三角形の個数dは次の式で表す

$$d = {}_k C_2$$

$$- \sum_{i=1}^k {}_{a _i}C _2$$

展開

$${}_k \mathrm{C}_2 = \frac{k!}{2!(k-2)!} = \frac{1}{6}k(k-1)(k-2)$$

$$d = \frac{1}{6}k(k-1)(k-2)-\frac{1}{2}\sum_{i=1}^k a_i(a_i-1)$$

$k$は試料数を示しており、$a_i$は試料iが得た票の合計を示す（表1を参照）

自由度$f$は次の式で表す

$$f = \frac{k(k-1)(k-2)}{(k-4)^2}$$

一意性の係数$\zeta$は次の式で表す($k$が偶数の時)

$$\zeta = 1 - \frac{24d}{k^3 - 4k}$$

一意性の係数$\zeta$は次の式で表す($k$が奇数の時)

$$\zeta = 1 - \frac{24d}{k^3 - k}$$

カイ二乗値は以下の式で表す

$$\chi_o^2= \frac{8}{k-4} ｛ \frac{k(k-1)(k-2)}{24} -d + \frac{1}{2} ｝ +f$$

カイ二乗分布表(表2)より，例えば有意水準5%での被験者の判定は首尾一貫しているといえるかどうか判断する。
### 表2
| 自由度 | 有意水準 .05 | 有意水準 .01 |
| :---: | :---: | :---: |
| 1 | 3.841 | 6.635 |
| 2 | 5.991 | 9.210 |
| 3 | 7.815 | 11.345 |
| 4 | 9.488 | 13.277 |
| 5 | 11.070 | 15.086 |
| 6 | 12.592 | 16.812 |
| 7 | 14.067 | 18.475 |
| 8 | 15.507 | 20.090 |
| 9 | 16.919 | 21.666 |
| 10 | 18.307 | 23.209 |
| - | - | - |
| 11 | 19.675 | 24.725 |
| 12 | 21.026 | 26.217 |
| 13 | 22.362 | 27.688 |
| 14 | 23.685 | 29.141 |
| 15 | 24.996 | 30.578 |
| 16 | 26.296 | 32.000 |
| 17 | 27.587 | 33.409 |
| 18 | 28.869 | 34.805 |
| 19 | 30.144 | 36.191 |
| 20 | 31.410 | 37.566 |
| - | - | - |
| 21 | 32.671 | 38.932 |
| 22 | 33.924 | 40.289 |
| 23 | 35.172 | 41.638 |
| 24 | 36.415 | 42.980 |
| 25 | 37.652 | 44.314 |
| 26 | 38.885 | 45.642 |
| 27 | 40.113 | 46.963 |
| 28 | 41.337 | 48.278 |
| 29 | 42.557 | 49.588 |
| 30 | 43.773 | 50.892 |

引用: 山田剛史・村井潤一郎「よくわかる心理統計」付表3より[^4]

# Python3を用いて実際にデータ集計から一意性の検定までを行う

###流れ

+ 試料の準備
+ 試料の提示と実験
+ データ集計
+ 実験データをcsvに出力
+ csvデータから一巡三角形の個数$d$を算出
+ csvデータから自由度$f$を算出
+ csvデータから一意性の係数$\zeta$を算出
+ csvデータからカイ二乗値$\chi_o^2$を算出
+ 算出した$\chi_o^2$とカイ二乗分布表(表2)を用いて一意性の検定を行う

## 試料の準備
試料の準備の際に注意しなければならない点
**kは試料数を表しています**
上述の通りだが、

$$k = 5$$の時、一巡三角形の数（$d$）が0個の場合には一意性あるといえる。
ただし、１個以上の場合には一意性がないと判断できるが、検定の有意水準が通常の5%ではなく、12%水準での検定となる。

また、$$k ≦ 4$$の時は、$d = 0$であっても、有意に達しないということをまず認識しておかなければならない。
つまり、一巡三角形が０個であっても有意な順位があることにはならず、
**試料数が最低でも5個以上**でないと検定結果を有効活用できないので注意が必要。

## 試料の提示と実験
試料の準備ができたら、試料について言語化、あるいは図化し、アイコンとして提示できる形にしていく。
このアイコンは自分にとっても被験者にとってもわかりやすい形にしておくのがベスト、最悪アルファベットを並べるだけでもアイコンとしては機能する。(例えば、前述のA~Fなど)
そしてもし被験者が１人で一対比較を行った場合，表3の一巡三角形の個数$d$の値のとき有意水準5%で「判断者に識別力がないこと」を棄却できることが知られている。[^5]

### 表3
|k|5以下|6|7|8|9|
| :---: | :---: | :---: | :---: | :---: | :---: |
| d | 有意水準5%に達しない | 1以下 | 3以下 | 7以下 | 14以下
| ${}_kC_3$ | 10以下 | 20 | 35 | 56 | 84 |

引用：「AHPにおける一対比較法に関する一考察 官能検査における一対比較法の利用」 飯田洋市より

## データ集計、PCPSによって得られた実験データをcsvに出力


即席で実験補助アプリとして「一対比較法実験集計システムver2:2021,1,3 Paired comparison method data processing software, codename PCPS」を作った(以下 PCPSと呼ぶ)

実験フロー

![実験フロー.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/110060/b45546d9-c758-013f-0428-bdd502cbe38b.png)

<details><summary>PCPSソースコード(paired_comparison_method/select_main.py)</summary><div>

```python:paired_comparison_method/select_main.py
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
    print("Welcome to 一対比較法実験集計システムver2:2021,1,3")
    print("Paired comparison method data processing software, PCPS")
    print("made by kazuya yuda.")

def exit_all(): # 終了処理
    sys.exit()

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

    try_num = combinations_count(N,2) # 試行回数取得(組み合わせを計算)
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

```

</div></details>



また、Arduino Leonardo(Pro Micro)を用いてPCPS用のHIDデバイス(PCPS_selector)を作る。

![0EBE9FEA-E8FE-4130-9C89-FCC6EEDF8646.jpeg](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/110060/7fceb53f-495d-a155-09f4-0219f461cb31.jpeg)


<details><summary>HIDデバイス(PCPS_selector)PCPS_selector.ino</summary><div>

```C:PCPS_selector.ino

#include "Keyboard.h"
#define select_left_0 5
#define select_right_1 6

void setup() {
  Keyboard.begin();
  pinMode(select_left_0, INPUT_PULLUP);
  pinMode(select_right_1, INPUT_PULLUP);
}

void loop() {
  if(digitalRead(select_left_0) == LOW){
    Keyboard.write('0'); //
    Keyboard.write('\n');
    delay(100);

    while(digitalRead(select_left_0) == LOW);
  }

  if(digitalRead(select_right_1) == LOW){
    Keyboard.write('1'); //
    Keyboard.write('\n');
    delay(100);

    while(digitalRead(select_right_1) == LOW);
  }

  delay(100);
}
```

</div></details>

### 「一対比較法実験集計システムver2:2021,1,3 Paired comparison method data processing software, codename PCPS」解説
使用するpython3のライブラリ(一部pipでインストールする必要があります)

+ time
+ datetime
+ math
+ itertools
+ sys
+ random
+ pandas
+ csv

ライブラリのインポート

```
import time
import datetime
import math
import itertools
import sys
import random
import pandas as pd
import csv
```

Welcomeメッセージの表示、
ここでは、表示させたい情報や、実験時の確認ポイントなどを記載すると良いと思う。

```python

def welcome_mes(): # 起動時のメッセージ
    print("Welcome to 一対比較法実験集計システムver2:2021,1,3")
    print("Paired comparison method data processing software, PCPS")
    print("made by kazuya yuda.")
```

プログラム終了のためのサブルーチンで,主にパラメータ確認のフェーズで間違っていた時に終了させる用途。

```python
def exit_all(): # 終了処理
    sys.exit()
```

試行回数を算出するため、組み合わせを計算する、mathライブラリを使用

```python

def combinations_count(n, r):
    return math.factorial(n) // (math.factorial(n - r) * math.factorial(r))
```

被験者情報の入力や試料数の確認等の初期設定
ちなみに絶対バリデーションすべきですが、未実装、余裕があるさい改良予定
（Unittest等も行うべき）

```python

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
```

試料数分の試料の読み込み、ない場合は生成も行う、
csvを読み込んで試料情報を取得することも可能
その際、同一ディレクトリにsample_info.csvを用意しておく必要がある。
以下のような内容でcsvを作成しておく↓(一例:試料数が6でA~Fの英字アイコン、ヘッダーもつけておきましょう)

```csv:sample_info.csv
No,試料情報
1,A
2,B
3,C
4,D
5,E
6,F

```

+ 上述のcsvを読み込む部分（UTF-8形式で作成しておく必要があります）
+ 初回、csvを用意していなかった場合にその場で提示情報を作成可能（ちなみにこの場合提示情報の記録はしません）

提示試料アイコンの格納にmaterialという名前で配列を作成（今後も使います）

```python

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
```


試行回数分一対比較用の比較試料生成
また、提示試料はランダムに決定する必要があるので、先程のmaterialをシャッフル

```python

def itertools_make_material(material): # 試行回数分一対比較用の比較試料生成
    itertools_material=[]
    for i in itertools.permutations(material, r=2):
        itertools_material.append(i)
    random.shuffle(itertools_material)
    return itertools_material
```

以上で全ての設定が完了なので、最後に各種パラメータや被験者情報を確認するフェーズを設ける
のちにリファクタリングして、captionをまとめているが、前述まで全てのパラメータ情報はdata配列に入っている
機能追加の際は基本的にdata配列を参照すれば良い

```python

def confirmation(data): # パラメータ確認フェーズ
    print("パラメータを確認してください↓")
    caption = ["被験者","備考","試料数:","試料:","試行回数:"]
    for i in range(5):
        print(caption[i],end=' ')
        print(data[i])
```

実験開始処理、役割としては時間を記録しておくこと
パラメータ確認フェーズを経て、本当に開始していいかの確認も行う
ちなみに、パラメータに誤りがある場合は一旦処理を終了する

```python

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
```

実際にデータを提示し、処理するフェーズ
入力間違えが発生した際に（HIDデバイスを作るなら、被験者の押し間違え）対応も可能だ
これは基本的に再帰で実現している

+ itertools_material は提示する試料が格納されている
+ main_data は選択結果を記録するもの
+ count は現在の試行回数を把握するもの
+ i はイテレータのi
+ option はファイナライズ中かそうでないかを判断するためのフラグ

```python

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
```

ファイナライズ処理、ちなみに、なぜことフェーズを書いたかというと、実験中最後の試行中に誤ってしまい、そのまま処理を終了してしまい、終了時間を正しく記録できない問題と、後でcsvをマニュアル修正する必要が出てきて、著しく利便性を損なったためである
基本は前述のサブルーチン(process)と同じです。

```python

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
```

終了時間記録

```python
def process_end(): # 終了時間記録
    end_time = datetime.datetime.now()
    return end_time

```

pandasでcsvに出力

```python

def result_export_process(data,integration_data,end_time): # CSV形式でエクスポート
    print(data[0:])
    print(integration_data[0:])
    Coulum = ['比較データ左','比較データ右','選択結果']
    df_info = pd.DataFrame(data)
    df_main = pd.DataFrame(integration_data,columns=Coulum)
    df_info.to_csv("%s%s%s_result_info.csv" % (data[0],"-",end_time))
    df_main.to_csv("%s%s%s_result_main.csv" % (data[0],"-",end_time))
```

最後にmainで各種サブルーチンの呼び出し

```python
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

```

ちなみに、processのイテレーションはmainで処理しています。

```python
    option="none"
    for i in range(try_num): # 試行回数分イテレーション
        count = i + 1
        main_data.append(process(itertools_material,main_data,count,i,option))
```

### Arduino Leonardo(Pro Micro)を用いてPCPS用のHIDデバイス(PCPS_selector)を作る

作りは非常にシンプルで、PCPSの一対提示試料の選択に必要な数値を入力できるキーボードを作るイメージ。

選択には以下の数値を割り当てている。
左　：　０
右　：　１

左のボタンを押せば0を右のボタンを押せば1を入力できるデバイスを作成した。
ボタンに関しては色分けしておくほうがわかりやすい。

### 用意するもの

+ Arduino Leonardo もしくは Arduino Pro Micro
+ プッシュボタンスイッチ

ちなみに参考として、当方はスイッチサイエンス版のArduino Pro Micro

![IMG_6328_500.jpg](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/110060/00d4afad-409c-93b6-9c0d-43170b41ead8.jpeg)


プッシュボタンスイッチは以下のものを用意した
mxuteuk 12個1A 250V AC 2ピンSPST 6色ノーマルオープンミニ瞬間プッシュボタンスイッチPBS-110-6C

![btn.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/110060/2811486b-03a9-cd8c-8946-36242d6d2a2b.png)

書き込みに関しては以下のページを参照
https://www.arduino.cc/en/Guide

```C:PCPS_selector.ino

#include "Keyboard.h"
#define select_left_0 5
#define select_right_1 6

void setup() {
  Keyboard.begin();
  pinMode(select_left_0, INPUT_PULLUP);
  pinMode(select_right_1, INPUT_PULLUP);
}

void loop() {
  if(digitalRead(select_left_0) == LOW){
    Keyboard.write('0');
    Keyboard.write('\n');
    delay(100);

    while(digitalRead(select_left_0) == LOW);
  }

  if(digitalRead(select_right_1) == LOW){
    Keyboard.write('1');
    Keyboard.write('\n');
    delay(100);

    while(digitalRead(select_right_1) == LOW);
  }

  delay(100);
}
```




## CSVデータより各種計算

**csvデータから一巡三角形の個数$d$を算出**
**csvデータから自由度$f$を算出**
**csvデータから一意性の係数$\zeta$を算出**
**csvデータからカイ二乗値$\chi_o^2$を算出**
**算出した$\chi_o^2$とカイ二乗分布表(表2)を用いて一意性の検定を行う**

### 流れ
+ まず、実験データを元に得票を行列に変換
+ 行列から得票合計$a_i$を算出
+ 一巡三角形の個数$d$を計算式より算出

<details><summary>PCVSソースコード(paired_comparison_method/vote_aggregate.py)</summary><div>


```python:vote_aggregate.py
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

def welcome_mes(): # 起動時のメッセージ
    print("Welcome to 一対比較法得票集計システムver2:2021,1,3")
    print("paired comparison method vote data aggregate software, PCVS")
    print("made by kazuya yuda.")

def import_csv(): # 試料読み込み
    material=[]
    info=[]

    # ファイル名確認
    return_code = subprocess.check_output(['ls'])
    code = return_code.split(b"\n")
    for i in range(len(code)):
        stdout_txt = str(code[i]).replace("b","").replace('\'',"")
        if re.search("csv",stdout_txt) and stdout_txt != "sample_info.csv":
            print(stdout_txt)
    print("拡張子を含めて、解析したいmainデータファイル名を入力してください")
    filename = input()
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

```

</div></details>

このような形で表示されます。
![一例.png](https://qiita-image-store.s3.ap-northeast-1.amazonaws.com/0/110060/5774e904-670b-5365-b34c-93cd1bcb4b91.png)


ちなみに、上図のデータは一例として提示するために、筆者が適当に生成。
当然dの数が1以上なので、回答に一意性がないことがわかる。

### 解説

各種ライブラリのインポート

```python
import math
import itertools
import pandas as pd
import csv
import subprocess
import re
import numpy as np
```

csvファイルのインポート
実験を完了した被験者分のデータがあると思うので、解析したいデータを確認し、入力する。
その際、mainのcsvファイル名が確認できるようにsubprocessを用いてlsコマンドを実行する。
標準出力にフィルターをかけて、csvファイルのみ抽出する。

```python
def import_csv(): # 試料読み込み
    material=[]
    info=[]

    # ファイル名確認
    return_code = subprocess.check_output(['ls'])
    code = return_code.split(b"\n")
    for i in range(len(code)):
        stdout_txt = str(code[i]).replace("b","").replace('\'',"")
        if re.search("csv",stdout_txt) and stdout_txt != "sample_info.csv":
            print(stdout_txt)
    print("拡張子を含めて、解析したいmainデータファイル名を入力してください")
    filename = input()
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
```

試料数kと試行回数nをPCPSより出力されたinfo.csvからロード

```python
def get_k(info):
    k = int(str(info[2]).replace("[","").replace("]","").replace("\'",""))
    return k

def get_n(info):
    n = int(str(info[4]).replace("[","").replace("]","").replace("\'",""))
    return n
```

自由度f算出

```python

def f_calculation(info):
    k = get_k(info)
    k_1 = k * (k-1) * (k-2)
    k_2 = (k-4) * (k-4)
    f = float(k_1/k_2)
    return f
```

得票を集計、一巡三角形の個数dを算出する。
集計の際に行列に変換するためnumpyを利用している。

```python
def make_vote_list_and_calculation(info,material):
    # infoからk,n読み込み
    k = get_k(info)
    n = get_n(info)

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
    return d
```

最後に$\zeta$と$\chi_o^2$を算出する

```python

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
```

一意性が認められたら、次は一致性の検定を行い、有効被験者間の回答は一致しているかを検定できる。

次回の記事で一致性の検定を書く予定。

### 参考
[^1]: 「一対比較法」 感性・官能評価システム J-SEMS https://j-sems.com/%E4%B8%80%E5%AF%BE%E6%AF%94%E8%BC%83%E6%B3%95/

[^2]: 「PC 画面上で見る三原色の季節感について」 https://core.ac.uk/download/pdf/233608433.pdf

[^3]: 修士論文 「拡張現実間における擬似触覚を用いた力覚フィードバック提示手法」 東京大学大学院工学系研究科電気系工学専攻 大塚 隆史 平成25年2月6日

[^4]: 「よくわかる心理統計」 山田剛史・村井潤一郎 ミネルヴァ書房

[^5]: 「AHPにおける一対比較法に関する一考察 官能検査における一対比較法の利用」 飯田洋市

