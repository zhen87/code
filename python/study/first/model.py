import functools, datetime
def log(text = 'call'):
    def decorator (func):
        @functools.wraps(func)
        def wrapper(*arg, **kw):
            print('%s: %s ' %(text, func.__name__))
            func(*arg, **kw)
            print('end %s' %func.__name__)
            return
        return wrapper
    return decorator
@log('excute')
def now():
    print(datetime.datetime.now())

class Student(object):
    #设置私有属性
    def __init__(self,name,score):
        self.__name=name
        self.__score=score
    #打印学生信息
    def print_info(self):
        return self.__name+':'+str(self.__score)
    #读取学生姓名
    def get_name(self):
        return self.__name
    #读取学生成绩
    def get_score(self):
        print(self.__score)
    #设置学生成绩
    def set_score(self,score):
        self.__score=score


#创建一个对象实例
tom=Student('TomCat',96)
#输出对象信息
print(tom.print_info())
#获取对象姓名
print(tom.get_name())
#获取对象成绩
tom#测试这样也可以访问到
print(tom._Student__name)
#绑定一个新属性
tom.age=19
print(tom.age)
#设置外部修改成绩.get_score()

tom.set_score(100)
#显示
tom.get_score()
