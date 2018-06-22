from ..core.flow import *
from ..core.utils import is_to_destruct, destruct_func

src = ''


@extension_class(dict, box=False)
def First(self: dict):
    return next(iter(self.items()), None)


@extension_class(dict, box=False)
def each(self: dict, f=None):
    if is_to_destruct(f):
        for k, v in self.items():
            f(k, v)
    else:
        for each in self.items():
            f(each)
