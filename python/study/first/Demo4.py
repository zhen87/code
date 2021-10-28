import math
def quadratic(a, b, c):
    na = b**2 - 4 * a * c
    if (na >= 0):
       nb = math.sqrt(na)
       x1 = (-b + nb) / (2 * a)
       x2 = (-b - nb) / (2 * a)
       return x1,x2
    else:
        print('此方程无解')
print(quadratic(2,3,1))
print(quadratic(1,3,-4))
print(quadratic(1,1,1))



