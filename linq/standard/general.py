from ..core.collections import ScanGenerator
from ..core.flow import *
from ..core.utils import *
from ._helper import _chunk, _group_by
from functools import reduce
from collections import Iterable

src = ''


@extension_std
def Sum(self: Iterable, f=None):
    if f is None:
        return sum(self)
    else:
        if is_to_destruct(f):
            f = destruct_func(f)
        return sum(map(f, self))


@extension_std
def Enum(self: Iterable):
    return enumerate(self)


@extension_std
def Map(self: Iterable, f):
    if is_to_destruct(f):
        f = destruct_func(f)
    return map(f, self)


@extension_std
def Then(self: object, f):
    if is_to_destruct(f):
        f = destruct_func(f)
    return f(self)


@extension_std
def Scan(self: Iterable, f, start_elem):
    return ScanGenerator(f, self, start_elem)


@extension_std
def Reduce(self: Iterable, f, start_elem=None):
    return reduce(f, self) if start_elem is None else reduce(f, self, start_elem)


@extension_std
def Filter(self: Iterable, f=None):
    if f is None:
        return (e for e in self if e)
    if is_to_destruct(f):
        f = destruct_func(f)
    return (e for e in self if f(e))


@extension_std
def Each(self: Iterable, f):
    if is_to_destruct(f):
        f = destruct_func(f)
    for e in self:
        f(e)


@extension_std
def Aggregate(self: Iterable, *functions):
    functions = map(unbox_if_flow, functions)
    return tuple(fn(self) for fn in map(lambda f: destruct_func(f) if is_to_destruct(f) else f, functions))


@extension_std
def Zip(self: Iterable, *others):
    return zip(self, *(unbox_if_flow(other) for other in others))


@extension_std
def Sorted(self: Iterable, by=None):
    if by is None:
        return sorted(self)
    if is_to_destruct(by):
        by = destruct_func(by)
    return sorted(self, key=by)


@extension_std
def ChunkBy(self, f=None):
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
        return _chunk(self)
    if is_to_destruct(f):
        f = destruct_func(f)
    return _chunk(self, f)


@extension_std
def Group(self, f=None):
    return (v for k, v in ChunkBy(self, f))


@extension_std
def GroupBy(self: Iterable, f=None):
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
    return _group_by(self, f)


@extension_std
def Take(self: Iterable, n):
    """
    [
        {
            'self': [1, 2, 3],
            'n': 2,
            'assert': lambda ret: list(ret)  == [1, 2]
         }
    ]
    """

    for i, e in enumerate(self):
        if i == n:
            break
        yield e


@extension_std
def TakeIf(self: Iterable, f):
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

    return (e for e in self if f(e))


@extension_std
def TakeWhile(self: Iterable, f):
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

    for e in self:
        if not f(e):
            break
        yield e


@extension_std
def First(self):
    return next(self, None)


@extension_std
def Drop(self: Iterable, n):
    """
    [
        {
            'self': [1, 2, 3, 4, 5],
            'n': 3,
            'assert': lambda ret: list(ret) == [1, 2]
         }
    ]
    """
    con = tuple(self)
    n = len(con) - n
    if n <= 0:
        yield from con
    else:
        for i, e in enumerate(con):
            if i == n:
                break
            yield e


@extension_std
def Skip(self: Iterable, n):
    """
        [
            {
                'self': [1, 2, 3, 4, 5],
                'n': 3,
                'assert': lambda ret: list(ret) == [4, 5]
             }
        ]
        """
    con = iter(self)
    for i, _ in enumerate(con):
        if i == n:
            break
    return con


@extension_std
def Shift(self, n):
    """
    [
        {
            'self': [1, 2, 3, 4, 5],
            'n': 3,
            'assert': lambda ret: list(ret) == [4, 5, 1, 2, 3]
         }
    ]
    """
    headn = tuple(Take(self, n))
    yield from self
    yield from headn


@extension_std
def Concat(self: Iterable, *others):
    """
    [
        {
            'self': [1, 2, 3],
            ':args': [[4, 5, 6], [7, 8, 9]],
            'assert': lambda ret: list(ret) == [1, 2, 3, 4, 5, 6, 7, 8, 9]
         }
    ]
    """
    return concat_generator(self, *[unbox_if_flow(other) for other in others])


@extension_std
def ToList(self: Iterable):
    return list(self)


@extension_std
def ToTuple(self: Iterable):
    return tuple(self)


@extension_std
def ToDict(self: Iterable):
    return dict(self)


@extension_std
def ToSet(self: Iterable):
    return set(self)


@extension_std
def All(self: Iterable, f=None):
    if f is None:
        return all(self)
    if is_to_destruct(f):
        f = destruct_func(f)
    return all(map(f, self))


@extension_std
def Any(self: Iterable, f=None):
    if f is None:
        return any(self)
    if is_to_destruct(f):
        f = destruct_func(f)
    return any(map(f, self))


@extension_std
def Intersects(self: Iterable, *others):
    return set.intersection(set(self), *[unbox_if_flow(other) for other in others])


@extension_std
def Union(self: set, *others):
    return set.union(set(self), *[unbox_if_flow(other) for other in others])
