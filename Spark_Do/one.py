# coding:utf-8
# author:LeiLei
import os

from pyspark import SparkConf,SparkContext
import os
# os.environ['PYSPARK_PYTHON'] = "D:/python/python.exe"
headers = {
        'User-Agent' : 'Mozilla/5.0 (windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/93.0.4573.0 Safari/537.36'
        }

if __name__ == '__main__':

    conf = SparkConf().setMaster("local[1]").setAppName("WordCountHelloWord")
    sc = SparkContext(conf = conf)
    file_rdd = sc.textFile("word.txt")

    words = file_rdd.flatMap(lambda li : li.split(" "))

    words_map = words.map(lambda x : (x, 1))

    key = words_map.reduceByKey(lambda a, b : a + b)
    collect = key.collect()

    print(collect)

