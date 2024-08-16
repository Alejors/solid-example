from database.memory import Memory
from entities.package import Package
from services import Shipping, Return, Transaction
from factory.saver_factory import PackageSaverFactory
from strategies.package_mailer import PackageFileMailer

def package_listing(transaction: Transaction):
  transaction.list_packages()

# Instantiate the saver factory
saver_factory = PackageSaverFactory()

# generate a base saver we know exists
extension = "txt"
text_saver = saver_factory.get_saver_strategy(extension=extension)

shipping_storage = Memory()
# Instantiate Shipping with base saver.
shipping = Shipping(storage=shipping_storage, saver=text_saver)
shipping.declare_intent()

# Create packages
new_york_package = Package('123', 'New York')
los_angeles_package = Package('456', 'Los Angeles') 

# Add packages for shipping service
shipping.add_package(new_york_package)
shipping.add_package(los_angeles_package)

package_listing(shipping)
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
  # If this was an API, we could define that this saver subclass is used when the 
  # request receives a "to_mail" attribute. 
  # Something like 
  # if mail := request.get("to_mail"):
  #   saver = PackageFileMailer(extension)
  # else:
  #   saver = saver_factory.get_saver_strategy(extension)
  txt_mailer = PackageFileMailer(extension)
  txt_mailer.set_destination("destination@mail.cl")
  shipping.set_saver(txt_mailer)
  shipping.save_packages(f'mailed-packages.{extension}')
except Exception as e:
  print(e)

returns_storage = Memory()

returns = Return(storage=returns_storage)

returns.declare_intent()
returns.add_package(new_york_package)

package_listing(returns)