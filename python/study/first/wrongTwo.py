def fact(n):
    def __init__(self,**kw):
        super(self,fact).__init__(self,**kw)

    def __getattr__(self,key):
        try:
            return self[key]
        except KeyError:
            raise  AttributeError("'xx'has not attribute '%s'" % key)

    def __setattr__(self,key,value):
        self[key]=value
    if n < 1:
         raise ValueError()
    if n == 1:
         return 1
         return n * fact(n - 1)

    if __name__ == '__main__':
     import doctest
     doctest.testmod()
     fact(4)
