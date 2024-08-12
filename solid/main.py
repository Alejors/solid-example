from services.shipping import Shipping
from entities.package import Package
from factory.saver_factory import PackageSaverFactory
from strategies.package_mailer import PackageFileMailer

# Instantiate the saver factory
saver_factory = PackageSaverFactory()

# generate a base saver we know exists
extension = "txt"
text_saver = saver_factory.get_saver_strategy(extension=extension)

# Instantiate Shipping with base saver.
shipping = Shipping(saver=text_saver)

# Create packages
new_york_package = Package('123', 'New York')
los_angeles_package = Package('456', 'Los Angeles') 

# Add packages for shipping service
shipping.add_package(new_york_package)
shipping.add_package(los_angeles_package)

shipping.list_packages()
shipping.save_packages(f'packages.{extension}')

try:
  # Define a different strategy
  extension = "csv"
  csv_saver = saver_factory.get_saver_strategy(extension=extension)
  shipping.set_saver(csv_saver)
  shipping.save_packages(f'packages.{extension}')
except Exception as e:
  print(e)

try:
  # Try a strategy not yet implemented
  extension = "pdf"
  pdf_saver = saver_factory.get_saver_strategy(extension=extension)
  shipping.set_saver(pdf_saver)
  shipping.save_packages(f'packages.{extension}')
except Exception as e:
  print(e)

try:
  extension = "txt"
  # Now let's try a subclass of PackageSaver, which "sends as email" after creating
  txt_mailer = PackageFileMailer("txt")
  txt_mailer.set_destination("destination@mail.cl")
  shipping.set_saver(txt_mailer)
  shipping.save_packages(f'mailed-packages.{extension}')
except Exception as e:
  print(e)
  