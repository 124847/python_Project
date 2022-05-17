# -*- coding:utf-8 -*-
# author:LeiLei
import requests
import pywifi,time

#保存包中写义的常量
from pywifi import const
def connect_wifi():
    wifi = pywifi.PyWiFi()  # 创建一个wifi对象
    ifaces = wifi.interfaces()[0]  # 取第一个无限网卡
    # print(ifaces.name())  # 输出无线网卡名称
    ifaces.disconnect()  # 断开网卡连接
    time.sleep(2)  # 缓冲2秒


    profile = pywifi.Profile()  # 配置文件
    profile.ssid = "HIST-Student"  # wifi名称


    ifaces.remove_all_network_profiles()  # 删除其他配置文件
    tmp_profile = ifaces.add_network_profile(profile)  # 加载配置文件

    ifaces.connect(tmp_profile)  # 连接
    time.sleep(2)  # 尝试2秒能否成功连接
    # isok = True
    if ifaces.status() == const.IFACE_CONNECTED:
        print("成功连接校园网")
        return True
    else:
        print("未成功连接校园网")
        return False
    #ifaces.disconnect()  # 断开连接
    # time.sleep(1)
    # return isok
if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/93.0.4573.0 Safari/537.36'
    }

    url = 'http://111.6.96.84:9999/portalAuthAction.do'
    data = {
    }
    while not connect_wifi():
        pass
    while True:
        text = ''
        try:
            text = requests.post(url,data,headers=headers,timeout=3)
        except :
                print('连接超时,再试一次')
        # text.encode('utf-8')
        else:
            # text.encoding = 'utf-8'
            print(text.text)
            break;
    else:
        print('成功登录校园网')