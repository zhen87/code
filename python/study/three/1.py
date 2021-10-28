str_list = ['a', 'a', 'b', 'a', 'b', 'c']

setA=set(str_list)
print(setA)
dictB={}
for i in setA:
    dictB[i]=str_list.count(i)
print(dictB)

str_list = ['a', 'a', 'b', 'a', 'b', 'c']
setA=set(str_list)
print(setA)
dictB={}
for i in setA:
        dictB=str_list.count(i)
