from database.storage import StorageInterface

class Memory(StorageInterface):
  def __init__(self):
    self.storage = []
    
  def save(self, args):
    self.storage.append(args)
    
  def remove(self, args):
    self.storage.remove(args)
    
  def as_list(self):
    return self.storage