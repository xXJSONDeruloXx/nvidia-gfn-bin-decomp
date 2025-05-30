# Source Generated with Decompyle++
# File: shlex.pyc (Python 3.10)

__doc__ = 'A lexical analyzer class for simple shell-like syntaxes.'
import os
import re
import sys
from collections import deque
from io import StringIO
__all__ = [
    'shlex',
    'split',
    'quote',
    'join']

class shlex:
    '''A lexical analyzer class for simple shell-like syntaxes.'''
    
    def __init__(self, instream, infile, posix, punctuation_chars = (None, None, False, False)):
        if isinstance(instream, str):
            instream = StringIO(instream)
        if instream is not None:
            self.instream = instream
            self.infile = infile
        else:
            self.instream = sys.stdin
            self.infile = None
        self.posix = posix
        if posix:
            self.eof = None
        else:
            self.eof = ''
        self.commenters = '#'
        self.wordchars = 'abcdfeghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ0123456789_'
        if self.posix:
            self.wordchars += 'ßàáâãäåæçèéêëìíîïðñòóôõöøùúûüýþÿÀÁÂÃÄÅÆÇÈÉÊËÌÍÎÏÐÑÒÓÔÕÖØÙÚÛÜÝÞ'
        self.whitespace = ' \t\r\n'
        self.whitespace_split = False
        self.quotes = '\'"'
        self.escape = '\\'
        self.escapedquotes = '"'
        self.state = ' '
        self.pushback = deque()
        self.lineno = 1
        self.debug = 0
        self.token = ''
        self.filestack = deque()
        self.source = None
        if not punctuation_chars:
            punctuation_chars = ''
        elif punctuation_chars is True:
            punctuation_chars = '();<>|&'
        self._punctuation_chars = punctuation_chars
        if punctuation_chars:
            self._pushback_chars = deque()
            self.wordchars += '~-./*?='
            t = self.wordchars.maketrans(dict.fromkeys(punctuation_chars))
            self.wordchars = self.wordchars.translate(t)
            return None
        return self

    
    def punctuation_chars(self):
        return self._punctuation_chars

    punctuation_chars = property(punctuation_chars)
    
    def push_token(self, tok):
        '''Push a token onto the stack popped by the get_token method'''
        if self.debug >= 1:
            print('shlex: pushing token ' + repr(tok))
        self.pushback.appendleft(tok)

    
    def push_source(self, newstream, newfile = (None,)):
        """Push an input source onto the lexer's input source stack."""
        if isinstance(newstream, str):
            newstream = StringIO(newstream)
        self.filestack.appendleft((self.infile, self.instream, self.lineno))
        self.infile = newfile
        self.instream = newstream
        self.lineno = 1
        if self.debug:
            if newfile is not None:
                print('shlex: pushing to file %s' % (self.infile,))
                return None
            None('shlex: pushing to stream %s' % (self.instream,))
            return None

    
    def pop_source(self):
        '''Pop the input source stack.'''
        self.instream.close()
        (self.infile, self.instream, self.lineno) = self.filestack.popleft()
        if self.debug:
            print('shlex: popping to %s, line %d' % (self.instream, self.lineno))
        self.state = ' '

    
    def get_token(self):
        """Get a token from the input stream (or from stack if it's nonempty)"""
        if self.pushback:
            tok = self.pushback.popleft()
            if self.debug >= 1:
                print('shlex: popping token ' + repr(tok))
            return tok
        raw = None.read_token()
        if self.source is not None and raw == self.source:
            spec = self.sourcehook(self.read_token())
            if spec:
                (newfile, newstream) = spec
                self.push_source(newstream, newfile)
            raw = self.get_token()
            if raw == self.source or raw == self.eof:
                if not self.filestack:
                    return self.eof
                None.pop_source()
                raw = self.get_token()
                if raw == self.eof or self.debug >= 1:
                    if raw != self.eof:
                        print('shlex: token=' + repr(raw))
                        return raw
                    None('shlex: token=EOF')
        return raw

    
    def read_token(self):
        quoted = False
        escapedstate = ' '
        if self.punctuation_chars and self._pushback_chars:
            nextchar = self._pushback_chars.pop()
        else:
            nextchar = self.instream.read(1)
        if nextchar == '\n':
            self.lineno += 1
        if self.debug >= 3:
            print('shlex: in state %r I see character: %r' % (self.state, nextchar))
        if self.state is None:
            self.token = ''
        elif self.state == ' ':
            if not nextchar:
                self.state = None
            elif nextchar in self.whitespace:
                if self.debug >= 2:
                    print('shlex: I see whitespace in whitespace state')
                if (self.token or self.posix) and quoted:
                    pass
                
            if nextchar in self.commenters:
                self.instream.readline()
                self.lineno += 1
            elif self.posix and nextchar in self.escape:
                escapedstate = 'a'
                self.state = nextchar
            elif nextchar in self.wordchars:
                self.token = nextchar
                self.state = 'a'
            elif nextchar in self.punctuation_chars:
                self.token = nextchar
                self.state = 'c'
            elif nextchar in self.quotes:
                if not self.posix:
                    self.token = nextchar
                self.state = nextchar
            elif self.whitespace_split:
                self.token = nextchar
                self.state = 'a'
            else:
                self.token = nextchar
                if (self.token or self.posix) and quoted:
                    pass
                
                if self.state in self.quotes:
                    quoted = True
                    if not nextchar:
                        if self.debug >= 2:
                            print('shlex: I see EOF in quotes state')
                        raise ValueError('No closing quotation')
                    if self == self.state:
                        if not self.posix:
                            self.token += nextchar
                            self.state = ' '
                        else:
                            self.state = 'a'
                    elif self.posix and nextchar in self.escape and self.state in self.escapedquotes:
                        escapedstate = self.state
                        self.state = nextchar
                    else:
                        self.token += nextchar
                elif self.state in self.escape:
                    if not nextchar:
                        if self.debug >= 2:
                            print('shlex: I see EOF in escape state')
                        raise ValueError('No escaped character')
                    if self in self.quotes and nextchar != self.state and nextchar != escapedstate:
                        self.token += self.state
                    self.token += nextchar
                    self.state = escapedstate
                elif self.state in ('a', 'c'):
                    if not nextchar:
                        self.state = None
                    elif nextchar in self.whitespace:
                        if self.debug >= 2:
                            print('shlex: I see whitespace in word state')
                        self.state = ' '
                        if (self.token or self.posix) and quoted:
                            pass
                        
                    if nextchar in self.commenters:
                        self.instream.readline()
                        self.lineno += 1
                        if self.posix:
                            self.state = ' '
                            if (self.token or self.posix) and quoted:
                                pass
                            
                        elif self.state == 'c':
                            if nextchar in self.punctuation_chars:
                                self.token += nextchar
                            elif nextchar not in self.whitespace:
                                self._pushback_chars.append(nextchar)
                            self.state = ' '
                        elif self.posix and nextchar in self.quotes:
                            self.state = nextchar
                        elif self.posix and nextchar in self.escape:
                            escapedstate = 'a'
                            self.state = nextchar
                        elif (nextchar in self.wordchars and nextchar in self.quotes or self.whitespace_split) and nextchar not in self.punctuation_chars:
                            self.token += nextchar
                        elif self.punctuation_chars:
                            self._pushback_chars.append(nextchar)
                        else:
                            self.pushback.appendleft(nextchar)
                    if self.debug >= 2:
                        print('shlex: I see punctuation in word state')
                    self.state = ' '
                    if (self.token or self.posix) and quoted:
                        pass
                    
        continue
        result = self.token
        self.token = ''
        if self.posix and quoted and result == '':
            result = None
        if self.debug > 1:
            if result:
                print('shlex: raw token=' + repr(result))
                return result
            self('shlex: raw token=EOF')
        return result

    
    def sourcehook(self, newfile):
        '''Hook called on a filename to be sourced.'''
        if newfile[0] == '"':
            newfile = newfile[1:-1]
        if not isinstance(self.infile, str) and os.path.isabs(newfile):
            newfile = os.path.join(os.path.dirname(self.infile), newfile)
        return (newfile, open(newfile, 'r'))

    
    def error_leader(self, infile, lineno = (None, None)):
        '''Emit a C-compiler-like, Emacs-friendly error-message leader.'''
        if infile is None:
            infile = self.infile
        if lineno is None:
            lineno = self.lineno
        return '"%s", line %d: ' % (infile, lineno)

    
    def __iter__(self):
        return self

    
    def __next__(self):
        token = self.get_token()
        if token == self.eof:
            raise StopIteration



def split(s, comments, posix = (False, True)):
    '''Split the string *s* using shell-like syntax.'''
    if s is None:
        import warnings
        warnings.warn("Passing None for 's' to shlex.split() is deprecated.", DeprecationWarning, 2, **('stacklevel',))
    lex = shlex(s, posix, **('posix',))
    lex.whitespace_split = True
    if not comments:
        lex.commenters = ''
    return list(lex)


def join(split_command):
    '''Return a shell-escaped string from *split_command*.'''
    return ' '.join((lambda .0: for arg in .0:
quote(arg))(split_command))

_find_unsafe = re.compile('[^\\w@%+=:,./-]', re.ASCII).search

def quote(s):
    '''Return a shell-escaped version of the string *s*.'''
    if not s:
        return "''"
    if None(s) is None:
        return s
    return None + s.replace("'", '\'"\'"\'') + "'"


def _print_tokens(lexer):
    tt = lexer.get_token()
    if not tt:
        return None
    None('Token: ' + repr(tt))
    continue

# WARNING: Decompyle incomplete
