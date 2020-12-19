# A tree walker to interpret Cuppa3 programs

from UwUpp_state import state
from grammar_stuff import assert_match

#########################################################################
# Use the exception mechanism to return values from function calls

class ReturnValue(Exception):

    def __init__(self, value):
        self.value = value

    def __str__(self):
        return(repr(self.value))

#########################################################################
def len_seq(seq_list):

    if seq_list[0] == 'nil':
        return 0

    elif seq_list[0] == 'seq':
        # unpack the seq node
        (SEQ, p1, p2) = seq_list

        return 1 + len_seq(p2)

    else:
            raise ValueError("unknown node type: {}".format(seq_list[0]))

#########################################################################
def eval_actual_args(args):

    if args[0] == 'nil':
        return ('nil',)

    elif args[0] == 'seq':
        # unpack the seq node
        (SEQ, p1, p2) = args

        val = walk(p1)

        return ('seq', val, eval_actual_args(p2))

    else:
        raise ValueError("unknown node type: {}".format(args[0]))

#########################################################################
def declare_formal_args(formal_args, actual_val_args):

    if len_seq(actual_val_args) != len_seq(formal_args):
        raise ValueError("actual and formal argument lists do not match")

    if formal_args[0] == 'nil':
        return

    # unpack the args
    (SEQ, (ID, sym), p1) = formal_args
    (SEQ, val, p2) = actual_val_args

    # declare the variable
    state.symbol_table.declare_scalar(sym, val)

    declare_formal_args(p1, p2)

#########################################################################
def handle_call(name, actual_arglist):

    (type, val) = state.symbol_table.lookup_sym(name)

    if type != 'function':
        raise ValueError("{} is not a function".format(name))

    # unpack the funval tuple
    (FUNVAL, formal_arglist, body, context) = val

    if len_seq(formal_arglist) != len_seq(actual_arglist):
        raise ValueError("function {} expects {} arguments".format(sym, len_seq(formal_arglist)))

    # set up the environment for static scoping and then execute the function
    actual_val_args = eval_actual_args(actual_arglist)   # evaluate actuals in current symtab
    save_symtab = state.symbol_table.get_config()        # save current symtab
    state.symbol_table.set_config(context)               # make function context current symtab
    state.symbol_table.push_scope()                      # push new function scope
    declare_formal_args(formal_arglist, actual_val_args) # declare formals in function scope

    return_value = None
    try:
        walk(body)                                       # execute the function
    except ReturnValue as val:
        return_value = val.value

    # NOTE: popping the function scope is not necessary because we
    # are restoring the original symtab configuration
    state.symbol_table.set_config(save_symtab)           # restore original symtab config

    return return_value

#########################################################################
# node functions
#########################################################################
def seq(node):

    (SEQ, stmt, stmt_list) = node
    assert_match(SEQ, 'seq')

    walk(stmt)
    walk(stmt_list)

#########################################################################
def nil(node):

    (NIL,) = node
    assert_match(NIL, 'nil')

    # do nothing!
    pass

#########################################################################
def fundecw_stmt(node):

    try: # try the fundecl pattern without arglist
        (FUNDECW, name, (NIL,), body) = node
        assert_match(FUNDECW, 'fundecw')
        assert_match(NIL, 'nil')

    except ValueError: # try fundecl with arglist
        (FUNDECW, name, arglist, body) = node
        assert_match(FUNDECW, 'fundecw')

        context = state.symbol_table.get_config()
        funval = ('funval', arglist, body, context)
        state.symbol_table.declare_fun(name, funval)

    else: # fundecl pattern matched
        # no arglist is present
        context = state.symbol_table.get_config()
        funval = ('funval', ('nil',), body, context)
        state.symbol_table.declare_fun(name, funval)


#########################################################################
def decwawe_stmt(node):

    try: # try the declare pattern without initializer
        (DECWAWE, name, (NIL,)) = node
        assert_match(DECWAWE, 'decwawe')
        assert_match(NIL, 'nil')

    except ValueError: # try declare with initializer
        (DECWAWE, name, init_val) = node
        assert_match(DECWAWE, 'decwawe')

        value = walk(init_val)
        state.symbol_table.declare_scalar(name, value)

    else: # declare pattern matched
        # when no initializer is present we init with the value 0
        state.symbol_table.declare_scalar(name, 0)

#########################################################################
def assign_stmt(node):

    (ASSIGN, name, exp) = node
    assert_match(ASSIGN, 'assign')

    value = walk(exp)
    state.symbol_table.update_sym(name, ('scalar', value))

#########################################################################
def wisten_stmt(node):

    (WISTEN, ) = node
    assert_match(WISTEN, 'wisten')

    s = input("( ͡° ͜ʖ ͡°) *UwU wats dis?* ( ͡° ͜ʖ ͡°) ")

    try:
        value = int(s)
    except ValueError:
        raise ValueError("Ewwow! expected a vawue")
    
    return value
    #state.symbol_table.update_sym(name, ('scalar', value))

#########################################################################
def nuzzels_stmt(node):

    (NUZZELS, exp) = node
    assert_match(NUZZELS, 'nuzzels')

    value = walk(exp)
    print("> {}".format(value))

#########################################################################
def call_stmt(node):

    (CALLSTMT, name, actual_args) = node
    assert_match(CALLSTMT, 'callstmt')

    handle_call(name, actual_args)

#########################################################################
def wetuwn_stmt(node):
    # if a return value exists the return stmt will record it
    # in the state object

    try: # try return without exp
        (WETUWN, (NIL,)) = node
        assert_match(WETUWN, 'wetuwn')
        assert_match(NIL, 'nil')

    except ValueError: # return with exp
        (WETUWN, exp) = node
        assert_match(WETUWN, 'wetuwn')

        value = walk(exp)
        raise ReturnValue(value)

    else: # return without exp
        raise ReturnValue(None)

