# Source Generated with Decompyle++
# File: parse.pyc (Python 3.10)

'''Parse (absolute and relative) URLs.

urlparse module is based upon the following RFC specifications.

RFC 3986 (STD66): "Uniform Resource Identifiers" by T. Berners-Lee, R. Fielding
and L.  Masinter, January 2005.

RFC 2732 : "Format for Literal IPv6 Addresses in URL\'s by R.Hinden, B.Carpenter
and L.Masinter, December 1999.

RFC 2396:  "Uniform Resource Identifiers (URI)": Generic Syntax by T.
Berners-Lee, R. Fielding, and L. Masinter, August 1998.

RFC 2368: "The mailto URL scheme", by P.Hoffman , L Masinter, J. Zawinski, July 1998.

RFC 1808: "Relative Uniform Resource Locators", by R. Fielding, UC Irvine, June
1995.

RFC 1738: "Uniform Resource Locators (URL)" by T. Berners-Lee, L. Masinter, M.
McCahill, December 1994

RFC 3986 is considered the current standard and any future changes to
urlparse module should conform with it.  The urlparse module is
currently not entirely compliant with this RFC due to defacto
scenarios for parsing, and for backward compatibility purposes, some
parsing quirks from older RFCs are retained. The testcases in
test_urlparse.py provides a good indicator of parsing behavior.

The WHATWG URL Parser spec should also be considered.  We are not compliant with
it either due to existing user code API behavior expectations (Hyrum\'s Law).
It serves as a useful guide when making changes.
'''
import re
import sys
import types
import collections
import warnings
import ipaddress
__all__ = [
    'urlparse',
    'urlunparse',
    'urljoin',
    'urldefrag',
    'urlsplit',
    'urlunsplit',
    'urlencode',
    'parse_qs',
    'parse_qsl',
    'quote',
    'quote_plus',
    'quote_from_bytes',
    'unquote',
    'unquote_plus',
    'unquote_to_bytes',
    'DefragResult',
    'ParseResult',
    'SplitResult',
    'DefragResultBytes',
    'ParseResultBytes',
    'SplitResultBytes']
uses_relative = [
    '',
    'ftp',
    'http',
    'gopher',
    'nntp',
    'imap',
    'wais',
    'file',
    'https',
    'shttp',
    'mms',
    'prospero',
    'rtsp',
    'rtspu',
    'sftp',
    'svn',
    'svn+ssh',
    'ws',
    'wss']
uses_netloc = [
    '',
    'ftp',
    'http',
    'gopher',
    'nntp',
    'telnet',
    'imap',
    'wais',
    'file',
    'mms',
    'https',
    'shttp',
    'snews',
    'prospero',
    'rtsp',
    'rtspu',
    'rsync',
    'svn',
    'svn+ssh',
    'sftp',
    'nfs',
    'git',
    'git+ssh',
    'ws',
    'wss']
uses_params = [
    '',
    'ftp',
    'hdl',
    'prospero',
    'http',
    'imap',
    'https',
    'shttp',
    'rtsp',
    'rtspu',
    'sip',
    'sips',
    'mms',
    'sftp',
    'tel']
non_hierarchical = [
    'gopher',
    'hdl',
    'mailto',
    'news',
    'telnet',
    'wais',
    'imap',
    'snews',
    'sip',
    'sips']
uses_query = [
    '',
    'http',
    'wais',
    'imap',
    'https',
    'shttp',
    'mms',
    'gopher',
    'rtsp',
    'rtspu',
    'sip',
    'sips']
uses_fragment = [
    '',
    'ftp',
    'hdl',
    'http',
    'gopher',
    'news',
    'nntp',
    'wais',
    'https',
    'shttp',
    'snews',
    'file',
    'prospero']
scheme_chars = 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789+-.'
_WHATWG_C0_CONTROL_OR_SPACE = '\x00\x01\x02\x03\x04\x05\x06\x07\x08\t\n\x0b\x0c\r\x0e\x0f\x10\x11\x12\x13\x14\x15\x16\x17\x18\x19\x1a\x1b\x1c\x1d\x1e\x1f '
_UNSAFE_URL_BYTES_TO_REMOVE = [
    '\t',
    '\r',
    '\n']
