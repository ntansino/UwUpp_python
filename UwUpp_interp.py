#!/usr/bin/env python
# UwUpp interpreter

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
    # parse command line args
    aparser = ArgumentParser()
    aparser.add_argument('input')

    args = vars(aparser.parse_args())

    f = open(args['input'], 'r')
    input_stream = f.read()
    f.close()

    # execute interpreter
    interp(input_stream=input_stream)

