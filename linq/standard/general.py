from ..core.flow import *
from ..core.utils import *
from functools import reduce

from sys import version_info

try:
    from cytoolz import compose
except (ModuleNotFoundError if version_info.minor >= 6 else ImportError):
    def compose(*fns):
        def call(e):
            return reduce(lambda x, y: y(x), fns[::-1], e)

        return call

src = globals()
__all__ = [src]


@extension_std
def Unboxed(self: Flow):
    return self.stream


@extension_std
def Sum(self: Flow, f=None):
    if f is None:
        return Flow(sum(self.stream))
    else:
        if not is_to_destruct(f):
            f = destruct_func(f)
        return Flow(sum(map(f, self.stream)))


@extension_std
def Enum(self: Flow):
    return Flow(enumerate(self.stream))


@extension_std
def Map(self: Flow, f):
    if not is_to_destruct(f):
        f = destruct_func(f)
    return Flow(map(f, self.stream))


@extension_std
def Then(self: Flow, f):
    if not is_to_destruct(f):
        f = destruct_func(f)
    return Flow(f(self.stream))


@extension_std
def Reduce(self: Flow, f) -> {'example': 'Flow([1,2,3]).Reduce(lambda x,y :x+y)'}:
    return Flow(reduce(f, self.stream))


@extension_std
def Filter(self: Flow, f):
    if not is_to_destruct(f):
        f = destruct_func(f)
    return Flow((e for e in self.stream if f(e)))


@extension_std
def Each(self: Flow, f):
    if not is_to_destruct(f):
        f = destruct_func(f)
    for e in self.stream:
        f(e)


@extension_std
def Aggregate(self: Flow, *functions) -> {'functions': 'Seq<Callable> | Seq<Flow<Callable>>'}:
    return Flow((fn(self.stream) for fn in
                 map(lambda f: f if is_to_destruct(unbox_if_flow(f)) else destruct_func(unbox_if_flow(f)),
                     functions)))


@extension_std
def Zip(self: Flow, *others) -> {'others': 'Seq<Seq> | Seq<Flow<Seq>>'}:
    return Flow(zip(self.stream, *[unbox_if_flow(other) for other in others]))


@extension_std
def Sorted(self: Flow, by=None):
    if by is None:
        return Flow(sorted(self.stream))
    if not is_to_destruct(by):
        by = destruct_func(by)
    return Flow(sorted(self.stream, key=by))


@extension_std
def ArgSorted(self: Flow, by=None):
    if by is None:
        return Flow(sorted(range(len(self.stream)), key=self.stream.__getitem__))
    if not is_to_destruct(by):
        by = destruct_func(by)
    return Flow(sorted(range(len(self.stream)), key=compose(by, self.stream.__getitem__)))


@extension_std
def Group(self, f=None):
    """The name of this function might be not proper."""
    if f is None:
        return Flow(_group(self.stream))
    if not is_to_destruct(f):
        f = destruct_func(f)
    return Flow(_group(self.stream, f))


@extension_std
def GroupBy(self: Flow, f=None):
    if f and not is_to_destruct(f):
        f = destruct_func(f)
    return Flow(_group_by(self.stream, f))


@extension_std
def Take(self: Flow, n):
    return Flow((e for _, e in zip(range(n), self.stream)))


@extension_std
def TakeIf(self: Flow, f):
    if not is_to_destruct(f):
        f = destruct_func(f)

    return Flow((e for e in self.stream if f(e)))


@extension_std
def TakeWhile(self: Flow, f):
    if not is_to_destruct(f):
        f = destruct_func(f)

    def take():
        for e in self.stream:
            if not f(e):
                break
            yield e

    return Flow(take())


@extension_std
def Drop(self: Flow, n):
    def drop():
        con = (e for e in self.stream)
        for _ in range(n):
            con.__next__()
        return con

    return Flow(drop())


@extension_std
def Concat(self: Flow, *others) -> {'others': 'Seq<Seq> | Seq<Flow<Seq>>'}:
    return Flow(concat_generator(self.stream, *[unbox_if_flow(other) for other in others]))


@extension_std
def ToList(self: Flow):
    return Flow(list(self.stream))


@extension_std
def ToTuple(self: Flow):
    return Flow(tuple(self.stream))


@extension_std
def ToDict(self: Flow):
    return Flow(dict(self.stream))


@extension_std
def ToSet(self: Flow):
    return Flow(set(self.stream))


@extension_std
def All(self: Flow, f=None):
    if f is None:
        return Flow(all(self.stream))
    if not is_to_destruct(f):
        f = destruct_func(f)
    return Flow(all(map(f, self.stream)))


@extension_std
def Any(self: Flow, f=None):
    if f is None:
        return Flow(any(self.stream))
    if not is_to_destruct(f):
        f = destruct_func(f)
    return Flow(any(map(f, self.stream)))


def _group_by(stream, f=None):
    res = dict()
    if f is None:
        for each in stream:
            if each not in res:
                res[each] = [each]
            res[each].append(each)
        return res

    if not is_to_destruct(f):
        f = destruct_func(f)

    for each in stream:
        group_id = f(each)
        if group_id not in res:
            res[group_id] = [each]
            continue
        res[group_id].append(each)

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