MAX_CACHE_SIZE = 20
_parse_cache = { }

def clear_cache():
    '''Clear the parse cache and the quoters cache.'''
    _parse_cache.clear()
    _safe_quoters.clear()

_implicit_encoding = 'ascii'
_implicit_errors = 'strict'

def _noop(obj):
    return obj


def _encode_result(obj, encoding, errors = (_implicit_encoding, _implicit_errors)):
    return obj.encode(encoding, errors)


def _decode_args(args, encoding, errors = (_implicit_encoding, _implicit_errors)):
    return None((lambda .0 = None: for x in .0:
x.decode(encoding, errors) if x else '')(args))


def _coerce_args(*args):
    str_input = isinstance(args[0], str)
    for arg in args[1:]:
        if arg and isinstance(arg, str) != str_input:
            raise TypeError('Cannot mix str and non-str arguments')
        if str_input:
            return args + (_noop,)
        return None(args) + (_encode_result,)


class _ResultMixinStr(object):
    '''Standard approach to encoding parsed results from str to bytes'''
    __slots__ = ()
    
    def encode(self, encoding, errors = ('ascii', 'strict')):
        pass
    # WARNING: Decompyle incomplete



class _ResultMixinBytes(object):
    '''Standard approach to decoding parsed results from bytes to str'''
    __slots__ = ()
    
    def decode(self, encoding, errors = ('ascii', 'strict')):
        pass
    # WARNING: Decompyle incomplete



class _NetlocResultMixinBase(object):
    '''Shared methods for the parsed result objects containing a netloc element'''
    __slots__ = ()
    
    def username(self):
        return self._userinfo[0]

    username = property(username)
    
    def password(self):
        return self._userinfo[1]

    password = property(password)
    
    def hostname(self):
        hostname = self._hostinfo[0]
        if not hostname:
            return None
        separator = '%' if None(hostname, str) else b'%'
        (hostname, percent, zone) = hostname.partition(separator)
        return hostname.lower() + percent + zone

    hostname = property(hostname)
    
    def port(self):
        port = self._hostinfo[1]
        if port is not None:
            if port.isdigit() and port.isascii():
                port = int(port)
            else:
                raise ValueError(f'''Port could not be cast to integer value as {port!r}''')
            if not port <= port or port <= 65535:
                raise ValueError('Port out of range 0-65535')
            raise ValueError('Port out of range 0-65535')

    port = property(port)
    __class_getitem__ = classmethod(types.GenericAlias)


class _NetlocResultMixinStr(_ResultMixinStr, _NetlocResultMixinBase):
    __slots__ = ()
    
    def _userinfo(self):
        netloc = self.netloc
        (userinfo, have_info, hostinfo) = netloc.rpartition('@')
        if have_info:
            (username, have_password, password) = userinfo.partition(':')
            if not have_password:
                password = None
            return (username, password)
        username = None
        password = None
        return (username, password)

    _userinfo = property(_userinfo)
    
    def _hostinfo(self):
        netloc = self.netloc
        (_, _, hostinfo) = netloc.rpartition('@')
        (_, have_open_br, bracketed) = hostinfo.partition('[')
        if have_open_br:
            (hostname, _, port) = bracketed.partition(']')
            (_, _, port) = port.partition(':')
        else:
            (hostname, _, port) = hostinfo.partition(':')
        if not port:
            port = None
        return (hostname, port)

    _hostinfo = property(_hostinfo)


class _NetlocResultMixinBytes(_ResultMixinBytes, _NetlocResultMixinBase):
    __slots__ = ()
    
    def _userinfo(self):
        netloc = self.netloc
        (userinfo, have_info, hostinfo) = netloc.rpartition(b'@')
        if have_info:
            (username, have_password, password) = userinfo.partition(b':')
            if not have_password:
                password = None
            return (username, password)
        username = None
        password = None
        return (username, password)

    _userinfo = property(_userinfo)
    
    def _hostinfo(self):
        netloc = self.netloc
        (_, _, hostinfo) = netloc.rpartition(b'@')
        (_, have_open_br, bracketed) = hostinfo.partition(b'[')
        if have_open_br:
            (hostname, _, port) = bracketed.partition(b']')
            (_, _, port) = port.partition(b':')
        else:
            (hostname, _, port) = hostinfo.partition(b':')
        if not port:
            port = None
        return (hostname, port)

    _hostinfo = property(_hostinfo)

