
from Ruikowa.ObjectRegex.Node import Ref, AstParser, SeqParser, LiteralParser, CharParser, MetaInfo, DependentAstParser
try:
    from .etoken import token
except:
    from etoken import token
import re
namespace     = globals()
recurSearcher = set()
Def = AstParser([LiteralParser('def', name='\'def\''),Ref('Name'),CharParser('(', name='\'(\''),Ref('paramList'),CharParser(')', name='\')\'')], name = 'Def', toIgnore = [{},{':','(',')','def'}])
NameIg = AstParser([LiteralParser('[a-zA-Z_][a-zA-Z_0-9]*', name='\'[a-zA-Z_][a-zA-Z_0-9]*\'', isRegex = True)], name = 'NameIg')
param = AstParser([SeqParser([CharParser('*', name='\'*\'')], atmost = 1),Ref('Name'),SeqParser([CharParser(':', name='\':\''),Ref('NameIg')], atmost = 1),SeqParser([CharParser('=', name='\'=\''),LiteralParser('None', name='\'None\'')], atmost = 1)], name = 'param', toIgnore = [{NameIg},{'=','None',':'}])
paramList = AstParser([Ref('param'),SeqParser([CharParser(',', name='\',\''),Ref('param')])], name = 'paramList', toIgnore = [{},{','}])
Name = LiteralParser('[a-zA-Z_][a-zA-Z_0-9]*', name = 'Name', isRegex = True)
Def.compile(namespace, recurSearcher)
NameIg.compile(namespace, recurSearcher)
param.compile(namespace, recurSearcher)
paramList.compile(namespace, recurSearcher)
