import  math
from  functools import  reduce
def fn(x,y):
         return x*10+y
a = reduce(fn,[1,2,3,4,5])
def char2nums(s):
    return {'0':0,'1':1,'2':2,'3':3,'4':4,}[s]
b=reduce(fn,map(char2nums,'1234'))
def normalize(name):
    return  name.title()
L1 = ['adam', 'LISA', 'barT']
L2 = list(map(normalize, L1))
print(L2)
def prod(L):
   return reduce(lambda x,y:x*y,L)
print('3 * 5 * 7 * 9 =', prod([3, 5, 7, 9]))
def str2float(s):
    def strsum(c):
        return {'0':0,'1':1,'2':2,'3':3,'4':4,'5':5,'6':6,'7':7,'8':8,'9':9,}[c]
    a,b =s.split('.')
    s = a + b
    return reduce(lambda x, y: x * 10 + y, map(strsum, s)) * math.pow(10, -len(b))
print('\nstr2float(\'123.456\') =', str2float('123.456'))
def as_odd(s):
    return s %2 == 0
print(list(filter(as_odd,[1,3,2,4,5,6,7])))
def not_empty(s):
    return s and s.strip()
print(list(filter(not_empty,['A','','D'])))
a= sorted([4,2,4,12,67,42,12,32,11])
print(a)

def add_iter():
    n = 1
    while True:
        n = n + 1
        yield n

def is_palindrome(n):
    return str(n)==str(n)[::-1]
output = filter(is_palindrome, range(1, 1000))
print(list(output))

L= [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
def by_name(t):
    for s in t :
        if isinstance(s,str) :
         return s.lower()
print(L2)
def by_score(t):
    for n in t :
        if isinstance(n,int) :
         return n
L2 = sorted(L, key=by_name)
L3 = sorted(L, key=by_score, reverse=True)
print(L3)

L= [('Bob', 75), ('Adam', 92), ('Bart', 66), ('Lisa', 88)]
print(sorted(L, key=lambda x:x[0],reverse = True))
print(sorted(L, key=lambda x:x[1], reverse = True))

print(list(map(lambda x:x*x,[1,2,3,4,5,6,7])))