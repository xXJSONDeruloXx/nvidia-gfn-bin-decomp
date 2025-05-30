# Source Generated with Decompyle++
# File: argparse.pyc (Python 3.10)

__doc__ = "Command-line parsing library\n\nThis module is an optparse-inspired command-line parsing library that:\n\n    - handles both optional and positional arguments\n    - produces highly informative usage messages\n    - supports parsers that dispatch to sub-parsers\n\nThe following is a simple usage example that sums integers from the\ncommand-line and writes the result to a file::\n\n    parser = argparse.ArgumentParser(\n        description='sum the integers at the command line')\n    parser.add_argument(\n        'integers', metavar='int', nargs='+', type=int,\n        help='an integer to be summed')\n    parser.add_argument(\n        '--log', default=sys.stdout, type=argparse.FileType('w'),\n        help='the file where the sum should be written')\n    args = parser.parse_args()\n    args.log.write('%s' % sum(args.integers))\n    args.log.close()\n\nThe module contains the following public classes:\n\n    - ArgumentParser -- The main entry point for command-line parsing. As the\n        example above shows, the add_argument() method is used to populate\n        the parser with actions for optional and positional arguments. Then\n        the parse_args() method is invoked to convert the args at the\n        command-line into an object with attributes.\n\n    - ArgumentError -- The exception raised by ArgumentParser objects when\n        there are errors with the parser's actions. Errors raised while\n        parsing the command-line are caught by ArgumentParser and emitted\n        as command-line messages.\n\n    - FileType -- A factory for defining types of files to be created. As the\n        example above shows, instances of FileType are typically passed as\n        the type= argument of add_argument() calls.\n\n    - Action -- The base class for parser actions. Typically actions are\n        selected by passing strings like 'store_true' or 'append_const' to\n        the action= argument of add_argument(). However, for greater\n        customization of ArgumentParser actions, subclasses of Action may\n        be defined and passed as the action= argument.\n\n    - HelpFormatter, RawDescriptionHelpFormatter, RawTextHelpFormatter,\n        ArgumentDefaultsHelpFormatter -- Formatter classes which\n        may be passed as the formatter_class= argument to the\n        ArgumentParser constructor. HelpFormatter is the default,\n        RawDescriptionHelpFormatter and RawTextHelpFormatter tell the parser\n        not to change the formatting for help text, and\n        ArgumentDefaultsHelpFormatter adds information about argument defaults\n        to the help.\n\nAll other classes in this module are considered implementation details.\n(Also note that HelpFormatter and RawDescriptionHelpFormatter are only\nconsidered public as object names -- the API of the formatter objects is\nstill considered an implementation detail.)\n"
__version__ = '1.1'
__all__ = [
    'ArgumentParser',
    'ArgumentError',
    'ArgumentTypeError',
    'BooleanOptionalAction',
    'FileType',
    'HelpFormatter',
    'ArgumentDefaultsHelpFormatter',
    'RawDescriptionHelpFormatter',
    'RawTextHelpFormatter',
    'MetavarTypeHelpFormatter',
    'Namespace',
    'Action',
    'ONE_OR_MORE',
    'OPTIONAL',
    'PARSER',
    'REMAINDER',
    'SUPPRESS',
    'ZERO_OR_MORE']
import os as _os
import re as _re
import sys as _sys
# WARNING: Decompyle incomplete
