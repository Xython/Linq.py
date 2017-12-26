import inspect


def concat_generator(*generators):
    for generator in generators:
        yield from generator


def is_to_destruct(f):
    if not callable(f):
        raise TypeError('Not callable argument!')
    try:
        if getattr(f, '__code__', None) is None:
            return False

        arg_info = inspect.getfullargspec(f)
    except TypeError:
        # In order to support some builtin functions :)
        return False

    if not is_lambda(f):
        if arg_info.varargs or arg_info.kwonlyargs or arg_info.defaults:
            return False
        n = len(arg_info.args)
    else:
        if arg_info.varargs:
            return True
        n = len(arg_info.args) + len(arg_info.kwonlyargs)

    if n is 0:
        raise ReferenceError('Function can not be with zero parameter.')
    return n is not 1


__lambda_name__ = '<lambda>'


def is_lambda(f):
    return f.__name__ == __lambda_name__


def destruct_func(f):
    def destruct(e):
        return f(*e)

    return destruct
