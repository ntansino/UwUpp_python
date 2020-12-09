# Lexer for UwU++ in Python

import re
from ply import lex

reserved = {
    'iws'     : 'IWS',
    'nyaa'    : 'NYAA',
    'gweatew twan' : 'GWEATEW TWAN',
    'wess twan' : 'WESS TWAN',
    'eqwall twoo' : 'EQWALL TWOO',
    'notices' : 'NOTICES',
    'ewse' : 'EWSE'
    'OwO' : 'OWO',
    'stawp' : 'STAWP',
    'pwus' : 'PWUS',
    'twimes' : 'TWIMES',
    'diwide' : 'DIWIDE',
    'nuzzels' : 'NUZZELS',
    'wetuwn' : 'WETUWN',
    'decwawe' : 'DECWAWE',
    'nowt' : 'NOWT'
}