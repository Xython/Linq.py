from ..core.flow import *
from sys import version_info

if version_info.minor > 4:
    from collections import Generator
else:
    from collections import Iterator as Generator
src = ''
_gen_cls = (i for i in (1,)).__class__


@extension_class(_gen_cls, box=False)
def Next(self: Generator):
    return next(self)
