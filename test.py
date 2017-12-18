from linq.core.collections import Generator as MGenerator
from linq.core.flow import Flow
import linq.standard  # see the standard library to get all the extension methods.

seq = Flow(MGenerator(lambda x: x + 1, start_elem=0))  # [0..\infty]
# See the definition of MGenerator at https://github.com/thautwarm/ActualFn.py/blob/master/linq/core/collections.py.
# It's a generalization of PyGenerator.
# What's more, it can be deepcopid and serialized!


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
    return Flow((k, v) for k, v in self.stream.items()).ToTuple().Unboxed()


try:
    seq.Take(10).ToTupleGenerator()
except Exception as e:
    print(e.args)
"""
 NameError: No extension method named `ToTupleGenerator` for builtins.object.
"""
print(seq.Take(10).Zip(seq.Take(10)).ToDict().ToTupleGenerator())
