# 一対比較法

記事にまとめてます。
https://zenn.dev/_kazuya/articles/0e0c95f82cb931

# 動作環境（作者の環境）

+ Python 3.9.1 (default, Dec 24 2020, 16:23:16)  
+ macOS Big Sur ver11.1（このOSで動作を確認）  

![plot](https://user-images.githubusercontent.com/15680172/104689637-35fc8180-5746-11eb-9cea-17d1be9a5cc0.gif)
(Plotの様子)

# 使い方

セットアップ

```
$ cd selector/
$ python3 selector/setup.py
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

実験のリセット(実験データが消えるので注意)

```
$ cd selector/
$ sh reset.sh

$ cd analyzer/
$ sh reset.sh
```

このツールは現在開発中です。（プルリク・イシューなどもらえると嬉しいです）

License
Copyright (c) 2021 Kazuya yuda. This software is released under the MIT License, see LICENSE.
https://opensource.org/licenses/mit-license.php

Authors
kazuya yuda.
