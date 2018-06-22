# Linq.py 

[![Build Status](https://travis-ci.org/Xython/Linq.py.svg?branch=typed-linq)](https://travis-ci.org/Xython/Linq.py)
[![License](https://img.shields.io/badge/license-MIT-yellow.svg)](https://github.com/Xython/Linq.py/blob/typed-linq/LICENSE)
[![codecov](https://codecov.io/gh/Xython/Linq.py/branch/typed-linq/graph/badge.svg)](https://codecov.io/gh/Xython/Linq.py)
[![Coverage Status](https://coveralls.io/repos/github/Xython/Linq.py/badge.svg?branch=typed-linq)](https://coveralls.io/github/Xython/Linq.py?branch=typed-linq)
[![PyPI version](https://img.shields.io/pypi/v/Linq.svg)](https://pypi.python.org/pypi/Linq)




## Install Typed-Linq

```
pip install -U linq-t
```

Here is an example to get top 10 frequent pixels in a picture.

```python

from linq import Flow
import numpy as np

def most_frequent(arr: np.ndarray) -> np.ndarray:
    return  Flow(arr.flatten())                        \
                    .group_by(None)                    \
                    .map(lambda k, v: (k, len(v)))     \
                    .sorted(by=lambda k, count: -count)\
                    .take(10)                          \
                    .map(lambda k, v: k)               \
                    .to_list()                         \
                    .then(np.array)
                    ._  # unbox
```


## About Linq

The well-known EDSL in .NET, `Language Integrated Query`, in my opinion, is one of the best design in .NET environment.  
Here is an example of C# Linq.  

```C#
// Calculate MSE loss.
/// <param name="Prediction"> the prediction of the neuron network</param>
/// <param name="Expected"> the expected target of the neuron network</param>

Prediction.Zip(Expected, (pred, expected)=> Math.Square(pred-expected)).Average()
```

It's so human readable and it doesn't cost much.  

- Reference:

    - Microsoft .NET general introduction => [LINQ: .NET Language-Integrated Query](https://msdn.microsoft.com/en-us/library/bb308959.aspx).
    - Wikipedia => [Language Integrated Query](https://en.wikipedia.org/wiki/Language_Integrated_Query).

And there are so many scenes very awkward to Python programmer, using `Linq` might help a lot.  

## Awkward Scenes in Python

```python

seq1 = range(100)
seq2 = range(100, 200)
zipped = zip(seq1, seq2)
mapped = map(lambda ab: ab[0] / ab[1], zipped)
grouped = dict()
group_fn = lambda x: x // 0.2
for e in mapped:
    group_id = group_fn(e)
    if group_id not in grouped:
        grouped[group_id] = [e]
        continue
    grouped[group_id].append(e)
for e in grouped.items():
    print(e)
```

The codes seems to be too long...  

Now we extract the function `group_by`:  

```python

def group_by(f, container):
    grouped = dict()
    for e in container:
        group_id = f(e)
        if group_id not in grouped:
            grouped[group_id] = [e]
            continue
        grouped[group_id].append(e)
    return grouped
res = group_by(lambda x: x//0.2, map(lambda ab[0]/ab[1], zip(seq1, seq2)))
```

Okay, it's not at fault, however, it makes me upset —— why do I have to write these ugly codes?  

**Now, let us try Linq!**

```Python

from linq import Flow, extension_std
seq = Flow(range(100))
res = seq.zip(range(100, 200)).map(lambda fst, snd : fst/snd).group_by(lambda num: num//0.2)._

```


## How does [Linq.py](https://github.com/Xython/Linq.py) work?

There is a core class object, `linq.core.flow.TSource`, which just has one member `_`.  
When you want to get a specific extension method from `TSource` object,
the `type` of its `_` member will be used to search whether the extension method exists.  
In other words, extension methods are binded with the type of `_`.

```python

class TSource:
    __slots__ = ['_']

    def __init__(self, sequence):
        self._ = sequence

    def __getattr__(self, k):
        for cls in self._.__class__.__mro__:
            namespace = Extension.get(cls, '')
            if k in namespace:
                return partial(namespace[k], self)

        where = ','.join('{}.{}'.format(cls.__module__, cls.__name__) for cls in self._.__class__.__mro__)

        raise NameError("No extension method named `{}` for types `{}`.".format(k, where))

    def __str__(self):
        return self._.__str__()

    def __repr__(self):
        return self._.__repr__()


class Flow(Generic[T]):
    def __new__(cls, seq):
        return TSource(seq)

```

## Extension Method

Here are two methods for you to do so.  

- you can use `extension_std` to add extension methods for all Flow objects.  

- you use `extension_class(cls)` to add extension methods for all Flow objects whose member `_`'s type is `cls`.

```python

@extension_std  # For all Flow objects
def Add(self, i):
    return self + i

@extension_class(int) # Just for type `int`
def Add(self: int, i):
    return self + i

assert Flow(4).add(2)._ is 6
```

## Documents of Standard Extension Methods 

Note: Docs haven't been finished yet.

- Index

    - [Sum](https://github.com/Xython/Linq.py/blob/typed-linq/docs/general.md#sum)
    - [Enum](https://github.com/Xython/Linq.py/blob/typed-linq/docs/general.md#enum)
    - [Map](https://github.com/Xython/Linq.py/blob/typed-linq/docs/general.md#map)
    - [Reduce](https://github.com/Xython/Linq.py/blob/typed-linq/docs/general.md#reduce)
    - [Then](https://github.com/Xython/Linq.py/blob/typed-linq/docs/general.md#then)
    - [Each](https://github.com/Xython/Linq.py/blob/typed-linq/docs/general.md#each)
    - [Aggregate](https://github.com/Xython/Linq.py/blob/typed-linq/docs/general.md#aggregate)
    - [Zip](https://github.com/Xython/Linq.py/blob/typed-linq/docs/general.md#zip)
    - [Sorted](https://github.com/Xython/Linq.py/blob/typed-linq/docs/general.md#sorted)
    - [ArgSorted](https://github.com/Xython/Linq.py/blob/typed-linq/docs/general.md#argsorted)
    - [ChunkBy](https://github.com/Xython/Linq.py/blob/typed-linq/docs/general.md#chunkby)
    - [GroupBy](https://github.com/Xython/Linq.py/blob/typed-linq/docs/general.md#groupby)
    - [Take](https://github.com/Xython/Linq.py/blob/typed-linq/docs/general.md#take)
    - [TakeWhile](https://github.com/Xython/Linq.py/blob/typed-linq/docs/general.md#takewhile)
    - [First](https://github.com/Xython/Linq.py/blob/typed-linq/docs/general.md#first)
    - [Drop|Skip](https://github.com/Xython/Linq.py/blob/typed-linq/docs/general.md#drop|skip)
    - [Concat](https://github.com/Xython/Linq.py/blob/typed-linq/docs/general.md#concat)
    - [ToList](https://github.com/Xython/Linq.py/blob/typed-linq/docs/general.md#tolist)
    - [ToTuple](https://github.com/Xython/Linq.py/blob/typed-linq/docs/general.md#totuple)
    - [ToDict](https://github.com/Xython/Linq.py/blob/typed-linq/docs/general.md#todict)
    - [ToSet](https://github.com/Xython/Linq.py/blob/typed-linq/docs/general.md#toset)
    - [All](https://github.com/Xython/Linq.py/blob/typed-linq/docs/general.md#all)
    - [Any](https://github.com/Xython/Linq.py/blob/typed-linq/docs/general.md#any)
    - [Intersects](https://github.com/Xython/Linq.py/blob/typed-linq/docs/set.md#intersects)
    - [Union](https://github.com/Xython/Linq.py/blob/typed-linq/docs/set.md#union)

## How to Contribute 

- Design the [standard library](https://github.com/Xython/Linq.py/tree/typed-linq/linq/standard) for [Linq.py](https://github.com/Xython/Linq.py).

- Write documents for the standard library and tutorials about how to use [Linq.py](https://github.com/Xython/Linq.py).  

- Join [LinqPy Room](https://gitter.im/LinqPy/Lobby) to discuss about any aspects of [Linq.py](https://github.com/Xython/Linq.py).

Feel free to pull requests here.
