# -*- coding:utf-8 -*-
# author:LeiLei

headers = {
        'User-Agent' : 'Mozilla/5.0 (windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/93.0.4573.0 Safari/537.36'
        }
from pyspark import SparkConf,SparkContext

if __name__ == '__main__':
    conf = SparkConf().setMaster("local[1]").setAppName("leilei")
    sc = SparkContext(conf = conf)
    rdd = sc.parallelize([("a", 1), ("b", 1), ("c", 2),("c", 3),("b", 1)])
    # print(rdd.groupBy(lambda t : t[0]).map(lambda m:(m[0],list(m[1]))).collect())

    print(rdd.sortBy(lambda x:x[1], ascending = False).collect())
    print(rdd.sortBy(lambda x:x[0]).collect())