#!/usr/bin/python3.7
# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/11/12 9:47
# @File    : 获取csv数据.py
# @Function:

# import csv
# path = r'./txt/knowle.csv'
# def read_csv(path):
#     mylist = []
#     with open(path,'r') as f:
#         info = csv.reader(f)
#         for i in info:
#             mylist.append(i)
#         return mylist
#
# # print(read_csv(path))
#
# from openpyxl.reader.excel import load_workbook
# path = r'./txt/knowedge.xlsx'
# file = load_workbook(filename=path)
# table = file.get_sheet_names() # 获取所有表格的名称
# # table = file.worksheets[0]
# print(table)
# # 拿出第一个表格
# # sheet = workbook.worksheets[0]
# anli = file.get_sheet_by_name(table[0])
# print(anli)
# # print(anli.max_row) # 获取第一个表的当前行数
# # print(anli.max_column) # 获取第一个表的当前列数
#
# for num in range(1,anli.max_row+1):
#     mylist =[]
#     col = 3
#     #for col in range(2,4):
#     val = anli.cell(row=num,column=col).value # 根据行和列进行取值
    # print(val)
#



# for i in range(1,10):
#     print("INSERT INTO `hn_job_service`.`broad_complain` (`id`, `classify`, `channel`, `phone_number`, `city`, `req_time`, `content`, `suggestion`) VALUES ('"+str(i)+"'", '移动业务→基础服务→资费套餐→全局流转→费用质疑→对套餐内资源扣减不认可→全局流转', '10086人工', '13525084692', ' ', '2020-08-01 01:13:24', '“（1）问题描述：河南省13525084692客户反映：本机对手机产生流量的费用不认可，客户不愿意通过掌上营业厅等自助渠道尝试办理，在8月1日使用的流量为什么计算在7月份的账单里，经夜间口径解释不认可（2）客服查证：夜间专席无权查询办理（3）客户要求：尽快查询处理并回复（4）备注：联系电话13525084692@~预处理情况:请处理，谢谢', '请处理，谢谢');")"

# for i in range(1,106):
#     print("INSERT INTO `after_knowledge_category` (`parent_id`, `title`, `update_time`, `update_user`, `create_time`, `create_user`, `knowledge_id`) VALUES (NULL, '" +'campus'+str(i)+"'"+", '2020-11-11 20:19:21', 'admin', '2020-11-13 14:33:21', 'admin', 4);")
# i = 8
# # for i in range(4,10):
# print("INSERT INTO `hn_job_service`.`broad_complain` (`id`, `classify`, `channel`, `phone_number`, `city`, `req_time`, `content`, `suggestion`) VALUES ("+"'"+str(i)+"'"+", '移动业务→基础服务→资费套餐→全局流转→费用质疑→对套餐内资源扣减不认可→全局流转', '10086人工', '13525084692', ' ', '2019-07-01 01:13:24', '“（1）问题描述：河南省13525084692客户反映：本机对手机产生流量的费用不认可，客户不愿意通过掌上营业厅等自助渠道尝试办理，在8月1日使用的流量为什么计算在7月份的账单里，经夜间口径解释不认可（2）客服查证：夜间专席无权查询办理（3）客户要求：尽快查询处理并回复（4）备注：联系电话13525084692@~预处理情况:请处理，谢谢', '请处理，谢谢');")



#INSERT INTO `hn_job_service`.`broad_complain` (`id`, `classify`, `channel`, `phone_number`, `city`, `req_time`, `content`, `suggestion`) VALUES ('20200801011905C854261581X', '移动业务→基础服务→资费套餐→全局流转→费用质疑→对套餐内资源扣减不认可→全局流转', '10086人工', '13525084692', ' ', '2020-08-01 01:13:24', '“（1）问题描述：河南省13525084692客户反映：本机对手机产生流量的费用不认可，客户不愿意通过掌上营业厅等自助渠道尝试办理，在8月1日使用的流量为什么计算在7月份的账单里，经夜间口径解释不认可（2）客服查证：夜间专席无权查询办理（3）客户要求：尽快查询处理并回复（4）备注：联系电话13525084692@~预处理情况:请处理，谢谢', '请处理，谢谢');

