# Source Generated with Decompyle++
# File: feedparser.pyc (Python 3.10)

"""FeedParser - An email feed parser.

The feed parser implements an interface for incrementally parsing an email
message, line by line.  This has advantages for certain applications, such as
those reading email messages off a socket.

FeedParser.feed() is the primary interface for pushing new data into the
parser.  It returns when there's nothing more it can do with the available
data.  When you have no more data to push into the parser, call .close().
This completes the parsing and returns the root message object.

The other advantage of this parser is that it will never raise a parsing
exception.  Instead, when it finds something unexpected, it adds a 'defect' to
the current message.  Defects are just instances that live on the message
object's .defects attribute.
"""
__all__ = [
    'FeedParser',
    'BytesFeedParser']
import re
from email import errors
from email._policybase import compat32
from collections import deque
from io import StringIO
NLCRE = re.compile('\\r\\n|\\r|\\n')
NLCRE_bol = re.compile('(\\r\\n|\\r|\\n)')
NLCRE_eol = re.compile('(\\r\\n|\\r|\\n)\\Z')
NLCRE_crack = re.compile('(\\r\\n|\\r|\\n)')
headerRE = re.compile('^(From |[\\041-\\071\\073-\\176]*:|[\\t ])')
EMPTYSTRING = ''
NL = '\n'
NeedMoreData = object()

class BufferedSubFile(object):
    '''A file-ish object that can have new data loaded into it.

    You can also push and pop line-matching predicates onto a stack.  When the
    current predicate matches the current line, a false EOF response
    (i.e. empty string) is returned instead.  This lets the parser adhere to a
    simple abstraction -- it parses until EOF closes the current message.
    '''
    
    def __init__(self):
        self._partial = StringIO('', **('newline',))
        self._lines = deque()
        self._eofstack = []
        self._closed = False

    
    def push_eof_matcher(self, pred):
        self._eofstack.append(pred)

    
    def pop_eof_matcher(self):
        return self._eofstack.pop()

    
    def close(self):
        self._partial.seek(0)
        self.pushlines(self._partial.readlines())
        self._partial.seek(0)
        self._partial.truncate()
        self._closed = True

    
    def readline(self):
        if not self._lines:
            if self._closed:
                return ''
            return None
        line = None._lines.popleft()
        for ateof in reversed(self._eofstack):
            if ateof(line):
                self._lines.appendleft(line)
                return ''
            return line

    
    def unreadline(self, line):
        pass
    # WARNING: Decompyle incomplete

    
    def push(self, data):
        '''Push some new data into this object.'''
        self._partial.write(data)
        if '\n' not in data and '\r' not in data:
            return None
        None._partial.seek(0)
        parts = self._partial.readlines()
        self._partial.seek(0)
        self._partial.truncate()
        if not parts[-1].endswith('\n'):
            self._partial.write(parts.pop())
        self.pushlines(parts)

    
    def pushlines(self, lines):
        self._lines.extend(lines)

    
    def __iter__(self):
        return self

    
    def __next__(self):
        line = self.readline()
        if line == '':
            raise StopIteration



class FeedParser:
    '''A feed-style parser of email.'''
    
    def __init__(self = None, _factory = (None,), *, policy):
        """_factory is called with no arguments to create a new message obj

        The policy keyword specifies a policy object that controls a number of
        aspects of the parser's operation.  The default policy maintains
        backward compatibility.

        """
        self.policy = policy
        self._old_style_factory = False
        if _factory is None:
            if policy.message_factory is None:
                Message = Message
                import email.message
                self._factory = Message
            else:
                self._factory = policy.message_factory
    # WARNING: Decompyle incomplete

    
    def _set_headersonly(self):
        self._headersonly = True

    
    def feed(self, data):
        '''Push more data into the parser.'''
        self._input.push(data)
        self._call_parse()

    
    def _call_parse(self):
        pass
    # WARNING: Decompyle incomplete

    
    def close(self):
        '''Parse all remaining data and return the root message object.'''
        self._input.close()
        self._call_parse()
        root = self._pop_message()
    # WARNING: Decompyle incomplete

    
    def _new_message(self):
        if self._old_style_factory:
            msg = self._factory()
        else:
            msg = self._factory(self.policy, **('policy',))
        if self._cur and self._cur.get_content_type() == 'multipart/digest':
            msg.set_default_type('message/rfc822')
        if self._msgstack:
            self._msgstack[-1].attach(msg)
        self._msgstack.append(msg)
        self._cur = msg
        self._last = msg

    
    def _pop_message(self):
        retval = self._msgstack.pop()
        if self._msgstack:
            self._cur = self._msgstack[-1]
            return retval
        self._cur = None
        return retval

    
    def _parsegen(self):
        self._new_message()
        headers = []
        for line in self._input:
            if line is NeedMoreData:
                yield NeedMoreData
                continue
            if not headerRE.match(line):
                if not NLCRE.match(line):
                    defect = errors.MissingHeaderBodySeparatorDefect()
                    self.policy.handle_defect(self._cur, defect)
                    self._input.unreadline(line)
            else:
                headers.append(line)
            self._parse_headers(headers)
            if self._headersonly:
                lines = []
                line = self._input.readline()
                if line is NeedMoreData:
                    yield NeedMoreData
                    continue
                if line == '':
                    pass
                else:
                    lines.append(line)
                self._cur.set_payload(EMPTYSTRING.join(lines))
                return None
            if None._cur.get_content_type() == 'message/delivery-status':
                self._input.push_eof_matcher(NLCRE.match)
                for retval in self._parsegen():
                    if retval is NeedMoreData:
                        yield NeedMoreData
                        continue
                    msg = self._pop_message()
                    self._input.pop_eof_matcher()
                    line = self._input.readline()
                    if line is NeedMoreData:
                        yield NeedMoreData
                        continue
                line = self._input.readline()
                if line is NeedMoreData:
                    yield NeedMoreData
                    continue
                if line == '':
                    return None
                None._input.unreadline(line)
                continue
    # WARNING: Decompyle incomplete

    
    def _parse_headers(self, lines):
        lastheader = ''
        lastvalue = []
    # WARNING: Decompyle incomplete



class BytesFeedParser(FeedParser):
    '''Like FeedParser, but feed accepts bytes.'''
    
    def feed(self = None, data = None):
        super().feed(data.decode('ascii', 'surrogateescape'))

    __classcell__ = None

