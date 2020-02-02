# -*- coding: utf-8 -*-

#########################Unit test##################################

import unittest

from myModule import MyDict

class TestDict(unittest.TestCase):
    
    def test_init(self):
        d = MyDict.MyDict(a = 1, b = "Test")
        self.assertEqual(d.a, 1)
        self.assertEqual(d.b, "Test")
        self.assertTrue(isinstance(d, dict))
        
    def test_key(self):
        d = MyDict.MyDict()
        d['key'] = 'value'
        self.assertEqual(d.key, "value")
    
    def test_attr(self):
        d = MyDict.MyDict()
        d.key = "value"
        self.assertTrue("key" in d)
        self.assertEqual(d["key"], "value")
        
    def test_keyError(self):
        d = MyDict.MyDict()
        with self.assertRaises(KeyError):
            value = d['empty']
    
    def test_attrerror(self):
        d = MyDict.MyDict()
        with self.assertRaises(AttributeError):
            value = d.empty

if __name__ == "__main__":
    unittest.main()
    
        