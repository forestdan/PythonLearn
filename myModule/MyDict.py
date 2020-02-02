# -*- coding: utf-8 -*-

class MyDict(dict):
    
    def __init__(self, **kw):
        super().__init__(**kw)
    
    def __getattribute__(self, key):
        try:
            return self[key]
        except KeyError as e:
            raise AttributeError("'Dict' object has no attribute '%s'" % key)
        
    def __setattr__(self, key, value):
        self[key] = value
