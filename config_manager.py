from module import Module

class ConfigManager(Module):
    
    config = {}
    
    def getHandle():
        return 'configManager'
    
    def get(self, key, default = None):
        if not key in self.config:
            return default
        
        self.config[key];
        
    def get(self, key, value):
        self.config[key] = value
