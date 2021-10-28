#左侧正三角形
# for i in range(1,10):
#     for x in range(1,i+1):
#         print(x,end='')
#     print()
#右侧正三角形
# for i in range(1,10):
#     for x in range(1,10-i):
#         print(' ',end='')
#     mylist =list(range(1,i+1))
#     mylist.reverse()#列表反转
#     for j in range(1,i+1):
#         print(j,end='')
#     print()
#左侧倒三角形
# for i in range(1,10):
#     for x in range(1,11-i):
#         print(x,end='')
#     print('')
#右侧倒三角形
mylist = list(range(1, 10))
mylist.reverse()  # 列表反转
for i in mylist:
    list2 = list(range(1,i+1))
    list2.reverse()
    for x in list2:
        print(x,end='')
    print()