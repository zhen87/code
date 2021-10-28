import  math
import random
i=1
m=random.randint(0,100)
a=int(input('你想要猜的数字\n'))
while a != m:
    if a>m:
        print('猜的有点大啦，可以再猜一猜\n')
        a=int(input())
    else:
        print('猜的有点小了，可以再猜一猜\n')
        a=int(input())
    i+=1
print('恭喜你，猜对了')
