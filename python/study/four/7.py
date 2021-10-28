#正三角形
# for i in range(1,10):
#     for x in range(i,i+1):
#         print(x,end='')
#     print()
#正三角形2
for i in range(1,10):
    for x in range(i,10):
        print(' ',end='')
    for m in range(1,i+1):
        print(m,end='')
    print()
#倒三角形
# for i in range(0,10):
#     for x in range(1,i+1):
#         print(' ',end='')
#         #print('',end='')
#     for m in range(i+1,10):
#         print(m,end='')
#     print()
# #倒三角形2
# for i in range(0,10):
#     for x in range(1,i+1):
#         print('',end='')
#         #print('',end='')
#     for m in range(i+1,10):
#         print(m,end='')
#     print()

for i in range(10):
    for j in range(0, 10 - i):
        print(end=" ")
    for k in range(10 - i, 10):
        print("$", end=" ")


    print("")