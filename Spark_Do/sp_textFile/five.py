# -*- coding:utf-8 -*-
# author:LeiLei
import re
from operator import add

import jieba
from pyspark import SparkConf,SparkContext
from pyspark.storagelevel import StorageLevel
headers = {
        'User-Agent' : 'Mozilla/5.0 (windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/93.0.4573.0 Safari/537.36'
        }


if __name__ == '__main__':
    conf = SparkConf().setMaster("local[3]").setAppName("leilei")
    sc = SparkContext(conf = conf)
    rdd = sc.textFile("SogouQ.sample")
    rdd_map = rdd.map(lambda x : x.split("\t"))
    rdd_map.persist(StorageLevel.DISK_ONLY)
    context = rdd_map.map(lambda x : x[2])

    words = context.flatMap(lambda x : list(jieba.cut_for_search(x)))
    words_filter = words.filter(lambda x : not re.match("\W",x))
    words_map = words_filter.map(lambda x: (x, 1))
    print(
        words_map.reduceByKey(lambda a, b : a + b).sortBy(lambda x : x[1], ascending = False, numPartitions = 1).take(5)
        )
    map_map = rdd_map.map(lambda x : (x[1], x[2]))
    flat_map = map_map.flatMap(lambda x : [(x[0]+"_" + i, 1) for i in jieba.cut_for_search(x[1]) if not re.match("\W", i)])
    print(flat_map.reduceByKey(lambda a, b : a + b).sortBy(lambda x:x[1],ascending = False,numPartitions = 1).take(5))
    tim = rdd_map.map(lambda x:x[0])
    rdd_map_map = tim.map(lambda x : (x.split(":")[1], 1))
    print(rdd_map_map.reduceByKey(add).sortBy(lambda x : x[1], ascending = False, numPartitions = 1).take(5))
    rdd_map.unpersist()
