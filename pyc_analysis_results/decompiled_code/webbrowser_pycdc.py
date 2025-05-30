# Source Generated with Decompyle++
# File: webbrowser.pyc (Python 3.10)

'''Interfaces for launching and remotely controlling web browsers.'''
import os
import shlex
import shutil
import sys
import subprocess
import threading
__all__ = [
    'Error',
    'open',
    'open_new',
    'open_new_tab',
    'get',
    'register']

class Error(Exception):
    pass

_lock = threading.RLock()
_browsers = { }
_tryorder = None
_os_preferred_browser = None

def register(name = None, klass = (None,), instance = {
    'preferred': False }, *, preferred):
    '''Register a browser connector.'''
    pass
# WARNING: Decompyle incomplete


def get(using = (None,)):
    '''Return a browser launcher instance appropriate for the environment.'''
    pass
# WARNING: Decompyle incomplete


def open(url, new, autoraise = (0, True)):
    '''Display url using the default browser.

    If possible, open url in a location determined by new.
    - 0: the same browser window (the default).
    - 1: a new browser window.
    - 2: a new browser page ("tab").
    If possible, autoraise raises the window (the default) or not.
    '''
    pass
# WARNING: Decompyle incomplete


def open_new(url):
    '''Open url in a new window of the default browser.

    If not possible, then open url in the only browser window.
    '''
    return open(url, 1)


def open_new_tab(url):
    '''Open url in a new page ("tab") of the default browser.

    If not possible, then the behavior becomes equivalent to open_new().
    '''
    return open(url, 2)


def _synthesize(browser = None, *, preferred):
    """Attempt to synthesize a controller based on existing controllers.

    This is useful to create a controller when a user specifies a path to
    an entry in the BROWSER environment variable -- we can copy a general
    controller to operate using a specific installation of the desired
    browser in this way.

    If we can't create a controller in this way, or if there is no
    executable for the requested browser, return [None, None].

    """
    cmd = browser.split()[0]
    if not shutil.which(cmd):
        return [
            None,
            None]
    name = None.path.basename(cmd)
# WARNING: Decompyle incomplete


class BaseBrowser(object):
    '''Parent class for all browsers. Do not use directly.'''
    args = [
        '%s']
    
    def __init__(self, name = ('',)):
        self.name = name
        self.basename = name

    
    def open(self, url, new, autoraise = (0, True)):
        raise NotImplementedError

    
    def open_new(self, url):
        return self.open(url, 1)

    
    def open_new_tab(self, url):
        return self.open(url, 2)



class GenericBrowser(BaseBrowser):
    '''Class for all browsers started with a command
       and without remote functionality.'''
    
    def __init__(self, name):
        if isinstance(name, str):
            self.name = name
            self.args = [
                '%s']
        else:
            self.name = name[0]
            self.args = name[1:]
        self.basename = os.path.basename(self.name)

    
    def open(self, url, new, autoraise = (0, True)):
        sys.audit('webbrowser.open', url)
        cmdline = None + (lambda .0 = None: [ arg.replace('%s', url) for arg in .0 ])(self.args)
    # WARNING: Decompyle incomplete



class BackgroundBrowser(GenericBrowser):
    '''Class for all browsers which are to be started in the
       background.'''
    
    def open(self, url, new, autoraise = (0, True)):
        cmdline = None + (lambda .0 = None: [ arg.replace('%s', url) for arg in .0 ])(self.args)
        sys.audit('webbrowser.open', url)
    # WARNING: Decompyle incomplete



