# Source Generated with Decompyle++
# File: readers.pyc (Python 3.10)

import collections
import zipfile
import pathlib
from  import abc

def remove_duplicates(items):
    return iter(collections.OrderedDict.fromkeys(items))


class FileReader(abc.TraversableResources):
    
    def __init__(self, loader):
        self.path = pathlib.Path(loader.path).parent

    
    def resource_path(self, resource):
        '''
        Return the file system path to prevent
        `resources.path()` from creating a temporary
        copy.
        '''
        return str(self.path.joinpath(resource))

    
    def files(self):
        return self.path



class ZipReader(abc.TraversableResources):
    
    def __init__(self, loader, module):
        (_, _, name) = module.rpartition('.')
        self.prefix = loader.prefix.replace('\\', '/') + name + '/'
        self.archive = loader.archive

    
    def open_resource(self = None, resource = None):
        pass
    # WARNING: Decompyle incomplete

    
    def is_resource(self, path):
        target = self.files().joinpath(path)
        if target.is_file():
            pass
        return target.exists()

    
    def files(self):
        return zipfile.Path(self.archive, self.prefix)

    __classcell__ = None


class MultiplexedPath(abc.Traversable):
    '''
    Given a series of Traversable objects, implement a merged
    version of the interface across all objects. Useful for
    namespace packages which may be multihomed at a single
    name.
    '''
    
    def __init__(self, *paths):
        self._paths = list(map(pathlib.Path, remove_duplicates(paths)))
        if not self._paths:
            message = 'MultiplexedPath must contain at least one path'
            raise FileNotFoundError(message)
        if not None((lambda .0: for path in .0:
path.is_dir())(self._paths)):
            raise NotADirectoryError('MultiplexedPath only supports directories')

    
    def iterdir(self):
        visited = []
        for path in self._paths:
            for file in path.iterdir():
                if file.name in visited:
                    continue
                visited.append(file.name)
                yield file

    
    def read_bytes(self):
        raise FileNotFoundError(f'''{self} is not a file''')

    
    def read_text(self, *args, **kwargs):
        raise FileNotFoundError(f'''{self} is not a file''')

    
    def is_dir(self):
        return True

    
    def is_file(self):
        return False

    
    def joinpath(self, child):
        for file in self.iterdir():
            if file.name == child:
                return file
            return self._paths[0] / child

    __truediv__ = joinpath
    
    def open(self, *args, **kwargs):
        raise FileNotFoundError(f'''{self} is not a file''')

    
    def name(self):
        return self._paths[0].name

    name = property(name)
    
    def __repr__(self):
        paths = ', '.join((lambda .0: for path in .0:
f'''\'{path}\'''')(self._paths))
        return f'''MultiplexedPath({paths})'''



class NamespaceReader(abc.TraversableResources):
    
    def __init__(self, namespace_path):
        if 'NamespacePath' not in str(namespace_path):
            raise ValueError('Invalid path')
    # WARNING: Decompyle incomplete

    
    def resource_path(self, resource):
        '''
        Return the file system path to prevent
        `resources.path()` from creating a temporary
        copy.
        '''
        return str(self.path.joinpath(resource))

    
    def files(self):
        return self.path


