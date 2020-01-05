from module import Module

class ImageLoader(Module):
    
    _loadedImages = {}
    
    def getHandle(self):
        return 'imageLoader'
    
    def isCached(self, fileName, ext = 'png'):
        path = self._buildPath(fileName, ext)
        return path in self._loadedImages
    
    def get(self, fileName, ext = 'png'):
        path = self._buildPath(fileName, ext)
        
        # Load image if not cached yet
        if not self.isCached(fileName, ext):
            return self.load(fileName, ext)
            
        return self._loadedImages[path]
        
    def load(self, fileName, ext = 'png'):
        path = self._buildPath(fileName, ext)

        # Load image if not cached yet
        if not self.isCached(fileName, ext):
            self._loadedImages[path] = loadImage(path)
        
        return self._loadedImages[path]
    
    def _buildPath(self, fileName, ext):
        return 'images/' + fileName + '.' + ext
