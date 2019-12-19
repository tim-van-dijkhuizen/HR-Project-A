from module import Module

class ImageLoader(Module):
    
    _loadedImages = {}
    
    def getHandle(self):
        return 'imageLoader'
    
    def get(self, fileName, ext = 'png'):
        path = self._buildPath(fileName, ext)
        
        # Load image if not cached yet
        if not (path in self._loadedImages):
            return self.load(path, ext)
            
        return self._loadedImages[path]
        
    def load(self, fileName, ext = 'png'):
        path = self._buildPath(fileName, ext)

        # Load image
        self._loadedImages[path] = loadImage(path)
        return self._loadedImages[path]
    
    def _buildPath(self, fileName, ext):
        return 'images/' + fileName + '.' + ext
