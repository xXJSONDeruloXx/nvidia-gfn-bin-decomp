# Source Generated with Decompyle++
# File: pathlib.pyc (Python 3.10)

import fnmatch
import functools
import io
import ntpath
import os
import posixpath
import re
import sys
import warnings
from _collections_abc import Sequence
from errno import EINVAL, ENOENT, ENOTDIR, EBADF, ELOOP
from operator import attrgetter
from stat import S_ISDIR, S_ISLNK, S_ISREG, S_ISSOCK, S_ISBLK, S_ISCHR, S_ISFIFO
from urllib.parse import quote_from_bytes as urlquote_from_bytes
__all__ = [
    'PurePath',
    'PurePosixPath',
    'PureWindowsPath',
    'Path',
    'PosixPath',
    'WindowsPath']
_WINERROR_NOT_READY = 21
_WINERROR_INVALID_NAME = 123
_WINERROR_CANT_RESOLVE_FILENAME = 1921
_IGNORED_ERROS = (ENOENT, ENOTDIR, EBADF, ELOOP)
_IGNORED_WINERRORS = (_WINERROR_NOT_READY, _WINERROR_INVALID_NAME, _WINERROR_CANT_RESOLVE_FILENAME)

def _ignore_error(exception):
    if not getattr(exception, 'errno', None) in _IGNORED_ERROS:
        pass
    return getattr(exception, 'winerror', None) in _IGNORED_WINERRORS


def _is_wildcard_pattern(pat):
    if not '*' in pat and '?' in pat:
        pass
    return '[' in pat


class _Flavour(object):
    '''A flavour implements a particular (platform-specific) set of path
    semantics.'''
    
    def __init__(self):
        self.join = self.sep.join

    
    def parse_parts(self, parts):
        parsed = []
        sep = self.sep
        altsep = self.altsep
        drv = root = ''
        it = reversed(parts)
        for part in it:
            if not part:
                continue
            if altsep:
                part = part.replace(altsep, sep)
            (drv, root, rel) = self.splitroot(part)
            if sep in rel:
                for x in reversed(rel.split(sep)):
                    if x and x != '.':
                        parsed.append(sys.intern(x))
            elif rel and rel != '.':
                parsed.append(sys.intern(rel))
            if drv or root:
                if not drv:
                    for part in it:
                        if not part:
                            continue
                        if altsep:
                            part = part.replace(altsep, sep)
                        drv = self.splitroot(part)[0]
                        if drv:
                            pass
                        
                    continue
                    if drv or root:
                        parsed.append(drv + root)
        parsed.reverse()
        return (drv, root, parsed)

    
    def join_parsed_parts(self, drv, root, parts, drv2, root2, parts2):
        '''
        Join the two paths represented by the respective
        (drive, root, parts) tuples.  Return a new (drive, root, parts) tuple.
        '''
        if root2:
            if drv2 and drv:
                return (drv, root2, [
                    drv + root2] + parts2[1:])
        if drv2:
            if drv2 == drv or self.casefold(drv2) == self.casefold(drv):
                return (drv, root, parts + parts2[1:])
        return (drv, root, parts + parts2)
        return (drv2, root2, parts2)



