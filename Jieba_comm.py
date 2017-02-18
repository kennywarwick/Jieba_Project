#coding:UTF-8
# 匯入資料
from collections import Counter
from operator import itemgetter #適合處理字典或是串列資料
import codecs #操作文件，讀寫數據，涉及到非ASCII的話，最好用codes模組操作，其會自動處理不同的編碼，效果最好
import json
import re
import jieba
import jieba.analyse
import jieba.posseg as pseg
from datetime import datetime

s1 = datetime.now()

# 建立 Dict
jieba.load_userdict("E:/AB104/TextMining/JeibaDict/userWord.txt")
jieba.load_userdict("E:/AB104/TextMining/JeibaDict/hotelName9943.txt")
jieba.load_userdict("E:/AB104/TextMining/JeibaDict/MRT584.txt")
jieba.load_userdict("E:/AB104/TextMining/JeibaDict/big176239.txt")
jieba.load_userdict("E:/AB104/TextMining/JeibaDict/big584429.txt")
jieba.load_userdict("E:/AB104/TextMining/JeibaDict/simple109750.txt")
jieba.load_userdict("E:/AB104/TextMining/JeibaDict/NightMarket86.txt")

# StopWords 載入
with codecs.open('E:/AB104/TextMining/JeibaDict/stop_words.txt','r', encoding='utf-8') as fs:
    stopwords = fs.read().split('\n')

## 抓取 JSON 內的 comment
# with open("E:/AB104/TextMining/JeibaDict/pttcontent1.json","r") as a:
#     seglist = json.load(a)
#     for i in seglist:
#         for j in i["comment_collection"]:
#             words = jieba.cut(j["comment"], cut_all=False, HMM=True)
#             for word in words:
#                 comment_list_jieba.append(word.upper().replace(' ',''))

#抓取 JSON 內的 comment 成 list
comments_list = []
with open("E:/AB104/Expedia/Taipei-Hotels-The-Sherwood-Taipei_comments.json","r") as a:
    Com_list = json.load(a)
    for i in Com_list:
        for j in i["comment_collection"]:
            comments_list.append(j)
            # print j
# for i in comments_list:
#     print i

## 拆出列數
# print len(comment_list_jieba)

# 指定關係詞性
# flag_limitted = ['ns']

# 給予詞性後傳出

with open('E:/AB104/Jieba_data/Expedia_Taipei-Hotels-The-Sherwood-Taipei_comments.txt','w') as output:
    for index,content in enumerate(comments_list):
        upperline = content['comment'].upper().replace(' ','')
#         print upperline
        words_pseq = pseg.cut(upperline)
        # 指定詞性版
        b = []
        for word in words_pseq:
            if word.word in stopwords or word.word == ' ':
                # print word.word
                continue
            if re.match('[0-9]+', word.word):
                continue
            else:
                output.write((word.word + ' ').encode('utf-8'))

output.close()

s2 = datetime.now()
print "All  Finish "+str(s2-s1)+"!!"
# All  Finish 0:00:29.160000!!