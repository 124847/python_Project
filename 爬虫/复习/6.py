# -*- coding:utf-8 -*-
# author:LeiLei
from copyheaders import headers_raw_to_dict
import copyheaders
if __name__ == '__main__':
    headers = {
        'User-Agent': 'Mozilla/5.0 (windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/93.0.4573.0 Safari/537.36'
    }
    rh = b'''
    wlanuserip: 10.102.15.48
    wlanacname: HIST-BRAS
    chal_id:
    chal_vector:
    auth_type: PAP
    seq_id:
    req_id:
    wlanacIp: 211.142.122.70
    ssid:
    vlan: 32003201
    mac: dc:71:96:f7:31:ef
    message:
    bank_acct:
    isCookies:
    version: 0
    authkey: 88----89
    url: http://www.gstatic.com/generate_204
    usertime: 0
    listpasscode: 0
    listgetpass: 0
    getpasstype: 0
    randstr: 6429
    domain:
    isRadiusProxy: true
    usertype: 0
    isHaveNotice: 0
    times: 12
    weizhi: 0
    smsid:
    freeuser:
    freepasswd:
    listwxauth: 0
    templatetype: 1
    tname: kjxy_pc_portal
    logintype: 0
    act:
    is189: false
    terminalType:
    checkterminal: true
    portalpageid: 484
    listfreeauth: 0
    viewlogin: 1
    userid: 20191574206@kjxyyd
    authGroupId:
    useridtemp: 20191574206@kjxyyd
    passwd: 111000ddd
    operator: @kjxyyd'''


dic = headers_raw_to_dict(rh)

for i in dic:
    print(i)
