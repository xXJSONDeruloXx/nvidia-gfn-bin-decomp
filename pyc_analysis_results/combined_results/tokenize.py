# Source Generated with Decompyle++
# File: tokenize.pyc (Python 3.10)

__doc__ = 'Tokenization help for Python programs.\n\ntokenize(readline) is a generator that breaks a stream of bytes into\nPython tokens.  It decodes the bytes according to PEP-0263 for\ndetermining source file encoding.\n\nIt accepts a readline-like method which is called repeatedly to get the\nnext line of input (or b"" for EOF).  It generates 5-tuples with these\nmembers:\n\n    the token type (see token.py)\n    the token (a string)\n    the starting (row, column) indices of the token (a 2-tuple of ints)\n    the ending (row, column) indices of the token (a 2-tuple of ints)\n    the original line (string)\n\nIt is designed to match the working of the Python tokenizer exactly, except\nthat it produces COMMENT tokens for comments and gives type OP for all\noperators.  Additionally, all token lists start with an ENCODING token\nwhich tells you which encoding was used to decode the bytes stream.\n'
__author__ = 'Ka-Ping Yee <ping@lfw.org>'
__credits__ = 'GvR, ESR, Tim Peters, Thomas Wouters, Fred Drake, Skip Montanaro, Raymond Hettinger, Trent Nelson, Michael Foord'
from builtins import open as _builtin_open
from codecs import lookup, BOM_UTF8
import collections
import functools
from io import TextIOWrapper
import itertools as _itertools
import re
import sys
from token import *
from token import EXACT_TOKEN_TYPES
cookie_re = re.compile('^[ \\t\\f]*#.*?coding[:=][ \\t]*([-\\w.]+)', re.ASCII)
blank_re = re.compile(b'^[ \\t\\f]*(?:[#\\r\\n]|$)', re.ASCII)
import token
__all__ = token.__all__ + [
    'tokenize',
    'generate_tokens',
    'detect_encoding',
    'untokenize',
    'TokenInfo']
del token

def TokenInfo():
    '''TokenInfo'''
    
    def __repr__(self):
        annotated_type = '%d (%s)' % (self.type, tok_name[self.type])
        return 'TokenInfo(type=%s, string=%r, start=%r, end=%r, line=%r)' % self._replace(annotated_type, **('type',))

    
    def exact_type(self):
        if self.type == OP and self.string in EXACT_TOKEN_TYPES:
            return EXACT_TOKEN_TYPES[self.string]
        return None.type

    exact_type = property(exact_type)

TokenInfo = <NODE:27>(TokenInfo, 'TokenInfo', collections.namedtuple('TokenInfo', 'type string start end line'))

def group(*choices):
    return '(' + '|'.join(choices) + ')'


def any(*choices):
    pass
# WARNING: Decompyle incomplete


def maybe(*choices):
    pass
# WARNING: Decompyle incomplete

Whitespace = '[ \\f\\t]*'
Comment = '#[^\\r\\n]*'
Ignore = Whitespace + any('\\\\\\r?\\n' + Whitespace) + maybe(Comment)
Name = '\\w+'
Hexnumber = '0[xX](?:_?[0-9a-fA-F])+'
Binnumber = '0[bB](?:_?[01])+'
Octnumber = '0[oO](?:_?[0-7])+'
Decnumber = '(?:0(?:_?0)*|[1-9](?:_?[0-9])*)'
Intnumber = group(Hexnumber, Binnumber, Octnumber, Decnumber)
Exponent = '[eE][-+]?[0-9](?:_?[0-9])*'
Pointfloat = group('[0-9](?:_?[0-9])*\\.(?:[0-9](?:_?[0-9])*)?', '\\.[0-9](?:_?[0-9])*') + maybe(Exponent)
Expfloat = '[0-9](?:_?[0-9])*' + Exponent
Floatnumber = group(Pointfloat, Expfloat)
Imagnumber = group('[0-9](?:_?[0-9])*[jJ]', Floatnumber + '[jJ]')
Number = group(Imagnumber, Floatnumber, Intnumber)

def _all_string_prefixes():
    _valid_string_prefixes = [
        'b',
        'r',
        'u',
        'f',
        'br',
        'fr']
    result = {
        ''}
# WARNING: Decompyle incomplete


def _compile(expr):
    return re.compile(expr, re.UNICODE)

_compile = functools.lru_cache(_compile)
# WARNING: Decompyle incomplete
