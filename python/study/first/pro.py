class Screen(object):
    @property
    def width(self):
        return self._width
    @property
    def height(self):
        return self._height
    @width.setter
    def width(self,value1):
        if not isinstance(value1, int):
            raise ValueError('please input int')
        if value1 < 0:
            raise ValueError('value>0')
        self._width = value1
    @height.setter
    def height(self,value2):
        if not isinstance(value2,int):
            raise ValueError('please input int')
        if value2 <0:
            raise ValueError('value>0')
        self._height = value2
    @property
    def resolution(self):
        return  self.width * self.height
s = Screen()
s.width =1024
s.height = 768
print(s.resolution)
assert s.resolution == 786432, '1024 * 768 = %d ?' % s.resolution