# Source Generated with Decompyle++
# File: fnmatch.pyc (Python 3.10)

'''Filename matching with shell patterns.

fnmatch(FILENAME, PATTERN) matches according to the local convention.
fnmatchcase(FILENAME, PATTERN) always takes case in account.

The functions operate by translating the pattern into a regular
expression.  They cache the compiled regular expressions for speed.

The function translate(PATTERN) returns a regular expression
corresponding to PATTERN.  (It does not compile it.)
'''
import os
import posixpath
import re
import functools
__all__ = [
    'filter',
    'fnmatch',
    'fnmatchcase',
    'translate']
from itertools import count
_nextgroupnum = count().__next__
del count

def fnmatch(name, pat):
    """Test whether FILENAME matches PATTERN.

    Patterns are Unix shell style:

    *       matches everything
    ?       matches any single character
    [seq]   matches any character in seq
    [!seq]  matches any char not in seq

    An initial period in FILENAME is not special.
    Both FILENAME and PATTERN are first case-normalized
    if the operating system requires it.
    If you don't want this, use fnmatchcase(FILENAME, PATTERN).
    """
    name = os.path.normcase(name)
    pat = os.path.normcase(pat)
    return fnmatchcase(name, pat)


def _compile_pattern(pat):
    if isinstance(pat, bytes):
        pat_str = str(pat, 'ISO-8859-1')
        res_str = translate(pat_str)
        res = bytes(res_str, 'ISO-8859-1')
    else:
        res = translate(pat)
    return re.compile(res).match

_compile_pattern = functools.lru_cache(256, True, **('maxsize', 'typed'))(_compile_pattern)

def filter(names, pat):
    '''Construct a list from those elements of the iterable NAMES that match PAT.'''
    result = []
    pat = os.path.normcase(pat)
    match = _compile_pattern(pat)
    if os.path is posixpath:
        for name in names:
            if match(name):
                result.append(name)
        return result
    for name in None:
        if match(os.path.normcase(name)):
            result.append(name)
    return result


def fnmatchcase(name, pat):
    """Test whether FILENAME matches PATTERN, including case.

    This is a version of fnmatch() which doesn't case-normalize
    its arguments.
    """
    match = _compile_pattern(pat)
    return match(name) is not None


def translate(pat):
    '''Translate a shell PATTERN to a regular expression.

    There is no way to quote meta-characters.
    '''
    STAR = object()
    res = []
    add = res.append
    i = 0
    n = len(pat)
# WARNING: Decompyle incomplete

