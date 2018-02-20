from ..core.collections import ScanGenerator
from ..core.flow import *
from ..core.utils import *
from functools import reduce
from collections import Iterable

from sys import version_info

try:
    from cytoolz import compose
except (ModuleNotFoundError if version_info.minor >= 6 else ImportError):
    def compose(*fns):
        def call(e):
            return reduce(lambda x, y: y(x), fns[::-1], e)

        return call

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
def Aggregate(self: Iterable, *functions) -> {'functions': 'Seq<Callable> | Seq<Iterable<Callable>>'}:
    functions = map(unbox_if_flow, functions)
    return (fn(self) for fn in
            map(lambda f: destruct_func(f) if is_to_destruct(f) else f,
                functions))


@extension_std
def Zip(self: Iterable, *others) -> {'others': 'Seq<Seq> | Seq<Iterable<Seq>>'}:
    return zip(self, *[unbox_if_flow(other) for other in others])


@extension_std
def Sorted(self: Iterable, by=None):
    if by is None:
        return sorted(self)
    if is_to_destruct(by):
        by = destruct_func(by)
    return sorted(self, key=by)


@extension_std
def ArgSorted(self: Iterable, by=None):
    if by is None:
        return sorted(range(len(self)), key=self.__getitem__)
    if is_to_destruct(by):
        by = destruct_func(by)
    return sorted(range(len(self)), key=compose(by, self.__getitem__))


@extension_std
def Group(self, f=None):
    """The name of this function might be not proper."""
    if f is None:
        return _group(self)
    if is_to_destruct(f):
        f = destruct_func(f)
    return _group(self, f)


@extension_std
def GroupBy(self: Iterable, f=None):
    if f and is_to_destruct(f):
        f = destruct_func(f)
    return _group_by(self, f)


@extension_std
def Take(self: Iterable, n):
    return (e for _, e in zip(range(n), self))


@extension_std
def TakeIf(self: Iterable, f):
    if is_to_destruct(f):
        f = destruct_func(f)

    return (e for e in self if f(e))


@extension_std
def TakeWhile(self: Iterable, f):
    if is_to_destruct(f):
        f = destruct_func(f)

    def take():
        for e in self:
            if not f(e):
                break
            yield e

    return take()


@extension_std
def Drop(self: Iterable, n):
    def drop():
        con = (e for e in self)
        for _ in range(n):
            con.__next__()
        return con

    return drop()


@extension_std
def Skip(self: Iterable, n):
    return Drop(self, n)


@extension_std
def Concat(self: Iterable, *others) -> {'others': 'Seq<Seq> | Seq<Iterable<Seq>>'}:
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


def _group_by(stream, f=None):
    res = defaultdict(list)
    if f is None:
        for each in stream:
            res[each].append(each)
        return res

    if is_to_destruct(f):
        f = destruct_func(f)

    for each in stream:
        res[f(each)].append(each)

    return res


def _group(stream, f=None):
    if f is None:
        grouped = None
        last = None
        for e in stream:
            if grouped is None:
                grouped = [e]
            elif last == e:
                grouped.append(e)
            else:
                yield grouped
                grouped = [e]
            last = e
        else:
            yield grouped
    else:
        grouped = None
        last = None
        for _e in stream:
            e = f(_e)
            if grouped is None:
                grouped = [_e]
            elif last == e:
                grouped.append(_e)
            else:
                yield grouped
                grouped = [_e]
            last = e
        else:
            yield grouped
