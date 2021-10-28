
#1-10的奇数
# a = 0
# while a < 10:
#     if a % 2 == 1:
#         print(a)
#     a += 1

myum = 8
while True:
    num = int(input('please'))
    if myum == num:
        print('yes')
    elif num > 8:
        print('big')
    else:
        print('small')