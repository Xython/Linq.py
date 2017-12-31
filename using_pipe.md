## Pipe

Here is a convenience for you to use `linq` in a different way.  
If you want to write the following codes, you have to install [pipe-fn](https://github.com/Xython/pipe-fn) with `pip install pipe-fn`.

```python

from pipe_fn import e
import linq.standard as std

[1, 2, 3] | e / std.general.Sum | e / print

[2, 3, -1] | e / std.list.Sort | e / print

{1, 2, 3} | e / std.general.Zip * ([1, 2, 3],) | e / list | e / print

1 | e / std.general.Then * (lambda x: [x] * 20,) | e / sum | e / print

1 | e / std.general.Then * (lambda x: [x] * 20,) + e / sum + e / print

```


