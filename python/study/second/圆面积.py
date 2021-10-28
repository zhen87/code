import  math
a=input('半径\n')
r = float(a)
if r>0:
    sum = float(3.14*r*r)
elif r>0:
    print('半径不能为0')
else:
    print('半径不能为负')
print(sum)
