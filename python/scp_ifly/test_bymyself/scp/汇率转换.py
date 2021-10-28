"""
1美元=7.077人民币 MR
1人民币 ≈ 0.1413美元 RM
1人民币=0.1145英镑 RY
1英镑 ≈ 8.7302人民币 YR
1美元=0.8106英镑 MY
1英镑 ≈ 1.2336美元 YM
"""
class father(object):
    def __init__(self, xx):
        self.HL = 1
        if xx == 'MR':
            self.HL = 7.077
        if xx == 'RM':
            self.HL = 0.1413
        if xx == 'RY':
            self.HL = 0.1145
        if xx == 'YR':
            self.HL = 8.7302
        if xx == 'MY':
            self.HL = 0.8106
        if  xx == 'YM':
            self.HL = 1.2336
    def HL_set(self,new):
        self.HL=new
class son1(father):#人民币转换为其他货币
    def __init__(self,HL):
        father.__init__(self,HL)
    def RM_price(self,number):
        print('人民币与美元汇率为[%s]，输入金额为[%s]，转换结果为[%s]'% (self.HL,number,self.HL*number))
    def MR_price(self,number):
        print('美元与人民币汇率为[%s]，输入金额为[%s]，转换结果为[%s]'% (self.HL,number,self.HL*number))
    def RY_price(self, number):
        print('人民币与英镑汇率为[%s]，输入金额为[%s]，转换结果为[%s]' % (self.HL, number, self.HL * number))
    def YR_price(self, number):
        print('英镑与人民币汇率为[%s]，输入金额为[%s]，转换结果为[%s]' % (self.HL, number, self.HL * number))
class son2(father):#非人民币转换为其他的货币
    def __init__(self,HL):
         father.__init__(self, HL)
    def MY_price(self,number):
        print('美元与英镑汇率为[%s]，输入金额为[%s]，转换结果为[%s]'% (self.HL,number,self.HL*number))
    def YM_price(self, number):
        print('英镑与美元汇率为[%s]，输入金额为[%s]，转换结果为[%s]' % (self.HL, number, self.HL * number))

if __name__ == '__main__':
    a = son1('MR')
    a.MR_price(10)
    b=son1('RY')
    b.RM_price(10)
    c = son2('MY')
    c.MY_price(10)















