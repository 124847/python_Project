# -*- coding:utf-8 -*-
# author:LeiLei
import time
import numpy as np
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium import webdriver
from cv2 import cv2
import requests
from selenium.webdriver import ActionChains
from selenium.webdriver.chrome.options import Options

if __name__ == '__main__':
    # 规避检测部分
    headers = {
        'User-Agent': 'Mozilla/5.0 (windows NT 10.0; Win64; x64) '
                      'AppleWebkit/537.36 (KHTML, like Gecko) Chrome/93.0.4573.0 Safari/537.36'
    }
    chrome_options = Options()
    # chrome_options.add_argument("--headless")  # 是否设置无头
    # chrome_options.add_argument('--disable-gpu') # 如果不加这个选项，有时定位会出现问题
    chrome_options.add_argument(
        f'user-agent={headers["User-Agent"]}'
    )
    chrome_options.add_experimental_option('excludeSwitches', ['enable-automation'])# 规避检测方法1
    # chrome_options.add_argument('--proxy-server=http://ip:port')
    bro = webdriver.Chrome(options=chrome_options)
    # bro.maximize_window()
    with open('D:/GitHub/stealth.min.js-main/stealth.min.js-main/stealth.min.js') as fp: # 规避检测方法2
        js = fp.read()
    bro.execute_cdp_cmd("Page.addScriptToEvaluateOnNewDocument", {"source": js})
    # 请求部分
    bro.get('https://qzone.qq.com/')
    bro.switch_to.frame('login_frame')
    loc1 = (By.ID, 'switcher_plogin')
    # 登录部分
    WebDriverWait(bro, 20, 0.5).until(EC.presence_of_element_located(loc1))
    wt = bro.find_element_by_id('switcher_plogin')
    wt.click()
    loc2 = (By.ID, 'u')
    loc3 = (By.ID, 'p')
    WebDriverWait(bro, 20, 0.5).until(EC.presence_of_element_located(loc2))
    WebDriverWait(bro, 20, 0.5).until(EC.presence_of_element_located(loc3))
    id_s = bro.find_element_by_id('u')
    password_s = bro.find_element_by_id('p')
    id_s.send_keys('1248479090')
    time.sleep(1)
    password_s.send_keys('111000ddd')
    time.sleep(1)
    login_s = bro.find_element_by_id('login_button')
    login_s.click()  # 点击登录
    time.sleep(1)
    try:
        bro.switch_to.frame('tcaptcha_iframe')
    except:
        pass
    # 滑动验证码验证
    while True:  # 循环进行刷新验证码，第一次验证不成功就刷新验证码再进行新图片的验证
        try:
            bak = bro.find_element_by_id('slideBg')
            mod = bro.find_element_by_id('slideBlock')
            bak_src = bak.get_attribute('src')
            mod_src = mod.get_attribute('src')
            b_content = requests.get(bak_src).content
            m_content = requests.get(mod_src).content
            with open('./qq_b.jpg', 'wb') as fp:
                fp.write(b_content)
                fp.close()
            with open('./qq_m.jpg', 'wb') as fp:
                fp.write(m_content)
                fp.close()
            # b_rgb = cv2.imdecode(np.fromfile('../文件/验证码/qq_b.jpg', dtype=np.uint8), -1)
            # m_rgb = cv2.imdecode(np.fromfile('../文件/验证码/qq_m.jpg', dtype=np.uint8), 1)
            b_rgb = cv2.imread('./qq_b.jpg')
            b_gray = cv2.cvtColor(b_rgb, cv2.COLOR_BGR2GRAY)
            m_rgb = cv2.imread('./qq_m.jpg', 0)
            res = cv2.matchTemplate(b_gray, m_rgb, cv2.TM_CCORR_NORMED)
            values = cv2.minMaxLoc(res)
            x = values[2][0]
            x = int(x * 280 / 680)
            x = x - 26
            action = ActionChains(bro)
            y = bro.find_element_by_id('tcaptcha_drag_thumb')
            action.click_and_hold(y).perform()
            action.move_by_offset(x, 0)
            action.release().perform()  # 松开进行验证
            time.sleep(1)
        except:
            break
        try:
            bro.find_element_by_id('e_reload').click()  # 查看这个标签还在不在
            # 因为如果在的话就表示验证码没有滑倒准确位置，点击刷新按钮进行刷新
            # 如果不在的话则说明验证码验证成功，页面已经跳转
            # 就会报异常
            time.sleep(1)
        except:
            break  # 跳出异常即可
    # 结束 关闭浏览器
    time.sleep(10)
    bro.quit()
