#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/7/21 15:48
# @File    : 12.py
# @Function:
import codecs


# mystr = 'abcdfg'
# print(mystr.find('g'))#字符串查找，从左侧查找 如果找到返回对应的索引值，找不到返回-1
# print(mystr.rfind('g'))#字符串查找，从右侧查找 如果找到返回对应的索引值，找不到返回-1

# path = 'C:\Users\admin\Desktop'
# 数据加载并返回函数
def load(path):
    # path = r'C:\Users\admin\Desktop\test.txt'  # r/R 将具有特殊意义的字符进行转义成普通字符
    f = codecs.open(path, 'rb', encoding='utf-8', errors='ignore')  # 解码出现问题，忽略
    lines = f.readlines()
    return lines


date = load(path=r'E:\study\python\python-python3.7\python-JB\学习\seven\test1.txt')


def search(name):
    # name = '张'
    namefile = r'E:\study\python\python-python3.7\python-JB\学习\seven\\' + name + '.txt'  # 用搜索的名字创建文件
    f = open(namefile, 'wb')
    num = 0
    for i in date:
        mysearch = i[0:4]  # 将名字的长度进行截取
        if mysearch.find(name) != -1:  # 在截取的名字中进行匹配
            # if i.find(name) != -1:
            print(i)
            f.write(i.encode('utf-8'))  # 以utf-8 的形式编码
            num = +1  # 次数统计+1
    f.close()
    print('有{}条数据'.format(num))  # 输出数据的总数


while True:
    name = input('请输入')
    search(name)
