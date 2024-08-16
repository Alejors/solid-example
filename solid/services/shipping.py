from database.storage import StorageInterface
from entities.package import Package
from services.transaction import Transaction
from strategies.package_saver import PackageSaver

class Shipping(Transaction):
    def __init__(self, storage: StorageInterface, saver: PackageSaver):
        self.memory = storage
        self.saver = saver
    
    def set_saver(self, saver: PackageSaver) -> None:
        self.saver = saver
    
    def add_package(self, package: Package):
        self.memory.save(package)
    
    def list_packages(self):
        for package in self.memory.as_list():
            print(f"Package ID: {package.package_id}, Destination: {package.destination}")
          
    def cancel_transaction(self, package: Package):
        self.memory.remove(package)
    
    def save_packages(self, filename: str):
        if self.saver:
            self.saver.save_packages(self.memory.as_list(), filename)
        else:
            raise NotImplementedError("Saver Not Implemented")