from collections import namedtuple
_DefragResultBase = namedtuple('DefragResult', 'url fragment')
_SplitResultBase = namedtuple('SplitResult', 'scheme netloc path query fragment')
_ParseResultBase = namedtuple('ParseResult', 'scheme netloc path params query fragment')
_DefragResultBase.__doc__ = '\nDefragResult(url, fragment)\n\nA 2-tuple that contains the url without fragment identifier and the fragment\nidentifier as a separate argument.\n'
_DefragResultBase.url.__doc__ = 'The URL with no fragment identifier.'
_DefragResultBase.fragment.__doc__ = '\nFragment identifier separated from URL, that allows indirect identification of a\nsecondary resource by reference to a primary resource and additional identifying\ninformation.\n'
_SplitResultBase.__doc__ = '\nSplitResult(scheme, netloc, path, query, fragment)\n\nA 5-tuple that contains the different components of a URL. Similar to\nParseResult, but does not split params.\n'
_SplitResultBase.scheme.__doc__ = 'Specifies URL scheme for the request.'
_SplitResultBase.netloc.__doc__ = '\nNetwork location where the request is made to.\n'
_SplitResultBase.path.__doc__ = '\nThe hierarchical path, such as the path to a file to download.\n'
_SplitResultBase.query.__doc__ = "\nThe query component, that contains non-hierarchical data, that along with data\nin path component, identifies a resource in the scope of URI's scheme and\nnetwork location.\n"
_SplitResultBase.fragment.__doc__ = '\nFragment identifier, that allows indirect identification of a secondary resource\nby reference to a primary resource and additional identifying information.\n'
_ParseResultBase.__doc__ = '\nParseResult(scheme, netloc, path, params, query, fragment)\n\nA 6-tuple that contains components of a parsed URL.\n'
_ParseResultBase.scheme.__doc__ = _SplitResultBase.scheme.__doc__
_ParseResultBase.netloc.__doc__ = _SplitResultBase.netloc.__doc__
_ParseResultBase.path.__doc__ = _SplitResultBase.path.__doc__
_ParseResultBase.params.__doc__ = '\nParameters for last path element used to dereference the URI in order to provide\naccess to perform some operation on the resource.\n'
_ParseResultBase.query.__doc__ = _SplitResultBase.query.__doc__
_ParseResultBase.fragment.__doc__ = _SplitResultBase.fragment.__doc__
ResultBase = _NetlocResultMixinStr

class DefragResult(_ResultMixinStr, _DefragResultBase):
    __slots__ = ()
    
    def geturl(self):
        if self.fragment:
            return self.url + '#' + self.fragment
        return None.url



class SplitResult(_NetlocResultMixinStr, _SplitResultBase):
    __slots__ = ()
    
    def geturl(self):
        return urlunsplit(self)



class ParseResult(_NetlocResultMixinStr, _ParseResultBase):
    __slots__ = ()
    
    def geturl(self):
        return urlunparse(self)



class DefragResultBytes(_ResultMixinBytes, _DefragResultBase):
    __slots__ = ()
    
    def geturl(self):
        if self.fragment:
            return self.url + b'#' + self.fragment
        return None.url



class SplitResultBytes(_NetlocResultMixinBytes, _SplitResultBase):
    __slots__ = ()
    
    def geturl(self):
        return urlunsplit(self)



class ParseResultBytes(_NetlocResultMixinBytes, _ParseResultBase):
    __slots__ = ()
    
    def geturl(self):
        return urlunparse(self)



def _fix_result_transcoding():
    _result_pairs = ((DefragResult, DefragResultBytes), (SplitResult, SplitResultBytes), (ParseResult, ParseResultBytes))
    for _decoded, _encoded in _result_pairs:
        _decoded._encoded_counterpart = _encoded
        _encoded._decoded_counterpart = _decoded

