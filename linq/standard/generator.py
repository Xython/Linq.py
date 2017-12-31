from ..core.flow import *
from collections import Generator

src = ''


@extension_class_name('generator')
def Next(self: Generator):
    return next(self)
