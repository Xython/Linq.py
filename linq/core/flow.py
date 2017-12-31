from collections import defaultdict
from functools import partial, update_wrapper

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


def linq_wrap_call(func):
    def call(self, *args, **kwargs):
        return Flow(func(self.stream, *args, **kwargs))

    update_wrapper(call, func)
    return call


class Flow:
    __slots__ = ['stream']

    def __init__(self, sequence):
        self.stream = sequence

    def __getattr__(self, k):
        for cls in self.stream.__class__.__mro__:
            namespace = Extension['{}.{}'.format(cls.__module__, cls.__name__)]
            if k in namespace:
                return partial(namespace[k], self)
        raise NameError(
            "No extension method named `{}` for {}.".format(
                k, '{}.{}'.format(object.__module__, object.__name__)))

    def __str__(self):
        return self.stream.__str__()

    def __repr__(self):
        return self.__str__()

    def Unboxed(self):
        return self.stream


def extension_std(func):
    Extension['{}.{}'.format(object.__module__, object.__name__)][func.__name__] = linq_wrap_call(func)
    return func


def extension_class(cls):
    name = '{}.{}'.format(cls.__module__, cls.__name__)
    if name not in Extension:
        Extension[name] = dict()

    def wrap(func):
        Extension[name][func.__name__] = linq_wrap_call(func)
        return func

    return wrap


def extension_class_name(cls_name, of_module='builtins'):
    name = '{}.{}'.format(of_module, cls_name)
    if name not in Extension:
        Extension[name] = dict()

    def wrap(func):
        Extension[name][func.__name__] = linq_wrap_call(func)
        return func

    return wrap


def unbox_if_flow(self):
    return self.stream if isinstance(self, Flow) else self
