from ..core.flow import *

src = ''


@extension_class(set)
def Intersects(self: set, *others):
    return set.intersection(self, *[unbox_if_flow(other) for other in others])
    # List comprehension goes faster, so we do not use lazy map here.


@extension_class(set)
def Union(self: set, *others):
    return set.union(self, *[unbox_if_flow(other) for other in others])
