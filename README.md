# text_visualize: 単語出現頻度の可視化
## word_wakati.py
`create_parser(worker, parts_of_speech=['名詞'],stopwords=[])`
- parserを構築して返す。
- `worker` *str*: パーサー種別　`'janome'` or `'mecab'`
- `parts_of_speech` *[str]*:解析結果に含まれる品詞
- `stopwords` *[str]*: 解析結果に含まれない不要語

`word_seq(text, parser=None)`
- 日本語文字列textに対し`parser`を使って形態素解析を行う
- 指定品詞を抽出
- 不要語、記号を削除
- 上記で得られた単語をリストで返す

## 卒業論文題目における単語出現頻度の可視化
- 卒業論文題目一覧表(.csv)を読み込み, pandas.DataFrameに保存
- 対象年度、対象研究室を指定
- 不要語、品詞を指定
- 集計対象年度範囲を指定
- 研究室・年度範囲の題目をリストとして抽出
- `word_seq()`を呼び出して解析し、単語リストをスペース区切りで再び文字列化
　<br>例えば "**自律走行ロボットの制御方法に関する研究**"->"**自律..走行..ロボット..制御..方法..関する..研究**"
- nlpotで出現頻度を調査し、WordCloud、Unigram図で可視化
