from math import sqrt
from math import tan

'''
高阶函数应用，返回一个数字不同方法计算结果
'''
def same(num, *kw):
    # 参数检查
    if not isinstance(num, (int, float)):
        raise TypeError('bad operand type')

    # 初始化结果字典
    rel = {}
    # 循环计算可变参数
    for func in kw:
        try:
            rel[str(func)[str(func).find('function ') + 9: -1]] = func(num)
        except ValueError:
            rel[str(func)[str(func).find('function ') + 9: -1]] = 'None'
    # 返回结果字典
    return rel

# 函数调用result = same(-10.5, sqrt, abs, tan)    print(result)

def f(x):
    return  x + x
r = map( f,[1,2,3,4,5,6,7,8])
print(list(r))