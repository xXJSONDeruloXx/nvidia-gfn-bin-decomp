# Source Generated with Decompyle++
# File: vdict.pyc (Python 3.10)

import sys
from collections import Counter
if sys.version_info[0] >= 3:
    _iter_values = 'values'
    _range = range
    _string_type = str
    from collections.abc import abc as _c
    
    class _kView(_c.KeysView):
        
        def __iter__(self):
            return self._mapping.iterkeys()


    
    class _vView(_c.ValuesView):
        
        def __iter__(self):
            return self._mapping.itervalues()


    
    class _iView(_c.ItemsView):
        
        def __iter__(self):
            return self._mapping.iteritems()


else:
    _iter_values = 'itervalues'
    _range = xrange
    _string_type = basestring
    
    _kView = lambda x: list(x.iterkeys())
    
    _vView = lambda x: list(x.itervalues())
    
    _iView = lambda x: list(x.iteritems())

class VDFDict(dict):
    
    def __init__(self, data = (None,)):
        """
        This is a dictionary that supports duplicate keys and preserves insert order

        ``data`` can be a ``dict``, or a sequence of key-value tuples. (e.g. ``[('key', 'value'),..]``)
        The only supported type for key is str.

        Get/set duplicates is done by tuples ``(index, key)``, where index is the duplicate index
        for the specified key. (e.g. ``(0, 'key')``, ``(1, 'key')``...)

        When the ``key`` is ``str``, instead of tuple, set will create a duplicate and get will look up ``(0, key)``
        """
        self._VDFDict__omap = []
        self._VDFDict__kcount = Counter()
        if data is not None:
            if not isinstance(data, (list, dict)):
                raise ValueError('Expected data to be list of pairs or dict, got %s' % type(data))
            None.update(data)
            return None

    
    def __repr__(self):
        out = '%s(' % self.__class__.__name__
        out += '%s)' % repr(list(self.iteritems()))
        return out

    
    def __len__(self):
        return len(self._VDFDict__omap)

    
    def _verify_key_tuple(self, key):
        if len(key) != 2:
            raise ValueError('Expected key tuple length to be 2, got %d' % len(key))
        if not None(key[0], int):
            raise TypeError('Key index should be an int')
        if not None(key[1], _string_type):
            raise TypeError('Key value should be a str')

    
    def _normalize_key(self, key):
        if isinstance(key, _string_type):
            key = (0, key)
            return key
        if None(key, tuple):
            self._verify_key_tuple(key)
            return key
        raise None('Expected key to be a str or tuple, got %s' % type(key))

    
    def __setitem__(self = None, key = None, value = None):
        if isinstance(key, _string_type):
            key = (self._VDFDict__kcount[key], key)
            self._VDFDict__omap.append(key)
        elif isinstance(key, tuple):
            self._verify_key_tuple(key)
            if key not in self:
                raise KeyError("%s doesn't exist" % repr(key))
        raise TypeError('Expected either a str or tuple for key')
        super(VDFDict, self).__setitem__(key, value)
        self._VDFDict__kcount[key[1]] += 1

    
    def __getitem__(self = None, key = None):
        return super(VDFDict, self).__getitem__(self._normalize_key(key))

    
    def __delitem__(self = None, key = None):
        key = self._normalize_key(key)
        result = super(VDFDict, self).__delitem__(key)
        start_idx = self._VDFDict__omap.index(key)
        del self._VDFDict__omap[start_idx]
        (dup_idx, skey) = key
        self._VDFDict__kcount[skey] -= 1
        tail_count = self._VDFDict__kcount[skey] - dup_idx
        if tail_count > 0:
            for idx in _range(start_idx, len(self._VDFDict__omap)):
                if self._VDFDict__omap[idx][1] == skey:
                    oldkey = self._VDFDict__omap[idx]
                    newkey = (dup_idx, skey)
                    super(VDFDict, self).__setitem__(newkey, self[oldkey])
                    super(VDFDict, self).__delitem__(oldkey)
                    self._VDFDict__omap[idx] = newkey
                    dup_idx += 1
                    tail_count -= 1
                    if tail_count == 0:
                        pass
                    
                    if self._VDFDict__kcount[skey] == 0:
                        del self._VDFDict__kcount[skey]
        return result

    
    def __iter__(self):
        return iter(self.iterkeys())

    
    def __contains__(self = None, key = None):
        return super(VDFDict, self).__contains__(self._normalize_key(key))

    
    def __eq__(self, other):
        if isinstance(other, VDFDict):
            return list(self.items()) == list(other.items())

    
    def __ne__(self, other):
        return not self.__eq__(other)

    
    def clear(self = None):
        super(VDFDict, self).clear()
        self._VDFDict__kcount.clear()
        self._VDFDict__omap = list()

    
    def get(self = None, key = None, *args):
        pass
    # WARNING: Decompyle incomplete

    
    def setdefault(self, key, default = (None,)):
        if key not in self:
            self.__setitem__(key, default)
        return self.__getitem__(key)

    
    def pop(self, key):
        key = self._normalize_key(key)
        value = self.__getitem__(key)
        self.__delitem__(key)
        return value

    
    def popitem(self):
        if not self._VDFDict__omap:
            raise KeyError('VDFDict is empty')
        key = None._VDFDict__omap[-1]
        return (key[1], self.pop(key))

    
    def update(self, data = (None,), **kwargs):
        if isinstance(data, dict):
            data = data.items()
        elif not isinstance(data, list):
            raise TypeError('Expected data to be a list or dict, got %s' % type(data))
        for key, value in data:
            self.__setitem__(key, value)

    
    def iterkeys(self):
        return (lambda .0: for key in .0:
key[1])(self._VDFDict__omap)

    
    def keys(self):
        return _kView(self)

    
    def itervalues(self):
        return (lambda .0 = None: for key in .0:
self[key])(self._VDFDict__omap)

    
    def values(self):
        return _vView(self)

    
    def iteritems(self):
        return (lambda .0 = None: for key in .0:
(key[1], self[key]))(self._VDFDict__omap)

    
    def items(self):
        return _iView(self)

    
    def get_all_for(self, key):
        ''' Returns all values of the given key '''
        if not isinstance(key, _string_type):
            raise TypeError('Key needs to be a string.')
        return (lambda .0 = None: [ self[(idx, key)] for idx in .0 ])(_range(self._VDFDict__kcount[key]))

    
    def remove_all_for(self = None, key = None):
        ''' Removes all items with the given key '''
        if not isinstance(key, _string_type):
            raise TypeError('Key need to be a string.')
        for idx in None(self._VDFDict__kcount[key]):
            super(VDFDict, self).__delitem__((idx, key))
        self._VDFDict__omap = None(None((lambda x = None: x[1] != key), self._VDFDict__omap))
        del self._VDFDict__kcount[key]

    
    def has_duplicates(self):
        '''
        Returns ``True`` if the dict contains keys with duplicates.
        Recurses through any all keys with value that is ``VDFDict``.
        '''
        for n in getattr(self._VDFDict__kcount, _iter_values)():
            if n != 1:
                return True
            
            def dict_recurse(obj = None):
                for v in getattr(obj, _iter_values)():
                    if isinstance(v, VDFDict) and v.has_duplicates():
                        return True
                    if None(v, dict):
                        return dict_recurse(v)
                    return False

            return dict_recurse(self)

    __classcell__ = None

