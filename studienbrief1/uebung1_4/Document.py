from uebung1_4.File import File

class Document(File):
  def __init__(self, filename, filepath):
    File.__init__(filename, filepath)  