_fix_result_transcoding()
del _fix_result_transcoding

def urlparse(url, scheme, allow_fragments = ('', True)):
    '''Parse a URL into 6 components:
    <scheme>://<netloc>/<path>;<params>?<query>#<fragment>

    The result is a named 6-tuple with fields corresponding to the
    above. It is either a ParseResult or ParseResultBytes object,
    depending on the type of the url parameter.

    The username, password, hostname, and port sub-components of netloc
    can also be accessed as attributes of the returned object.

    The scheme argument provides the default value of the scheme
    component when no scheme is found in url.

    If allow_fragments is False, no attempt is made to separate the
    fragment component from the previous component, which can be either
    path or query.

    Note that % escapes are not expanded.
    '''
    (url, scheme, _coerce_result) = _coerce_args(url, scheme)
    splitresult = urlsplit(url, scheme, allow_fragments)
    (scheme, netloc, url, query, fragment) = splitresult
    if scheme in uses_params and ';' in url:
        (url, params) = _splitparams(url)
    else:
        params = ''
    result = ParseResult(scheme, netloc, url, params, query, fragment)
    return _coerce_result(result)


def _splitparams(url):
    if '/' in url:
        i = url.find(';', url.rfind('/'))
        if i < 0:
            return (url, '')
    i = url.find(';')
    return (url[:i], url[i + 1:])


def _splitnetloc(url, start = (0,)):
    delim = len(url)
    for c in '/?#':
        wdelim = url.find(c, start)
        if wdelim >= 0:
            delim = min(delim, wdelim)
    return (url[start:delim], url[delim:])


def _checknetloc(netloc):
    if netloc or netloc.isascii():
        return None
    import unicodedata
    n = netloc.replace('@', '')
    n = n.replace(':', '')
    n = n.replace('#', '')
    n = n.replace('?', '')
    netloc2 = unicodedata.normalize('NFKC', n)
    if n == netloc2:
        return None
    for c in None:
        if c in netloc2:
            raise ValueError("netloc '" + netloc + "' contains invalid " + 'characters under NFKC normalization')
        return None


def _check_bracketed_netloc(netloc):
    hostname_and_port = netloc.rpartition('@')[2]
    (before_bracket, have_open_br, bracketed) = hostname_and_port.partition('[')
    if have_open_br:
        if before_bracket:
            raise ValueError('Invalid IPv6 URL')
        (hostname, _, port) = None.partition(']')
        if not port and port.startswith(':'):
            raise ValueError('Invalid IPv6 URL')
    (hostname, _, port) = hostname_and_port.partition(':')
    _check_bracketed_host(hostname)


def _check_bracketed_host(hostname):
    if hostname.startswith('v'):
        if not re.match('\\Av[a-fA-F0-9]+\\..+\\Z', hostname):
            raise ValueError('IPvFuture address is invalid')
        return None
    ip = None.ip_address(hostname)
    if isinstance(ip, ipaddress.IPv4Address):
        raise ValueError('An IPv4 address cannot be in brackets')


