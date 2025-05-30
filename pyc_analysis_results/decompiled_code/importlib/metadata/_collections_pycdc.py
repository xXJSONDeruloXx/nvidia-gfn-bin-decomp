# Source Generated with Decompyle++
# File: _collections.pyc (Python 3.10)

import collections

class FreezableDefaultDict(collections.defaultdict):
    """
    Often it is desirable to prevent the mutation of
    a default dict after its initial construction, such
    as to prevent mutation during iteration.

    >>> dd = FreezableDefaultDict(list)
    >>> dd[0].append('1')
    >>> dd.freeze()
    >>> dd[1]
    []
    >>> len(dd)
    1
    """
    
    def __missing__(self = None, key = None):
        return getattr(self, '_frozen', super().__missing__)(key)

    
    def freeze(self):
        
        self._frozen = lambda key = None: self.default_factory()

    __classcell__ = None


def Pair():
    '''Pair'''
    
    def parse(cls, text):
        pass
    # WARNING: Decompyle incomplete

    parse = classmethod(parse)

Pair = <NODE:27>(Pair, 'Pair', collections.namedtuple('Pair', 'name value'))