class _WindowsFlavour(_Flavour):
    sep = '\\'
    altsep = '/'
    has_drv = True
    pathmod = ntpath
    is_supported = os.name == 'nt'
    drive_letters = set('abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ')
    ext_namespace_prefix = '\\\\?\\'
    reserved_names = {
        'CONIN$',
        'CONOUT$',
        'AUX',
        'CON',
        'NUL',
        'PRN'} | (lambda .0: pass# WARNING: Decompyle incomplete
)('123456789¹²³') | (lambda .0: pass# WARNING: Decompyle incomplete
)('123456789¹²³')
    
    def splitroot(self, part, sep = (sep,)):
        first = part[0:1]
        second = part[1:2]
        if second == sep and first == sep:
            (prefix, part) = self._split_extended_path(part)
            first = part[0:1]
            second = part[1:2]
        else:
            prefix = ''
        third = part[2:3]
        if second == sep and first == sep and third != sep:
            index = part.find(sep, 2)
            if index != -1:
                index2 = part.find(sep, index + 1)
                if index2 != index + 1:
                    if index2 == -1:
                        index2 = len(part)
                    if prefix:
                        return (prefix + part[1:index2], sep, part[index2 + 1:])
                    return (None[:index2], sep, part[index2 + 1:])
                drv = None
                root = None
                if second == ':' and first in self.drive_letters:
                    drv = part[:2]
                    part = part[2:]
                    first = third
        if first == sep:
            root = first
            part = part.lstrip(sep)
        return (prefix + drv, root, part)

    
    def casefold(self, s):
        return s.lower()

    
    def casefold_parts(self, parts):
        return (lambda .0: [ p.lower() for p in .0 ])(parts)

    
    def compile_pattern(self, pattern):
        return re.compile(fnmatch.translate(pattern), re.IGNORECASE).fullmatch

    
    def _split_extended_path(self, s, ext_prefix = (ext_namespace_prefix,)):
        prefix = ''
        if s.startswith(ext_prefix):
            prefix = s[:4]
            s = s[4:]
            if s.startswith('UNC\\'):
                prefix += s[:3]
                s = '\\' + s[3:]
        return (prefix, s)

    
    def is_reserved(self, parts):
        if not parts:
            return False
        if None[0].startswith('\\\\'):
            return False
        name = None[-1].partition('.')[0].partition(':')[0].rstrip(' ')
        return name.upper() in self.reserved_names

    
    def make_uri(self, path):
        drive = path.drive
        if len(drive) == 2 and drive[1] == ':':
            rest = path.as_posix()[2:].lstrip('/')
            return 'file:///%s/%s' % (drive, urlquote_from_bytes(rest.encode('utf-8')))
        return None + urlquote_from_bytes(path.as_posix().encode('utf-8'))



class _PosixFlavour(_Flavour):
    sep = '/'
    altsep = ''
    has_drv = False
    pathmod = posixpath
    is_supported = os.name != 'nt'
    
    def splitroot(self, part, sep = (sep,)):
        if part and part[0] == sep:
            stripped_part = part.lstrip(sep)
            if len(part) - len(stripped_part) == 2:
                return ('', sep * 2, stripped_part)
            return (None, sep, stripped_part)
        return (None, '', part)

    
    def casefold(self, s):
        return s

    
    def casefold_parts(self, parts):
        return parts

    
    def compile_pattern(self, pattern):
        return re.compile(fnmatch.translate(pattern)).fullmatch

    
    def is_reserved(self, parts):
        return False

    
    def make_uri(self, path):
        bpath = bytes(path)
        return 'file://' + urlquote_from_bytes(bpath)


_windows_flavour = _WindowsFlavour()
_posix_flavour = _PosixFlavour()

class _Accessor:
    '''An accessor implements a particular (system-specific or not) way of
    accessing paths on the filesystem.'''
    pass


class _NormalAccessor(_Accessor):
    stat = os.stat
    open = io.open
    listdir = os.listdir
    scandir = os.scandir
    chmod = os.chmod
    mkdir = os.mkdir
    unlink = os.unlink
    if hasattr(os, 'link'):
        link = os.link
    else:
        
        def link(self, src, dst):
            raise NotImplementedError('os.link() not available on this system')

    rmdir = os.rmdir
    rename = os.rename
    replace = os.replace
    if hasattr(os, 'symlink'):
        symlink = os.symlink
    else:
        
        def symlink(self, src, dst, target_is_directory = (False,)):
            raise NotImplementedError('os.symlink() not available on this system')

    
    def touch(self, path, mode, exist_ok = (438, True)):
        pass
    # WARNING: Decompyle incomplete

    if hasattr(os, 'readlink'):
        readlink = os.readlink
    else:
        
        def readlink(self, path):
            raise NotImplementedError('os.readlink() not available on this system')

    
    def owner(self, path):
        pass
    # WARNING: Decompyle incomplete

    
    def group(self, path):
        pass
    # WARNING: Decompyle incomplete

    getcwd = os.getcwd
    expanduser = staticmethod(os.path.expanduser)
    realpath = staticmethod(os.path.realpath)

_normal_accessor = _NormalAccessor()

def _make_selector(pattern_parts, flavour):
    pat = pattern_parts[0]
    child_parts = pattern_parts[1:]
    if pat == '**':
        cls = _RecursiveWildcardSelector
    elif '**' in pat:
        raise ValueError("Invalid pattern: '**' can only be an entire path component")
    if _is_wildcard_pattern(pat):
        cls = _WildcardSelector
    else:
        cls = _PreciseSelector
    return cls(pat, child_parts, flavour)

