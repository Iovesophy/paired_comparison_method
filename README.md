# 一対比較法における一意性の検定

記事にまとめてます。
https://zenn.dev/_kazuya/articles/0e0c95f82cb931

# 使い方

PCPS(実験補助機能)
※実行前にsample_info.cavに試料情報を入力すること。

```
$ cd selector/
$ python3 select_main.py
```

PCVS(集計,一意性の検定)

```
$ cd analyze
$ python3 vote_aggregate.py
```

PCCS(集計,一致性の検定)

```
$ cd analyze
$ python3 consistency_vote_aggregatae_and_calculation.py
```
