from abc import ABC, abstractmethod
from typing import List
from entities.package import Package

class PackageSaver(ABC):
    @abstractmethod
    def save_packages(self, packages: List[Package], filename: str):
        pass

class TextFileSaver(PackageSaver):
    def save_packages(self, packages: List[Package], filename: str):
        with open(filename, 'w') as file:
            for package in packages:
                file.write(f"{package.package_id} to {package.destination}\n")

class CSVFileSaver(PackageSaver):
    def save_packages(self, packages: List[Package], filename: str):
        import csv
        with open(filename, 'w', newline='') as file:
            writer = csv.writer(file)
            for package in packages:
                writer.writerow([package.package_id, package.destination])
