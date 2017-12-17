# Linq(Language Integrated Query)
Like C# in some degree, but not the same.
```python
from linq.core.collections import Generator as MGenerator
from linq.core.flow import Flow
import linq.standard  # see the standard library to get all the extension methods.

seq = Flow(MGenerator(lambda x: x + 1, 0))  # [0..\infty]

"""
First Example:
"""

print(seq.Take(10).Enum().Map(lambda a, b: a * b).Sum().Unboxed())
#   Support infinite sequences, parameters destruct and so on.
#   Limited by Python's syntax grammar, parameters destruct 
# cannot be as powerful as pattern matching.

# => 285
print('\n================\n')

print(sum([a * b for a, b in enumerate(range(10))]))
# => 285



"""
Second Example:
"""

print('\n================\n')
seq1 = seq.Take(100)
seq2 = seq.Take(200).Drop(100)
s = seq1.Zip(seq2) \
    .Map(lambda a, b: a / b) \
    .GroupBy(lambda x: x // 0.2) \
    .Then(lambda x: x.items()) \
    .Each(print)

print('\n================\n')

seq1 = range(100)
seq2 = range(100, 200)
zipped = zip(seq1, seq2)
mapped = map(lambda ab: ab[0] / ab[1], zipped)
grouped = dict();
group_fn = lambda x: x // 0.2
for e in mapped:
    group_id = group_fn(e)
    if group_id not in grouped:
        grouped[group_id] = [e]
        continue
    grouped[group_id].append(e)
for e in grouped.items():
    print(e)

"""
Last Example:
"""

from linq.core.flow import extension_class, Flow


@extension_class(dict)
def ToTupleGenerator(self: Flow):
    return Flow((k, v) for k, v in self.stream.items()).ToList().Unboxed()


try:
    seq.Take(10).ToTupleGenerator()
except Exception as e:
    print(e.args)
"""
 NameError: No extension method named `ToTupleGenerator` for builtins.object.
"""
print(seq.Take(10).Zip(seq.Take(10)).ToDict().ToTupleGenerator())

```

```python
%timeit sum(set_.stream)
2.7 ms ± 127 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)
 
%timeit set_.Sum()
2.67 ms ± 137 µs per loop (mean ± std. dev. of 7 runs, 100 loops each)

%timeit sum(set_.stream)
2.5 ms ± 67.3 µs per loop (mean ± std. dev. of 7 runs, 100 loops each) 

%timeit set_.Sum()
2.55 ms ± 49.1 µs per loop (mean ± std. dev. of 7 runs, 100 loops each) 
```

```python

from core.flow import Flow, extension_std, extension_class

@extension_std  # extension method for the standard(class object) 
def Sum(self: Flow, f=None):
    if f is None:
        return sum(self.stream)
    else:
        return sum(map(f, self.stream))

@extension_class(list)  # extension method for class list 
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

seq.Extend([4, 5, 6, 7]).Sum(lambda x: x*2)
```

---------
To Be Continue.
