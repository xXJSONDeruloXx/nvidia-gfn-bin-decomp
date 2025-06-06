# Module Import Dependencies

## .py

- `import time`
- `import calendar`

## _abc

- `import abc`
- `import warnings`

## _adapters

- `import re`
- `import textwrap`
- `import email.message as email`
- `from _text import FoldedCase`

## _bootstrap

- `import implementation is desired.`
- `import _frozen_importlib_external`

## _bootstrap_external

- `import _imp`
- `import _io`
- `import sys`
- `import _warnings`
- `import marshal`
- `import nt as _os`
- `import winreg`
- `import posix as _os`

## _collections

- `import collections`

## _compression

- `import io`
- `import sys`

## _encoded_words

- `import re`
- `import base64`
- `import binascii`
- `import functools`
- `from string import ascii_letters, digits`
- `from email import errors`

## _functools

- `import types`
- `import functools`

## _header_value_parser

- `import re`
- `import sys`
- `import urllib`
- `from string import hexdigits`
- `from operator import itemgetter`
- `from email import _encoded_words as _ew`
- `from email import errors`
- `from email import utils`

## _itertools

- `from itertools import filterfalse`

## _meta

- `from typing import Any, Dict, Iterator, List, Protocol, TypeVar, Union`

## _parseaddr

- `import time`
- `import calendar`

## _policybase

- `import abc`
- `from email import header`
- `from email import charset as _charset`
- `from email.utils import _has_surrogates`

## _py_abc

- `from _weakrefset import WeakSet`

## _pydecimal

- `import math as _math`
- `import numbers as _numbers`
- `import sys`

## _strptime

- `import time`
- `import locale`
- `import calendar`
- `from re import compile as re_compile`
- `from re import IGNORECASE`
- `from re import escape as re_escape`
- `from datetime import date as datetime_date, timedelta as datetime_timedelta, timezone as datetime_timezone`
- `from _thread import allocate_lock as _thread_allocate_lock`

## _text

- `import re`
- `from _functools import method_cache`

## _threading_local

- `from weakref import ref`
- `from contextlib import contextmanager`
- `from threading import current_thread, RLock`

## argparse

- `import os as _os`
- `import re as _re`
- `import sys as _sys`

## base64

- `import re`
- `import struct`
- `import binascii`
- `import sys`
- `import getopt`

## base64mime

- `from base64 import b64encode`
- `from binascii import b2a_base64, a2b_base64`

## bz2

- `from builtins import open as _builtin_open`
- `import io`
- `import os`
- `import _compression`
- `from _bz2 import BZ2Compressor, BZ2Decompressor`

## calendar

- `import sys`
- `import datetime`
- `import locale as _locale`
- `from itertools import repeat`
- `import argparse`

## charset

- `from functools import partial`
- `import email.base64mime as email`
- `import email.quoprimime as email`
- `from email import errors`
- `from email.encoders import encode_7or8bit`

## contentmanager

- `import binascii`
- `import email.charset as email`
- `import email.message as email`
- `import email.errors as email`
- `from email import quoprimime`

## contextlib

- `import abc`
- `import sys`
- `import _collections_abc`
- `from collections import deque`
- `from functools import wraps`
- `from types import MethodType, GenericAlias`

## contextvars

- `from _contextvars import Context, ContextVar, Token, copy_context`

## copy

- `import types`
- `import weakref`
- `from copyreg import dispatch_table`

## csv

- `import re`
- `from _csv import Error, __version__, writer, reader, register_dialect, unregister_dialect, get_dialect, list_dialects, field_size_limit, QUOTE_MINIMAL, QUOTE_ALL, QUOTE_NONNUMERIC, QUOTE_NONE, __doc__`
- `from _csv import Dialect as _Dialect`
- `from io import StringIO`

## dataclasses

- `import re`
- `import sys`
- `import copy`
- `import types`
- `import inspect`
- `import keyword`
- `import builtins`
- `import functools`
- `import abc`
- `import _thread`
- `from types import FunctionType, GenericAlias`

## datetime

- `import time as _time`
- `import math as _math`
- `import sys`
- `from operator import index as _index`

## decoder

- `import re`
- `from json import scanner`

## dis

- `import sys`
- `import types`
- `import collections`
- `import io`
- `from opcode import *`
- `from opcode import __all__ as _opcodes_all`
- `import argparse`

## encoder

- `import re`

## feedparser

- `import re`
- `from email import errors`
- `from email._policybase import compat32`
- `from collections import deque`
- `from io import StringIO`
- `import email.message`

## fnmatch

- `import os`
- `import posixpath`
- `import re`
- `import functools`
- `from itertools import count`

## fractions

- `from decimal import Decimal`
- `import math`
- `import numbers`
- `import operator`
- `import re`
- `import sys`
- `import decimal`

## generator

- `import re`
- `import sys`
- `import time`
- `import random`
- `from copy import deepcopy`
- `from io import StringIO, BytesIO`
- `from email.utils import _has_surrogates`
- `from email.errors import HeaderWriteError`

## getopt

- `import os`

