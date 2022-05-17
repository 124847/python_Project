# -*- coding:utf-8 -*-
# author:LeiLei

headers = {
        'User-Agent' : 'Mozilla/5.0 (windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/93.0.4573.0 Safari/537.36'
        }
from pyspark import SparkConf,SparkContext

if __name__ == '__main__':
    conf = SparkConf().setMaster("local[1]").setAppName("leilei")
    sc = SparkContext(conf = conf)
    rdd = sc.parallelize(["1 2", "5 4", "5 6", "7 8", "4 10", "3 12"], 3)
    rdd_map = rdd.flatMap(lambda x : x.split(" ")).map(lambda y:(y,1))
    # rdd_map_h = rdd.flatMap(lambda x : x.split(" "))
    # print(rdd_map.reduceByKey(lambda a,b:a+b).collect())
    # print(rdd_map.mapValues(lambda x:x*10).union(rdd_map.reduceByKey(lambda a,b:a+b)).collect())
    # print(rdd_map_h.filter(lambda x :int(x) % 2 == 0).distinct().collect())
    


