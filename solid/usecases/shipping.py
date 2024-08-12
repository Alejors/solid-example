from entities.package import Package
from strategies.package_saver import PackageSaver

class Shipping:
    def __init__(self, saver: PackageSaver):
        self.packages = []
        self.saver = saver
    
    def set_saver(self, saver: PackageSaver) -> None:
        self.saver = saver
    
    def add_package(self, package: Package):
        self.packages.append(package)
    
    def list_packages(self):
        for package in self.packages:
            print(f"Package ID: {package.package_id}, Destination: {package.destination}")
    
    def save_packages(self, filename: str):
        if self.saver:
            self.saver.save_packages(self.packages, filename)
        else:
            raise NotImplementedError("Saver Not Implemented")