def urlsplit(url, scheme, allow_fragments = ('', True)):
    '''Parse a URL into 5 components:
    <scheme>://<netloc>/<path>?<query>#<fragment>

    The result is a named 5-tuple with fields corresponding to the
    above. It is either a SplitResult or SplitResultBytes object,
    depending on the type of the url parameter.

    The username, password, hostname, and port sub-components of netloc
    can also be accessed as attributes of the returned object.

    The scheme argument provides the default value of the scheme
    component when no scheme is found in url.

    If allow_fragments is False, no attempt is made to separate the
    fragment component from the previous component, which can be either
    path or query.

    Note that % escapes are not expanded.
    '''
    (url, scheme, _coerce_result) = _coerce_args(url, scheme)
    url = url.lstrip(_WHATWG_C0_CONTROL_OR_SPACE)
    scheme = scheme.strip(_WHATWG_C0_CONTROL_OR_SPACE)
    for b in _UNSAFE_URL_BYTES_TO_REMOVE:
        url = url.replace(b, '')
        scheme = scheme.replace(b, '')
    allow_fragments = bool(allow_fragments)
    key = (url, scheme, allow_fragments, type(url), type(scheme))
    cached = _parse_cache.get(key, None)
    if cached:
        return _coerce_result(cached)
    if None(_parse_cache) >= MAX_CACHE_SIZE:
        clear_cache()
    netloc = query = fragment = ''
    i = url.find(':')
    if i > 0:
        for c in url[:i]:
            if c not in scheme_chars:
                pass
            
            scheme = url[:i].lower()
            url = url[i + 1:]
            if url[:2] == '//':
                (netloc, url) = _splitnetloc(url, 2)
                if ('[' in netloc or ']' not in netloc or ']' in netloc) and '[' not in netloc:
                    raise ValueError('Invalid IPv6 URL')
                if None in netloc and ']' in netloc:
                    _check_bracketed_netloc(netloc)
    if allow_fragments and '#' in url:
        (url, fragment) = url.split('#', 1)
    if '?' in url:
        (url, query) = url.split('?', 1)
    _checknetloc(netloc)
    v = SplitResult(scheme, netloc, url, query, fragment)
    _parse_cache[key] = v
    return _coerce_result(v)


def urlunparse(components):
    '''Put a parsed URL back together again.  This may result in a
    slightly different, but equivalent URL, if the URL that was parsed
    originally had redundant delimiters, e.g. a ? with an empty query
    (the draft states that these are equivalent).'''
    pass
# WARNING: Decompyle incomplete


def urlunsplit(components):
    '''Combine the elements of a tuple as returned by urlsplit() into a
    complete URL as a string. The data argument can be any five-item iterable.
    This may result in a slightly different, but equivalent URL, if the URL that
    was parsed originally had unnecessary delimiters (for example, a ? with an
    empty query; the RFC states that these are equivalent).'''
    pass
# WARNING: Decompyle incomplete


def urljoin(base, url, allow_fragments = (True,)):
    '''Join a base URL and a possibly relative URL to form an absolute
    interpretation of the latter.'''
    if not base:
        return url
    if not None:
        return base
    (base, url, _coerce_result) = None(base, url)
    (bscheme, bnetloc, bpath, bparams, bquery, bfragment) = urlparse(base, '', allow_fragments)
    (scheme, netloc, path, params, query, fragment) = urlparse(url, bscheme, allow_fragments)
    if scheme != bscheme or scheme not in uses_relative:
        return _coerce_result(url)
    if None in uses_netloc:
        if netloc:
            return _coerce_result(urlunparse((scheme, netloc, path, params, query, fragment)))
        netloc = None
    if not path and params:
        path = bpath
        params = bparams
        if not query:
            query = bquery
        return _coerce_result(urlunparse((scheme, netloc, path, params, query, fragment)))
    base_parts = None.split('/')
    if base_parts[-1] != '':
        del base_parts[-1]
    if path[:1] == '/':
        segments = path.split('/')
    else:
        segments = base_parts + path.split('/')
        segments[1:-1] = filter(None, segments[1:-1])
    resolved_path = []
# WARNING: Decompyle incomplete


def urldefrag(url):
    '''Removes any existing fragment from URL.

    Returns a tuple of the defragmented URL and the fragment.  If
    the URL contained no fragments, the second element is the
    empty string.
    '''
    (url, _coerce_result) = _coerce_args(url)
    if '#' in url:
        (s, n, p, a, q, frag) = urlparse(url)
        defrag = urlunparse((s, n, p, a, q, ''))
    else:
        frag = ''
        defrag = url
    return _coerce_result(DefragResult(defrag, frag))

_hexdig = '0123456789ABCDEFabcdef'
_hextobyte = None

def unquote_to_bytes(string):
    """unquote_to_bytes('abc%20def') -> b'abc def'."""
    global _hextobyte
    if not string:
        string.split
        return b''
    if None(string, str):
        string = string.encode('utf-8')
    bits = string.split(b'%')
    if len(bits) == 1:
        return string
    res = [
        None[0]]
    append = res.append
    if _hextobyte is None:
        _hextobyte = (lambda .0: pass# WARNING: Decompyle incomplete
)(_hexdig)
# WARNING: Decompyle incomplete

