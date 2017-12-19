import os

from Ruikowa.ObjectRegex.MetaInfo import MetaInfo

from linq import Flow
import linq.standard
from code_gen_test.mparser import Def, token
from Ruikowa.ObjectRegex.ASTDef import Ast
from Ruikowa.ErrorFamily import handle_error

_parser = handle_error(Def)


def read(file):
    with open(file, encoding='utf8') as cur:
        return cur.read()


def recursive_list(directory):
    files = map(lambda f: f'{directory}/{f}', os.listdir(directory))
    res = []
    for file in files:
        if file.endswith('.py'):
            res.append(read(file))
        elif os.path.isdir(file):
            res.extend(recursive_list(file))
        continue
    return res


from typing import List


def gen_expr(arg):
    if isinstance(arg, str):
        if arg in ('f', 'by'):
            return '(lambda x: x)'
        elif arg in ('other',):
            return ' [1, 2] '
    elif len(arg) is 2:
        arg = arg[1]
        if arg in ('functions',):
            return '(lambda x: x)'
        elif arg in ('others',):
            return '[1, 2]'
    else:
        return None


def parser(ast: Ast):
    if ast is None:
        return None
    print(ast)
    name = ast[0]
    params = ast[1][1:]
    try:
        params = ','.join(map(gen_expr, params))
    except:
        return None
    return 'Flow([1, 2, 3]).{name}({params})'.format(name=name, params=params)


def gen_functions(files: List[str]):
    generated = []
    for codes in files:
        sources = codes.split('\n')
        index = Flow(sources) \
            .Enum() \
            .Map(lambda i, x: i + 1 if x.startswith('@extension_') else None) \
            .Filter(lambda x: x).ToTuple().Unboxed()

        generated.extend(list(filter(lambda x: x, map(lambda i: parser(_parser(token(sources[i]), meta=MetaInfo())), index))))
    return '\n'.join(generated)


print(gen_functions(recursive_list('linq')))
