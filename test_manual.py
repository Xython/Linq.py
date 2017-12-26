# see the standard library to get all the extension methods.

from linq.core.collections import Generator as MGenerator
from linq import Flow, extension_class, extension_class_name


def test_other():
    def block_lambda(e):
        e = e + 1
        if e < 10:
            return e
        else:
            raise StopIteration

    res = Flow(MGenerator(block_lambda, 0)).Take(100).ToList()

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

    print(seq.Take(10).Enum().Map(lambda a, b: a * b).Sum().Unboxed())
    #   Support infinite sequences, parameters destruct and so on.
    #   Limited by Python's syntax grammar, parameters destruct
    # cannot be as powerful as pattern matching.

    # => 285
    print('\n================\n')

    print(sum([a * b for a, b in enumerate(range(10))]))
    # => 285


test_example1()


@my_test
def test_example2():
    """
    Example 2:
    """

    # Adding Skip to provide another semantic of Drop
    print(seq.Skip(10).Take(5).ToList().Unboxed())
    # => [10, 11, 12, 13, 14]
    print(seq.Take(10).Drop(5).ToList().Unboxed())
    # => [5, 6, 7, 8, 9]
    print(seq.Skip(5).Take(10).Drop(5).ToList().Unboxed())
    # => [10, 11, 12, 13, 14]


test_example2()


@my_test
def test_example3():
    """
    Example 3:
    """

    print(seq.Take(10).Reduce(lambda x, y: x + y, 10).Unboxed())
    # cumulate a single result using a start value.
    # => 55
    print(seq.Take(10).Scan(lambda x, y: x + y, 10).ToList().Unboxed())
    # cumulate a collection of intermediate cumulative results using a start value.
    # => [10, 11, 13, 16, 20, 25, 31, 38, 46, 55]


test_example3()


@my_test
def test_example4():
    """
    Example 4:
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
    def ToTupleGenerator(self: Flow):
        return Flow((k, v) for k, v in self.stream.items()).ToTuple().Unboxed()

    try:
        seq.Take(10).ToTupleGenerator()
    except Exception as e:
        print(e.args)
    """
    NameError: No extension method named `ToTupleGenerator` for builtins.object.
    """
    print(seq.Take(10).Zip(seq.Take(10)).ToDict().ToTupleGenerator())


test_example5()


@my_test
def test_extension_byclsname():
    @extension_class_name('generator')
    def MyNext(self: Flow):
        return self.Then(next)


test_extension_byclsname()
Flow((i for i in range(10))).MyNext()
