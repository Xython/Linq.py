from ..core.flow import *
from ..core.utils import is_to_destruct, destruct_func, concat_generator
from ..core.collections import ScanGenerator
from ._helper import _group_by, _chunk
from functools import reduce
from itertools import islice

src = ''

_ext_dict = extension_class(dict)


@_ext_dict
def first(self: dict):
    return next(iter(self.items()), None)


@_ext_dict
def each(self: dict, f=None):
    if is_to_destruct(f):
        for k, v in self.items():
            f(k, v)
    else:
        for each in self.items():
            f(each)


@_ext_dict
def enum(self: dict):
    return enumerate(self.items())


@_ext_dict
def Map(self: dict, f):
    if is_to_destruct(f):
        f = destruct_func(f)
    return map(f, self.items())


@_ext_dict
def scan(self: dict, f, start_elem):
    return ScanGenerator(f, self.items(), start_elem)


@_ext_dict
def Reduce(self: dict, f, start_elem):
    return reduce(f, self.items()) if start_elem is None else reduce(f, self.items(), start_elem)


@_ext_dict
def Filter(self: dict, f=None):
    if f is None:
        return (e for e in self.items() if e)
    if is_to_destruct(f):
        f = destruct_func(f)
    return (e for e in self.items() if f(e))


@_ext_dict
def Zip(self: dict, *others):
    return zip(self.items(), *(unbox_if_flow(other) for other in others))


@_ext_dict
def Sorted(self: dict, by=None):
    if by is None:
        return sorted(self.items())
    if is_to_destruct(by):
        by = destruct_func(by)
    return sorted(self.items(), key=by)


@_ext_dict
def ChunkBy(self: dict, f=None):
    """
    [
        {
            'self': [1, 1, 3, 3, 1, 1],
            'f': lambda x: x%2,
            'assert': lambda ret: ret == [[1, 1], [3, 3], [1, 1]]
         }
    ]
    """
    if f is None:
        return _chunk(self.items())
    if is_to_destruct(f):
        f = destruct_func(f)
    return _chunk(self.items(), f)


@_ext_dict
def GroupBy(self: dict, f=None):
    """
    [
        {
            'self': [1, 2, 3],
            'f': lambda x: x%2,
            'assert': lambda ret: ret[0] == [2] and ret[1] == [1, 3]
         }
    ]
    """
    if f and is_to_destruct(f):
        f = destruct_func(f)
    return _group_by(self.items(), f)


@_ext_dict
def Take(self: dict, n):
    """
    [
        {
            'self': [1, 2, 3],
            'n': 2,
            'assert': lambda ret: list(ret)  == [1, 2]
         }
    ]
    """

    for i, e in enumerate(self.items()):
        if i == n:
            break
        yield e


@_ext_dict
def TakeIf(self: dict, f):
    """
    [
        {
            'self': [1, 2, 3],
            'f': lambda e: e%2,
            'assert': lambda ret: list(ret)  == [1, 3]
         }
    ]
    """
    if is_to_destruct(f):
        f = destruct_func(f)

    return (e for e in self.items() if f(e))


@_ext_dict
def TakeWhile(self: dict, f):
    """
    [
        {
            'self': [1, 2, 3, 4, 5],
            'f': lambda x: x < 4,
            'assert': lambda ret: list(ret)  == [1, 2, 3]
         }
    ]
    """
    if is_to_destruct(f):
        f = destruct_func(f)

    for e in self.items():
        if not f(e):
            break
        yield e


@_ext_dict
def Drop(self: dict, n):
    """
    [
        {
            'self': [1, 2, 3, 4, 5],
            'n': 3,
            'assert': lambda ret: list(ret) == [1, 2]
         }
    ]
    """
    n = len(self) - n
    if n <= 0:
        yield from self.items()
    else:
        for i, e in enumerate(self.items()):
            if i == n:
                break
            yield e


@_ext_dict
def Skip(self: dict, n):
    """
        [
            {
                'self': [1, 2, 3, 4, 5],
                'n': 3,
                'assert': lambda ret: list(ret) == [4, 5]
             }
        ]
        """

    con = self.items()
    for i, _ in enumerate(con):
        if i == n:
            break
    return con


@_ext_dict
def Shift(self: dict, n):
    con = iter(self.items())
    headn = tuple(islice(con, n))
    yield from con
    yield from headn


@_ext_dict
def Concat(self: dict, *others):
    return concat_generator(self.items(), *[unbox_if_flow(other) for other in others])


@_ext_dict
def ToList(self: dict):
    return list(self.items())


@_ext_dict
def ToTuple(self: dict):
    return tuple(self.items())


@_ext_dict
def ToDict(self: dict):
    return self.copy()


@_ext_dict
def ToSet(self: dict):
    return set(self.items())


@_ext_dict
def All(self: dict, f=None):
    if f is None:
        return all(self)
    if is_to_destruct(f):
        f = destruct_func(f)
    return all(map(f, self.items()))


@_ext_dict
def Any(self: dict, f=None):
    if f is None:
        return any(self)
    if is_to_destruct(f):
        f = destruct_func(f)
    return any(map(f, self.items()))


@_ext_dict
def Intersects(self: dict, *others):
    return set.intersection(set(self.items()), *[unbox_if_flow(other) for other in others])


@_ext_dict
def Union(self: dict, *others):
    return set.union(set(self.items()), *[unbox_if_flow(other) for other in others])