## gettext

- `import os`
- `import re`
- `import sys`

## glob

- `import contextlib`
- `import os`
- `import re`
- `import fnmatch`
- `import itertools`
- `import stat`
- `import sys`

## gzip

- `import struct`
- `import sys`
- `import time`
- `import os`
- `import zlib`
- `import builtins`
- `import io`
- `import _compression`
- `import warnings`
- `import warnings`
- `import errno`
- `import errno`
- `import errno`
- `import errno`
- `import argparse`

## header

- `import re`
- `import binascii`
- `import email.quoprimime as email`
- `import email.base64mime as email`
- `from email.errors import HeaderParseError`
- `from email import charset as _charset`

## headerregistry

- `from types import MappingProxyType`
- `from email import utils`
- `from email import errors`
- `from email import _header_value_parser as parser`

## inspect

- `import abc`
- `import ast`
- `import dis`
- `import collections.abc as collections`
- `import enum`
- `import importlib.machinery as importlib`
- `import itertools`
- `import linecache`
- `import os`
- `import re`
- `import sys`
- `import tokenize`
- `import token`
- `import types`
- `import warnings`
- `import functools`
- `import builtins`
- `from operator import attrgetter`
- `from collections import namedtuple, OrderedDict`

## install

- `import tkinter as tk`
- `from tkinter import ttk`
- `import time`
- `import os`
- `import sys`
- `import webbrowser`
- `from translate import Translate`

## ipaddress

- `import functools`

## iterators

- `import sys`
- `from io import StringIO`

## lzma

- `import builtins`
- `import io`
- `import os`
- `from _lzma import *`
- `from _lzma import _encode_filter_properties, _decode_filter_properties`
- `import _compression`

## machinery

- `from _bootstrap import ModuleSpec`
- `from _bootstrap import BuiltinImporter`
- `from _bootstrap import FrozenImporter`
- `from _bootstrap_external import SOURCE_SUFFIXES, DEBUG_BYTECODE_SUFFIXES, OPTIMIZED_BYTECODE_SUFFIXES, BYTECODE_SUFFIXES, EXTENSION_SUFFIXES`
- `from _bootstrap_external import WindowsRegistryFinder`
- `from _bootstrap_external import PathFinder`
- `from _bootstrap_external import FileFinder`
- `from _bootstrap_external import SourceFileLoader`
- `from _bootstrap_external import SourcelessFileLoader`
- `from _bootstrap_external import ExtensionFileLoader`

## numbers

- `from abc import ABCMeta, abstractmethod`

## optparse

- `import sys`
- `import os`
- `import textwrap`

## parse

- `import re`
- `import sys`
- `import types`
- `import collections`
- `import warnings`
- `import ipaddress`
- `from collections import namedtuple`
- `import unicodedata`

## parser

- `from io import StringIO, TextIOWrapper`
- `from email.feedparser import FeedParser, BytesFeedParser`
- `from email._policybase import compat32`

## pathlib

- `import fnmatch`
- `import functools`
- `import io`
- `import ntpath`
- `import os`
- `import posixpath`
- `import re`
- `import sys`
- `import warnings`
- `from _collections_abc import Sequence`
- `from errno import EINVAL, ENOENT, ENOTDIR, EBADF, ELOOP`
- `from operator import attrgetter`
- `from stat import S_ISDIR, S_ISLNK, S_ISREG, S_ISSOCK, S_ISBLK, S_ISCHR, S_ISFIFO`
- `from urllib.parse import quote_from_bytes as urlquote_from_bytes`

## pickle

- `from types import FunctionType`
- `from copyreg import dispatch_table`
- `from copyreg import _extension_registry, _inverted_registry, _extension_cache`
- `from itertools import islice`
- `from functools import partial`
- `import sys`
- `from sys import maxsize`
- `from struct import pack, unpack`
- `import re`
- `import io`
- `import codecs`
- `import _compat_pickle`

## platform

- `import collections`
- `import os`
- `import re`
- `import sys`
- `import subprocess`
- `import functools`
- `import itertools`
- `import subprocess`

## policy

- `import re`
- `import sys`
- `from email._policybase import Policy, Compat32, compat32, _extend_docstrings`
- `from email.utils import _has_surrogates`
- `from email.headerregistry import HeaderRegistry`
- `from email.contentmanager import raw_data_manager`
- `from email.message import EmailMessage`

## pprint

- `import collections as _collections`
- `import dataclasses as _dataclasses`
- `import re`
- `import sys as _sys`
- `import types as _types`
- `from io import StringIO as _StringIO`
- `import time`

## py_compile

- `import enum`
- `import importlib._bootstrap_external as importlib`
- `import importlib.machinery as importlib`
- `import importlib.util as importlib`
- `import os`
- `import os.path as os`
- `import sys`
- `import traceback`
- `import argparse`

## quoprimime

- `import re`
- `from string import ascii_letters, digits, hexdigits`

## random

