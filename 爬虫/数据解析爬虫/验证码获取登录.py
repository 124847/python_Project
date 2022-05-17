# -*- coding:utf-8 -*-
# author:LeiLei
import os
import pytesseract
import requests
from lxml import etree
from PIL import Image

if __name__ == '__main__':
    session = requests.Session()
    headers = {
        'User-Agent': 'Mozilla/5.0 (windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/93.0.4573.0 Safari/537.36'
    }
    if not os.path.exists('../文件/验证码'):
        os.mkdir('../文件/验证码')
    url_root = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'
    result = ''
    while len(result) != 4:
        headers_text = requests.get(url_root, headers=headers).text
        etree_html = etree.HTML(headers_text)
        img_check = 'https://so.gushiwen.cn' + etree_html.xpath('//*[@id="imgCode"]/@src')[0]
        requests_get = session.get(img_check, headers=headers).content
        with open('../文件/验证码/1.jpg', 'wb') as fp:
            fp.write(requests_get)
            fp.close()
        image = Image.open('../文件/验证码/1.jpg')
        image = image.convert('RGB')#
        result = pytesseract.image_to_string(image).strip().replace("\n","").replace("\r","")
    print(result)
    data = {
        '__VIEWSTATE': 'VqdLNVCJ2bVYmr7siu0CIBoUQzcJ4kP469QJhyY0cHDeNPAAN28XnYFVMBkaD0YGRgpbh77atdy4g25W8ljaqvTzfT63JMQtLqhfjg3DaqOdaOmB730bcClGPRM=',
        '__VIEWSTATEGENERATOR': 'C93BE1AE',
        'from': 'http://so.gushiwen.cn/user/collect.aspx',
        'email': '1248479090@qq.com',
        'pwd': '111000aaa',
        'code': '{}'.format(result),
        'denglu': '登录'
    }
    log_url = 'https://so.gushiwen.cn/user/login.aspx?from=http%3a%2f%2fso.gushiwen.cn%2fuser%2fcollect.aspx'
    log_text = session.post(log_url, data=data, headers=headers)
    url_data = 'https://so.gushiwen.cn/gushi/shijing.aspx'
    data_lists = session.get(url_data, headers=headers).text
    data_dats = etree.HTML(data_lists)
    lists = data_dats.xpath('//div[@class="sons"]//text()')
    print(''.join(lists))
