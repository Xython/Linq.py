## Unboxed

Use `Flow._` to Unbox a `Flow` object.

- Type: `Flow[T] => T`

- Usage:

    ```python
    Flow([1, 2, 3]).map(lambda x: x+1).to_list()._
    # => [2, 3, 4]
    ```

## Sum

- Type: 
    - `(Flow[Iterable[number]], number => number) => number`.

        ```python
        res = Flow([1, 2, 3]).sum(lambda x: x**2)
        res  # => 14 = 1**2 + 2**2 + 3**2 
        res._ == 14  # => True
        ```
    - `Flow[Iterable[number]] => number`.
    
        ```python
        Flow([1, 2, 3]).sum()._ == 6  # => True
        ```
## Enum

```python
Flow(['a', 'b']).enum().to_list()._
# => [(0, 'a'), (1, 'b')]
```

## Map

Lazy map operation. Support parameter destruction.

```python
Flow(['a', 'b']).zip([1, 2]).map(lambda a, b: a + '_' * b).then(','.join)._
# => 'a_,b__' 

```

## Reduce

Don't support parameter destruction.

- Type: `(Flow[Iterable[T]], (R, T) => R) => R`

```python
assert Flow([1, 2, 3]).reduce(lambda a, b: a + b)._ == 6
```

- Type: `(Flow[Iterable[T]], (R, T) => R, R) => R`

```python
assert Flow([1, 2, 3]).reduce(lambda a, b: a + b, 3)._ == 9
```

## Then

 Support parameter destruction.

```python
assert Flow((1, 2, 3)).then(lambda a, b, c: a * b * c)._ == 6
```

## Each

 Support parameter destruction.

```python
Flow(['red', 'blue', 'yellow']).zip(range(3)).each(lambda a, b: print(a * b))
# =>
# red
# blue
# blue
# yellow
# yellow
# yellow
```
## Aggregate

- Type: `(Flow[Iterable[T]], (T=>V)...) => Tuple[V, ...]`

```python
import numpy as np
Flow(range(100)).aggregate(sum, max, min, np.mean)._
# => (4950, 99, 0, 49.5)
```

## Zip

```python

a, b, c = 'abc'
x = Flow((a, b, c)).zip([b, c, a], [c, a, b])
s = x.map(lambda _1, _2, _3: _1 + _2 + _3).to_tuple()._
print(s)
# => ('abc', 'bca', 'cab')
```

## Sorted

```python
Flow([(1, 2), (2, 1)]).sorted()._
Flow([(1, 2), (2, 1)]).sorted(lambda a, b: b)._
# =>
# [(1, 2), (2, 1)]
# [(2, 1), (1, 2)]
```
## ArgSorted

```python
Flow([(1, 2), (2, 1)]).arg_sorted()._
Flow([(1, 2), (2, 1)]).arg_sorted(lambda a, b: b)._
# =>
# [0, 1]
# [1, 0]
```

## ChunkBy

```python
Flow(range(20)).chunk_by(lambda e: e//5 % 3).to_list()._
# =>
# [(0, [0, 1, 2, 3, 4]),
#  (1, [5, 6, 7, 8, 9]),
#  (2, [10, 11, 12, 13, 14]),
#  (0, [15, 16, 17, 18, 19])]
```

## Take

```python
Flow(range(20)).take(10).to_list()._
# =>
# [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
```

## TakeWhile

```python
Flow(range(20)).take_while(lambda e: e ** 2 < 12).to_list()._
# =>
# [0, 1, 2, 3]
```

## First

```python
from linq.core.collections import Generator as MyGenerator
Flow(
    MyGenerator(lambda e: e + 1, 3)
).filter(
        lambda e: e ** 4 + e < (e // 2) ** (e // 3)
).first()
# => 18
```

## Drop|Skip

```python
from linq.core.collections import Generator as MyGenerator
inf = Flow(MyGenerator(lambda e: e + 1, 0))
inf.skip(2).first()._
# => 3

Flow([1, 2, 3]).drop(1).skip(1).to_tuple()._
# => (2,)
```

## Concat

## ToList

## ToTuple

## ToDict

## ToSet

## All

## Any