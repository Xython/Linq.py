# Linq.py 
[![Build Status](https://travis-ci.org/thautwarm/Linq.py.svg?branch=master)](https://travis-ci.org/thautwarm/Linq.py)
[![License](https://img.shields.io/badge/license-MIT-yellow.svg)](https://github.com/thautwarm/Linq.py/blob/master/LICENSE)
[![codecov](https://codecov.io/gh/thautwarm/Linq.py/branch/master/graph/badge.svg)](https://codecov.io/gh/thautwarm/Linq.py)

- PS: [Coverage Here](https://travis-ci.org/thautwarm/Linq.py/jobs/318643137).

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
res = seq.Zip(range(100, 200)).Map(lambda fst, snd : fst/snd).GroupBy(lambda num: num//0.2).Unboxed()
```


## How does [Linq.py](https://github.com/thautwarm/Linq.py) work?

There is a core class object, `linq.core.flow.Flow`, which just has one member `stream`.  
When you want to get a specific extension method from `Flow` object, 
the `type` of its `stream` member will be used to search whether the extension method exists,
in other words, extension methods are binded with the type(precisely, `{type.__module__}.{type.__name__}`).

```python
class Flow:
    __slots__ = ['stream']

    def __init__(self, sequence):
        self.stream = sequence

    def __getattr__(self, k):
        for cls in self.stream.__class__.__mro__:
            namespace = Extension['{}.{}'.format(cls.__module__, cls.__name__)]
            if k in namespace:
                return partial(namespace[k], self)
        raise NameError(
            "No extension method named `{}` for {}.".format(
                k, '{}.{}'.format(object.__module__, object.__name__)))

    def __str__(self):
        return self.stream.__str__()

    def __repr__(self):
        return self.__str__()
```

## Extension Method
Here are three methods for you to do so.  
- Firstly, you can use `extension_std` to add extension methods for all Flow objects.  

- Next, you use `extension_class(cls: type)` to add extension methods for all Flow objects whose member `stream`'s type is named `{cls.__module}.{cls.__name__}`.  

- Finally, you can use `extension_class(cls_name: str, of_module='builtins')` to add extension methods for all Flow objects whose member `stream`'s type is named is named `{of_module}.{cls_name}`.  
(This way to make extension methods is for the **implicit types** in Python, each of which cannot be got except from its instances' meta member `__class__`.)

```python
@extension_std  # For all Flow objects
def Add(self, i):
    return Flow(self.stream + (i.stream if isinstance(i, Flow) else i)))

@extension_class(int) # Just for type `int`
def Add(self, i):
    return Flow(self.stream + (i.stream if isinstance(i, Flow) else i)))

@extension_class_name('int',  of_module=int.__module__) # Also for type `int`.
def Add(self, i):
    return Flow(self.stream + (i.stream if isinstance(i, Flow) else i)))
```

## Documents of Standard Extension Methods 
Note: Docs haven't been finished yet.
- General(can be used by all Flow objects)
    - [Unboxed]()
    - [Sum]()
    - [Enum]()
    - [Map]()
    - [Reduce]()
    - [Then]()
    - [Each]()
    - [Aggregate]()
    - [Zip]()
    - [Sorted]()
    - [ArgSorted]()
    - [Group]()
    - [GroupBy]()
    - [Take]()
    - [TakeWhile]()
    - [Drop]()
    - [Concat]()
    - [ToList]()
    - [ToTuple]()
    - [ToDict]()
    - [ToSet]()
    - [All]()
    - [Any]()

- List
    - [Extended]()
    - [Extend]()
    - [Sort]()
    - [Reversed]()
    - [Reverse]()
    
- Set
    - [Intersects]()
    - [Union]()

## How to Contribute 

- Design the [standard library](https://github.com/thautwarm/Linq.py/tree/master/linq/standard) for [Linq.py](https://github.com/thautwarm/Linq.py).

- Write documents for the standard library and tutorials about how to use [Linq.py](https://github.com/thautwarm/Linq.py).  

- Join [LinqPy Room](https://gitter.im/LinqPy/Lobby) to discuss about any aspects of [Linq.py](https://github.com/thautwarm/Linq.py).

Feel free to pull requests here.
