from ..core.flow import *
from ..core.utils import *

src = globals()
__all__ = [src]


@extension_class(list)
def Extended(self: Flow, *others):
    stream = []
    stream.extend(self.stream)
    for other in map(unbox_if_flow, others):
        stream.extend(other)
    return Flow(stream)


@extension_class(list)
def Extend(self: Flow, *others):
    for other in map(unbox_if_flow, others):
        self.stream.extend(other)
    return self


@extension_class(list)
def Sort(self: Flow, by):
    if is_to_destruct(by):
        by = destruct_func(by)
    self.stream.sort(key=by)
    return self


@extension_class(list)
def Reverse(self: Flow):
    self.stream.reverse()
    return self


@extension_class(list)
def Reversed(self: Flow):
    return Flow(self.stream[::-1])
