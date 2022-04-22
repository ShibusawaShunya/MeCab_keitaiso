!pip install mecab-python3
!pip install unidic-lite
!pip install japanize_matplotlib

conda install -c anaconda swig

import MeCab
import re
import csv
import pandas as pd

df = pd.read_csv("aaaa.csv")

df


#MeCab等、必要なパッケージをimport
import MeCab
import re
import csv


#MeCabのインスタンスを作成する
mecab = MeCab.Tagger('')


wordFreq_dic = {}
wordcount_output = []

 
#単語頻出度カウント
def WordFrequencyCount(word):
        if word in wordFreq_dic:
            wordFreq_dic[word] +=1
 
        else:
            wordFreq_dic.setdefault(word, 1)
        return wordFreq_dic


#最終的な結果を出力するためのData Frameを作成する
df1 = pd.DataFrame( columns=['user','word0','word1','word2','word3','word4','word5','word6'] )


#dfにセットしたcsvファイルを一行ずつ読み込む
for row, item in df.iterrows():
    #形態素解析結果をセットする変数。一行ずつ（opinionaireid単位）処理するため、処理前に一度クリアする
    result = ''
    
    #一行ずつ形態素解析を行い、単語ごとに分ける
    result = mecab.parse(item[0])
    node = mecab.parseToNode(item[0])
    #一行ごとに分けて変数にセットする
    lines = result.split("\n")
    
    #名詞、動詞、形容詞、形容動詞を抽出する
    while node:
        if node.feature.split(",")[0] == "名詞":
            word = node.surface
            WordFrequencyCount(word)
        elif node.feature.split(",")[0] =="動詞":
            word = node.surface
            WordFrequencyCount(word)
        elif node.feature.split(",")[0] == "形容詞":
            word = node.surface
            WordFrequencyCount(word)
        elif node.feature.split(",")[0] == "形容動詞":
            word = node.surface
            WordFrequencyCount(word)
        else:pass
        node = node.next
    #後ろから２列は不要のため削除する
    lines = lines[0:-2]
    #一行ずつに分けた形態素解析結果の変数を上から順に読み込む
    for words in lines:
        #タブとカンマで区切られているため、配列して新たな変数にセットする
        word = re.split('\t|,',words)
        #結果をData Frameにセットする
        df1 = df1.append({'user':row, 'word0':word[0], 'word1':word[1], 
                          'word2':word[2], 'word3':word[3], 'word4':word[4], 'word5':word[5], 
                          'word6':word[6]},ignore_index=True)        

#リストを昇順にする       
for item in wordFreq_dic.items():
    wordcount_output.append(item)
wordcount_output = sorted(wordcount_output, key = lambda x:x[1], reverse=True)        
        
#全件表示
pd.set_option('display.max_rows', None)
#Data Frameの中身を表示する
 
#CSVで保存する    
df1.to_csv("test.csv")
with open('test2.csv', 'w', newline='') as file:
    writer = csv.writer(file, quoting=csv.QUOTE_ALL,delimiter=';')
    writer.writerows(wordcount_output)
