# Source Generated with Decompyle++
# File: tempfile.pyc (Python 3.10)

__doc__ = "Temporary files.\n\nThis module provides generic, low- and high-level interfaces for\ncreating temporary files and directories.  All of the interfaces\nprovided by this module can be used without fear of race conditions\nexcept for 'mktemp'.  'mktemp' is subject to race conditions and\nshould not be used; it is provided for backward compatibility only.\n\nThe default path names are returned as str.  If you supply bytes as\ninput, all return values will be in bytes.  Ex:\n\n    >>> tempfile.mkstemp()\n    (4, '/tmp/tmptpu9nin8')\n    >>> tempfile.mkdtemp(suffix=b'')\n    b'/tmp/tmppbi8f0hy'\n\nThis module also provides some data items to the user:\n\n  TMP_MAX  - maximum number of names that will be tried before\n             giving up.\n  tempdir  - If this is set to a string before the first use of\n             any routine from this module, it will be considered as\n             another candidate location to store temporary files.\n"
__all__ = [
    'NamedTemporaryFile',
    'TemporaryFile',
    'SpooledTemporaryFile',
    'TemporaryDirectory',
    'mkstemp',
    'mkdtemp',
    'mktemp',
    'TMP_MAX',
    'gettempprefix',
    'tempdir',
    'gettempdir',
    'gettempprefixb',
    'gettempdirb']
import functools as _functools
import warnings as _warnings
import io as _io
import os as _os
# WARNING: Decompyle incomplete
