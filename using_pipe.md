## Pipe

Here is a convenience for you to use `linq` in a different way.  
If you want to write the following codes, you have to install [pipe-fn](https://github.com/Xython/pipe-fn) with `pip install pipe-fn`.

```python

from pipe_fn import e
import linq.standard as std

[1, 2, 3] | e / std.general.Sum | e / print
# <=> print(std.general.Sum([1,2, 3]))

[2, 3, -1] | e / std.list.Sort | e / print
# <=> print(std.list.Sort([2, 3, -1])) 

{1, 2, 3} | e / std.general.Zip * ([1, 2, 3],) | e / list | e / print

# print(list(zip({1, 2, 3}, [1, 2, 3])))

1 | e / std.general.Then * (lambda x: [x] * 20,) | e / sum | e / print
# <=> print(sum(std.general.Then(1, lambda x: [x] * 20)))

1 | e / std.general.Then * (lambda x: [x] * 20,) + e / sum + e / print
# <=> print(
#       and_then(
#            std.general.Then,
#            lambda x: [x] * 20,
#            sum))

```


