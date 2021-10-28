import struct

def test1(test):
    try:
        with open(test,'rb') as f:
            file = f.read(30)
            s=struct.unpack('<ccIIIIIIHH',file)
            assert s[0]==b'B' and s[1]==b'M'
            print('此文件是位图文件，','图片大小为：%是，颜色数为：%s'%(s[2],s[-1]))
    except Exception as e:
        print('文件有问题')
if __name__ == '__main__':
     test1(r'F:\python\test.bmp')
