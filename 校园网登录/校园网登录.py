# -*- coding:utf-8 -*-
# author:LeiLei
import requests


def connect() :
    cookies = {
            'JSESSIONID' : '37665417F0054D1CDA48038A966A1909',
            }

    headers = {
            'Connection' : 'keep-alive',
            'Cache-Control' : 'max-age=0',
            'Upgrade-Insecure-Requests' : '1',
            'Origin' : 'http://111.6.96.84:9999',
            'Content-Type' : 'application/x-www-form-urlencoded',
            'User-Agent' : 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/97.0.4676.0 Safari/537.36',
            'Accept' : 'text/html,application/xhtml+xml,application/xml;q=0.9,image/avif,image/webp,image/apng,*/*;q=0.8,application/signed-exchange;v=b3;q=0.9',
            'Referer' : 'http://111.6.96.84:9999/portal.do?wlanuserip=10.102.15.48&wlanacname=HIST-BRAS&mac=dc:71:96:f7:31:ef&vlan=32003201&rand=3d6bb002c0949e&url=http://www.msftconnecttest.com/redirect',
            'Accept-Language' : 'zh-CN,zh;q=0.9',
            }

    data = {
            'wlanuserip' : '10.102.15.48',
            'wlanacname' : 'HIST-BRAS',
            'chal_id' : '',
            'chal_vector' : '',
            'auth_type' : 'PAP',
            'seq_id' : '',
            'req_id' : '',
            'wlanacIp' : '211.142.122.70',
            'ssid' : '',
            'vlan' : '32003201',
            'mac' : 'dc:71:96:f7:31:ef',
            'message' : '',
            'bank_acct' : '',
            'isCookies' : '',
            'version' : '0',
            'authkey' : '88----89',
            'url' : 'http://www.msftconnecttest.com/redirect',
            'usertime' : '0',
            'listpasscode' : '0',
            'listgetpass' : '0',
            'getpasstype' : '0',
            'randstr' : '4721',
            'domain' : '',
            'isRadiusProxy' : 'true',
            'usertype' : '0',
            'isHaveNotice' : '0',
            'times' : '12',
            'weizhi' : '0',
            'smsid' : '',
            'freeuser' : '',
            'freepasswd' : '',
            'listwxauth' : '0',
            'templatetype' : '1',
            'tname' : 'kjxy_pc_portal',
            'logintype' : '0',
            'act' : '',
            'is189' : 'false',
            'terminalType' : '',
            'checkterminal' : 'true',
            'portalpageid' : '484',
            'listfreeauth' : '0',
            'viewlogin' : '1',
            'userid' : '21201701304@kjxyyd',
            'authGroupId' : '',
            'useridtemp' : '21201701304@kjxyyd',
            'passwd' : '1234567890abc',
            'operator' : '@kjxyyd'
            }
    response = requests.post(
            'http://111.6.96.84:9999/portalAuthAction.do', headers = headers, cookies = cookies, data = data,
            verify = False
            )
    return response.status_code


import pywifi, time

# ???????????????????????????
from pywifi import const


def connect_wifi() :
    wifi = pywifi.PyWiFi()  # ????????????wifi??????
    ifaces = wifi.interfaces()[0]  # ????????????????????????
    # print(ifaces.name())  # ????????????????????????
    ifaces.disconnect()  # ??????????????????
    time.sleep(2)  # ??????2???

    profile = pywifi.Profile()  # ????????????
    profile.ssid = "HIST-Student"  # wifi??????

    ifaces.remove_all_network_profiles()  # ????????????????????????
    tmp_profile = ifaces.add_network_profile(profile)  # ??????????????????

    ifaces.connect(tmp_profile)  # ??????
    time.sleep(2)  # ??????2?????????????????????
    # isok = True
    if ifaces.status() == const.IFACE_CONNECTED :
        print("?????????????????????")
        return True
    else :
        print("????????????????????????")
        return False
    # ifaces.disconnect()  # ????????????
    # time.sleep(1)
    # return isok


if __name__ == '__main__' :
    headers = {
            'User-Agent' : 'Mozilla/5.0 (windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/93.0.4573.0 Safari/537.36'
            }
    while True :
        if connect_wifi() :
            while True :
                i = connect()
                print("?????????" + str(i))
                if requests.get("http://www.baidu.com", headers = headers).status_code == 200 :
                    print("????????????")
                    break
                print("??????????????????")
            break
