# -*- coding:utf-8 -*-
# author:LeiLei
headers = {
        'User-Agent' : 'Mozilla/5.0 (windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/93.0.4573.0 Safari/537.36'
        }
from pyspark import SparkConf,SparkContext

if __name__ == '__main__':
    conf = SparkConf().setMaster("local[1]").setAppName("leilei")
    sc = SparkContext(conf = conf)
    rdd = sc.parallelize([1, 2, 3, 4, 5, 6, 7, 8],3)

    rdd.foreachPartition(lambda x:print([s*10 for s in x]))
    # print(rdd.takeSample(False, 22))
    # print(rdd.takeOrdered(3,lambda x:-x))

    # def haha(data):
    #     return data
    # print(sc.textFile("../word.txt").map(haha).collect())
    # date = sc.wholeTextFiles("../da_ta")
    # rm = date.map(lambda x:x[1])
    # rm = rm.flatMap(lambda x : x.split("o"))
    # print(rm.map(lambda x:x+"10").collect())