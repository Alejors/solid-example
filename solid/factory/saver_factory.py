from strategies.package_saver import TextFileSaver, CSVFileSaver, PackageSaver

class PackageSaverFactory():
  @staticmethod
  def get_saver_strategy(extension: str) -> PackageSaver:
    extensions = {
      "txt": TextFileSaver,
      "csv": CSVFileSaver
    }
    
    if strategy := extensions.get(extension):
      return strategy()
    else:
      raise TypeError("Format Not Implemented")