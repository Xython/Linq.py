# see the standard library to get all the extension methods.
from typing import List

from linq.core.collections import Generator as MGenerator
from linq import Flow, extension_class, generator_type


def test_other():
    def block_lambda(e):
        e = e + 1
        if e < 10:
            return e
        else:
            raise StopIteration

    res = Flow(MGenerator(block_lambda, 0)).take(100).to_list()

    assert res.__str__() == res.__repr__()


test_other()


def my_test(func):
    def call():
        global seq
        seq = Flow(MGenerator(lambda x: x + 1, start_elem=0))  # [0..\infty]
        func.__globals__['seq'] = seq
        func()

    return call


@my_test
def test_example1():
    # See the definition of MGenerator at https://github.com/thautwarm/ActualFn.py/blob/master/linq/core/collections.py.
    # It's a generalization of PyGenerator.
    # What's more, it can be deepcopid and serialized!

    """
    Example 1:
    """

    print(seq.take(10).enum().map(lambda a, b: a * b).sum())
    #   Support infinite sequences, parameters destruct and so on.
    #   Limited by Python's syntax grammar, parameters destruct
    # cannot be as powerful as pattern matching.

    # => 285
    print('\n================\n')

    print(sum([a * b for a, b in enumerate(range(10))]))  # => 285


test_example1()


@my_test
def test_example2():
    """
    Example 2:
    """

    print(seq.take(100).skip(10).drop(5).to_list())


test_example2()


@my_test
def test_example3():
    """
    Example 3:
    """

    print(seq.take(10).reduce(lambda x, y: x + y, 10))
    # cumulate a single result using a start value.
    # => 55
    print(seq.take(10).scan(lambda x, y: x + y,
                            10).to_list())  # cumulate a collection of intermediate cumulative results using a start value.  # => [10, 11, 13, 16, 20, 25, 31, 38, 46, 55]


test_example3()


@my_test
def test_example4():
    """
    Example 4:
    """

    print('\n================\n')
    seq1 = seq.take(100)
    seq2 = seq.take(200).skip(100)

    seq1.zip(seq2).map(lambda a, b: a / b).group_by(lambda x: x // 0.2).each(print)

    print('\n================\n')

    seq1 = range(100)
    seq2 = range(100, 200)
    zipped = zip(seq1, seq2)
    mapped = map(lambda ab: ab[0] / ab[1], zipped)
    grouped = dict()

    def group_fn(x):
        return x // 0.2

    for e in mapped:
        group_id = group_fn(e)
        if group_id not in grouped:
            grouped[group_id] = [e]
            continue
        grouped[group_id].append(e)
    for e in grouped.items():
        print(e)


test_example4()


@my_test
def test_example5():
    """
    Example 5:
    """

    @extension_class(dict)
    def ToTupleGenerator(self: dict):
        return Flow(((k, v) for k, v in self.items())).to_tuple()

    try:
        seq.take(10).ToTupleGenerator()
    except Exception as e:
        print(e.args)
    """
    NameError: No extension method named `ToTupleGenerator` for builtins.object.
    """
    print(Flow(seq.take(10).zip(seq.take(10)).to_dict()).ToTupleGenerator())


test_example5()


@my_test
def test_extension_byclsname():
    @extension_class(generator_type, box=False)
    def MyNext(self):
        return next(self)


test_extension_byclsname()
print(Flow((i for i in range(10))).my_next())

# class MyFlow(Flow):
#
#     @extension_class(list)
#     def apply(self, n) -> Flow[List[int]]:
#         return [e + n for e in self]


print(Flow({1: 2, 3: 4}).map(lambda a, b: a + b).reduce(lambda a, b: a + b))

print(Flow({1: 2, 3: 4, 5: 6}).shift(2).to_list())

Flow([1, 2, 3]).intersects([2, 3, 4]).then(lambda a, b: print(a * 3 + b))
