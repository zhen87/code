def add(x,y):#加
    return x+y

def substract(x,y):#减
    return x-y

def multiple(x,y):#乘
    return x*y

def divide(x,y): #除
    return x/y

print('choose')
print('1:+',end='')
print('2:-',end='')
print('3,*',end='')
print('4:/')
mychoice = int(input('请选择选择1/2/3/4'))
num1 = int(input('输入数字1'))
num2 = int(input('输入数字2'))

if mychoice == 1:
    print(num1,"+",num2,"=",add(num1,num2))
elif mychoice == 2:
    print(num1,"+",num2,"=",substract(num1,num2))
elif mychoice == 3:
    print(num1,"+",num2,"=",multiple(num1,num2))
elif mychoice == 4:
    print(num1, "+", num2, "=", divide(num1,num2))

