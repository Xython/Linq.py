from ..core.flow import *

src = globals()
__all__ = [src]


@extension_class_name('generator')
def Next(self: Flow):
    return Flow(next(self.stream))
