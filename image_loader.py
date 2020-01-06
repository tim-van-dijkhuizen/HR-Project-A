from module import Module

class ImageLoader(Module):
    
    _loadedImages = {}
    
    def getHandle(self):
        return 'imageLoader'
    
    # Returns whether the specified image is cached
    def isCached(self, fileName, ext = 'png'):
        path = self._buildPath(fileName, ext)
        return path in self._loadedImages
    
    # Returns an image by its fileName and extension
    # The image will be loaded if not cached yet
    def get(self, fileName, ext = 'png'):
        path = self._buildPath(fileName, ext)
        
        # Load image if not cached yet
        if not self.isCached(fileName, ext):
            return self.load(fileName, ext)
            
        return self._loadedImages[path]
        
    # Loads an image by its fileName and extension
    def load(self, fileName, ext = 'png'):
        path = self._buildPath(fileName, ext)

        # Load image if not cached yet
        if not self.isCached(fileName, ext):
            self._loadedImages[path] = loadImage(path)
        
        return self._loadedImages[path]
    
    # Creates a path from a fileName and extension
    def _buildPath(self, fileName, ext):
        return 'images/' + fileName + '.' + ext
