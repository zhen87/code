
import struct,os

def check_bmp():
    path = input('请输入文件路径：')
    with open(path,'rb') as f:
        file=f.read(30)
        s=struct.unpack('<ccIIIIIIHH',file)
        if s[0]==b'B' and s[1]==b'M':
            print('此文件是位图文件,')
            print('图片大小为:%s,颜色数为:%s'%(s[2],s[-1]))
        else:
            print('文件有问题')
if __name__ == '__main__':
     # test1(r'F:/python/test.bmp')
    check_bmp()
