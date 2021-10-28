class Error(ValueError):
    pass
def foo(s):
    n = int(s)
    if n == 0:
        raise Error('invalid value: %s' % s )
    return 10/n
foo(0)

