import requests

if __name__ == '__main__':
    url = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsList'
    url_detail = 'http://scxk.nmpa.gov.cn:81/xk/itownet/portalAction.do?method=getXkzsById'
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/93.0.4573.0 Safari/537.36'
    }
    id_list = []
    all_details = []
    for page_detail in range(1, 5):
        data = {
            'on': 'true',
            'page': page_detail,
            'pageSize': '15',
            'productName': '',
            'conditionType': '1',
            'applyname': '',
            'applysn': ''
        }
        json_id = requests.post(url, data=data, headers=headers).json()
        for dic in json_id['list']:
            id_list.append(dic['ID'])
        print(id_list)
    fp = open('../文件/药监总局.txt','w',encoding='utf-8')
    for id_detail in id_list:
        data_detail = {
            'id': id_detail
        }
        json_details = requests.post(url_detail, data=data_detail, headers=headers).json()
        all_details.append([json_details['epsName'],json_details['epsProductAddress']])
    all_details = str(all_details)
    fp.write(all_details)
    fp.close()