# mylist = []
with open('08-25.sql','w',encoding='utf-8') as f:
    for i in range(540000,570000):
        f.write("INSERT INTO `hn_job_service`.`broad_complain` (`id`, `classify`, `channel`, `phone_number`, `city`, `req_time`, `content`, `suggestion`) VALUES ("+"'"+str(i)+"'"+", '移动业务→基础服务→资费套餐→全局流转→费用质疑→对套餐内资源扣减不认可→全局流转', '10086人工', '13525084692', ' ', '2020-08-25 01:13:24', '“（1）问题描述：河南省13525084692客户反映：本机对手机产生流量的费用不认可，客户不愿意通过掌上营业厅等自助渠道尝试办理，在8月1日使用的流量为什么计算在7月份的账单里，经夜间口径解释不认可（2）客服查证：夜间专席无权查询办理（3）客户要求：尽快查询处理并回复（4）备注：联系电话13525084692@~预处理情况:请处理，谢谢', '请处理，谢谢');")

with open('08-26.sql','w',encoding='utf-8') as f:
    for i in range(570000,600000):
        f.write("INSERT INTO `hn_job_service`.`broad_complain` (`id`, `classify`, `channel`, `phone_number`, `city`, `req_time`, `content`, `suggestion`) VALUES ("+"'"+str(i)+"'"+", '移动业务→基础服务→资费套餐→全局流转→费用质疑→对套餐内资源扣减不认可→全局流转', '10086人工', '13525084692', ' ', '2020-08-26 01:13:24', '“（1）问题描述：河南省13525084692客户反映：本机对手机产生流量的费用不认可，客户不愿意通过掌上营业厅等自助渠道尝试办理，在8月1日使用的流量为什么计算在7月份的账单里，经夜间口径解释不认可（2）客服查证：夜间专席无权查询办理（3）客户要求：尽快查询处理并回复（4）备注：联系电话13525084692@~预处理情况:请处理，谢谢', '请处理，谢谢');")

with open('08-27.sql','w',encoding='utf-8') as f:
    for i in range(600000,630000):
        f.write("INSERT INTO `hn_job_service`.`broad_complain` (`id`, `classify`, `channel`, `phone_number`, `city`, `req_time`, `content`, `suggestion`) VALUES ("+"'"+str(i)+"'"+", '移动业务→基础服务→资费套餐→全局流转→费用质疑→对套餐内资源扣减不认可→全局流转', '10086人工', '13525084692', ' ', '2020-08-27 01:13:24', '“（1）问题描述：河南省13525084692客户反映：本机对手机产生流量的费用不认可，客户不愿意通过掌上营业厅等自助渠道尝试办理，在8月1日使用的流量为什么计算在7月份的账单里，经夜间口径解释不认可（2）客服查证：夜间专席无权查询办理（3）客户要求：尽快查询处理并回复（4）备注：联系电话13525084692@~预处理情况:请处理，谢谢', '请处理，谢谢');")
with open('08-28.sql', 'w', encoding='utf-8') as f:
    for i in range(630000, 660000):
        f.write(
            "INSERT INTO `hn_job_service`.`broad_complain` (`id`, `classify`, `channel`, `phone_number`, `city`, `req_time`, `content`, `suggestion`) VALUES (" + "'" + str(
                i) + "'" + ", '移动业务→基础服务→资费套餐→全局流转→费用质疑→对套餐内资源扣减不认可→全局流转', '10086人工', '13525084692', ' ', '2020-08-28 01:13:24', '“（1）问题描述：河南省13525084692客户反映：本机对手机产生流量的费用不认可，客户不愿意通过掌上营业厅等自助渠道尝试办理，在8月1日使用的流量为什么计算在7月份的账单里，经夜间口径解释不认可（2）客服查证：夜间专席无权查询办理（3）客户要求：尽快查询处理并回复（4）备注：联系电话13525084692@~预处理情况:请处理，谢谢', '请处理，谢谢');")

with open('08-29.sql', 'w', encoding='utf-8') as f:
    for i in range(690000, 720000):
        f.write(
            "INSERT INTO `hn_job_service`.`broad_complain` (`id`, `classify`, `channel`, `phone_number`, `city`, `req_time`, `content`, `suggestion`) VALUES (" + "'" + str(
                i) + "'" + ", '移动业务→基础服务→资费套餐→全局流转→费用质疑→对套餐内资源扣减不认可→全局流转', '10086人工', '13525084692', ' ', '2020-08-29 01:13:24', '“（1）问题描述：河南省13525084692客户反映：本机对手机产生流量的费用不认可，客户不愿意通过掌上营业厅等自助渠道尝试办理，在8月1日使用的流量为什么计算在7月份的账单里，经夜间口径解释不认可（2）客服查证：夜间专席无权查询办理（3）客户要求：尽快查询处理并回复（4）备注：联系电话13525084692@~预处理情况:请处理，谢谢', '请处理，谢谢');")

