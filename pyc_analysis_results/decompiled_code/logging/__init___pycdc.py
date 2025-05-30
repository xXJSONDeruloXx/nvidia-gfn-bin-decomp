# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.10)

"""
Logging package for Python. Based on PEP 282 and comments thereto in
comp.lang.python.

Copyright (C) 2001-2019 Vinay Sajip. All Rights Reserved.

To use, simply 'import logging' and log away!
"""
import sys
import os
import time
import io
import re
import traceback
import warnings
import weakref
import collections.abc as collections
from string import Template
from string import Formatter as StrFormatter
__all__ = [
    'BASIC_FORMAT',
    'BufferingFormatter',
    'CRITICAL',
    'DEBUG',
    'ERROR',
    'FATAL',
    'FileHandler',
    'Filter',
    'Formatter',
    'Handler',
    'INFO',
    'LogRecord',
    'Logger',
    'LoggerAdapter',
    'NOTSET',
    'NullHandler',
    'StreamHandler',
    'WARN',
    'WARNING',
    'addLevelName',
    'basicConfig',
    'captureWarnings',
    'critical',
    'debug',
    'disable',
    'error',
    'exception',
    'fatal',
    'getLevelName',
    'getLogger',
    'getLoggerClass',
    'info',
    'log',
    'makeLogRecord',
    'setLoggerClass',
    'shutdown',
    'warn',
    'warning',
    'getLogRecordFactory',
    'setLogRecordFactory',
    'lastResort',
    'raiseExceptions']
import threading
__author__ = 'Vinay Sajip <vinay_sajip@red-dove.com>'
__status__ = 'production'
__version__ = '0.5.1.2'
__date__ = '07 February 2010'
_startTime = time.time()
raiseExceptions = True
logThreads = True
logMultiprocessing = True
logProcesses = True
CRITICAL = 50
FATAL = CRITICAL
ERROR = 40
WARNING = 30
WARN = WARNING
INFO = 20
DEBUG = 10
NOTSET = 0
_levelToName = {
    NOTSET: 'NOTSET',
    DEBUG: 'DEBUG',
    INFO: 'INFO',
    WARNING: 'WARNING',
    ERROR: 'ERROR',
    CRITICAL: 'CRITICAL' }
_nameToLevel = {
    'CRITICAL': CRITICAL,
    'FATAL': FATAL,
    'ERROR': ERROR,
    'WARN': WARNING,
    'WARNING': WARNING,
    'INFO': INFO,
    'DEBUG': DEBUG,
    'NOTSET': NOTSET }

def getLevelName(level):
    """
    Return the textual or numeric representation of logging level 'level'.

    If the level is one of the predefined levels (CRITICAL, ERROR, WARNING,
    INFO, DEBUG) then you get the corresponding string. If you have
    associated levels with names using addLevelName then the name you have
    associated with 'level' is returned.

    If a numeric value corresponding to one of the defined levels is passed
    in, the corresponding string representation is returned.

    If a string representation of the level is passed in, the corresponding
    numeric value is returned.

    If no matching numeric or string value is passed in, the string
    'Level %s' % level is returned.
    """
    result = _levelToName.get(level)
    if result is not None:
        return result
    result = None.get(level)
    if result is not None:
        return result
    return None % level


def addLevelName(level, levelName):
    """
    Associate 'levelName' with 'level'.

    This is used when converting levels to text during message formatting.
    """
    _acquireLock()
# WARNING: Decompyle incomplete

if hasattr(sys, '_getframe'):
    
    currentframe = lambda : sys._getframe(3)
else:
    
    def currentframe():
        """Return the frame object for the caller's stack frame."""
        pass
    # WARNING: Decompyle incomplete

_srcfile = os.path.normcase(addLevelName.__code__.co_filename)

def _checkLevel(level):
    if isinstance(level, int):
        rv = level
        return rv
    if None(level) == level:
        if level not in _nameToLevel:
            raise ValueError('Unknown level: %r' % level)
        rv = None[level]
        return rv
    raise None('Level not an integer or a valid string: %r' % (level,))

_lock = threading.RLock()

