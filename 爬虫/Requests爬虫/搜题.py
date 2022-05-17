# -*- coding:utf-8 -*-
# author:LeiLei
import json

import requests
from hello import Ui_MainWindow
from PyQt5 import QtCore, QtGui, QtWidgets
import sys
from threading import Thread

headers = {
    'User-Agent': 'Mozilla/5.0 (windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/93.0.4573.0 Safari/537.36'
}

class query_window(QtWidgets.QMainWindow):
    def __init__(self):
        QtWidgets.QMainWindow.__init__(self)
        self.ui = Ui_MainWindow()
        self.ui.setupUi(self)
        #查询
        self.ui.s.clicked.connect(self.query)
        #关闭
        self.ui.e.clicked.connect(self.exit)
        #设置接口
        self.url1 = 'http://q.zhizhuoshuma.cn/?question={}'
        self.url2 = 'http://api.902000.xyz:88/wkapi.php?q={}'
    def query(self):
        self.ui.a.setText('')
        Thread(target=self.deepsearch1,args=(self.url1,)).start()
        Thread(target=self.deepsearch2,args=(self.url2,)).start()



    def deepsearch1(self,url):
        try:
            text = requests.get(url.format(self.ui.q.toPlainText()), headers, timeout=5).text
        except:
            self.ui.a.append('超时即不存在此题')
            return ''
        else:
            te = json.loads(text.split('}')[0] + '}')
            self.ui.a.append(te['question'] + '\n' + te['answer'] + '\n' * 3)
    def deepsearch2(self,url):
        try:
            text = requests.get(url.format(self.ui.q.toPlainText()), headers, timeout=5).text
        except:
            self.ui.a.append('超时即不存在此题')
        else:
            te = json.loads(text)
            self.ui.a.append(te['tm'] + '\n' + te['answer']+'\n'*3)
    def exit(self):
        # 退出
        sys.exit(app.exec_())
if __name__ == '__main__':
    app = QtWidgets.QApplication(sys.argv)
    window = query_window()
    window.show()
    sys.exit(app.exec_())




