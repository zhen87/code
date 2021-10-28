#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/8/31 17:17
# @File    : 10.py
# @Function: 继承

# class Demo(object): # 基类  也称为父类 所有的类都会继承
#     def speak(self):
#         print('我是说的方法')
#
#
# d = Demo()
# d.speak()


class Animal:
    def eat(self):
        print('eating')

    def wangwang(self):
        print('狗在汪汪汪')


class Dog(Animal):
    pass

class Cat(Animal):
    def wangwang(self): #方法的重写
        # Animal.wangwang(self)
        # super().wangwang() #使用super调用我的父类方法
        super(Cat,self).wangwang() #super 参数之类的类名，self
        print('猫在叫')
    pass



cat = Cat()
dog = Dog()
# dog.eat()
# cat.eat()
# dog.wangwang()
cat.wangwang()
