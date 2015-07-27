# -*- coding: utf-8 -*-

# -*- coding: utf-8 -*-

import json
class MyObj(object):

    def __init__(self,s):
        self.s = s

    def __repr__(self):
        return "<MyObj(%s)>" % self.s

class MyEncoder(json.JSONEncoder):

    def default(self, obj):
        print 'default(', repr(obj), ')'
        # Convert objects to a dictionary of their representation
        d = { '__class__':obj.__class__.__name__, 
              '__module__':obj.__module__,
              }
        d.update(obj.__dict__)
        return d

obj = MyObj('helloworld')
print MyEncoder().encode(obj)

# data = [{'a':"A",'b':(2,4),'c':3.0}]  #list对象
# print "DATA:",repr(data)

# data_string = json.dumps(data)
# print "JSON:",data_string