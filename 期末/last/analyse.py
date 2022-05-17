# -*- coding:utf-8 -*-
# author:LeiYiBo
# date: 2021-12-28
import json


import jieba
from pyspark import SparkConf, SparkContext, StorageLevel
from operator import add
if __name__ == '__main__':

    #初始化
    # conf = SparkConf().setAppName("leilei").setMaster('yarn')
    conf = SparkConf().setAppName("leilei").setMaster('local[3]')
    sc = SparkContext(conf = conf)
    rdd_src = sc.textFile('newstmp.txt')
    # rdd_src = sc.textFile('hdfs://192.168.2.10:9000/newstmp.txt')
    src_map = rdd_src.map(lambda x : x.split(','))
    src_map.persist(storageLevel=StorageLevel.DISK_ONLY)




    #需求1 统计浏览次数 top10
    top10_map = src_map.map(lambda x : (x[1], x[2]))
    top10_map.persist(storageLevel=StorageLevel.DISK_ONLY)
    top10_result = top10_map.sortBy(lambda x:int(x[1]),ascending = False,numPartitions = 1).take(10)
    print("-----------------统计浏览次数 top10----------------")
    print(top10_result)


    #需求二 统计top3 的小时的活跃度
    top3_map = src_map.map(lambda x:(x[0].split(' ')[1].split(':')[0],x[2])).reduceByKey(lambda a,b:str(int(a)+int(b)))
    top3_result = top3_map.sortBy(lambda x:int(x[1]),ascending = False,numPartitions = 1).take(3)
    print("--------------统计top3 的小时的活跃度----------------")
    print(top3_result)


    #需求三 统计top10的关键词
    top_10_world_map = top10_map.flatMap(lambda x : [(y, x[1]) for y in list(jieba.cut_for_search(x[0]))])
    top_10_world_map.persist(storageLevel=StorageLevel.DISK_ONLY)
    top_10_world_words = top_10_world_map.filter(lambda x:len(x[0])>3).reduceByKey(lambda a,b:str(int(a)+int(b))).sortBy(lambda x:int(x[1]),ascending = False,numPartitions = 1).take(10)
    print("--------------统计top10的关键词----------------")
    print(top_10_world_words)


    #需求四 统计浏览次数 top10中 的关键词
    top_10_wo = sc.parallelize(top10_result)
    top_10_wo = top_10_wo.flatMap(lambda x : [(y, x[1]) for y in list(jieba.cut_for_search(x[0]))])
    top_10_wo_reslut = top_10_wo.filter(lambda x:len(x[0])>3).reduceByKey(lambda a,b:str(int(a)+int(b))).sortBy(lambda x:int(x[1]),ascending = False,numPartitions = 1).take(10)
    print("-------------统计浏览次数 top10中 的关键词-------------")
    # print(top_10_wo_reslut)
    #将top10 关键词和次数进行保存
    with open('top_10_words.txt','w',encoding = 'utf-8') as fp:
        for i in top_10_wo_reslut:
            fp.write(i[0]+"|"+i[1])
            fp.write('\n')



    #需求五 统计最活跃的月份
    top1_map = src_map.map(lambda x : (x[0].split('-')[1], x[2])).reduceByKey(
        lambda a, b : str(int(a) + int(b))
        )
    top1_result = top1_map.sortBy(lambda x : int(x[1]), ascending = False, numPartitions = 1).first()
    print("--------------统计top1 的小时的活跃度----------------")
    print(top1_result)

    #所有的词统计
    all_words = top_10_world_words = top_10_world_map.filter(lambda x : len(x[0]) > 3).reduceByKey(
        lambda a, b : str(int(a) + int(b))
        ).sortBy(lambda x:int(x[1]),ascending = False,numPartitions = 1).collect()
    print("--------------所有的词统计---------")
    #将所有jieba过滤后的词进行保存到all_words.txt
    with open('all_words.txt','w',encoding = 'utf-8') as fp:
        for i in all_words:
            fp.write(i[0]+"|"+i[1])
            fp.write('\n')
    print(all_words)


    #删除缓存RDD
    top_10_world_map.unpersist()
    top10_map.unpersist()
    src_map.unpersist()

