## Unboxed

Unbox a `Flow` object.
- Type: `Flow[T] => T`
- Usage:

    ```python
    Flow([1, 2, 3]).Map(lambda x: x+1).ToList().Unboxed()
    # => [2, 3, 4]
    ```

## Sum

- Type: 
    - `(Flow[Sequence[T]], T => G) => G`, where `G` must have meta method `__add__`. Support parameter destruction.

        ```python
        res = Flow([1, 2, 3]).Sum(lambda x: x**2)
        res  # => 14 = 1**2 + 2**2 + 3**2 
        res == Flow(14)  # => True 
        res.Unboxed() == 14  # => True
        ```
    - `Flow[Sequence[T]] => T`, where `T` must have meta method `__add__`.
    
        ```python
        Flow([1, 2, 3]).Sum() == Flow(6)  # => True
        Flow([1, 2, 3]).Sum().Unboxed() == 6 # => True
        ```
    



## Enum

## Map

## Reduce

## Then

## Each

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