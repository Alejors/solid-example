# Only one class responsible for storing, adding and saving to file
class Shipping:
    def __init__(self):
        self.packages = []
    
    def add_package(self, package):
        self.packages.append(package)
    
    def list_packages(self):
        for package in self.packages:
            print(f"Package ID: {package['id']}, Destination: {package['destination']}")
    
    def save_to_file(self, filename):
        with open(filename, 'w') as file:
            for package in self.packages:
                file.write(f"{package['id']} to {package['destination']}\n")

# The code itself works fine adding packages for a shipping process, listing them and saving to a file.
# But if this is required to be extended, the code could get messy
shipping = Shipping()
shipping.add_package({'id': '123', 'destination': 'New York'})
shipping.add_package({'id': '456', 'destination': 'Los Angeles'})
shipping.list_packages()
shipping.save_to_file('packages.txt')
