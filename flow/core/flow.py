from collections import defaultdict
from functools import partial

Extension = defaultdict(dict)
"""
`Extension` is a dictionary structured as 
    {'Module.ClassName1':
        {'Method1Name': Method1, 'Method2Name':Method2},
     'Module.ClassName2':
        {'Method1Name': Method1, 'Method2Name':Method2},
    ...
     }
It is an index of extension methods 
    which tells the `Flow` object that which method can be used for specific type. 
"""


class Flow:
    __slots__ = ['stream']
    def __init__(self, sequence):
        self.stream = sequence
    
    def __getattr__(self, k):
        for cls in self.stream.__class__.__mro__:
            namespace = Extension['{}.{}'.format(cls.__module__, cls.__name__)]
            if k in namespace:
                return partial(namespace[k], self)
        raise NameError("No extension method named `{name}`.".format(name=k))
        
def extension_std(func):
    Extension['{}.{}'.format(object.__module__, object.__name__)][func.__name__] = func

def extension_class(cls):
    name = '{}.{}'.format(cls.__module__, cls.__name__)
    if name not in Extension:
        Extension[name] = dict()
    def wrap(func):
        Extension[name][func.__name__] = func
        return func
    return wrap
    
    
