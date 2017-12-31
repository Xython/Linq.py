from ..core.flow import *
from ..core.utils import *

src = ''


@extension_class(list)
def Extended(self: list, *others):
    stream = []
    stream.extend(self)
    for other in map(unbox_if_flow, others):
        stream.extend(other)
    return stream


@extension_class(list)
def Extend(self: list, *others):
    for other in map(unbox_if_flow, others):
        self.extend(other)
    return self


@extension_class(list)
def Sort(self: list, by=None):
    if by and is_to_destruct(by):
        by = destruct_func(by)
    self.sort(key=by)
    return self


@extension_class(list)
def Reverse(self: list):
    self.reverse()
    return self


@extension_class(list)
def Reversed(self: list):
    return self[::-1]
