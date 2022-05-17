# -*- coding:utf-8 -*-
# author:LeiLei
import time

import pyautogui
import requests


def click(name) :
    while True :
        screen = pyautogui.locateCenterOnScreen(name, confidence = 0.80)
        if screen != None :
            pyautogui.click(screen.x, screen.y, clicks = 1, interval = 0.2, duration = 0.2, button = "left")
            break;
        if screen== None and name == "img_4.png" :
            pyautogui.scroll(-100)
        time.sleep(0.1)


def gen() :
    click("img_5.png")
    click("img_6.png")
    click("img_7.png")
    click("img_8.png")
    while True :
        click("img_4.png")


if __name__ == '__main__' :
    gen()
