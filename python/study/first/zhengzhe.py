import re
e1 = 'someone@gmail.com'
e2 = '<Tom Paris> tom@voyager.org'
m1 = re.match(r'^([0-9a-zA-Z.?]+)\@([0-9a-z]+).([a-z]{3})$',e1)
m2 = re.match(r'^(<\w+\s\w+>)\s+(\w+)@(\w+.\w+)$',e2)
if m1!=None:
    print('Email is ok! The Email is :',m1.group(0))
else:
    print('Email is failed! Please check it again. Your input is:\n',e)
if m2!=None:
    print('Email is ok! The Email is :',m2.group(0))
else:
    print('Email is failed! Please check it again. Your input is:\n',e)
