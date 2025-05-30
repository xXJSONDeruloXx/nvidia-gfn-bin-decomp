# Source Generated with Decompyle++
# File: utils.pyc (Python 3.10)

'''Miscellaneous utilities.'''
__all__ = [
    'collapse_rfc2231_value',
    'decode_params',
    'decode_rfc2231',
    'encode_rfc2231',
    'formataddr',
    'formatdate',
    'format_datetime',
    'getaddresses',
    'make_msgid',
    'mktime_tz',
    'parseaddr',
    'parsedate',
    'parsedate_tz',
    'parsedate_to_datetime',
    'unquote']
import os
import re
import time
import random
import socket
import datetime
import urllib.parse as urllib
from email._parseaddr import quote
from email._parseaddr import AddressList as _AddressList
from email._parseaddr import mktime_tz
from email._parseaddr import parsedate, parsedate_tz, _parsedate_tz
from email.charset import Charset
COMMASPACE = ', '
EMPTYSTRING = ''
UEMPTYSTRING = ''
CRLF = '\r\n'
TICK = "'"
specialsre = re.compile('[][\\\\()<>@,:;".]')
escapesre = re.compile('[\\\\"]')

def _has_surrogates(s):
    '''Return True if s contains surrogate-escaped binary data.'''
    pass
# WARNING: Decompyle incomplete


def _sanitize(string):
    original_bytes = string.encode('utf-8', 'surrogateescape')
    return original_bytes.decode('utf-8', 'replace')


def formataddr(pair, charset = ('utf-8',)):
    """The inverse of parseaddr(), this takes a 2-tuple of the form
    (realname, email_address) and returns the string value suitable
    for an RFC 2822 From, To or Cc header.

    If the first element of pair is false, then the second element is
    returned unmodified.

    The optional charset is the character set that is used to encode
    realname in case realname is not ASCII safe.  Can be an instance of str or
    a Charset-like object which has a header_encode method.  Default is
    'utf-8'.
    """
    (name, address) = pair
    address.encode('ascii')
# WARNING: Decompyle incomplete


def _iter_escaped_chars(addr):
    pos = 0
    escape = False
    for pos, ch in enumerate(addr):
        if escape:
            yield (pos, '\\' + ch)
            escape = False
            continue
        if ch == '\\':
            escape = True
            continue
        yield (pos, ch)
    if escape:
        yield (pos, '\\')
        return None


def _strip_quoted_realnames(addr):
    '''Strip real names between quotes.'''
    if '"' not in addr:
        return addr
    start = None
    open_pos = None
    result = []
    for pos, ch in _iter_escaped_chars(addr):
        if ch == '"':
            if open_pos is None:
                open_pos = pos
                continue
            if start != open_pos:
                result.append(addr[start:open_pos])
            start = pos + 1
            open_pos = None
    if start < len(addr):
        result.append(addr[start:])
    return ''.join(result)

supports_strict_parsing = True

def getaddresses(fieldvalues = None, *, strict):
    """Return a list of (REALNAME, EMAIL) or ('','') for each fieldvalue.

    When parsing fails for a fieldvalue, a 2-tuple of ('', '') is returned in
    its place.

    If strict is true, use a strict parser which rejects malformed inputs.
    """
    if not strict:
        all = COMMASPACE.join((lambda .0: for v in .0:
str(v))(fieldvalues))
        a = _AddressList(all)
        return a.addresslist
    fieldvalues = (lambda 