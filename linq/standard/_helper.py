from collections import defaultdict
from linq.core.utils import *


def _group_by(stream, f=None):
    res = defaultdict(list)
    if f is None:
        for each in stream:
            res[each].append(each)
        return res

    if is_to_destruct(f):
        f = destruct_func(f)

    for each in stream:
        res[f(each)].append(each)

    return res


def _chunk(stream, f=None):
    grouped = None
    _append = None
    last = None

    if f is None:
        for e in stream:
            if grouped is None:
                grouped = [e]
                _append = grouped.append
            elif last == e:
                _append(e)
            else:
                yield (last, grouped)
                grouped = [e]
                _append = grouped.append
            last = e
        else:
            yield (last, grouped)
    else:
        for _e in stream:
            e = f(_e)
            if grouped is None:
                grouped = [_e]
                _append = grouped.append
            elif last == e:
                _append(_e)
            else:
                yield (last, grouped)
                grouped = [_e]
                _append = grouped.append
            last = e
        else:
            yield (last, grouped)
