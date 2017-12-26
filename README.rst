Linq.py
=======

|Build Status| |License| |codecov| |Coverage Status| |PyPI version|

Install
-------

::

    pip install -U Linq

Here is an example to get top 10 frequent pixels in a picture.

.. code:: python


    from linq import Flow
    import numpy as np

    def most_frequent(arr: np.ndarray) -> np.ndarray:
        return  Flow(arr.flatten())                     \
                        .GroupBy(lambda _: _)           \
                        .Then(lambda x: x.items())      \
                        .Map(lambda k, v: (k, len(v)))  \
                        .Sorted(by=lambda _, v: -v)     \
                        .Take(10)                       \
                        .Map(lambda k, _: k)            \
                        .ToList()                       \
                        .Then(np.array).Unboxed()

About Linq
----------

| The well-known EDSL in .NET, ``Language Integrated Query``, in my
  opinion, is one of the best design in .NET environment.
| Here is an example of C# Linq.

.. code:: c#

    // Calculate MSE loss.
    /// <param name="Prediction"> the prediction of the neuron network</param>
    /// <param name="Expected"> the expected target of the neuron network</param>

    Prediction.Zip(Expected, (pred, expected)=> Math.Square(pred-expected)).Average()

It's so human readable and it doesn't cost much.

-  Reference:

   -  Microsoft .NET general introduction => `LINQ: .NET
      Language-Integrated
      Query <https://msdn.microsoft.com/en-us/library/bb308959.aspx>`__.
   -  Wikipedia => `Language Integrated
      Query <https://en.wikipedia.org/wiki/Language_Integrated_Query>`__.

And there are so many scenes very awkward to Python programmer, using
``Linq`` might help a lot.

Awkward Scenes in Python
------------------------

.. code:: python


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

The codes seems to be too long...

Now we extract the function ``group_by``:

.. code:: python


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

Okay, it's not at fault, however, it makes me upset —— why do I have to
write these ugly codes?

**Now, let us try Linq!**

.. code:: python


    from linq import Flow, extension_std
    seq = Flow(range(100))
    res = seq.Zip(range(100, 200)).Map(lambda fst, snd : fst/snd).GroupBy(lambda num: num//0.2).Unboxed()

How does `Linq.py <https://github.com/Xython/Linq.py>`__ work?
--------------------------------------------------------------

| There is a core class object, ``linq.core.flow.Flow``, which just has
  one member ``stream``.
| When you want to get a specific extension method from ``Flow`` object,
  the ``type`` of its ``stream`` member will be used to search whether
  the extension method exists.
| In other words, extension methods are binded with the type(precisely,
  ``{type.__module__}.{type.__name__}``).

.. code:: python


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

Extension Method
----------------

Here are three methods for you to do so.

-  Firstly, you can use ``extension_std`` to add extension methods for
   all Flow objects.

-  Next, you use ``extension_class(cls: type)`` to add extension methods
   for all Flow objects whose member ``stream``'s type is named
   ``{cls.__module}.{cls.__name__}``.

-  Finally, you can use
   ``extension_class(cls_name: str,  of_module='builtins')`` to add
   extension methods for all Flow objects whose member ``stream``'s type
   is named is named ``{of_module}.{cls_name}``.

(This way to make extension methods is for the **implicit types** in
Python, each of which cannot be got except from its instances' meta
member ``__class__``.)

.. code:: python


    @extension_std  # For all Flow objects
    def Add(self, i):
        return Flow(self.stream + (i.stream if isinstance(i, Flow) else i)))

    @extension_class(int) # Just for type `int`
    def Add(self, i):
        return Flow(self.stream + (i.stream if isinstance(i, Flow) else i)))

    @extension_class_name('int',  of_module=int.__module__) # Also for type `int`.
    def Add(self, i):
        return Flow(self.stream + (i.stream if isinstance(i, Flow) else i)))

Documents of Standard Extension Methods
---------------------------------------

Note: Docs haven't been finished yet.

