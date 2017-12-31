from ..core.flow import *
from sys import version_info

if version_info.minor > 4:
    from collections import Generator
else:
    from collections import Iterator as Generator

src = ''


@extension_class_name('generator')
def Next(self: Generator):
    return next(self)
