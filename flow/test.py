# -*- coding: utf-8 -*-
"""
Created on Sat Dec 16 02:07:45 2017

@author: v-wazhao
"""

from core.flow import Flow, extension_std, extension_class

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

seq = Flow([1,2,3])
print(seq.Sum())

set_ = Flow(set(range(100000)))
print(set_.Sum())

# =============================================================================
# %timeit sum(set_.stream)
# 2.7 ms ± 127 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
# 
# %timeit set_.Sum()
# 2.67 ms ± 137 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
# 
# %timeit sum(set_.stream)
# 2.5 ms ± 67.3 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
# 
# %timeit set_.Sum()
# 2.55 ms ± 49.1 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
# 
# =============================================================================
