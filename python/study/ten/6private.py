#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/8/20 15:32
# @File    : 6private.py
# @Function:

class Test:
    __money =1000
    mymoney = 100
    age = 10
    def speak(self):
        print('我有{}钱'.format(self.__money))
        # return self.__money
    def updateAge(self,age):
        try:
            if age >0 and age <100: #判断年龄是否在1-99的范围内
                self.__age=age #在这个范围内，需改他的值
            else:
                raise ValueError('error')  #age是数值类型，但是不符合条件，抛出ValueError的异常，错误信息为 error
        except TypeError as T: #捕获age的类型错误
            print(T)  #将错误信息输出

test = Test()
test.updateAge('a')
test.updateAge('a')
test.updateAge(1010)

# # # money = test.mymoney
# # # # money = test.__money
# # # print('我有{}钱'.format(money))
# #
# # test.speak()
# # print(test._Test__money)#私有属性的获取方式
#
# test.__money = '我是类的外部去修改的值' #错误的修改私有属性的值，因为这样子属于动态添加
# print(test.__money)# 错误的
# test.speak()

