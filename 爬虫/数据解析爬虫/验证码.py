# -*- coding:utf-8 -*-
# author:LeiLei
# 有这一警告的原因在于，验证码的图片模式为RGBA，是无法分配调色盘给透明通道的。更换为RGB模式则不会出现该问题。
#
# 所以我对原先的代码进行修改，变为：image = image.convert('RGB') 即可


# python对tesseract封装有tesserocr和pytesseract，当pip3
# install
# tesserocr失败可以用pyteseract安装  tesserocr不支持64位
#
# 1
# 安装的是tesseract - ocr - w64 - setup - v5
# .0
# .0
# .20190623.exe 。地址https: // digi.bib.uni - mannheim.de / tesseract /     。
#
# 2
# 勾选Additional
# language
# data(download)，里面的简体中文。（fanqiang）
#
# 3
# 下载完。配置环境变量，Path：你的安装目录\Tesseract - OCR。配置环境变量，新建变量名TESSDATA_PREFIX，变量值：你的安装目录\Tesseract - OCR\tessdata
#
# 4.
# cmd命令行tesseract - v可以查看版本
#
# 5.
# 在命令行输入下列命令
# pip
# install
# pytesseract
# pip
# install
# pillow
#
# 6
#
# import pytesseract
# from PIL import Image
#
# image = Image.open('D://vote//test//tesseract.png')
# print(pytesseract.image_to_string(image))
#
# 注意验证码使用时要注意 一定要使用同一个session      Session保存那种状态,否则不是一次请求,验证码也不同，验证码识别出来也没用
# 即如果不用session第二次请求的验证码和第一次不是一个验证码
# 所以先创建Session对象   session = requests.Session()  使用requests中的方法实例化
# 然后就用 session.get()  session.post()   和 requests用法是一样的 只是保持了cookie的状态
