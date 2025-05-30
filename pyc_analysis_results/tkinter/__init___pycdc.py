# Source Generated with Decompyle++
# File: __init__.pyc (Python 3.10)

__doc__ = 'Wrapper functions for Tcl/Tk.\n\nTkinter provides classes which allow the display, positioning and\ncontrol of widgets. Toplevel widgets are Tk and Toplevel. Other\nwidgets are Frame, Label, Entry, Text, Canvas, Button, Radiobutton,\nCheckbutton, Scale, Listbox, Scrollbar, OptionMenu, Spinbox\nLabelFrame and PanedWindow.\n\nProperties of the widgets are specified with keyword arguments.\nKeyword arguments have the same name as the corresponding resource\nunder Tk.\n\nWidgets are positioned with one of the geometry managers Place, Pack\nor Grid. These managers can be called with methods place, pack, grid\navailable in every Widget.\n\nActions are bound to events by resources (e.g. keyword argument\ncommand) or with the method bind.\n\nExample (Hello, World):\nimport tkinter\nfrom tkinter.constants import *\ntk = tkinter.Tk()\nframe = tkinter.Frame(tk, relief=RIDGE, borderwidth=2)\nframe.pack(fill=BOTH,expand=1)\nlabel = tkinter.Label(frame, text="Hello, World")\nlabel.pack(fill=X, expand=1)\nbutton = tkinter.Button(frame,text="Exit",command=tk.destroy)\nbutton.pack(side=BOTTOM)\ntk.mainloop()\n'
import enum
import sys
import types
import _tkinter
TclError = _tkinter.TclError
from tkinter.constants import *
import re
wantobjects = 1
TkVersion = float(_tkinter.TK_VERSION)
TclVersion = float(_tkinter.TCL_VERSION)
READABLE = _tkinter.READABLE
WRITABLE = _tkinter.WRITABLE
EXCEPTION = _tkinter.EXCEPTION
_magic_re = re.compile('([\\\\{}])')
_space_re = re.compile('([\\s])', re.ASCII)

def _join(value):
    '''Internal function.'''
    return ' '.join(map(_stringify, value))


def _stringify(value):
    '''Internal function.'''
    if isinstance(value, (list, tuple)):
        if len(value) == 1:
            value = _stringify(value[0])
            if _magic_re.search(value):
                value = '{%s}' % value
            return value
        value = None % _join(value)
        return value
    value = None(value)
    if not value:
        value = '{}'
        return value
    if None.search(value):
        value = _magic_re.sub('\\\\\\1', value)
        value = value.replace('\n', '\\n')
        value = _space_re.sub('\\\\\\1', value)
        if value[0] == '"':
            value = '\\' + value
        return value
    if None[0] == '"' or _space_re.search(value):
        value = '{%s}' % value
    return value


def _flatten(seq):
    '''Internal function.'''
    res = ()
    for item in seq:
        if isinstance(item, (tuple, list)):
            res = res + _flatten(item)
            continue
        if item is not None:
            res = res + (item,)
    return res

# WARNING: Decompyle incomplete
