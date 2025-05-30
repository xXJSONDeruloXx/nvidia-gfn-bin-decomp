# Source Generated with Decompyle++
# File: py_compile.pyc (Python 3.10)

'''Routine to "compile" a .py file to a .pyc file.

This module has intimate knowledge of the format of .pyc files.
'''
import enum
import importlib._bootstrap_external as importlib
import importlib.machinery as importlib
import importlib.util as importlib
import os
import os.path as os
import sys
import traceback
__all__ = [
    'compile',
    'main',
    'PyCompileError',
    'PycInvalidationMode']

class PyCompileError(Exception):
    """Exception raised when an error occurs while attempting to
    compile the file.

    To raise this exception, use

        raise PyCompileError(exc_type,exc_value,file[,msg])

    where

        exc_type:   exception type to be used in error message
                    type name can be accesses as class variable
                    'exc_type_name'

        exc_value:  exception value to be used in error message
                    can be accesses as class variable 'exc_value'

        file:       name of file being compiled to be used in error message
                    can be accesses as class variable 'file'

        msg:        string message to be written as error message
                    If no value is given, a default exception message will be
                    given, consistent with 'standard' py_compile output.
                    message (or default) can be accesses as class variable
                    'msg'

    """
    
    def __init__(self, exc_type, exc_value, file, msg = ('',)):
        exc_type_name = exc_type.__name__
        if exc_type is SyntaxError:
            tbtext = ''.join(traceback.format_exception_only(exc_type, exc_value))
            errmsg = tbtext.replace('File "<string>"', 'File "%s"' % file)
        else:
            errmsg = 'Sorry: %s: %s' % (exc_type_name, exc_value)
        if not msg:
            pass
        Exception.__init__(self, errmsg, exc_type_name, exc_value, file)
        self.exc_type_name = exc_type_name
        self.exc_value = exc_value
        self.file = file
        if not msg:
            pass
        self.msg = errmsg

    
    def __str__(self):
        return self.msg



class PycInvalidationMode(enum.Enum):
    TIMESTAMP = 1
    CHECKED_HASH = 2
    UNCHECKED_HASH = 3


def _get_default_invalidation_mode():
    if os.environ.get('SOURCE_DATE_EPOCH'):
        return PycInvalidationMode.CHECKED_HASH
    return None.TIMESTAMP


def compile(file, cfile, dfile, doraise, optimize, invalidation_mode, quiet = (None, None, False, -1, None, 0)):
    """Byte-compile one Python source file to Python bytecode.

    :param file: The source file name.
    :param cfile: The target byte compiled file name.  When not given, this
        defaults to the PEP 3147/PEP 488 location.
    :param dfile: Purported file name, i.e. the file name that shows up in
        error messages.  Defaults to the source file name.
    :param doraise: Flag indicating whether or not an exception should be
        raised when a compile error is found.  If an exception occurs and this
        flag is set to False, a string indicating the nature of the exception
        will be printed, and the function will return to the caller. If an
        exception occurs and this flag is set to True, a PyCompileError
        exception will be raised.
    :param optimize: The optimization level for the compiler.  Valid values
        are -1, 0, 1 and 2.  A value of -1 means to use the optimization
        level of the current interpreter, as given by -O command line options.
    :param invalidation_mode:
    :param quiet: Return full output with False or 0, errors only with 1,
        and no output with 2.

    :return: Path to the resulting byte compiled file.

    Note that it isn't necessary to byte-compile Python modules for
    execution efficiency -- Python itself byte-compiles a module when
    it is loaded, and if it can, writes out the bytecode to the
    corresponding .pyc file.

    However, if a Python installation is shared between users, it is a
    good idea to byte-compile all modules upon installation, since
    other users may not be able to write in the source directories,
    and thus they won't be able to write the .pyc file, and then
    they would be byte-compiling every module each time it is loaded.
    This can slow down program start-up considerably.

    See compileall.py for a script/module that uses this module to
    byte-compile all installed files (or all files in selected
    directories).

    Do note that FileExistsError is raised if cfile ends up pointing at a
    non-regular file or symlink. Because the compilation uses a file renaming,
    the resulting file would be regular and thus not the same type of file as
    it was previously.
    """
    if invalidation_mode is None:
        invalidation_mode = _get_default_invalidation_mode()
    if cfile is None:
        if optimize >= 0:
            optimization = optimize if optimize >= 1 else ''
            cfile = importlib.util.cache_from_source(file, optimization, **('optimization',))
        else:
            cfile = importlib.util.cache_from_source(file)
    if os.path.islink(cfile):
        msg = '{} is a symlink and will be changed into a regular file if import writes a byte-compiled file to it'
        raise FileExistsError(msg.format(cfile))
    if not None.path.exists(cfile) and os.path.isfile(cfile):
        msg = '{} is a non-regular file and will be changed into a regular one if import writes a byte-compiled file to it'
        raise FileExistsError(msg.format(cfile))
    loader = None.machinery.SourceFileLoader('<py_compile>', file)
    source_bytes = loader.get_data(file)
# WARNING: Decompyle incomplete


def main():
    import argparse
    description = 'A simple command-line interface for py_compile module.'
    parser = argparse.ArgumentParser(description, **('description',))
    parser.add_argument('-q', '--quiet', 'store_true', 'Suppress error output', **('action', 'help'))
    parser.add_argument('filenames', '+', 'Files to compile', **('nargs', 'help'))
    args = parser.parse_args()
    if args.filenames == [
        '-']:
        filenames = (lambda .0: [ filename.rstrip('\n') for filename in .0 ])(sys.stdin.readlines())
    else:
        filenames = args.filenames
# WARNING: Decompyle incomplete

if __name__ == '__main__':
    main()
    return None
