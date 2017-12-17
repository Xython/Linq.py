import inspect


def concat_generator(*generators):
    for generator in generators:
        yield from generator


def is_single_param(f):
    if not callable(f):
        raise TypeError('Not callable argument!')
    try:
        arg_info = inspect.getfullargspec(f)
    except TypeError:
        # In order to support some builtin functions :)
        return True
    if arg_info.varargs:
        return True
    n = len(arg_info.args) + len(arg_info.kwonlyargs)
    if n is 0:
        raise ReferenceError('Function can not be with zero parameter.')
    return n is 1


def destruct_func(f):
    def destruct(e):
        return f(*e)

    return destruct
