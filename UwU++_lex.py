# Lexer for UwU++ in Python

import re
from ply import lex

reserved = {
    'iws'          : 'IWS',
    'nyaa'         : 'NYAA',
    'notices'      : 'NOTICES',
    'ewse'         : 'EWSE',
    'OwO'          : 'OWO',
    'stawp'        : 'STAWP',
    'nuzzels'      : 'NUZZELS',
    'wetuwn'       : 'WETUWN',
    'decwawe'      : 'DECWAWE',
    'nowt'         : 'NOWT'
}

literals = [',',';','=','(',')','{','}']

tokens = [
          'PLUS','MINUS','TIMES','DIVIDE',
          'GT', 'EQ','LT', 
          'INTEGER','ID',
          ] + list(reserved.values())

t_PLUS    = r'pwus'
t_MINUS   = r'miwus'
t_TIMES   = r'TWIMES'
t_DIVIDE  = r'DIWIDE'
t_GT      = r'GWEATEW TWAN'
t_EQ      = r'EQWALL TWOO'
t_LT      = r'WESS TWAN'

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
    'UwU'
    pass

def t_NEWLINE(t):
    r'\n'
    pass

def t_error(t):
    print("Illegal character %s" % t.value[0])
    t.lexer.skip(1)

# Build the lexer
lexer = lex.lex(debug=0)