# -*- coding:utf-8 -*-
# author:LeiLei

headers = {
        'User-Agent' : 'Mozilla/5.0 (windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/93.0.4573.0 Safari/537.36'
        }

from pyspark import SparkConf,SparkContext
if __name__ == '__main__':
    sc = SparkContext(conf = SparkConf().setMaster("local[3]").setAppName("leilei"))
    rdd = sc.parallelize([1, 2, 3, 4,5, 5, 6])
    print(rdd.map(lambda x:(x,1)).groupByKey().map(lambda t:(t[0],list(t[1]))).collect())
