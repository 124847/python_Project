import requests
import time
if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4573.0 Safari/537.36'
    }
    url = 'https://movie.douban.com/j/new_search_subjects?'
    for start in range(0,pow(10,10),10):
        params = {
            'sort': 'U',
            'range': '0,10',
            'tags': '电影',
            'start': str(start) +'',
            'genres': '喜剧'
        }
        get = requests.get(url, params, headers=headers)
        js = get.json()
        for i in dict(js)['data']:
            print(i['title'],i['rate'],i['cover'])
