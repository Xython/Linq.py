from collections import defaultdict
from functools import partial, update_wrapper

try:
    from typing import Generic, TypeVar
except:
    class GenericMeta(type):
        def __getitem__(self, item):
            return object


    class Generic(metaclass=GenericMeta):
        pass


    class TypeVar:
        def __new__(cls, *args, **kwargs):
            return args

T = TypeVar('T')

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
        return Flow(func(self._, *args, **kwargs))

    update_wrapper(call, func)
    return call


class TSource:
    __slots__ = ['_']

    def __init__(self, sequence):
        self._ = sequence

    def __getattr__(self, k):
        for cls in self._.__class__.__mro__:
            namespace = Extension.get(cls, '')
            if k in namespace:
                return partial(namespace[k], self)

        where = ','.join('{}.{}'.format(cls.__module__, cls.__name__) for cls in self._.__class__.__mro__)

        raise NameError("No extension method named `{}` for types `{}`.".format(k, where))

    def __str__(self):
        return self._.__str__()

    def __repr__(self):
        return self._.__repr__()

    def Unboxed(self):
        return self._


class Flow(Generic[T]):
    def __new__(cls, seq):
        return TSource(seq)


def extension_std(func):
    ext = Extension[object]
    name = func.__name__
    ext[name] = ext[_camel_to_underline(name)] = linq_wrap_call(func)
    return func


def extension_class(cls):
    if cls not in Extension:
        Extension[cls] = dict()

    ext = Extension[cls]

    def wrap(func):
        name = func.__name__
        ext[name] = ext[_camel_to_underline(name)] = linq_wrap_call(func)
        return func

    return wrap


def unbox_if_flow(self):
    return self._ if isinstance(self, TSource) else self


def _camel_to_underline(s: str):
    where = [i for i, e in enumerate(s) if e.isupper()]
    where.append(len(s))
    name = []
    active = False

    for start, end in zip(where[:-1], where[1:]):
        if active:
            name.append('_')
            active = False

        if end == start + 1:
            name.append(s[start].lower())
            active = False
        else:
            name.append(s[start: end].lower())
            active = True
    return ''.join(name)
