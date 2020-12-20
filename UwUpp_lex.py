# Lexer for UwU++ in Python

import re
from ply import lex

reserved = {
    'notices'      : 'NOTICES',
    'ewse'         : 'EWSE',
    'owo'          : 'OWO',
    'stawp'        : 'STAWP',
    'nuzzels'      : 'NUZZELS',
    'wetuwn'       : 'WETUWN',
    'decwawe'      : 'DECWAWE',
    'not'          : 'NOT',
    'wisten'       : 'WISTEN',
    'pwus'         : 'PWUS',
    'minwus'       : 'MINWUS',
    'twimes'       : 'TWIMES',
    'diwide'       : 'DIWIDE',
    'gweatew_twan' : 'GWEATEW_TWAN',
    'eqwall_twoo'  : 'EQWALL_TWOO',
    'wess_twan'    : 'WESS_TWAN'
}

literals = [',',';','=','(',')','{','}','*','\"']

tokens = [ 'INTEGER','ID', 'STRING'
          ] + list(reserved.values())

t_ignore = ' \t'

def t_ID(t):
    r'[a-zA-Z_][a-zA-Z_0-9]*'
    t.type = reserved.get(t.value,'ID')    # Check for reserved words
    return t

def is_ID(s):
    m = re.match(r'[a-zA-Z_][a-zA-Z_0-9]*', s)
    
    if s in list(reserved.keys()):
        return False
    elif m and len(m.group(0)) == len(s):
        return True
    else:
        return False

def t_INTEGER(t):
    r'[0-9]+'
    return t

def t_COMMENT(t):
    r'/UwU.*'
    pass

def t_NEWLINE(t):
    r'\n'
    pass

def t_error(t):
    print("Illegal character %s" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex(debug=0)