#########################################################################
def owo_stmt(node):

    (OWO, cond, body, STAWP) = node
    assert_match(OWO, 'owo')
    assert_match(STAWP, 'stawp')

    value = walk(cond)
    while value != 0:
        walk(body)
        value = walk(cond)

#########################################################################
def notices_stmt(node):

    try: # try the if-then pattern
        (NOTICES, cond, then_stmt, (NIL,), STAWP) = node
        assert_match(NOTICES, 'notices')
        assert_match(STAWP, 'stawp')
        assert_match(NIL, 'nil')

    except ValueError: # if-then pattern didn't match
        (NOTICES, cond, then_stmt, else_stmt, STAWP) = node
        assert_match(NOTICES, 'notices')

        value = walk(cond)

        if value != 0:
            walk(then_stmt)
        else:
            walk(else_stmt)
            
        assert_match(STAWP, 'stawp')

    else: # if-then pattern matched
        value = walk(cond)
        if value != 0:
            walk(then_stmt)

#########################################################################
def block_stmt(node):

    (BLOCK, stmt_list) = node
    assert_match(BLOCK, 'block')

    state.symbol_table.push_scope()
    walk(stmt_list)
    state.symbol_table.pop_scope()

#########################################################################
def pwus_exp(node):

    (PWUS, c1, c2) = node
    assert_match(PWUS, 'pwus')

    v1 = walk(c1)
    v2 = walk(c2)

    return v1 + v2

#########################################################################
def minwus_exp(node):

    (MINWUS, c1, c2) = node
    assert_match(MINWUS, 'minwus')

    v1 = walk(c1)
    v2 = walk(c2)

    return v1 - v2

#########################################################################
def twimes_exp(node):

    (TWIMES,c1,c2) = node
    assert_match(TWIMES, 'twimes')

    v1 = walk(c1)
    v2 = walk(c2)

    return v1 * v2

#########################################################################
def diwide_exp(node):

    (DIWIDE,c1,c2) = node
    assert_match(DIWIDE, 'diwide')

    v1 = walk(c1)
    v2 = walk(c2)

    return v1 // v2

#########################################################################
def gweatew_twan_exp(node):

    (GWEATEW_TWAN,c1,c2) = node
    assert_match(GWEATEW_TWAN, 'gweatew_twan')

    v1 = walk(c1)
    v2 = walk(c2)

    return 1 if v1 > v2 else 0

#########################################################################
def eqwall_twoo_exp(node):

    (EQWALL_TWOO, c1, c2) = node
    assert_match(EQWALL_TWOO, 'eqwall_twoo')

    v1 = walk(c1)
    v2 = walk(c2)

    return 1 if v1 == v2 else 0

#########################################################################
def wess_twan_exp(node):

    (WESS_TWAN, c1, c2) = node
    assert_match(WESS_TWAN, 'wess_twan')

    v1 = walk(c1)
    v2 = walk(c2)

    return 1 if v1 <= v2 else 0

#########################################################################
def integer_exp(node):

    (INTEGER, value) = node
    assert_match(INTEGER, 'integer')

    return value

#########################################################################
def id_exp(node):

    (ID, name) = node
    assert_match(ID, 'id')

    (type, val) = state.symbol_table.lookup_sym(name)

    if type != 'scalar':
        raise ValueError("{} is not a scalar".format(name))

    return val

#########################################################################
def call_exp(node):
    # call_exp works just like call_stmt with the exception
    # that we have to pass back a return value

    (CALLEXP, name, args) = node
    assert_match(CALLEXP, 'callexp')

    return_value = handle_call(name, args)

    if return_value is None:
        raise ValueError("No return value from function {}".format(name))

    return return_value

#########################################################################
def uminus_exp(node):

    (UMINUS, exp) = node
    assert_match(UMINUS, 'uminus')

    val = walk(exp)
    return - val

#########################################################################
def not_exp(node):

    (NOT, exp) = node
    assert_match(NOT, 'not')

    val = walk(exp)
    return 0 if val != 0 else 1

#########################################################################
def paren_exp(node):

    (PAREN, exp) = node
    assert_match(PAREN, 'paren')

    # return the value of the parenthesized expression
    return walk(exp)

#########################################################################
# walk
#########################################################################
def walk(node):
    # node format: (TYPE, [child1[, child2[, ...]]])
    type = node[0]

    if type in dispatch_dict:
        node_function = dispatch_dict[type]
        return node_function(node)
    else:
        raise ValueError("walk: unknown tree node type: " + type)

# a dictionary to associate tree nodes with node functions
dispatch_dict = {
    'seq'          : seq,
    'nil'          : nil,
    'fundecw'      : fundecw_stmt,
    'decwawe'      : decwawe_stmt,
    'assign'       : assign_stmt,
    'wisten'       : wisten_stmt,
    'nuzzels'      : nuzzels_stmt,
    'callstmt'     : call_stmt,
    'wetuwn'       : wetuwn_stmt,
    'owo'          : owo_stmt,
    'notices'      : notices_stmt,
    'block'        : block_stmt,
    'id'           : id_exp,
    'integer'      : integer_exp,
    'callexp'      : call_exp,
    'paren'        : paren_exp,
    'pwus'         : pwus_exp,
    'minwus'       : minwus_exp,
    'twimes'       : twimes_exp,
    'diwide'       : diwide_exp,
    'gweatew_twan' : gweatew_twan_exp,
    'eqwall_twoo'  : eqwall_twoo_exp,
    'wess_twan'    : wess_twan_exp,
    'uminus'       : uminus_exp,
    'not'          : not_exp
}
