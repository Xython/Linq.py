import os

from Ruikowa.ObjectRegex.MetaInfo import MetaInfo

from linq import Flow
import linq.standard
import json
from code_gen_test.mparser import Def, token, paramList
from Ruikowa.ObjectRegex.ASTDef import Ast
from Ruikowa.ErrorFamily import handle_error

_parser = handle_error(Def)
_param_parser = handle_error(paramList)


def read(file):
    with open(file, encoding='utf8') as cur:
        return cur.read()


def recursive_list(directory):
    files = map(lambda f: '{directory}/{f}'.format(f=f, directory=directory), os.listdir(directory))
    res = []
    for file in files:
        if file.endswith('.py'):
            res.append(read(file))
        elif os.path.isdir(file):
            res.extend(recursive_list(file))
        continue
    return res


with open('code_gen_test/specific.json', 'r') as _:
    Specific = json.load(_)


def gen_expr(arg):
    if len(arg) is 1:
        arg = arg[0]
        if arg in ('f', 'by'):
            return 'lambda x, y: x + y'
        elif arg in ('other',):
            return ' [(1, 2), (2, 2), (3, 3)] '
        elif arg in ('n',):
            return '1'
    elif len(arg) is 2:
        arg = arg[1]
        if arg in ('functions',):
            return 'lambda x, y: x + y'
        elif arg in ('others',):
            return ' [(1, 2), (2, 2), (3, 3)] '
    else:
        return None


Lazy = Specific['Lazy']


def parser(ast: Ast, value: str):
    if ast is None:
        return None
    name = ast[0]
    if name in Specific['Replace']:
        ret = Specific['Replace'][name]
    else:
        params = ast[1][1:]
        try:
            params = ','.join(map(gen_expr, params))
        except:
            return None
        ret = 'Flow({value}).{name}({params}){tail}'.format(value=value, name=name, params=params,
                                                            tail='.ToTuple()' if name in Lazy else '')
    if name in Specific['Addition']:
        ret = ret + ';' + Specific['Addition'][name]
    return """
def test_{}():
    {}
test_{}()""".format(name, ret, name)


N_extension_class = len('@extension_class(')
N_extension_class_name = len('@extension_class_name(')


def get_class_value(extension_head: str):
    if extension_head.startswith('@extension_class('):
        ast = _param_parser(token(extension_head[N_extension_class:-1]), meta=MetaInfo())
        if len(ast) is not 1:
            raise SyntaxError('Invalid `extension_class` usage.')
        else:
            param = ast[0]
            if len(param) is not 1:
                Warning('Might use invalid `extension_class`.')
            param = param[0]
            if param == 'list':
                return '[(1, 2), (2, 2), (3, 3)]'
            elif param == 'set':
                return '{(1, 1), (2, 2), (3, 3)}'
            elif param == 'dict':
                return '{(1, 1):(1, 1), (2, 2):(2, 2), (3, 3):(3, 3)}'
            elif param == 'tuple':
                return '((1, 2), (2, 2), (3, 3))'
            else:
                raise SyntaxWarning('[extension_class]: Cannot recognize user defined class object.')
    elif extension_head.startswith('@extension_std'):
        return '[(1, 2), (2, 3), (3, 2)]'
    elif extension_head.startswith('@extension_class_name('):
        ast = _param_parser(token(extension_head[N_extension_class_name + 1:-2]), meta=MetaInfo())
        param = ast[0][0]
        if param == 'generator':
            return '(i for i in range(3))'
        else:
            raise SyntaxError('[extension_class_name]: Cannot recognize user defined class object.')
    else:
        raise SyntaxError('Unknown extension head.')


def gen_functions(files):
    generated = []
    for codes in files:
        sources = codes.split('\n')

        Flow(sources) \
            .Enum() \
            .Map(lambda i, x: (i + 1, get_class_value(x)) if x.startswith('@extension_') else None) \
            .Filter(lambda x: x) \
            .Map(lambda i, value: parser(_parser(token(sources[i]), meta=MetaInfo(), partial=True)
                                         , value)) \
            .Filter(lambda x: x) \
            .Then(generated.extend)

    return '\n'.join(generated)


with open('test.py', 'w', encoding='utf8') as auto_gen_file:
    auto_gen_file.write("""

from linq import Flow
{tests}
""".format(tests=gen_functions(recursive_list('linq')))
                        )
print(gen_functions(recursive_list('linq')))
