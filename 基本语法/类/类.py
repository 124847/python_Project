# -*- coding: utf-8 -*-

# Form implementation generated from reading ui file '类'
#
# Created by: PyQt5 UI code generator 5.15.2
#
# WARNING: Any manual changes made to this file will be lost when pyuic5 is
# run again.  Do not edit this file unless you know what you are doing.


class Au(object):

    def __init__(self, name):
        self.name = name
    def __setitem__(self, k, v):
        self.k = v

    def __str__(self):
        return "name:%s, %s" % (self.name, self.k)
if __name__ == '__main__':
    t = Au('5')
    t['a'] = 12
    t['b'] = 16
    print(t)