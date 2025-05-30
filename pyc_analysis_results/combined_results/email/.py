# Source Generated with Decompyle++
# File: _parseaddr.pyc (Python 3.10)

'''Email address parsing code.

Lifted directly from rfc822.py.  This should eventually be rewritten.
'''
__all__ = [
    'mktime_tz',
    'parsedate',
    'parsedate_tz',
    'quote']
import time
import calendar
SPACE = ' '
EMPTYSTRING = ''
COMMASPACE = ', '
_monthnames = [
    'jan',
    'feb',
    'mar',
    'apr',
    'may',
    'jun',
    'jul',
    'aug',
    'sep',
    'oct',
    'nov',
    'dec',
    'january',
    'february',
    'march',
    'april',
    'may',
    'june',
    'july',
    'august',
    'september',
    'october',
    'november',
    'december']
_daynames = [
    'mon',
    'tue',
    'wed',
    'thu',
    'fri',
    'sat',
    'sun']
_timezones = {
    'UT': 0,
    'UTC': 0,
    'GMT': 0,
    'Z': 0,
    'AST': -400,
    'ADT': -300,
    'EST': -500,
    'EDT': -400,
    'CST': -600,
    'CDT': -500,
    'MST': -700,
    'MDT': -600,
    'PST': -800,
    'PDT': -700 }

def parsedate_tz(data):
    '''Convert a date string to a time tuple.

    Accounts for military timezones.
    '''
    res = _parsedate_tz(data)
    if not res:
        return None
    if None[9] is None:
        res[9] = 0
    return tuple(res)


def _parsedate_tz(data):
    '''Convert date to extended time tuple.

    The last (additional) element is the time zone offset in seconds, except if
    the timezone was specified as -0000.  In that case the last element is
    None.  This indicates a UTC timestamp that explicitly declaims knowledge of
    the source timezone, as opposed to a +0000 timestamp that indicates the
    source timezone really was UTC.

    '''
    if not data:
        return None
    data = None.split()
    if not data:
        return None
    if None[0].endswith(',') or data[0].lower() in _daynames:
        del data[0]
    else:
        i = data[0].rfind(',')
        if i >= 0:
            data[0] = data[0][i + 1:]
    if len(data) == 3:
        stuff = data[0].split('-')
        if len(stuff) == 3:
            data = stuff + data[1:]
    if len(data) == 4:
        s = data[3]
        i = s.find('+')
        if i == -1:
            i = s.find('-')
        if i > 0:
            data[3:] = [
                s[:i],
                s[i:]]
        else:
            data.append('')
    if len(data) < 5:
        return None
    data = None[:5]
    (dd, mm, yy, tm, tz) = data
    if not dd and mm or yy:
        return None
    mm = None.lower()
    if mm not in _monthnames:
        dd = mm
        mm = dd.lower()
        if mm not in _monthnames:
            return None
        mm = None.index(mm) + 1
        if mm > 12:
            mm -= 12
    if dd[-1] == ',':
        dd = dd[:-1]
    i = yy.find(':')
    if i > 0:
        yy = tm
        tm = yy
    if yy[-1] == ',':
        yy = yy[:-1]
        if not yy:
            return None
        if not None[0].isdigit():
            yy = tz
            tz = yy
    if tm[-1] == ',':
        tm = tm[:-1]
    tm = tm.split(':')
    if len(tm) == 2:
        (thh, tmm) = tm
        tss = '0'
    elif len(tm) == 3:
        (thh, tmm, tss) = tm
# WARNING: Decompyle incomplete


def parsedate(data):
    '''Convert a time string to a time tuple.'''
    t = parsedate_tz(data)
    if isinstance(t, tuple):
        return t[:9]


def mktime_tz(data):
    '''Turn a 10-tuple as returned by parsedate_tz() into a POSIX timestamp.'''
    if data[9] is None:
        return time.mktime(data[:8] + (-1,))
    t = None.timegm(data)
    return t - data[9]


def quote(str):
    '''Prepare string to be used in a quoted string.

    Turns backslash and double quote characters into quoted pairs.  These
    are the only characters that need to be quoted inside a quoted string.
    Does not add the surrounding double quotes.
    '''
    return str.replace('\\', '\\\\').replace('"', '\\"')


