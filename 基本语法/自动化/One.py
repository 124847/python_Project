# -*- coding:utf-8 -*-
# author:LeiLei

headers = {
        'User-Agent' : 'Mozilla/5.0 (windows NT 10.0; Win64; x64) AppleWebkit/537.36 (KHTML, like Gecko) Chrome/93.0.4573.0 Safari/537.36'
        }


import pyautogui

pyautogui.screenshot("1.png")



# pyautogui.moveTo(x=500, y=500, duration=2, tween=pyautogui.easeInOutQuad)
#鼠标拖拽
# pyautogui.dragTo(x=427, y=535, duration=3,button='left')

#鼠标相对拖拽
# pyautogui.dragRel(xOffset=-30,yOffset=-30,duration=2,button='left',mouseDownUp=True)



# im1 = pyautogui.screenshot()
# im1.save('my_screenshot.png')
# coords = pyautogui.locateCenterOnScreen("img.png")
# coords = pyautogui.locateCenterOnScreen("img_1.png")
# coords = pyautogui.locateCenterOnScreen("img_2.png")
# pyautogui.click(coords[0],coords[1]);
# pyautogui.click(x=471, y=613,clicks=1000,interval=0.0)



# #鼠标移动到x=1796, y=778位置按下
# pyautogui.mouseDown(x=1796, y=778, button='left')
#
# #鼠标移动到x=2745, y=778位置松开（与mouseDown组合使用选中）
# pyautogui.mouseUp(x=2745, y=778, button='left',duration=5)
