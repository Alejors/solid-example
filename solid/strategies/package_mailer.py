from strategies.package_saver import PackageSaver
from entities.package import Package
from factory.saver_factory import PackageSaverFactory
from typing import List

class PackageFileMailer(PackageSaver):
    # Since we need to have a saver_strategy to implement save_packages, 
    # we get the strategy with the extension from the constructor
    def __init__(self, extension: str):
        super().__init__()
        self.to_email = None
        self.saver_strategy = PackageSaverFactory().get_saver_strategy(extension=extension)

    # We could set a default destination, 
    # but that would hardcode the recipient 
    # so we use a set_destination method
    def set_destination(self, to_email: str):
      self.to_email = to_email
      
    def send_email(self, attachment: str):
      if self.to_email:
        print(f"Email sent to {self.to_email} with attachment {attachment}")
      else:
        print("You must set destination first")

    # We implement save_packages just like a PackageSaver would 
    # and then do other processes, in this case "send as email"
    def save_packages(self, packages: List[Package], filename: str):
        self.saver_strategy.save_packages(packages, filename)
        self.send_email(filename)