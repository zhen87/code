# -*- coding: utf-8 -*-
# @Author  : lzqian
# @Time    : 2020/6/29 


'''
1美元=7.077人民币 MR
1人民币 ≈ 0.1413美元 RM
1人民币=0.1145英镑 RY
1英镑 ≈ 8.7302人民币 YR
1美元=0.8106英镑 MY
1英镑 ≈ 1.2336美元 YM
'''
class father(object):
    def __init__(self,BZ):
        self.HL = 1
        mydict = {'MR': 7.077, 'RM': 0.1413, 'RY': 0.1145, 'YR': 8.7302, 'MY': 0.8106, 'YM': 1.2336}
        if BZ in mydict:
            self.HL = mydict.get(BZ)
           # print(self.HL)

# def HL(self):
#     self.HL == 0.1413
class son1(father):#人民币转换为其他货币
    def __init__(self,HL):
        father.__init__(self,HL)
    def RM_price(self,number):
        print('人民币与美元汇率为%s，%s人民币=%s美元'% (self.HL,number,self.HL*number))
    def MR_price(self,number):
        print('美元与人民币汇率为%s，%s美元=%s人民币'% (self.HL,number,self.HL*number))
    def RY_price(self, number):
        print('人民币与英镑汇率为%s，%s人民币=%s英镑' % (self.HL, number, self.HL * number))
    def YR_price(self, number):
        print('英镑与人民币汇率为%s，%s英镑=%s人民币' % (self.HL, number, self.HL * number))

class son2(father):#非人民币转换为其他的货币
    def __init__(self,HL):
         father.__init__(self, HL)
    def MY_price(self,number):
        print('美元与英镑汇率为%s，%s美元=%s英镑'% (self.HL,number,self.HL*number))
    def YM_price(self, number):
        print('英镑与美元汇率为%s，%s英镑=%s美元' % (self.HL, number, self.HL * number))

class range(object):
    def __init__(self,First,Finial,number):
        self.First = First
        self.Finial = Finial
        First_price = 1
        Finial_price = 1
        #print(First)
        mydict1 = {1: 7.077, 2: 7.378, 3: 7.110, 4: 7.027, 5: 7.002, 6: 7.005, 7: 7.180}
        #修改汇率
        # mydict1[2]=4
        # print(mydict1)
        if First in mydict1:
            First_price = mydict1.get(First)
            #print(self.First)
            #print(First_price)
        else:
            print('error1')
        if Finial in mydict1:
            Finial_price = mydict1.get(Finial)
            #print(self.Finial)
            #print(Finial_price)
        else:
            print('error2')
        sum=Finial_price-First_price
        print('人民币与美元收益计算：第%s天的汇率是%s，第%s天的汇率是%s，投资金额为%s元，收益结果为%s￥'%
              (self.First,First_price,self.Finial,Finial_price,number,round(sum*number,2)))
def RMB(num):
        #num=str(input('请输入人民币金额'))
        num=str(num)
        i=0
        result = '.00'
        for result_part in num[:: -1]:
            i = i+1
            if i % 3 == 0 and i != len(num):
                result_part = ','+result_part
                result = result_part+result
            else:
                result = result_part+result
        print('￥'+result)

if __name__ == '__main__':
    #1、输入任意字符，可以自动转换为人民币金额转换
    RMB(1000000)
    #2、人民币转换其他货币
    a = son1('MR')
    a.MR_price(10000)
    b = son1('RY')
    b.RM_price(10000)
    #3、设置汇率
    mydict1 = {1: 7.077, 2: 7.378, 3: 7.110, 4: 7.027, 5: 7.002, 6: 7.005, 7: 7.180}
    mydict1[2]=4
    #print(mydict1)
    # 4、非人民币转换货币
    c = son2('YM')
    c.YM_price(10000)
    #5、选择一周内的外汇收益
    d = range(1, 4, 10)

