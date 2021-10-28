str1 = 'x'
def a():
    global str1#将str1变量申明为全局变量，内外使用同一个，否则在函数内可获取函数外的变量，
                       #但修改后生成一个新的局部变量，和函数外不是同一个变量
    print(str1)
    str1 = 2
print(str1)
a()
print(str1)
