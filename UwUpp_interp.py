#!/usr/bin/env python
# Cuppa3 interpreter

from argparse import ArgumentParser
from UwUpp_lex import lexer
from UwUpp_frontend import parser
from UwUpp_state import state
from UwUpp_interp_walk import walk
from grammar_stuff import dump_AST

def interp(input_stream):

    # initialize the state object
    state.initialize()

    # build the AST
    parser.parse(input_stream, lexer=lexer)

    # walk the AST
    #dump_AST(state.AST)
    walk(state.AST)

if __name__ == "__main__":
    add = \
    """
    decwawe *add(a)* {
        decwawe x = 1
        decwawe y = x pwus a
        wetuwn y
    }
    nuzzels(add(5))
    """
    interp(add)

    test_wisten = \
    """
    decwawe input
    input = wisten
    nuzzels(input)
    """
    #interp(test_wisten)

    notices = \
    """
    decwawe x = 100000
    decwawe y = 54321
    * notices x wess_twan y *
        nuzzels(x)
    ewse
        nuzzels(y)
        stawp
    """
    interp(notices)

    notices = \
    """
    decwawe x = 1000
    decwawe y = 54321
    * notices x wess_twan y *
        nuzzels(x)
        stawp
    """
    interp(notices)

    binop = \
    """
    decwawe x = 10
    decwawe y = 122
    decwawe z = x pwus y
    nuzzels(z)

    decwawe a = 150
    decwawe b = 50
    decwawe c = a minwus b
    nuzzels(c)

    decwawe d = 10
    decwawe e = 5
    decwawe f = d twimes e
    nuzzels(f)

    decwawe m = 1000
    decwawe n = 20
    decwawe o = m diwide n
    nuzzels(o)
    """
    interp(binop)

    OwO = \
    """
    decwawe x = 1000
    decwawe y = 54321

    owo * x wess_twan y *{
        nuzzels(x)
        x = x twimes 2
        nuzzels(y)}
        stawp
    """
    print("OwO:")
    interp(OwO)
    

    test_all = \
    """
    decwawe input = wisten
    decwawe *math(a)* {
        decwawe x = 10
        decwawe y = 122
        decwawe z = x pwus y
        nuzzels(z)

        decwawe b = 50
        decwawe c = a minwus b
        nuzzels(c)

        decwawe d = 10
        decwawe e = 5
        decwawe f = d twimes e
        nuzzels(f)

        decwawe m = 1000
        decwawe n = 20
        decwawe o = m diwide n
        wetuwn o
    }
    math(input)
    decwawe y = 122
    * notices input wess_twan y *
        nuzzels(input)
    ewse
        nuzzels(y)
    stawp

    decwawe x = 200
    owo * x gweatew_twan y *{
        nuzzels(x)
        x = x diwide 2
        nuzzels(y)
        }
        stawp
    
    * notices 10 eqwall_twoo 10 *
        nuzzels(10)
        stawp
    
    * notices 20 eqwall_twoo 10 *
        nuzzels(10)
    ewse
        nuzzels(20)
        stawp
    """
    #interp(test_all)

    negative = \
        """
        decwawe x = 200
        decwawe y = minwus 200
        nuzzels(y)
        nuzzels(x minwus y)
        nuzzels(x minwus minwus 20)
        """
    print("negative:")
    interp(negative)
    
"""     # parse command line args
    aparser = ArgumentParser()
    aparser.add_argument('input')

    args = vars(aparser.parse_args())

    f = open(args['input'], 'r')
    input_stream = f.read()
    f.close()

    # execute interpreter
    interp(input_stream=input_stream) """

