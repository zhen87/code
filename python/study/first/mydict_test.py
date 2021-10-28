import  unittest
from Demo.mydict import Dict
class TestDict(unittest.TestCase):
    def test__init__(self):
        d = Dict(a=1,b='test')
        self.assertEqual(d.a,1)
        self.assertEqual(d.b,'test')
        self.assertTrue(isinstance(d,dict))
    def test_key_(self):
        d=Dict()
        d['key']='value'
        self.assertEqual(d.key,'value')
    def test_attr_(self):
        d=Dict()
        d.key='value'
        self.assertTrue('key'in d)
        self.assertEqual(d['key'] ,'value')
    def test_keyerror(self):
        d = Dict()
        with self.assertRaises(KeyError):
            value = d['empty']

    def test_atterror(self):
        d = Dict()
        with self.assertRaises(AttributeError):
            value = d.empty
if __name__ == '__main__':
    unittest()

