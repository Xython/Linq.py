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

## Zip

## Sorted

## ArgSorted

## Group

## Take

## TakeWhile

## Drop|Skip

## Concat

## ToList

## ToTuple

## ToDict

## ToSet

## All

## Any