import re
import urllib.request
path = "http://quote.stockstar.com/stock/sha.shtml"
data = urllib.request.urlopen(path).read().decode("gbk")

preg = re.compile("<tbody>.*</tbody>",re.DOTALL) #贪婪模式  匹配所有的tbody
# preg = re.compile("<tbody>[\s\S]*</tbody>")
tbody = preg.findall(data)
newPreg = re.compile(">(.*?)<")#将每个标签包含的内容取出来
newdata = newPreg.findall(tbody[0]) #将列表里面的内容取出来
# print(newdata)
newdatalist = newdata.copy() #将我当前的数据 进行拷贝一份
for i in newdata: #去除空的字符串
    if i =='':
        newdatalist.remove(i)
# print(newdatalist)
myindex = 0#查找第一个股票代码的索引位置
for i in range(len(newdatalist)):
    if newdatalist[i]=='601949':
        myindex=i
        break
for i in range(myindex,len(newdatalist),12):#从当前的第一个股票代码开始取 步长为12 因为12为 每一行的数据  特就是说 外侧的循环 走一次为一行
    for j in range(12):#将每一行的数据进行遍历
        print(newdatalist[i+j],end=' ')
    print('')
