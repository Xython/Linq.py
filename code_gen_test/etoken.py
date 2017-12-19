
import re
token = re.compile('|'.join(['\=','\:','\,','\*','\)','\(','[a-zA-Z_][a-zA-Z_0-9]*','[a-zA-Z_][a-zA-Z_0-9]*'])).findall
