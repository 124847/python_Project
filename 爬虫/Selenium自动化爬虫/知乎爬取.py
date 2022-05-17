# -*- coding:utf-8 -*-
# author:LeiLei
import time

import numpy as np
from cv2 import cv2
from selenium.webdriver.support import expected_conditions as EC
import requests
from selenium.webdriver import Chrome, ActionChains
from selenium.webdriver.chrome.options import Options
if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/93.0.4573.0 Safari/537.36'
    }
    option = Options()
    option.add_argument(f'use-agent={headers["User-Agent"]}')
    # option.add_argument('--headless')
    # option.add_argument('--disable-gpu')
    # option.add_experimental_option('excludeSwitches',['enable-automation'])
    bro = Chrome(options=option)
    with open('D:/GitHub/stealth.min.js-main/stealth.min.js-main/stealth.min.js') as f:
        js = f.read()

    bro.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {
        "source": js
    })
    bro.get('https://www.zhihu.com/signin?next=%2F')
    bu = bro.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[1]/div/div[1]/form/div[1]/div[2]')
    bu.click()
    time.sleep(2)
    users = bro.find_element_by_name('username')
    pads = bro.find_element_by_name('password')
    users.send_keys('15090387837')
    time.sleep(0.5)
    pads.send_keys('LYB110d#')
    time.sleep(0.5)
    sub = bro.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[1]/div/div[1]/form/button')
    sub.click()
    time.sleep(1)
    # fr = bro.find_element_by_css_selector('.yidun_cover-frame')
    # print(fr)
    # bro.switch_to.frame(fr)
    time.sleep(1)


        # 滑动验证码验证
    while True:  # 循环进行刷新验证码，第一次验证不成功就刷新验证码再进行新图片的验证

        bak = bro.find_element_by_css_selector('.yidun_bg-img')
        mod = bro.find_element_by_css_selector('.yidun_jigsaw')
        bak_url = bak.get_attribute('src')
        mod_url = mod.get_attribute('src')
        with open('zh_b.jpg', 'wb') as fp:
            bak_content = requests.get(bak_url, headers=headers).content
            fp.write(bak_content)
            fp.close()
        with open('zh_m.jpg', 'wb') as fp:
            mod_content = requests.get(mod_url, headers=headers).content
            fp.write(mod_content)
            fp.close()
        # b_rgb = cv2.imdecode(np.fromfile('../文件/验证码/qq_b.jpg', dtype=np.uint8), -1)
        # m_rgb = cv2.imdecode(np.fromfile('../文件/验证码/qq_m.jpg', dtype=np.uint8), 1)
        b_rgb = cv2.imread('./zh_b.jpg')
        b_gray = cv2.cvtColor(b_rgb, cv2.COLOR_BGR2GRAY)
        m_rgb = cv2.imread('./zh_m.jpg', 0)
        res = cv2.matchTemplate(b_gray, m_rgb, cv2.TM_CCORR_NORMED)
        values = cv2.minMaxLoc(res)
        x = values[2][0]
        # x = int(x * 280 / 680)
        # x = x - 26
        x = x + 10
        action = ActionChains(bro)
        y = bro.find_element_by_css_selector('.yidun_jigsaw')
        action.click_and_hold(y).perform()
        # for mo in range(5):
        #     action.move_by_offset(int(x/5), 0)
        #     time.sleep(0.5)
        action.move_by_offset(x,0)
        action.release().perform()  # 松开进行验证
        time.sleep(3)
        try:
            bro.find_element_by_xpath('//*[@id="root"]/div/main/div/div/div/div[1]/div/div[1]/form/button')  # 查看这个标签还在不在
            # 因为如果在的话就表示验证码没有滑倒准确位置，点击刷新按钮进行刷新
            # 如果不在的话则说明验证码验证成功，页面已经跳转
            # 就会报异常
            time.sleep(1)
        except:
            break  # 跳出异常即可
    te = bro.find_element_by_css_selector('.Input')
    te.send_keys('python')
    by = bro.find_element_by_css_selector('.Zi')
    by.click()
    time.sleep(3)
    bro.quit()