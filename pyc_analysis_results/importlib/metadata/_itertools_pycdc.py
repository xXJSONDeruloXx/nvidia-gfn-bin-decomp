# Source Generated with Decompyle++
# File: _itertools.pyc (Python 3.10)

from itertools import filterfalse

def unique_everseen(iterable, key = (None,)):
    '''List unique elements, preserving order. Remember all elements ever seen.'''
    seen = set()
    seen_add = seen.add
    if key is None:
        for element in filterfalse(seen.__contains__, iterable):
            seen_add(element)
            yield element
        return None
    for element in None:
        k = key(element)
        if k not in seen:
            seen_add(k)
            yield element