_asciire = re.compile('([\x00-\x7f]+)')

def unquote(string, encoding, errors = ('utf-8', 'replace')):
    """Replace %xx escapes by their single-character equivalent. The optional
    encoding and errors parameters specify how to decode percent-encoded
    sequences into Unicode characters, as accepted by the bytes.decode()
    method.
    By default, percent-encoded sequences are decoded with UTF-8, and invalid
    sequences are replaced by a placeholder character.

    unquote('abc%20def') -> 'abc def'.
    """
    if isinstance(string, bytes):
        return unquote_to_bytes(string).decode(encoding, errors)
    if None not in string:
        string.split
        return string
    if None is None:
        encoding = 'utf-8'
    if errors is None:
        errors = 'replace'
    bits = _asciire.split(string)
    res = [
        bits[0]]
    append = res.append
    for i in range(1, len(bits), 2):
        append(unquote_to_bytes(bits[i]).decode(encoding, errors))
        append(bits[i + 1])
    return ''.join(res)


def parse_qs(qs, keep_blank_values, strict_parsing, encoding, errors, max_num_fields, separator = (False, False, 'utf-8', 'replace', None, '&')):
    '''Parse a query given as a string argument.

        Arguments:

        qs: percent-encoded query string to be parsed

        keep_blank_values: flag indicating whether blank values in
            percent-encoded queries should be treated as blank strings.
            A true value indicates that blanks should be retained as
            blank strings.  The default false value indicates that
            blank values are to be ignored and treated as if they were
            not included.

        strict_parsing: flag indicating what to do with parsing errors.
            If false (the default), errors are silently ignored.
            If true, errors raise a ValueError exception.

        encoding and errors: specify how to decode percent-encoded sequences
            into Unicode characters, as accepted by the bytes.decode() method.

        max_num_fields: int. If set, then throws a ValueError if there
            are more than n fields read by parse_qsl().

        separator: str. The symbol to use for separating the query arguments.
            Defaults to &.

        Returns a dictionary.
    '''
    parsed_result = { }
    pairs = parse_qsl(qs, keep_blank_values, strict_parsing, encoding, errors, max_num_fields, separator, **('encoding', 'errors', 'max_num_fields', 'separator'))
    for name, value in pairs:
        if name in parsed_result:
            parsed_result[name].append(value)
            continue
        parsed_result[name] = [
            value]
    return parsed_result


def parse_qsl(qs, keep_blank_values, strict_parsing, encoding, errors, max_num_fields, separator = (False, False, 'utf-8', 'replace', None, '&')):
    '''Parse a query given as a string argument.

        Arguments:

        qs: percent-encoded query string to be parsed

        keep_blank_values: flag indicating whether blank values in
            percent-encoded queries should be treated as blank strings.
            A true value indicates that blanks should be retained as blank
            strings.  The default false value indicates that blank values
            are to be ignored and treated as if they were  not included.

        strict_parsing: flag indicating what to do with parsing errors. If
            false (the default), errors are silently ignored. If true,
            errors raise a ValueError exception.

        encoding and errors: specify how to decode percent-encoded sequences
            into Unicode characters, as accepted by the bytes.decode() method.

        max_num_fields: int. If set, then throws a ValueError
            if there are more than n fields read by parse_qsl().

        separator: str. The symbol to use for separating the query arguments.
            Defaults to &.

        Returns a list, as G-d intended.
    '''
    (qs, _coerce_result) = _coerce_args(qs)
    (separator, _) = _coerce_args(separator)
    if not separator or isinstance(separator, (str, bytes)):
        raise ValueError('Separator must be of type string or bytes.')
    if None is not None:
        num_fields = 1 + qs.count(separator)
        if max_num_fields < num_fields:
            raise ValueError('Max number of fields exceeded')
        r = None
        for name_value in qs.split(separator):
            if not name_value and strict_parsing:
                continue
            nv = name_value.split('=', 1)
            if len(nv) != 2:
                if strict_parsing:
                    raise ValueError('bad query field: %r' % (name_value,))
                if None:
                    nv.append('')
                
            if len(nv[1]) or keep_blank_values:
                name = nv[0].replace('+', ' ')
                name = unquote(name, encoding, errors, **('encoding', 'errors'))
                name = _coerce_result(name)
                value = nv[1].replace('+', ' ')
                value = unquote(value, encoding, errors, **('encoding', 'errors'))
                value = _coerce_result(value)
                r.append((name, value))
        return r


