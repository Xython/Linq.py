from linq.core.collections import Generator as MGenerator
from linq.core.flow import Flow
# see the standard library to get all the extension methods.
import linq.standard

seq = Flow(MGenerator(lambda x: x + 1, start_elem=0))  # [0..\infty]
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


"""
Example 2:
"""

print(seq.Skip(10).Take(5).ToList().Unboxed())
# => [10, 11, 12, 13, 14]
print(seq.Take(10).Drop(5).ToList().Unboxed())
# => [5, 6, 7, 8, 9]
print(seq.Skip(5).Take(10).Drop(5).ToList().Unboxed())
# => [10, 11, 12, 13, 14]


"""
Example 3:
"""

print(seq.Take(10).Reduce(lambda x, y: x + y, 10).Unboxed())
# cumulate a single result using a start value.
# => 55
print(seq.Take(10).Scan(lambda x, y: x + y, 10).ToList().Unboxed())
# cumulate a collection of intermediate cumulative results using a start value.
# => [10, 11, 13, 16, 20, 25, 31, 38, 46, 55]


"""
Example 4:
"""

print('\n================\n')
seq1 = seq.Take(100)
seq2 = seq.Take(200).Drop(100)
s = seq1.Zip(seq2)               \
    .Map(lambda a, b: a / b)     \
    .GroupBy(lambda x: x // 0.2) \
    .Then(lambda x: x.items())   \
    .Each(print)

print('\n================\n')

seq1 = range(100)
seq2 = range(100, 200)
zipped = zip(seq1, seq2)
mapped = map(lambda ab: ab[0] / ab[1], zipped)
grouped = dict()


def group_fn(x): return x // 0.2


for e in mapped:
    group_id = group_fn(e)
    if group_id not in grouped:
        grouped[group_id] = [e]
        continue
    grouped[group_id].append(e)
for e in grouped.items():
    print(e)

"""
Example 5:
"""

from linq.core.flow import extension_class, Flow


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
