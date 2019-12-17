from module import Module

class ImageLoader(Module):
    
    _loadedImages = {}
    
    def getHandle(self):
        return 'imageLoader'
    
    def getImage(self, fileName, ext = 'png'):
        path = f"{fileName}.{ext}"
        
        # Load image if not cached yet
        if not (path in self._loadedImages):
            self.loadImage(path)
            
        return self._loadedImages[path]
        
    def loadImage(self, path):
        self._loadedImages[path] = loadImage(path)
