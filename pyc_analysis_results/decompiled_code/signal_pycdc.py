# Source Generated with Decompyle++
# File: signal.pyc (Python 3.10)

import _signal
from _signal import *
from enum import IntEnum as _IntEnum
_globals = globals()
_IntEnum._convert_('Signals', __name__, (lambda name: if name.isupper():
if not name.startswith('SIG') and not name.startswith('SIG_'):
passname.startswith('CTRL_')))
_IntEnum._convert_('Handlers', __name__, (lambda name: name in ('SIG_DFL', 'SIG_IGN')))
if 'pthread_sigmask' in _globals:
    _IntEnum._convert_('Sigmasks', __name__, (lambda name: name in ('SIG_BLOCK', 'SIG_UNBLOCK', 'SIG_SETMASK')))

def _int_to_enum(value, enum_klass):
    """Convert a numeric value to an IntEnum member.
    If it's not a known member, return the numeric value itself.
    """
    pass
# WARNING: Decompyle incomplete


def _enum_to_int(value):
    """Convert an IntEnum member to a numeric value.
    If it's not an IntEnum member return the value itself.
    """
    pass
# WARNING: Decompyle incomplete


def _wraps(wrapped):
    
    def decorator(wrapper = None):
        wrapper.__doc__ = wrapped.__doc__
        return wrapper

    return decorator


def signal(signalnum, handler):
    handler = _signal.signal(_enum_to_int(signalnum), _enum_to_int(handler))
    return _int_to_enum(handler, Handlers)

signal = _wraps(_signal.signal)(signal)

def getsignal(signalnum):
    handler = _signal.getsignal(signalnum)
    return _int_to_enum(handler, Handlers)

getsignal = _wraps(_signal.getsignal)(getsignal)
if 'pthread_sigmask' in _globals:
    
    def pthread_sigmask(how, mask):
        sigs_set = _signal.pthread_sigmask(how, mask)
        return set((lambda .0: for x in .0:
_int_to_enum(x, Signals))(sigs_set))

    pthread_sigmask = _wraps(_signal.pthread_sigmask)(pthread_sigmask)
if 'sigpending' in _globals:
    
    def sigpending():
        return (lambda .0: pass# WARNING: Decompyle incomplete
)(_signal.sigpending())

    sigpending = _wraps(_signal.sigpending)(sigpending)
if 'sigwait' in _globals:
    
    def sigwait(sigset):
        retsig = _signal.sigwait(sigset)
        return _int_to_enum(retsig, Signals)

    sigwait = _wraps(_signal.sigwait)(sigwait)
if 'valid_signals' in _globals:
    
    def valid_signals():
        return (lambda .0: pass# WARNING: Decompyle incomplete
)(_signal.valid_signals())

    valid_signals = _wraps(_signal.valid_signals)(valid_signals)
del _globals
del _wraps
