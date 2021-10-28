import  random

moneymunber =20
time=0
while True:
    num = random.randrange(1,100)
    time += 1
    if moneymunber == num:
        print('yes',num)
        break
print(time)

