# -*- coding: utf-8 -*-
#字典类型
#成键值对出现，需手动指定

mydict = {"mangod": 1,"womengod":2,"womengod":3}
print(mydict["womengod"])
mydict["womengod"] = '1234'
print(mydict)
mydict['animal'] = 23
print(mydict)

del mydict['mangod']
print(mydict)
del mydict
print(mydict)