-  General(can be used by all Flow objects)

   -  `Unboxed <https://github.com/Xython/Linq.py/blob/master/docs/general.md#unboxed>`__
   -  `Sum <https://github.com/Xython/Linq.py/blob/master/docs/general.md#sum>`__
   -  `Enum <https://github.com/Xython/Linq.py/blob/master/docs/general.md#enum>`__
   -  `Map <https://github.com/Xython/Linq.py/blob/master/docs/general.md#map>`__
   -  `Reduce <https://github.com/Xython/Linq.py/blob/master/docs/general.md#reduce>`__
   -  `Then <https://github.com/Xython/Linq.py/blob/master/docs/general.md#then>`__
   -  `Each <https://github.com/Xython/Linq.py/blob/master/docs/general.md#each>`__
   -  `Aggregate <https://github.com/Xython/Linq.py/blob/master/docs/general.md#aggregate>`__
   -  `Zip <https://github.com/Xython/Linq.py/blob/master/docs/general.md#zip>`__
   -  `Sorted <https://github.com/Xython/Linq.py/blob/master/docs/general.md#sorted>`__
   -  `ArgSorted <https://github.com/Xython/Linq.py/blob/master/docs/general.md#argsorted>`__
   -  `Group <https://github.com/Xython/Linq.py/blob/master/docs/general.md#group>`__
   -  `GroupBy <https://github.com/Xython/Linq.py/blob/master/docs/general.md#groupby>`__
   -  `Take <https://github.com/Xython/Linq.py/blob/master/docs/general.md#take>`__
   -  `TakeWhile <https://github.com/Xython/Linq.py/blob/master/docs/general.md#takewhile>`__
   -  `Drop\|Skip <https://github.com/Xython/Linq.py/blob/master/docs/general.md#drop%7Cskip>`__
   -  `Concat <https://github.com/Xython/Linq.py/blob/master/docs/general.md#concat>`__
   -  `ToList <https://github.com/Xython/Linq.py/blob/master/docs/general.md#tolist>`__
   -  `ToTuple <https://github.com/Xython/Linq.py/blob/master/docs/general.md#totuple>`__
   -  `ToDict <https://github.com/Xython/Linq.py/blob/master/docs/general.md#todict>`__
   -  `ToSet <https://github.com/Xython/Linq.py/blob/master/docs/general.md#toset>`__
   -  `All <https://github.com/Xython/Linq.py/blob/master/docs/general.md#all>`__
   -  `Any <https://github.com/Xython/Linq.py/blob/master/docs/general.md#any>`__

-  List

   -  `Extended <https://github.com/Xython/Linq.py/blob/master/docs/list.md#extended>`__
   -  `Extend <https://github.com/Xython/Linq.py/blob/master/docs/list.md#extend>`__
   -  `Sort <https://github.com/Xython/Linq.py/blob/master/docs/list.md#sort>`__
   -  `Reversed <https://github.com/Xython/Linq.py/blob/master/docs/list.md#reversed>`__
   -  `Reverse <https://github.com/Xython/Linq.py/blob/master/docs/list.md#reverse>`__

-  Set

   -  `Intersects <https://github.com/Xython/Linq.py/blob/master/docs/set.md#intersects>`__
   -  `Union <https://github.com/Xython/Linq.py/blob/master/docs/set.md#union>`__

How to Contribute
-----------------

-  Design the `standard
   library <https://github.com/Xython/Linq.py/tree/master/linq/standard>`__
   for `Linq.py <https://github.com/Xython/Linq.py>`__.

-  Write documents for the standard library and tutorials about how to
   use `Linq.py <https://github.com/Xython/Linq.py>`__.

-  Join `LinqPy Room <https://gitter.im/LinqPy/Lobby>`__ to discuss
   about any aspects of `Linq.py <https://github.com/Xython/Linq.py>`__.

Feel free to pull requests here.

.. |Build Status| image:: https://travis-ci.org/Xython/Linq.py.svg?branch=master
   :target: https://travis-ci.org/Xython/Linq.py
.. |License| image:: https://img.shields.io/badge/license-MIT-yellow.svg
   :target: https://github.com/Xython/Linq.py/blob/master/LICENSE
.. |codecov| image:: https://codecov.io/gh/Xython/Linq.py/branch/master/graph/badge.svg
   :target: https://codecov.io/gh/Xython/Linq.py
.. |Coverage Status| image:: https://coveralls.io/repos/github/Xython/Linq.py/badge.svg?branch=master
   :target: https://coveralls.io/github/Xython/Linq.py?branch=master
.. |PyPI version| image:: https://img.shields.io/pypi/v/Linq.svg
   :target: https://pypi.python.org/pypi/Linq
