# -*- coding:utf-8 -*-
# author:LeiLei
# selenium 浏览器自动化模块
# from selenium import webdriver
# bro = webdriver.Chrome()  创建一个浏览器对象
# bro.get(url) 发起请求
# 标签定位 bro.find 系列方法
# 标签定位返回对象.send_keys('xxx') 传入数据  进行交互
# 执行 js 代码    bro.execute_script('jsCode')
# 前进后退     bro.back() ,bro.forward()
# 关闭浏览器  bro.quit()
#
# 如果定位的标签试存在于iframe标签之中的则必须通过如下操作在进行标签定位
# bro.switch_to.frame('xxx') 切换浏览器标签到作用域  如果不切换 默认是最外层的作用域
# 所以 如果要得到嵌套内部的frame的标签要作用域的切换
#
# from selenium.webdriver import ActionChains
# 导入动作链对应的类
# action = ActionChains(bro)
# action.click_and_hold(标签) 点击长按指定的标签
# action.move_by_offset(x,y).perform()   移动
# action.release()
#
#
# 等待实例
# from selenium import webdriver
# from selenium.webdriver.support.wait import WebDriverWait
# from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.common.by import By
#
# driver = webdriver.Firefox()
# driver.implicitly_wait(10)  # 隐性等待和显性等待可以同时用，但要注意：等待的最长时间取两者之中的大者
# driver.get('https://huilansame.github.io')
# locator = (By.LINK_TEXT, 'CSDN')
#
# try:
#     WebDriverWait(driver, 20, 0.5).until(EC.presence_of_element_located(locator))
#     print driver.find_element_by_link_text('CSDN').get_attribute('href')
# finally:
#     driver.close()
#
# 规避检测
from selenium.webdriver.chrome.options import Options
from selenium.webdriver import ChromeOptions

# 实现无可视化界面操作
# chrome_options = Options()
# chrome_options.add_argument('--headless')
# chrome_options.add_argument('--disable-gpu')
# chrome_options.add_argument('--headless') # 无头模式
# chrome_options.add_argument('--disable-gpu') # 禁用GPU加速
# chrome_options.add_argument('--start-maximized')#浏览器最大化
# chrome_options.add_argument('--window-size=1280x1024') # 设置浏览器分辨率（窗口大小）
# chrome_options.add_argument('log-level=3')
# #info(default) = 0
# #warning = 1
# #LOG_ERROR = 2
# #LOG_FATAL = 3
#
# chrome_options.add_argument('--user-agent=""') # 设置请求头的User-Agent
# chrome_options.add_argument('--disable-infobars') # 禁用浏览器正在被自动化程序控制的提示
# chrome_options.add_argument('--incognito') # 隐身模式（无痕模式）
# chrome_options.add_argument('--hide-scrollbars') # 隐藏滚动条, 应对一些特殊页面
# chrome_options.add_argument('--disable-javascript') # 禁用javascript
# chrome_options.add_argument('--blink-settings=imagesEnabled=false') # 不加载图片, 提升速度
#
# chrome_options.add_argument('--ignore-certificate-errors') # 禁用扩展插件并实现窗口最大化
# chrome_options.add_argument('–disable-software-rasterizer')
# chrome_options.add_argument('--disable-extensions')
# 实现规避检测
# option = ChromeOptions()
# option.add_experimental_option('excludeSwitches', ['enable-automation'])
# bro = webdriver.Chrome(chrome_options=chrome_options, options=option)


# bro.switch_to.window(bro.window_handles[1])  #注意移动界面