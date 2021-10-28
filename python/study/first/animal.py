
from types import MethodType
class A(object):
    def __init__(self,name):
        self.name=name
    def get_name(self):
        print(self.name)
def set_name(self,name):
    self.name=name

A.set_name = MethodType(set_name,A)
a1 = A('a1')
print(a1.name) #result: a1
a1.set_name('B1')
print(a1.name)