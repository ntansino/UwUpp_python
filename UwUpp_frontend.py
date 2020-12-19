# Specification of the UwU++ Frontend

from ply import yacc
from UwUpp_lex import tokens, lexer, is_ID
from UwUpp_state import state

#########################################################################
# set precedence and associativity
# NOTE: all operators need to have tokens
#       so that we can put them into the precedence table
precedence = (
              ('left', 'GWEATEW_TWAN', 'EQWALL_TWOO', 'WESS_TWAN'),
              ('left', 'PWUS', 'MINWUS'),
              ('left', 'TWIMES', 'DIWIDE'),
              ('right', 'UMINUS', 'NOT')
             )

#########################################################################
# grammar rules with embedded actions
#########################################################################
def p_prog(p):
    '''
    program : stmt_list
    '''
    state.AST = p[1]

#########################################################################
def p_stmt_list(p):
    '''
    stmt_list : stmt stmt_list
              | empty
    '''
    if (len(p) == 3):
        p[0] = ('seq', p[1], p[2])
    elif (len(p) == 2):
        p[0] = p[1]

#########################################################################
def p_stmt(p):
    '''
    stmt : DECWAWE '*' ID '(' opt_formal_args ')' '*' stmt
         | DECWAWE ID opt_init
         | ID '=' exp
         | NUZZELS exp 
         | ID '(' opt_actual_args ')' 
         | WETUWN opt_exp 
         | OWO '*' exp '*' stmt STAWP
         | '*' NOTICES exp '*' stmt opt_ewse STAWP
         | '{' stmt_list '}'
    '''
    if p[1] == 'decwawe' and p[2] == '*' and p[4] == '(':
        p[0] = ('fundecw', p[3], p[5], p[8])
    elif p[1] == 'decwawe':
        p[0] = ('decwawe', p[2], p[3])
    elif is_ID(p[1]) and p[2] == '=':
        p[0] = ('assign', p[1], p[3])
    elif p[1] == 'nuzzels':
        p[0] = ('nuzzels', p[2])
    elif is_ID(p[1]) and p[2] == '(':
        p[0] = ('callstmt', p[1], p[3])
    elif p[1] == 'wetuwn':
        p[0] = ('wetuwn', p[2])
    elif p[1] == 'owo':
        p[0] = ('owo', p[3], p[5], p[6])
    elif p[1] == '*' and p[2] == 'notices':
        p[0] = ('notices', p[3], p[5], p[6], p[7])
    elif p[1] == '{':
        p[0] = ('block', p[2])
    else:
        raise ValueError("unexpected symbol {}".format(p[1]))

#########################################################################
def p_opt_formal_args(p):
    '''
    opt_formal_args : formal_args
                    | empty
    '''
    p[0] = p[1]

#########################################################################
def p_formal_args(p):
    '''
    formal_args : ID ',' formal_args
                | ID
    '''
    if (len(p) == 4):
        p[0] = ('seq', ('id', p[1]), p[3])
    else:
        p[0] = ('seq', ('id', p[1]), ('nil',))

#########################################################################
def p_opt_init(p):
    '''
    opt_init : '=' exp
             | empty
    '''
    if p[1] == '=':
        p[0] = p[2]
    else:
        p[0] = p[1]

#########################################################################
def p_opt_actual_args(p):
    '''
    opt_actual_args : actual_args
                    | empty
    '''
    p[0] = p[1]

#########################################################################
def p_actual_args(p):
    '''
    actual_args : exp ',' actual_args
                | exp
    '''
    if (len(p) == 4):
        p[0] = ('seq', p[1], p[3])
    else:
        p[0] = ('seq', p[1], ('nil',))

#########################################################################
def p_opt_exp(p):
    '''
    opt_exp : exp
            | empty
    '''
    p[0] = p[1]

#########################################################################
def p_opt_ewse(p):
    '''
    opt_ewse : EWSE stmt
             | empty
    '''
    if p[1] == 'ewse':
        p[0] = p[2]
    else:
        p[0] = p[1]

#########################################################################
def p_binop_exp(p):
    '''
    exp : exp PWUS exp
        | exp MINWUS exp
        | exp TWIMES exp
        | exp DIWIDE exp
        | exp GWEATEW_TWAN exp
        | exp EQWALL_TWOO exp
        | exp WESS_TWAN exp
    '''
    p[0] = (p[2], p[1], p[3])

#########################################################################
def p_integer_exp(p):
    '''
    exp : INTEGER
    '''
    p[0] = ('integer', int(p[1]))

#########################################################################
def p_wisten_exp(p):
    '''
    exp : WISTEN '(' ')'
    '''
    p[0] = (p[1], )

#########################################################################
def p_string_exp(p):
    '''
    exp : '"' STRING '"'
    '''
    p[0] = ('string', p[1])

#########################################################################
def p_id_exp(p):
    '''
    exp : ID
    '''
    p[0] = ('id', p[1])

#########################################################################
def p_call_exp(p):
    '''
    exp : ID '(' opt_actual_args ')'
    '''
    p[0] = ('callexp', p[1], p[3])

#########################################################################
def p_paren_exp(p):
    '''
    exp : '(' exp ')'
    '''
    p[0] = ('paren', p[2])

#########################################################################
def p_uminus_exp(p):
    '''
    exp : MINWUS exp %prec UMINUS
    '''
    p[0] = ('uminus', p[2])

#########################################################################
def p_not_exp(p):
    '''
    exp : NOT exp
    '''
    p[0] = ('not', p[2])

#########################################################################
def p_empty(p):
    '''
    empty :
    '''
    p[0] = ('nil',)

#########################################################################
def p_error(t):
    print("Syntax error at '%s'" % t.value)

#########################################################################
# build the parser
#########################################################################
parser = yacc.yacc(debug=False,tabmodule='UwUppparsetab')