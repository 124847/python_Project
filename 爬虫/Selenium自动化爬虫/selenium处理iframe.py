# -*- coding:utf-8 -*-
# author:LeiLei
from time import sleep

from selenium import  webdriver
from selenium.webdriver import ActionChains
if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/93.0.4573.0 Safari/537.36'
    }
    bro = webdriver.Chrome()
    bro.get('https://www.runoob.com/try/try.php?filename=jqueryui-api-droppable')
    bro.switch_to.frame('iframeResult')
    x = bro.find_element_by_id('draggable')
    action = ActionChains(bro)
    action.click_and_hold(x)
    for i in range(5):
        action.move_by_offset(17,0).perform()
        sleep(0.3)
    action.release()