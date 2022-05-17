# -*- coding:utf-8 -*-
# author:LeiLei
import json

headers = {
        'User-Agent' : 'Mozilla/5.0 (windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/93.0.4573.0 Safari/537.36'
        }

# # 进入控制台
# from pyspark import SparkConf, SparkContext
#
# conf = SparkConf().setMaster("local[1]").setAppName("LeiLei")
# sc = SparkContext(conf = conf)
# print(sc.textFile("word.txt", 3).collect())
# print(sc.parallelize([1, 2, 3, 4, 5]).map(lambda x:x).collect())
print(type((str([(1,2),(4,5)]))))