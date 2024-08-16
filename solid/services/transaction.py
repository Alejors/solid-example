from entities.package import Package

class Transaction:
  def declare_intent(self):
    print(f"This is a: {self.__class__.__name__}")
    
  def add_package(self, package: Package):
    pass
  
  def list_packages(self):
    pass