- `from warnings import warn as _warn`
- `from math import log as _log, exp as _exp, pi as _pi, e as _e, ceil as _ceil`
- `from math import sqrt as _sqrt, acos as _acos, cos as _cos, sin as _sin`
- `from math import tau as TWOPI, floor as _floor, isfinite as _isfinite`
- `from os import urandom as _urandom`
- `from _collections_abc import Set as _Set, Sequence as _Sequence`
- `from operator import index as _index`
- `from itertools import accumulate as _accumulate, repeat as _repeat`
- `from bisect import bisect as _bisect`
- `import os as _os`
- `import _random`

## readers

- `import collections`
- `import zipfile`
- `import pathlib`

## scanner

- `import re`

## selectors

- `from abc import ABCMeta, abstractmethod`
- `from collections import namedtuple`
- `from collections.abc import Mapping`
- `import math`
- `import select`
- `import sys`

## shlex

- `import os`
- `import re`
- `import sys`
- `from collections import deque`
- `from io import StringIO`
- `import warnings`

## shutil

- `import os`
- `import sys`
- `import stat`
- `import fnmatch`
- `import collections`
- `import errno`

## signal

- `import _signal`
- `from _signal import *`
- `from enum import IntEnum as _IntEnum`

## socket

- `import _socket`
- `from _socket import *`
- `import os`
- `import sys`
- `import io`
- `import selectors`
- `from enum import IntEnum, IntFlag`

## statistics

- `import math`
- `import numbers`
- `import random`
- `from fractions import Fraction`
- `from decimal import Decimal`
- `from itertools import groupby, repeat`
- `from bisect import bisect_left, bisect_right`
- `from math import hypot, sqrt, fabs, exp, erf, tau, log, fsum`
- `from operator import itemgetter`
- `from collections import Counter, namedtuple`

## string

- `import _string`
- `import re as _re`
- `from collections import ChainMap as _ChainMap`

## stringprep

- `from unicodedata import ucd_3_2_0 as unicodedata`

## subprocess

- `import builtins`
- `import errno`
- `import io`
- `import os`
- `import time`
- `import signal`
- `import sys`
- `import threading`
- `import warnings`
- `import contextlib`
- `from time import monotonic as _time`
- `import types`

## tarfile

- `from builtins import open as bltn_open`
- `import sys`
- `import os`
- `import io`
- `import shutil`
- `import stat`
- `import time`
- `import struct`
- `import copy`
- `import re`
- `import warnings`

## tempfile

- `import functools as _functools`
- `import warnings as _warnings`
- `import io as _io`
- `import os as _os`

## textwrap

- `import re`

## threading

- `import os as _os`
- `import sys as _sys`
- `import _thread`
- `import functools`
- `from time import monotonic as _time`
- `from _weakrefset import WeakSet`
- `from itertools import islice as _islice, count as _count`

## tokenize

- `from builtins import open as _builtin_open`
- `from codecs import lookup, BOM_UTF8`
- `import collections`
- `import functools`
- `from io import TextIOWrapper`
- `import itertools as _itertools`
- `import re`
- `import sys`
- `from token import *`
- `from token import EXACT_TOKEN_TYPES`
- `import token`

## tracemalloc

- `from collections.abc import Sequence, Iterable`
- `from functools import total_ordering`
- `import fnmatch`
- `import linecache`
- `import os.path as os`
- `import pickle`
- `from _tracemalloc import *`
- `from _tracemalloc import _get_object_traceback, _get_traces`

## translate

- `import os`
- `import sys`
- `import json`
- `import locale`
- `import logging`

## ttk

- `import tkinter`
- `from tkinter import _flatten, _join, _stringify, _splitdict`
- `import os`

## typing

- `from abc import abstractmethod, ABCMeta`
- `import collections`
- `import collections.abc as collections`
- `import contextlib`
- `import functools`
- `import operator`
- `import re as stdlib_re`
- `import sys`
- `import types`
- `from types import WrapperDescriptorType, MethodWrapperType, MethodDescriptorType, GenericAlias`
- `from typing import NoReturn`

## utils

- `import os`
- `import re`
- `import time`
- `import random`
- `import socket`
- `import datetime`
- `import urllib.parse as urllib`
- `from email._parseaddr import quote`
- `from email._parseaddr import AddressList as _AddressList`
- `from email._parseaddr import mktime_tz`
- `from email._parseaddr import parsedate, parsedate_tz, _parsedate_tz`
- `from email.charset import Charset`

## uu

- `import binascii`
- `import os`
- `import sys`
- `import optparse`

## vdict

- `import sys`
- `from collections import Counter`
- `from collections.abc import abc as _c`

## webbrowser

- `import os`
- `import shlex`
- `import shutil`
- `import sys`
- `import subprocess`
- `import threading`
- `import glob`
- `import pwd`
- `import socket`
- `import tempfile`
- `import getopt`

## zipfile

- `import binascii`
- `import importlib.util as importlib`
- `import io`
- `import itertools`
- `import os`
- `import posixpath`
- `import re`
- `import shutil`
- `import stat`
- `import struct`
- `import sys`
- `import threading`
- `import time`
- `import contextlib`
- `import pathlib`

