#!/usr/bin/python3.6
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/9/25 10:04
# @File    : 6.py
# @Function:

import re
mystr = '''
曹　艳	Caoyan	6895	13811661805	caoyan@baidu.com
曹　宇	Yu Cao	8366	13911404565	caoyu@baidu.com
曹　越	Shirley Cao	6519	13683604090	caoyue@baidu.com
曹　政	Cao Zheng	8290	13718160690	caozheng@baidu.com
查玲莉	Zha Lingli	6259	13552551952	zhalingli@baidu.com
查　杉	Zha Shan	8580	13811691291	zhashan@baidu.com
查　宇	Rachel	8825	13341012971	zhayu@baidu.com
柴桥子	John	6262	13141498105	chaiqiaozi@baidu.com
常丽莉	lily	6190	13661003657	changlili@baidu.com
车承轩	Che Chengxuan	6358	13810729040	chechengxuan@baidu.com
陈　洁	Che	13811696984	chenxi_cs@baidu.com
陈　超	allen	8391	13810707562	chenchao@baidu.com
陈朝辉		13714189826	chenchaohui@baidu.com
陈　辰	Chen Chen	6729	13126735289	chenchen_qa@baidu.com
陈　枫	windy	8361	13601365213	chenfeng@baidu.com
陈海腾	Chen Haiteng	8684	13911884480	chenhaiteng@baidu.com
陈　红	Hebe	8614	13581610652	chenhong@baidu.com
陈后猛	Chen Houmeng	8238	13811753474	chenhoumeng@baidu.com
陈健军	Chen Jianjun	8692	13910828583	chenjianjun@baidu.com
陈　景	Chen Jing	6227	13366069932	chenjing@baidu.com
陈竞凯	Chen Jingkai	6511	13911087971	jchen@baidu.com
陈　坤	Isa13810136756	chenlei@baidu.com
陈　林	Lin Chen	6828	13520364278	chenlin@qq.com
'''

# print(re.findall('\w{5,10}@baidu.com',mystr))
# print(re.findall('\w*@baidu.com',mystr))
# print(re.findall('\w+@baidu.com',mystr))
# print(re.findall('\w+@\w+.com',mystr))
# print(re.findall('\w+@\w+\.\w{2,4}',mystr))# 读取邮箱

# print(re.findall('\d{11}',mystr))
# print(re.findall('[1][3-8][0-9]{9}',mystr))
#
# prg = re.compile('[1][3-8][0-9]{9}')
# print(prg.findall(mystr))


mystr1 = '''<b>wsdfghj你会
         不会</b>
         <B>第二分过火把节</b>'''

# print(re.findall('<b>.*?</b>',mystr1,flags=re.I))
# print(re.findall('<b>.*?</b>',mystr1,flags=re.S))
# print(re.findall('<b>.*?</b>',mystr1,flags=re.I|re.S)) #将大小写和换行都匹配出来