if hasattr(functools, 'lru_cache'):
    _make_selector = functools.lru_cache()(_make_selector)

class _Selector:
    '''A selector matches a specific glob pattern part against the children
    of a given path.'''
    
    def __init__(self, child_parts, flavour):
        self.child_parts = child_parts
        if child_parts:
            self.successor = _make_selector(child_parts, flavour)
            self.dironly = True
            return None
        self.successor = None()
        self.dironly = False

    
    def select_from(self, parent_path):
        '''Iterate over all child paths of `parent_path` matched by this
        selector.  This can contain parent_path itself.'''
        path_cls = type(parent_path)
        is_dir = path_cls.is_dir
        exists = path_cls.exists
        scandir = parent_path._accessor.scandir
        if not is_dir(parent_path):
            return iter([])
        return None._select_from(parent_path, is_dir, exists, scandir)



class _TerminatingSelector:
    
    def _select_from(self, parent_path, is_dir, exists, scandir):
        yield parent_path



class _PreciseSelector(_Selector):
    
    def __init__(self, name, child_parts, flavour):
        self.name = name
        _Selector.__init__(self, child_parts, flavour)

    
    def _select_from(self, parent_path, is_dir, exists, scandir):
        pass
    # WARNING: Decompyle incomplete



class _WildcardSelector(_Selector):
    
    def __init__(self, pat, child_parts, flavour):
        self.match = flavour.compile_pattern(pat)
        _Selector.__init__(self, child_parts, flavour)

    
    def _select_from(self, parent_path, is_dir, exists, scandir):
        pass
    # WARNING: Decompyle incomplete



class _RecursiveWildcardSelector(_Selector):
    
    def __init__(self, pat, child_parts, flavour):
        _Selector.__init__(self, child_parts, flavour)

    
    def _iterate_directories(self, parent_path, is_dir, scandir):
        yield parent_path
    # WARNING: Decompyle incomplete

    
    def _select_from(self, parent_path, is_dir, exists, scandir):
        pass
    # WARNING: Decompyle incomplete



class _PathParents(Sequence):
    """This object provides sequence-like access to the logical ancestors
    of a path.  Don't try to construct it yourself."""
    __slots__ = ('_pathcls', '_drv', '_root', '_parts')
    
    def __init__(self, path):
        self._pathcls = type(path)
        self._drv = path._drv
        self._root = path._root
        self._parts = path._parts

    
    def __len__(self):
        if self._drv or self._root:
            return len(self._parts) - 1
        return None(self._parts)

    
    def __getitem__(self, idx):
        pass
    # WARNING: Decompyle incomplete

    
    def __repr__(self):
        return '<{}.parents>'.format(self._pathcls.__name__)



