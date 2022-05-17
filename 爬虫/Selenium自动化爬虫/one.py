# -*- coding:utf-8 -*-
# author:LeiLei

from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait
from twisted.conch.telnet import EC

headers = {
        'User-Agent' : 'Mozilla/5.0 (windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/93.0.4573.0 Safari/537.36'
        }
if __name__ == '__main__':
    bro = webdriver.Chrome()
    bro.get('https://www.baidu.com/')
    bro.implicitly_wait(2)
    # WebDriverWait(bro,2,0.5).until(expected_conditions.presence_of_element_located((By.ID,'idming')),message = "");

    bro.close()
