from typing import Iterable
import requests
import json

if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4573.0 Safari/537.36'
    }
    url = 'https://fanyi.baidu.com/sug'
    word = input('请输入单词')
    data = {'kw': word}
    post = requests.post(url, data, headers=headers)
    js = post.json()  # 返回obj对象 确定响应是json类型时才能使用 返回字典
    for i in js:
        if isinstance(js[i],Iterable):
            for j in js[i]:
                print(j)


    fp = open('../文件/单词{}.json'.format(word), 'w', encoding='utf-8')
    json.dump(js, fp, ensure_ascii=False)
    print('爬取完成')
