from .flow import Flow, extension_class, extension_std

@extension_std
def Sum(self: Flow, f=None):
    if f is None:
        return sum(self.stream)
    else:
        return sum(map(f, self.stream))


@extension_class(list)
def Extend(self: Flow, other):
    if self.stream is None:
        self.stream = other
    else:
        self.stream.extend(other)
    return self
