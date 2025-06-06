# Source Generated with Decompyle++
# File: _compression.pyc (Python 3.10)

'''Internal classes used by the gzip, lzma and bz2 modules'''
import io
import sys
BUFFER_SIZE = io.DEFAULT_BUFFER_SIZE

class BaseStream(io.BufferedIOBase):
    '''Mode-checking helper functions.'''
    
    def _check_not_closed(self):
        if self.closed:
            raise ValueError('I/O operation on closed file')

    
    def _check_can_read(self):
        if not self.readable():
            raise io.UnsupportedOperation('File not open for reading')

    
    def _check_can_write(self):
        if not self.writable():
            raise io.UnsupportedOperation('File not open for writing')

    
    def _check_can_seek(self):
        if not self.readable():
            raise io.UnsupportedOperation('Seeking is only supported on files open for reading')
        if not None.seekable():
            raise io.UnsupportedOperation('The underlying file object does not support seeking')



class DecompressReader(io.RawIOBase):
    '''Adapts the decompressor API to a RawIOBase reader API'''
    
    def readable(self):
        return True

    
    def __init__(self, fp, decomp_factory, trailing_error = ((),), **decomp_args):
        self._fp = fp
        self._eof = False
        self._pos = 0
        self._size = -1
        self._decomp_factory = decomp_factory
        self._decomp_args = decomp_args
    # WARNING: Decompyle incomplete

    
    def close(self = None):
        self._decompressor = None
        return super().close()

    
    def seekable(self):
        return self._fp.seekable()

    
    def readinto(self, b):
        pass
    # WARNING: Decompyle incomplete

    
    def read(self, size = (-1,)):
        if size < 0:
            return self.readall()
        if None or self._eof:
            return b''
        data = None
    # WARNING: Decompyle incomplete

    
    def readall(self):
        chunks = []
        if data = self.read(sys.maxsize):
            chunks.append(data)
            if not data = self.read(sys.maxsize):
                return b''.join(chunks)

    
    def _rewind(self):
        self._fp.seek(0)
        self._eof = False
        self._pos = 0
    # WARNING: Decompyle incomplete

    
    def seek(self, offset, whence = (io.SEEK_SET,)):
        if whence == io.SEEK_SET:
            pass
        elif whence == io.SEEK_CUR:
            offset = self._pos + offset
        elif whence == io.SEEK_END:
            if self._size < 0 and self.read(io.DEFAULT_BUFFER_SIZE):
                if not self.read(io.DEFAULT_BUFFER_SIZE):
                    offset = self._size + offset
                else:
                    raise ValueError('Invalid value for whence: {}'.format(whence))
                if None < self._pos:
                    self._rewind()
                else:
                    offset -= self._pos
        if offset > 0:
            data = self.read(min(io.DEFAULT_BUFFER_SIZE, offset))
            if not data:
                return self._pos
            None -= len(data)
            if not offset > 0:
                return self._pos

    
    def tell(self):
        '''Return the current file position.'''
        return self._pos

    __classcell__ = None

