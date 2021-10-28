import urllib.request
import re

#封装一个获取数据的方法
def getData(path):
    request = urllib.request.Request(url=path,headers={"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/60.0.3112.101 Safari/537.36"})
    data = urllib.request.urlopen(request).read().decode("GBK")
    return data

def getTbody(data):
    preg = re.compile("<tbody class=\"tbody_right\" id=\"datalist\">[\s\S]*</tbody>")
    newData = preg.findall(data)
    newPreg = re.compile(">(.*?)<")
    return newPreg.findall(newData[0])

def showData(data):
    dataList = data.copy()
    for i in data:
        if i=='':
            dataList.remove(i)

    for i in range(0,len(dataList),10):
        for j in range(10):
            print(dataList[i+j],end=' ')
        print('')


data = getData("http://quote.stockstar.com/fund/stock.shtml")
newData = getTbody(data)
showData(newData)