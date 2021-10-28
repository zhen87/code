#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/11/23 18:01
# @File    : csq.py
# @Function: word 数据转换为excel

import re
import xlwt



path = r'../txt/CCP&OPRP.txt'
# path1 = r'./txt/CCP&OPRP1.xls'
# path = r'./txt/csq_1.txt'
path1 = r'../txt/CCP&OPRP1.xls'


# def readtxt(path):
# def writeCsv(mylist):
#     with open(path1,"w",newline='') as f: # 生成文件无空行
#         write = csv.writer(f)
#         for i in mylist:
#             print("row=", i)
#             write.writecolumn(i)

def writeCsv(mylist):
    workbook = xlwt.Workbook(encoding='utf-8')
    worksheet = workbook.add_sheet('test')
    title = ['题干', '选项A', '选项B', '选项C', '选项D', '选项E', '选项F', '选项G']
    for x in range(len(title)):
        worksheet.write(0, x, title[x])
    # i = 题目,列,mylist[0]
    # print(len(mylist[0]))
    # print(len(mylist))
    for i in range(0, len(mylist[0])):
        for j in range(0, len(mylist)):
            # print(mylist[j][i])
            try:
                worksheet.write(i + 1, j, mylist[j][i])
            except IndexError:
                # worksheet.write('/',mylist[j][i])
                print('索引越界')

    workbook.save(path1)
    # # print(path)
    # print(mylist[0][0])
    # print(mylist[1][0])
    # print(mylist[2][0])
    # print(mylist[3][0])
    # print(mylist[4][0])


with open(path, 'r', encoding='utf-8') as f:
    mylist_before = []
    mylistA = []
    mylistB = []
    mylistC = []
    mylistD = []
    mylistE = []
    mylistF = []
    mylistG = []
    state = 0
    mylist_question = []
    for word in f.readlines():
        word = word.replace('\n', '')
        # 首字符是否为数字，若为数字，将该行添加到mylist_question 列表中
        if word[0].isdigit() == True:
            mylist_question.append(word)
            # 判断当前的 state 的状态
            if state == 1:
                #state =1,代表只有A选项，则后续选项均用"/"填补
                mylistB.append('/')
                mylistC.append('/')
                mylistD.append('/')
                mylistE.append('/')
                mylistF.append('/')
                mylistG.append('/')
            elif state == 2:
                # state =2,代表只有A,B选项，则后续选项均用"/"填补
                mylistC.append('/')
                mylistD.append('/')
                mylistE.append('/')
                mylistF.append('/')
                mylistG.append('/')
            elif state == 3:
                #以此类推
                mylistD.append('/')
                mylistE.append('/')
                mylistF.append('/')
                mylistG.append('/')
            elif state == 4:
                mylistE.append('/')
                mylistF.append('/')
                mylistG.append('/')
            elif state == 5:
                mylistF.append('/')
                mylistG.append('/')
            elif state == 6:
                mylistG.append('/')

        # 判断方式一
        # 首字符是否为A，若为A，将该行添加到mylistA列表中 列表中
        elif word[0] == 'A':
            # 将A选项的A字符删除
            word = re.sub('A.', '', word)
            # 将该行添加到mylistA列表中
            mylistA.append(word)
            # 修改状态为A选项的状态
            state = 1
        elif word[0] == 'B':
            word = re.sub('B.', '', word)
            mylistB.append(word)
            state = 2
        elif word[0] == 'C':
            word = re.sub('C.', '', word)
            mylistC.append(word)
            state = 3
        elif word[0] == 'D':
            word = re.sub('D.', '', word)
            mylistD.append(word)
            state = 4
        elif word[0] == 'E':
            word = re.sub('E.', '', word)
            mylistE.append(word)
            state = 5
        elif word[0] == 'F':
            word = re.sub('F.', '', word)
            mylistF.append(word)
            state = 6
        elif word[0] == 'G':
            word = re.sub('G.', '', word)
            mylistG.append(word)
            state = 7
    # print(state)
    mylist = [mylist_question, mylistA, mylistB, mylistC, mylistD, mylistE, mylistF, mylistG]


    print(mylistF)
    # print(mylist_question)
writeCsv(mylist)
# print(mylist)