def _acquireLock():
    '''
    Acquire the module-level lock for serializing access to shared data.

    This should be released with _releaseLock().
    '''
    if _lock:
        _lock.acquire()
        return None


def _releaseLock():
    '''
    Release the module-level lock acquired by calling _acquireLock().
    '''
    if _lock:
        _lock.release()
        return None

if not hasattr(os, 'register_at_fork'):
    
    def _register_at_fork_reinit_lock(instance):
        pass

else:
    _at_fork_reinit_lock_weakset = weakref.WeakSet()
    
    def _register_at_fork_reinit_lock(instance):
        _acquireLock()
    # WARNING: Decompyle incomplete

    
    def _after_at_fork_child_reinit_locks():
        for handler in _at_fork_reinit_lock_weakset:
            handler._at_fork_reinit()
        _lock._at_fork_reinit()

    os.register_at_fork(_acquireLock, _after_at_fork_child_reinit_locks, _releaseLock, **('before', 'after_in_child', 'after_in_parent'))

class LogRecord(object):
    '''
    A LogRecord instance represents an event being logged.

    LogRecord instances are created every time something is logged. They
    contain all the information pertinent to the event being logged. The
    main information passed in is in msg and args, which are combined
    using str(msg) % args to create the message field of the record. The
    record also includes information such as when the record was created,
    the source line where the logging call was made, and any exception
    information to be logged.
    '''
    
    def __init__(self, name, level, pathname, lineno, msg, args, exc_info, func, sinfo = (None, None), **kwargs):
        '''
        Initialize a logging record with interesting information.
        '''
        ct = time.time()
        self.name = name
        self.msg = msg
        if args and len(args) == 1 and isinstance(args[0], collections.abc.Mapping) and args[0]:
            args = args[0]
        self.args = args
        self.levelname = getLevelName(level)
        self.levelno = level
        self.pathname = pathname
    # WARNING: Decompyle incomplete

    
    def __repr__(self):
        return '<LogRecord: %s, %s, %s, %s, "%s">' % (self.name, self.levelno, self.pathname, self.lineno, self.msg)

    
    def getMessage(self):
        '''
        Return the message for this LogRecord.

        Return the message for this LogRecord after merging any user-supplied
        arguments with the message.
        '''
        msg = str(self.msg)
        if self.args:
            msg = msg % self.args
        return msg


_logRecordFactory = LogRecord

def setLogRecordFactory(factory):
    '''
    Set the factory to be used when instantiating a log record.

    :param factory: A callable which will be called to instantiate
    a log record.
    '''
    global _logRecordFactory
    _logRecordFactory = factory


def getLogRecordFactory():
    '''
    Return the factory to be used when instantiating a log record.
    '''
    return _logRecordFactory


def makeLogRecord(dict):
    '''
    Make a LogRecord whose attributes are defined by the specified dictionary,
    This function is useful for converting a logging event received over
    a socket connection (which is sent as a dictionary) into a LogRecord
    instance.
    '''
    rv = _logRecordFactory(None, None, '', 0, '', (), None, None)
    rv.__dict__.update(dict)
    return rv

_str_formatter = StrFormatter()
del StrFormatter

class PercentStyle(object):
    default_format = '%(message)s'
    asctime_format = '%(asctime)s'
    asctime_search = '%(asctime)'
    validation_pattern = re.compile('%\\(\\w+\\)[#0+ -]*(\\*|\\d+)?(\\.(\\*|\\d+))?[diouxefgcrsa%]', re.I)
    
    def __init__(self = None, fmt = {
        'defaults': None }, *, defaults):
        if not fmt:
            pass
        self._fmt = self.default_format
        self._defaults = defaults

    
    def usesTime(self):
        return self._fmt.find(self.asctime_search) >= 0

    
    def validate(self):
        '''Validate the input format, ensure it matches the correct style'''
        if not self.validation_pattern.search(self._fmt):
            raise ValueError("Invalid format '%s' for '%s' style" % (self._fmt, self.default_format[0]))

    
    def _format(self, record):
        return self._fmt % values

    
    def format(self, record):
        pass
    # WARNING: Decompyle incomplete



class StrFormatStyle(PercentStyle):
    default_format = '{mes