def unquote_plus(string, encoding, errors = ('utf-8', 'replace')):
    """Like unquote(), but also replace plus signs by spaces, as required for
    unquoting HTML form values.

    unquote_plus('%7e/abc+def') -> '~/abc def'
    """
    string = string.replace('+', ' ')
    return unquote(string, encoding, errors)

_ALWAYS_SAFE = frozenset(b'ABCDEFGHIJKLMNOPQRSTUVWXYZabcdefghijklmnopqrstuvwxyz0123456789_.-~')
_ALWAYS_SAFE_BYTES = bytes(_ALWAYS_SAFE)
_safe_quoters = { }

class Quoter(collections.defaultdict):
    '''A mapping from bytes (in range(0,256)) to strings.

    String values are percent-encoded byte values, unless the key < 128, and
    in the "safe" set (either the specified safe set, or default set).
    '''
    
    def __init__(self, safe):
        '''safe: bytes object.'''
        self.safe = _ALWAYS_SAFE.union(safe)

    
    def __repr__(self):
        return '<%s %r>' % (self.__class__.__name__, dict(self))

    
    def __missing__(self, b):
        res = chr(b) if b in self.safe else '%{:02X}'.format(b)
        self[b] = res
        return res



def quote(string, safe, encoding, errors = ('/', None, None)):
    '''quote(\'abc def\') -> \'abc%20def\'

    Each part of a URL, e.g. the path info, the query, etc., has a
    different set of reserved characters that must be quoted. The
    quote function offers a cautious (not minimal) way to quote a
    string for most of these parts.

    RFC 3986 Uniform Resource Identifier (URI): Generic Syntax lists
    the following (un)reserved characters.

    unreserved    = ALPHA / DIGIT / "-" / "." / "_" / "~"
    reserved      = gen-delims / sub-delims
    gen-delims    = ":" / "/" / "?" / "#" / "[" / "]" / "@"
    sub-delims    = "!" / "$" / "&" / "\'" / "(" / ")"
                  / "*" / "+" / "," / ";" / "="

    Each of the reserved characters is reserved in some component of a URL,
    but not necessarily in all of them.

    The quote function %-escapes all characters that are neither in the
    unreserved chars ("always safe") nor the additional chars set via the
    safe arg.

    The default for the safe arg is \'/\'. The character is reserved, but in
    typical usage the quote function is being called on a path where the
    existing slash characters are to be preserved.

    Python 3.7 updates from using RFC 2396 to RFC 3986 to quote URL strings.
    Now, "~" is included in the set of unreserved characters.

    string and safe may be either str or bytes objects. encoding and errors
    must not be specified if string is a bytes object.

    The optional encoding and errors parameters specify how to deal with
    non-ASCII characters, as accepted by the str.encode method.
    By default, encoding=\'utf-8\' (characters are encoded with UTF-8), and
    errors=\'strict\' (unsupported characters raise a UnicodeEncodeError).
    '''
    if isinstance(string, str):
        if not string:
            return string
        if None is None:
            encoding = 'utf-8'
        if errors is None:
            errors = 'strict'
        string = string.encode(encoding, errors)
    elif encoding is not None:
        raise TypeError("quote() doesn't support 'encoding' for bytes")
    if errors is not None:
        raise TypeError("quote() doesn't support 'errors' for bytes")
    return None(string, safe)


def quote_plus(string, safe, encoding, errors = ('', None, None)):
    """Like quote(), but also replace ' ' with '+', as required for quoting
    HTML form values. Plus signs in the