class PurePath(object):
    """Base class for manipulating paths without I/O.

    PurePath represents a filesystem path and offers operations which
    don't imply any actual filesystem I/O.  Depending on your system,
    instantiating a PurePath will return either a PurePosixPath or a
    PureWindowsPath object.  You can also instantiate either of these classes
    directly, regardless of your system.
    """
    __slots__ = ('_drv', '_root', '_parts', '_str', '_hash', '_pparts', '_cached_cparts')
    
    def __new__(cls, *args):
        '''Construct a PurePath from one or several strings and or existing
        PurePath objects.  The strings and path objects are combined so as
        to yield a canonicalized path, which is incorporated into the
        new PurePath object.
        '''
        if cls is PurePath:
            cls = PureWindowsPath if os.name == 'nt' else PurePosixPath
        return cls._from_parts(args)

    
    def __reduce__(self):
        return (self.__class__, tuple(self._parts))

    
    def _parse_args(cls, args):
        parts = []
        for a in args:
            if isinstance(a, PurePath):
                parts += a._parts
                continue
            a = os.fspath(a)
            if isinstance(a, str):
                parts.append(str(a))
                continue
            raise TypeError('argument should be a str object or an os.PathLike object returning str, not %r' % type(a))
            return cls._flavour.parse_parts(parts)

    _parse_args = classmethod(_parse_args)
    
    def _from_parts(cls, args):
        self = object.__new__(cls)
        (drv, root, parts) = self._parse_args(args)
        self._drv = drv
        self._root = root
        self._parts = parts
        return self

    _from_parts = classmethod(_from_parts)
    
    def _from_parsed_parts(cls, drv, root, parts):
        self = object.__new__(cls)
        self._drv = drv
        self._root = root
        self._parts = parts
        return self

    _from_parsed_parts = classmethod(_from_parsed_parts)
    
    def _format_parsed_parts(cls, drv, root, parts):
        if drv or root:
            return drv + root + cls._flavour.join(parts[1:])
        return None._flavour.join(parts)

    _format_parsed_parts = classmethod(_format_parsed_parts)
    
    def _make_child(self, args):
        (drv, root, parts) = self._parse_args(args)
        (drv, root, parts) = self._flavour.join_parsed_parts(self._drv, self._root, self._parts, drv, root, parts)
        return self._from_parsed_parts(drv, root, parts)

    
    def __str__(self):
        '''Return the string representation of the path, suitable for
        passing to system calls.'''
        pass
    # WARNING: Decompyle incomplete

    
    def __fspath__(self):
        return str(self)

    
    def as_posix(self):
        '''Return the string representation of the path with forward (/)
        slashes.'''
        f = self._flavour
        return str(self).replace(f.sep, '/')

    
    def __bytes__(self):
        '''Return the bytes representation of the path.  This is only
        recommended to use under Unix.'''
        return os.fsencode(self)

    
    def __repr__(self):
        return '{}({!r})'.format(self.__class__.__name__, self.as_posix())

    
    def as_uri(self):
        """Return the path as a 'file' URI."""
        if not self.is_absolute():
            raise ValueError("relative path can't be expressed as a file URI")
        return None._flavour.make_uri(self)

    
    def _cparts(self):
        pass
    # WARNING: Decompyle incomplete

    _cparts = property(_cparts)
    
    def __eq__(self, other):
        if not isinstance(other, PurePath):
            return NotImplemented
        if None._cparts == other._cparts:
            pass
        return self._flavour is other._flavour

    
    def __hash__(self):
        pass
    # WARNING: Decompyle incomplete

    
    def __lt__(self, other):
        if isinstance(other, PurePath) or self._flavour is not other._flavour:
            return NotImplemented
        return None._cparts < other._cparts

    
    def __le__(self, other):
        if isinstance(other, PurePath) or self._flavour is not other._flavour:
            return NotImplemented
        return None._cparts <= other._cparts

    
    def __gt__(self, other):
        if isinstance(other, PurePath) or self._flavour is not other._flavour:
            return NotImplemented
        return None._cparts > other._cparts

    
    def __ge__(self, other):
        if isinstance(other, PurePath) or self._flavour is not other._flavour:
            return NotImplemented
        return None._cparts >= other._cparts

    
    def __class_getitem__(cls, type):
        return cls

    drive = property(attrgetter('_drv'), 'The drive prefix (letter or UNC path), if any.', **('doc',))
    root = property(attrgetter('_root'), 'The root of the path, if any.', **('doc',))
    
    def anchor(self):
        """The concatenation of the drive and root, or ''."""
        anchor = self._drv + self._root
        return anchor

    anchor = property(anchor)
    
    def name(self):
        '''The final path component, if any.'''
        parts = self._parts
        if len(parts) == 1 if self._drv or self._root else 0:
            return ''
        return None[-1]

    name = property(name)
    
    def suffix(self):
        """
        The final component's last suffix, if any.

        This includes the leading period. For example: '.txt'
        """
        name = self.name
        i = name.rfind('.')
        if i < i or i < len(name) - 1:
            pass
        else:
            0
            return ''
        return 0[i:]
        return ''

    suffix = property(suffix)
    
    def suffixes(self):
        """
        A list of the final component's suffixes, if any.

        These include the leading periods. For example: ['.tar', '.gz']
        """
        name = self.name
        if name.endswith('.'):
            return []
        name = None.lstrip('.')
        return (lambda .0: [ '.' + suffix for suffix in .0 ])(name.split('.')[1:])

    suffixes = property(suffixes)
    
    def stem(self):
        '''The final path component, minus its last suffix.'''
        name = self.name
        i = name.rfind('.')
        if i < i or i < len(name) - 1:
            pass
        else:
            0
            return name
        return 0[:i]
        return name

    stem = property(stem)
    
    def with_name(self, name):
        '''Return a new path with the file name changed.'''
        if not self.name:
            raise ValueError('%r has an empty name' % (self,))
        (drv, root, parts) = None._flavour.parse_parts((name,))
        if name and name[-1] in (self._flavour.sep, self._flavour.altsep) and drv and root or len(parts) != 1:
            raise ValueError('Invalid name %r' % name)
        return None._from_parsed_parts(self._drv, self._root, self._parts[:-1] + [
            name])

    
    def with_stem(self, stem):
        '''Return a new path with the stem changed.'''
        return self.with_name(stem + self.suffix)

    
    def with_suffix(self, suffix):
        '''Return a new path with the file suffix changed.  If the path
        has no suffix, add given suffix.  If the given suffix is an empty
        string, remove the suffix from the path.
        '''
        f = self._flavour
        if (f.sep in suffix or f.altsep) and f.altsep in suffix:
            raise ValueError('Invalid suffix %r' % (suffix,))
        if None or suffix.startswith('.') or suffix == '.':
            raise ValueError('Invalid suffix %r' % suffix)
        name = None.name
        if not name:
            raise ValueError('%r has an empty name' % (self,))
        old_suffix = None.suffix
        if not old_suffix:
            name = name + suffix
        else:
            name = name[:-len(old_suffix)] + suffix
        return self._from_parsed_parts(self._drv, self._root, self._parts[:-1] + [
            name])

    
    def relative_to(self, *other):
        '''Return the relative path to another path identified by the passed
        arguments.  If the operation is not possible (because this is not
        a subpath of the other path), raise ValueError.
        '''
        if not other:
            raise TypeError('need at least one argument')
        parts = None._parts
        drv = self._drv
        root = self._root
        if root:
            abs_parts = [
                drv,
                root] + parts[1:]
        else:
            abs_parts = parts
        (to_drv, to_root, to_parts) = self._parse_args(other)
        if to_root:
            to_abs_parts = [
                to_drv,
                to_root] + to_parts[1:]
        else:
            to_abs_parts = to_parts
        n = len(to_abs_parts)
        cf = self._flavour.casefold_parts
        if n == 0:
            if root or drv:
                pass
            elif cf(abs_parts[:n]) != cf(to_abs_parts):
                formatted = self._format_parsed_parts(to_drv, to_root, to_parts)
                raise ValueError('{!r} is not in the subpath of {!r} OR one path is relative and the other is absolute.'.format(str(self), str(formatted)))
        return self._from_parsed_parts('', root if n == 1 else '', abs_parts[n:])

    
    def is_relative_to(self, *other):
        '''Return True if the path is relative to another path or False.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def parts(self):
        '''An object providing sequence-like access to the
        components in the filesystem path.'''
        pass
    # WARNING: Decompyle incomplete

    parts = property(parts)
    
    def joinpath(self, *args):
        '''Combine this path with one or several arguments, and return a
        new path representing either a subpath (if all arguments are relative
        paths) or a totally different path (if one of the arguments is
        anchored).
        '''
        return self._make_child(args)

    
    def __truediv__(self, key):
        pass
    # WARNING: Decompyle incomplete

    
    def __rtruediv__(self, key):
        pass
    # WARNING: Decompyle incomplete

    
    def parent(self):
        '''The logical parent of the path.'''
        drv = self._drv
        root = self._root
        parts = self._parts
        if len(parts) == 1:
            if drv or root:
                return self
            return None._from_parsed_parts(drv, root, parts[:-1])

    parent = property(parent)
    
    def parents(self):
        """A sequence of this path's logical parents."""
        return _PathParents(self)

    parents = property(parents)
    
    def is_absolute(self):
        '''True if the path is absolute (has both a root and, if applicable,
        a drive).'''
        if not self._root:
            return False
        if not not (None._flavour.has_drv):
            pass
        return bool(self._drv)

    
    def is_reserved(self):
        '''Return True if the path contains one of the special names reserved
        by the system, if any.'''
        return self._flavour.is_reserved(self._parts)

    
    def match(self, path_pattern):
        '''
        Return True if this path matches the given pattern.
        '''
        cf = self._flavour.casefold
        path_pattern = cf(path_pattern)
        (drv, root, pat_parts) = self._flavour.parse_parts((path_pattern,))
        if not pat_parts:
            raise ValueError('empty pattern')
        if None and drv != cf(self._drv):
            return False
        if None and root != cf(self._root):
            return False
        parts = None._cparts
        if drv or root:
            if len(pat_parts) != len(parts):
                return False
            pat_parts = None[1:]
        elif len(pat_parts) > len(parts):
            return False
        for part, pat in zip(reversed(parts), reversed(pat_parts)):
            if not fnmatch.fnmatchcase(part, pat):
                return False
            return True


os.PathLike.register(PurePath)

class PurePosixPath(PurePath):
    '''PurePath subclass for non-Windows systems.

    On a POSIX system, instantiating a PurePath should return this object.
    However, you can also instantiate it directly on any system.
    '''
    _flavour = _posix_flavour
    __slots__ = ()


class PureWindowsPath(PurePath):
    '''PurePath subclass for Windows systems.

    On a Windows system, instantiating a PurePath should return this object.
    However, you can also instantiate it directly on any system.
    '''
    _flavour = _windows_flavour
    __slots__ = ()


class Path(PurePath):
    '''PurePath subclass that can make system calls.

    Path represents a filesystem path but unlike PurePath, also offers
    methods to do system calls on path objects. Depending on your system,
    instantiating a Path will return either a PosixPath or a WindowsPath
    object. You can also instantiate a PosixPath or WindowsPath directly,
    but cannot instantiate a WindowsPath on a POSIX system or vice versa.
    '''
    _accessor = _normal_accessor
    __slots__ = ()
    
    def __new__(cls, *args, **kwargs):
        if cls is Path:
            cls = WindowsPath if os.name == 'nt' else PosixPath
        self = cls._from_parts(args)
        if not self._flavour.is_supported:
            raise NotImplementedError('cannot instantiate %r on your system' % (cls.__name__,))

    
    def _make_child_relpath(self, part):
        parts = self._parts + [
            part]
        return self._from_parsed_parts(self._drv, self._root, parts)

    
    def __enter__(self):
        return self

    
    def __exit__(self, t, v, tb):
        pass

    
    def cwd(cls):
        '''Return a new path pointing to the current working directory
        (as returned by os.getcwd()).
        '''
        return cls(cls._accessor.getcwd())

    cwd = classmethod(cwd)
    
    def home(cls):
        """Return a new path pointing to the user's home directory (as
        returned by os.path.expanduser('~')).
        """
        return cls('~').expanduser()

    home = classmethod(home)
    
    def samefile(self, other_path):
        '''Return whether other_path is the same or not as this file
        (as returned by os.path.samefile()).
        '''
        st = self.stat()
    # WARNING: Decompyle incomplete

    
    def iterdir(self):
        """Iterate over the files in this directory.  Does not yield any
        result for the special paths '.' and '..'.
        """
        for name in self._accessor.listdir(self):
            if name in frozenset({'..', '.'}):
                continue
            yield self._make_child_relpath(name)

    
    def glob(self, pattern):
        '''Iterate over this subtree and yield all existing files (of any
        kind, including directories) matching the given relative pattern.
        '''
        sys.audit('pathlib.Path.glob', self, pattern)
        if not pattern:
            raise ValueError('Unacceptable pattern: {!r}'.format(pattern))
        (drv, root, pattern_parts) = None._flavour.parse_parts((pattern,))
        if drv or root:
            raise NotImplementedError('Non-relative patterns are unsupported')
        selector = None(tuple(pattern_parts), self._flavour)
        for p in selector.select_from(self):
            yield p

    
    def rglob(self, pattern):
        '''Recursively yield all existing files (of any kind, including
        directories) matching the given relative pattern, anywhere in
        this subtree.
        '''
        sys.audit('pathlib.Path.rglob', self, pattern)
        (drv, root, pattern_parts) = self._flavour.parse_parts((pattern,))
        if drv or root:
            raise NotImplementedError('Non-relative patterns are unsupported')
        selector = None(('**',) + tuple(pattern_parts), self._flavour)
        for p in selector.select_from(self):
            yield p

    
    def absolute(self):
        """Return an absolute version of this path.  This function works
        even if the path doesn't point to anything.

        No normalization is done, i.e. all '.' and '..' will be kept along.
        Use resolve() to get the canonical path to a file.
        """
        if self.is_absolute():
            return self
        return None._from_parts([
            self._accessor.getcwd()] + self._parts)

    
    def resolve(self, strict = (False,)):
        '''
        Make the path absolute, resolving all symlinks on the way and also
        normalizing it (for example turning slashes into backslashes under
        Windows).
        '''
        
        def check_eloop(e):
            winerror = getattr(e, 'winerror', 0)
            if e.errno == ELOOP or winerror == _WINERROR_CANT_RESOLVE_FILENAME:
                raise RuntimeError('Symlink loop from %r' % e.filename)

    # WARNING: Decompyle incomplete

    
    def stat(self = None, *, follow_symlinks):
        '''
        Return the result of the stat() system call on this path, like
        os.stat() does.
        '''
        return self._accessor.stat(self, follow_symlinks, **('follow_symlinks',))

    
    def owner(self):
        '''
        Return the login name of the file owner.
        '''
        return self._accessor.owner(self)

    
    def group(self):
        '''
        Return the group name of the file gid.
        '''
        return self._accessor.group(self)

    
    def open(self, mode, buffering, encoding, errors, newline = ('r', -1, None, None, None)):
        '''
        Open the file pointed by this path and return a file object, as
        the built-in open() function does.
        '''
        if 'b' not in mode:
            encoding = io.text_encoding(encoding)
        return self._accessor.open(self, mode, buffering, encoding, errors, newline)

    
    def read_bytes(self):
        '''
        Open the file in bytes mode, read it, and close the file.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def read_text(self, encoding, errors = (None, None)):
        '''
        Open the file in text mode, read it, and close the file.
        '''
        encoding = io.text_encoding(encoding)
    # WARNING: Decompyle incomplete

    
    def write_bytes(self, data):
        '''
        Open the file in bytes mode, write to it, and close the file.
        '''
        view = memoryview(data)
    # WARNING: Decompyle incomplete

    
    def write_text(self, data, encoding, errors, newline = (None, None, None)):
        '''
        Open the file in text mode, write to it, and close the file.
        '''
        if not isinstance(data, str):
            raise TypeError('data must be str, not %s' % data.__class__.__name__)
        encoding = None.text_encoding(encoding)
    # WARNING: Decompyle incomplete

    
    def readlink(self):
        '''
        Return the path to which the symbolic link points.
        '''
        path = self._accessor.readlink(self)
        return self._from_parts((path,))

    
    def touch(self, mode, exist_ok = (438, True)):
        """
        Create this file with the given access mode, if it doesn't exist.
        """
        self._accessor.touch(self, mode, exist_ok)

    
    def mkdir(self, mode, parents, exist_ok = (511, False, False)):
        '''
        Create a new directory at this given path.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def chmod(self = None, mode = {
        'follow_symlinks': True }, *, follow_symlinks):
        '''
        Change the permissions of the path, like os.chmod().
        '''
        self._accessor.chmod(self, mode, follow_symlinks, **('follow_symlinks',))

    
    def lchmod(self, mode):
        """
        Like chmod(), except if the path points to a symlink, the symlink's
        permissions are changed, rather than its target's.
        """
        self.chmod(mode, False, **('follow_symlinks',))

    
    def unlink(self, missing_ok = (False,)):
        '''
        Remove this file or link.
        If the path is a directory, use rmdir() instead.
        '''
        pass
    # WARNING: Decompyle incomplete

    
    def rmdir(self):
        '''
        Remove this directory.  The directory must be empty.
        '''
        self._accessor.rmdir(self)

    
    def lstat(self):
        """
        Like stat(), except if the path points to a symlink, the symlink's
        status information is returned, rather than its target's.
        """
        return self.stat(False, **('follow_symlinks',))

    
    def rename(self, target):
        '''
        Rename this path to the target path.

        The target path may be absolute or relative. Relative paths are
        interpreted relative to the current working directory, *not* the
        directory of the Path object.

        Returns the new Path instance pointing to the target path.
        '''
        self._accessor.rename(self, target)
        return self.__class__(target)

    
    def replace(self, target):
        '''
        Rename this path to the target path, overwriting if that path e