class AddrlistClass:
    '''Address parser class by Ben Escoto.

    To understand what this class does, it helps to have a copy of RFC 2822 in
    front of you.

    Note: this class interface is deprecated and may be removed in the future.
    Use email.utils.AddressList instead.
    '''
    
    def __init__(self, field):
        """Initialize a new instance.

        `field' is an unparsed address header field, containing
        one or more addresses.
        """
        self.specials = '()<>@,:;."[]'
        self.pos = 0
        self.LWS = ' \t'
        self.CR = '\r\n'
        self.FWS = self.LWS + self.CR
        self.atomends = self.specials + self.LWS + self.CR
        self.phraseends = self.atomends.replace('.', '')
        self.field = field
        self.commentlist = []

    
    def gotonext(self):
        '''Skip white space and extract comments.'''
        wslist = []
        if self.pos < len(self.field):
            if self.field[self.pos] in self.LWS + '\n\r':
                if self.field[self.pos] not in '\n\r':
                    wslist.append(self.field[self.pos])
                self.pos += 1
            elif self.field[self.pos] == '(':
                self.commentlist.append(self.getcomment())
            
        elif not self.pos < len(self.field):
            return EMPTYSTRING.join(wslist)

    
    def getaddrlist(self):
        '''Parse all addresses.

        Returns a list containing all of the addresses.
        '''
        result = []
        if self.pos < len(self.field):
            ad = self.getaddress()
            if ad:
                result += ad
            else:
                result.append(('', ''))
            if not self.pos < len(self.field):
                return result

    
    def getaddress(self):
        '''Parse the next address.'''
        self.commentlist = []
        self.gotonext()
        oldpos = self.pos
        oldcl = self.commentlist
        plist = self.getphraselist()
        self.gotonext()
        returnlist = []
        if self.pos >= len(self.field):
            if plist:
                returnlist = [
                    (SPACE.join(self.commentlist), plist[0])]
            elif self.field[self.pos] in '.@':
                self.pos = oldpos
                self.commentlist = oldcl
                addrspec = self.getaddrspec()
                returnlist = [
                    (SPACE.join(self.commentlist), addrspec)]
            elif self.field[self.pos] == ':':
                returnlist = []
                fieldlen = len(self.field)
                self.pos += 1
                if self.pos < len(self.field):
                    self.gotonext()
        self.gotonext()
        if self.pos < len(self.field) and self.field[self.pos] == ',':
            self.pos += 1
        return returnlist

    
    def getrouteaddr(self):
        '''Parse a route address (Return-path value).

        This method just skips all the route stuff and returns the addrspec.
        '''
        if self.field[self.pos] != '<':
            return None
        expectroute = None
        self.pos += 1
        self.gotonext()
        adlist = ''
        if self.pos < len(self.field):
            if expectroute:
                self.getdomain()
                expectroute = False
            elif self.field[self.pos] == '>':
                self.pos += 1
                return adlist
            if self.field[self.pos] == '@':
                self.pos += 1
                expectroute = True
            elif self.field[self.pos] == ':':
                self.pos += 1
            else:
                adlist = self.getaddrspec()
                self.pos += 1
                return adlist
            self.gotonext()
            if not self.pos < len(self.field):
                return adlist

    
    def getaddrspec(self):
        '''Parse an RFC 2822 addr-spec.'''
        aslist = []
        self.gotonext()
        if self.pos < len(self.field):
            preserve_ws = True
            if self.field[self.pos] == '.':
                if not aslist and aslist[-1].strip():
                    aslist.pop()
                aslist.append('.')
                self.pos += 1
                preserve_ws = False
            elif self.field[self.pos] == '"':
                aslist.append('"%s"' % quote(self.getquote()))
            elif self.field[self.pos] in self.atomends:
                if not aslist and aslist[-1].strip():
                    aslist.pop()
                else:
                    aslist.append(self.getatom())
                    ws = self.gotonext()
                    if preserve_ws and ws:
                        aslist.append(ws)
                    if self.pos < len(self.field) or self.pos >= len(self.field) or self.field[self.pos] != '@':
                        return EMPTYSTRING.join(aslist)
                    self.append('@')
                    self.pos += 1
                    self.gotonext()
                    domain = self.getdomain()
                    if not domain:
                        return EMPTYSTRING
                    return self.join(aslist) + domain

    
    def getdomain(self):
        '''Get the complete domain name from an address.'''
        sdlist = []
        if self.pos < len(self.field):
            if self.field[self.pos] in self.LWS:
                self.pos += 1
            elif self.field[self.pos] == '(':
                self.commentlist.append(self.getcomment())
            elif self.field[self.pos] == '[':
                sdlist.append(self.getdomainliteral())
            elif self.field[self.pos] == '.':
                self.pos += 1
                sdlist.append('.')
            elif self.field[self.pos] == '@':
                return EMPTYSTRING
            if self.field[self.pos] in self.atomends:
                pass
            else:
                sdlist.append(self.getatom())
                if not self.pos < len(self.field):
                    return EMPTYSTRING.join(sdlist)

    
    def getdelimited(self, beginchar, endchars, allowcomments = (True,)):
        """Parse a header fragment delimited by special characters.

        `beginchar' is the start character for the fragment.
        If self is not looking at an instance of `beginchar' then
        getdelimited returns the empty string.

        `endchars' is a sequence of allowable end-delimiting characters.
        Parsing stops when one of these is encountered.

        If `allowcomments' is non-zero, embedded RFC 2822 comments are allowed
        within the parsed fragment.
        """
        if self.field[self.pos] != beginchar:
            return ''
        slist = [
            None]
        quote = False
        self.pos += 1
        if self.pos < len(self.field):
            if quote:
                slist.append(self.field[self.pos])
                quote = False
            elif self.field[self.pos] in endchars:
                self.pos += 1
            elif allowcomments and self.field[self.pos] == '(':
                slist.append(self.getcomment())
                continue
            self.pos += 1
            if not self.pos < len(self.field):
                return EMPTYSTRING.join(slist)

    
    def getquote(self):
        """Get a quote-delimited fragment from self's field."""
        return self.getdelimited('"', '"\r', False)

    
    def getcomment(self):
        """Get a parenthesis-delimited fragment from self's field."""
        return self.getdelimited('(', ')\r', True)

    
    def getdomainliteral(self):
        '''Parse an RFC 2822 domain-literal.'''
        return '[%s]' % self.getdelimited('[', ']\r', False)

    
    def getatom(self, atomends = (None,)):
        """Parse an RFC 2822 atom.

        Optional atomends specifies a different set of end token delimiters
        (the default is to use self.atomends).  This is used e.g. in
        getphraselist() since phrase endings must not include the `.' (which
        is legal in phrases)."""
        atomlist = [
            '']
        if atomends is None:
            atomends = self.atomends
        if self.pos < len(self.field):
            if self.field[self.pos] in atomends:
                pass
            else:
                atomlist.append(self.field[self.pos])
                self.pos += 1
                if not self.pos < len(self.field):
                    return EMPTYSTRING.join(atomlist)

    
    def getphraselist(self):
        '''Parse a sequence of RFC 2822 phrases.

        A phrase is a sequence of words, which are in turn either RFC 2822
        atoms or quoted-strings.  Phrases are canonicalized by squeezing all
        runs of continuous whitespace into one space.
        '''
        plist = []
        if self.pos < len(self.field):
            if self.field[self.pos] in self.FWS:
                self.pos += 1
            elif self.field[self.pos] == '"':
                plist.append(self.getquote())
            elif self.field[self.pos] == '(':
                self.commentlist.append(self.getcomment())
            elif self.field[self.pos] in self.phraseends:
                return plist
            plist.append(self.getatom(self.phraseends))
            if not self.pos < len(self.field):
                return plist



class AddressList(AddrlistClass):
    '''An AddressList encapsulates a list of parsed RFC 2822 addresses.'''
    
    def __init__(self, field):
        AddrlistClass.__init__(self, field)
        if field:
            self.addresslist = self.getaddrlist()
            return None
        self.addresslist = None

    
    def __len__(self):
        return len(self.addresslist)

    
    def __add__(self, other):
        newaddr = AddressList(None)
        newaddr.addresslist = self.addresslist[:]
        for x in other.addresslist:
            if x not in self.addresslist:
                newaddr.addresslist.append(x)
        return newaddr

    
    def __iadd__(self, other):
        for x in other.addresslist:
            if x not in self.addresslist:
                self.addresslist.append(x)
        return self

    
    def __sub__(self, other):
        newaddr = AddressList(None)
        for x in self.addresslist:
            if x not in other.addresslist:
                newaddr.addresslist.append(x)
        return newaddr

    
    def __isub__(self, other):
        for x in other.addresslist:
            if x in self.addresslist:
                self.addresslist.remove(x)
        return self

    
    def __getitem__(self, index):
        return self.addresslist[index]


