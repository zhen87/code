class chain(object):
    def __init__(self,path='' ):
        self._path=path
    def __getattr__(self, path):
        return chain('%s%s' % (self._path,path))
    def __str__(self):
        return self._path
    __repr__=__str__
print(chain().status.user.timeline.list)