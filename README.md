# 一対比較法

記事にまとめてます。
https://zenn.dev/_kazuya/articles/0e0c95f82cb931

# 動作環境（作者の環境）

+ Python 3.9.1 (default, Dec 24 2020, 16:23:16)  
+ macOS Big Sur ver11.1（このOSで動作を確認）  

# 使い方

セットアップ

```
$ cd selector/
$ python3 selector/setup.py

$ cd analyzer/
$ python3 analyzer/setup.py
```

PCPS(実験補助機能)
※実行前にsample_info.csvに試料情報を入力すること。

```
$ cd selector/
$ python3 select_main.py
```

PCVS(集計,一意性の検定)

```
$ cd analyzer/
$ python3 vote_aggregate.py
```

PCCS(集計,一致性の検定)

```
$ cd analyzer/
$ python3 consistency_vote_aggregatae_and_calculation.py
```

PCZPS(サーストン法ケースV、標準得点Z算出、尺度プロット)

```
$ cd analyzer/
$ python3 z_calculation.py
```

