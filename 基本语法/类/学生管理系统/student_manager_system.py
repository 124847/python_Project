# -*- coding:utf-8 -*-
# author:LeiLei
import student


class StudentManagerSystem(object):
    def __init__(self):
        self.stu_dicts = {}

    @staticmethod
    def show_menu():
        print('1.添加学生')
        print('2.删除学生')
        print('3.修改学生信息')
        print('4.查询单个学生信息')
        print('5.查询所有学生信息')
        print('6.退出系统')

    def insert_student(self):
        stu_id = input('请输入学生的学号:')
        if stu_id in self.stu_dicts:
            print('学生信息已经存在,不需要再次添加...')
            return
        name = input('请输入学生的姓名:')
        age = input('请输入学生的年龄:')
        gender = input('请输入学生的性别:')
        stu = student.Student(stu_id, name, age, gender)
        self.stu_dicts[stu_id] = stu

    def show_all_info(self):
        for stu in self.stu_dicts.values():
            print(stu)

    def remove_student(self):
        stu_id = input('请输入学号')
        if stu_id in self.stu_dicts:
            del self.stu_dicts[stu_id]
            print('学生已经删除')
        else:
            print('学生信息不存在，无法删除...')

    def modify_student(self):
        stu_id = input('请输入学号')
        if stu_id in self.stu_dicts:
            stu = self.stu_dicts[stu_id]
            stu.age = input('请输入新的年龄')
            print('学生已经修改完毕...')
        else:
            print('学生信息不存在，不能修改...')

    def search_student(self):
        stu_id = input('请输入学号')
        if stu_id in self.stu_dicts:
            print(self.stu_dicts[stu_id])
        else:
            print('学生信息不存在，不能查看...')

    def save(self):
        f = open('学生信息.txt', 'w', encoding='utf-8')
        for stu in self.stu_dicts.values():
            f.write(str(stu) + '\n')
        f.close()

    def load_info(self):
        fp = open('学生信息.txt', 'r', encoding='utf-8')
        lists = fp.readlines()
        for li in lists:
            li = li.strip()
            stu_d = li.split(',')
            stu = student.Student(*stu_d)
            self.stu_dicts[stu_d[0]] = stu
        fp.close()

    def start(self):
        self.load_info()
        while True:
            self.show_menu()
            opt = input('请输入用来选择的操作编号:')
            if opt == '1':
                self.insert_student()
            elif opt == '2':
                self.remove_student()
            elif opt == '3':
                self.modify_student()
            elif opt == '4':
                self.search_student()
            elif opt == '5':
                self.show_all_info()
            elif opt == '6':
                self.save()
                print('欢迎下次使用本系统...')
                break
            else:
                print('输入有误，请再次输入')
                continue
            input('...回车继续操作...')
