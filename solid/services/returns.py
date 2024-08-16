from database.storage import StorageInterface
from services.transaction import Transaction
from entities.package import Package

class Return(Transaction):
  
  def __init__(self, storage: StorageInterface):
    self.memory = storage
    
  def add_package(self, package: Package):
    self.memory.save(package)

  def list_packages(self):
    for package in self.memory.storage:
      print(f"Package ID: {package.package_id} to {package.destination}")