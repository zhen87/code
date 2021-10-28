import math
import random
print(type(10/2))
print(10/2)

float=1.23
print(round(float))


float=1.234
# print(math.ceil(float))
# print(math.floor(float))
# print(math.pow(2,2))


print(random.choice('qasxx'))
str='去玩儿提测待定'
for i in range(len(str)):
    print(str[i])

print(random.randrange(1,10,3))

list=[1,2,3]
random.shuffle(list)
print(list)