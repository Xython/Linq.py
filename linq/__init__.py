
__all__ = ['Flow', 'extension_class', 'extension_std', 'generator_type',
           'destruct_func', 'is_to_destruct', 'List', 'Dict', 'Set', 'Generator']
        

from linq.core.flow import Flow, extension_class, extension_std

from linq.core.utils import (destruct_func, is_to_destruct)

from linq.standard import src
from linq.standard import general, list as List , dict as Dict, set as Set, generator as Generator

generator_type = Generator._gen_cls

try:
    from typing import List as _List, Dict as _Dict, Set as _Set, Generator as _Generator
except:
    class TypingObj:
        def __getitem__(self, item):
            return ...
    _List = TypingObj()
    _Set = TypingObj()
    _Dict = TypingObj()
    _Generator = TypingObj()
    
class TypingCompat:

    def __init__(self, module, typing_object):
        self._typing_object = typing_object

        for name, obj in module.__dict__.items():
            if not name.startswith("__"):
                setattr(self, name, obj)


    def __getitem__(self, item):
        return self._typing_object[item]

exec(
"""
List = TypingCompat(List, _List)
Dict = TypingCompat(Dict, _Dict)
Set  = TypingCompat(Set, _Set)
Generator = TypingCompat(Generator, _Generator)
""")