class UnixBrowser(BaseBrowser):
    '''Parent class for all Unix browsers with remote functionality.'''
    raise_opts = None
    background = False
    redirect_stdout = True
    remote_args = [
        '%action',
        '%s']
    remote_action = None
    remote_action_newwin = None
    remote_action_newtab = None
    
    def _invoke(self, args, remote, autoraise, url = (None,)):
        raise_opt = []
        if remote and self.raise_opts:
            autoraise = int(autoraise)
            opt = self.raise_opts[autoraise]
            if opt:
                raise_opt = [
                    opt]
        cmdline = [
            self.name] + raise_opt + args
        if remote or self.background:
            inout = subprocess.DEVNULL
        else:
            inout = None
        if not self.redirect_stdout or inout:
            pass
        p = subprocess.Popen(cmdline, True, inout, None, inout, True, **('close_fds', 'stdin', 'stdout', 'stderr', 'start_new_session'))
    # WARNING: Decompyle incomplete

    
    def open(self, url, new, autoraise = (0, True)):
        sys.audit('webbrowser.open', url)
        if new == 0:
            action = self.remote_action
        elif new == 1:
            action = self.remote_action_newwin
        elif new == 2:
            if self.remote_action_newtab is None:
                action = self.remote_action_newwin
            else:
                action = self.remote_action_newtab
        else:
            raise Error("Bad 'new' parameter to open(); " + 'expected 0, 1, or 2, got %s' % new)
        args = (lambda .0 = None: [ arg.replace('%s', url).replace('%action', action) for arg in .0 ])(self.remote_args)
        args = (lambda .0: [ arg for arg in .0 if arg ])(args)
        success = self._invoke(args, True, autoraise, url)
        if not success:
            args = (lambda .0 = None: [ arg.replace('%s', url) for arg in .0 ])(self.args)
            return self._invoke(args, False, False)



class Mozilla(UnixBrowser):
    '''Launcher class for Mozilla browsers.'''
    remote_args = [
        '%action',
        '%s']
    remote_action = ''
    remote_action_newwin = '-new-window'
    remote_action_newtab = '-new-tab'
    background = True


class Netscape(UnixBrowser):
    '''Launcher class for Netscape browser.'''
    raise_opts = [
        '-noraise',
        '-raise']
    remote_args = [
        '-remote',
        'openURL(%s%action)']
    remote_action = ''
    remote_action_newwin = ',new-window'
    remote_action_newtab = ',new-tab'
    background = True


class Galeon(UnixBrowser):
    '''Launcher class for Galeon/Epiphany browsers.'''
    raise_opts = [
        '-noraise',
        '']
    remote_args = [
        '%action',
        '%s']
    remote_action = '-n'
    remote_action_newwin = '-w'
    background = True


class Chrome(UnixBrowser):
    '''Launcher class for Google Chrome browser.'''
    remote_args = [
        '%action',
        '%s']
    remote_action = ''
    remote_action_newwin = '--new-window'
    remote_action_newtab = ''
    background = True

Chromium = Chrome

class Opera(UnixBrowser):
    '''Launcher class for Opera browser.'''
    remote_args = [
        '%action',
        '%s']
    remote_action = ''
    remote_action_newwin = '--new-window'
    remote_action_newtab = ''
    background = True


class Elinks(UnixBrowser):
    '''Launcher class for Elinks browsers.'''
    remote_args = [
        '-remote',
        'openURL(%s%action)']
    remote_action = ''
    remote_action_newwin = ',new-window'
    remote_action_newtab = ',new-tab'
    background = False
    redirect_stdout = False


class Konqueror(BaseBrowser):
    '''Controller for the KDE File Manager (kfm, or Konqueror).

    See the output of ``kfmclient --commands``
    for more information on the Konqueror remote-control interface.
    '''
    
    def open(self, url, new, autoraise = (0, True)):
        sys.audit('webbrowser.open', url)
        if new == 2:
            action = 'newTab'
        else:
            action = 'openURL'
        devnull = subprocess.DEVNULL
    # WARNING: Decompyle incomplete



class Grail(BaseBrowser):
    
    def _find_grail_rc(self):
        import glob
        import pwd
        import socket
        import tempfile
        tempdir = os.path.join(tempfile.gettempdir(), '.grail-unix')
        user = pwd.getpwuid(os.getuid())[0]
        filename = os.path.join(glob.escape(tempdir), glob.escape(user) + '-*')
        maybes = glob.glob(filename)
        if not maybes:
            return None
        s = None.socket(socket.AF_UNIX, socket.SOCK_STREAM)
    # WARNING: Decompyle incomplete

    
    def _remote(self, action):
        s = self._find_grail_rc()
        if not s:
            return 0
        None.send(action)
        s.close()
        return 1

    
    def open(self, url, new, autoraise = (0, True)):
        sys.audit('webbrowser.open', url)
        if new:
            ok = self._remote('LOADNEW ' + url)
            return ok
        ok = None._remote('LOAD ' + url)
        return ok



def register_X_browsers():
    if shutil.which('xdg-open'):
        register('xdg-open', None, BackgroundBrowser('xdg-open'))
    if 'GNOME_DESKTOP_SESSION_ID' in os.environ and shutil.which('gvfs-open'):
        register('gvfs-open', None, BackgroundBrowser('gvfs-open'))
    if 'GNOME_DESKTOP_SESSION_ID' in os.environ and shutil.which('gnome-open'):
        register('gnome-open', None, BackgroundBrowser('gnome-open'))
    if 'KDE_FULL_SESSION' in os.environ and shutil.which('kfmclient'):
        register('kfmclient', Konqueror, Konqueror('kfmclient'))
    if shutil.which('x-www-browser'):
        register('x-www-browser', None, BackgroundBrowser('x-www-browser'))
    for browser in ('firefox', 'iceweasel', 'iceape', 'seamonkey'):
        if shutil.which(browser):
            register(browser, None, Mozilla(browser))
    for browser in ('mozilla-firefox', 'mozilla-firebird', 'firebird', 'mozilla', 'netscape'):
        if shutil.which(browser):
            register(browser, None, Netscape(browser))
    if shutil.which('kfm'):
        register('kfm', Konqueror, Konqueror('kfm'))
    elif shutil.which('konqueror'):
        register('konqueror', Konqueror, Konqueror('konqueror'))
    for browser in ('galeon', 'epiphany'):
        if shutil.which(browser):
            register(browser, None, Galeon(browser))
    if shutil.which('skipstone'):
        register('skipstone', None, BackgroundBrowser('skipstone'))
    for browser in ('google-chrome', 'chrome', 'chromium', 'chromium-browser'):
        if shutil.which(browser):
            register(browser, None, Chrome(browser))
    if shutil.which('opera'):
        register('opera', None, Opera('opera'))
    if shutil.which('mosaic'):
        register('mosaic', None, BackgroundBrowser('mosaic'))
    if shutil.which('grail'):
        register('grail', Grail, None)
        return None


def register_standard_browsers():
    global _tryorder
    _tryorder = []
    if sys.platform == 'darwin':
        register('MacOSX', None, MacOSXOSAScript('default'))
        register('chrome', None, MacOSXOSAScript('chrome'))
        register('firefox', None, MacOSXOSAScript('firefox'))
        register('safari', None, MacOSXOSAScript('safari'))
    if sys.platform == 'serenityos':
        register('Browser', None, BackgroundBrowser('Browser'))
    if sys.platform[:3] == 'win':
        register('windows-default', WindowsDefault)
        iexplore = os.path.join(os.environ.get('PROGRAMFILES', 'C:\\Program Files'), 'Internet Explorer\\IEXPLORE.EXE')
        for browser in ('firefox', 'firebird', 'seamonkey', 'mozilla', 'netscape', 'opera', iexplore):
            if shutil.which(browser):
                register(browser, None, BackgroundBrowser(browser))
# WARNING: Decompyle incomplete

if sys.platform[:3] == 'win':
    
    class WindowsDefault(BaseBrowser):
        
        def open(self, url, new, autoraise = (0, True)):
            sys.audit('webbrowser.open', url)
        # WARNING: Decompyle incomplete


if sys.platform == 'darwin':
    
    class MacOSX(BaseBrowser):
        '''Launcher class for Aqua browsers on Mac OS X

        Optionally specify a browser name on instantiation.  Note that this
        will not work for Aqua browsers if the user has moved the application
        package after installation.

        If no browser is specified, the default browser, as specified in the
        Internet System Preferences panel, will be used.
        '''
        
        def __init__(self, name):
            self.name = name

        
        def open(self, url, new, autoraise = (0, True)):
            sys.audit('webbrowser.open', url)
        # WARNING: Decompyle incomplete


    
    class MacOSXOSAScript(BaseBrowser):
        
        def __init__(self, name):
            self._name = name

        
        def open(self, url, new, autoraise = (0, True)):
            if self._name == 'default':
                script = 'open location "%s"' % url.replace('"', '%22')
            else:
                script = '\n                   tell application "%s"\n                       activate\n                       open location "%s"\n                   end\n                   ' % (self._name, url.replace('"', '%22'))
            osapipe = os.popen('osascript', 'w')
            if osapipe is None:
                return False
            None.write(script)
            rc = osapipe.close()
            return not rc



def main():
    import getopt
    usage = 'Usage: %s [-n | -t] url\n    -n: open new window\n    -t: open new tab' % sys.argv[0]
# WARNING: Decompyle incomplete

if __name__ == '__main__':
    main()
    return None
