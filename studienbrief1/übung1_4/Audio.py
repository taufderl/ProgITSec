from übung1_4.File import File
from pytag import Audio as PyTagAudio
import os

class Audio(File):
  def __init__(self, filename, filepath):
    File.__init__(self, filename, filepath)
    self.retrieve_mp3info()
    

  def retrieve_mp3info(self):
    audiofile = PyTagAudio(self.filepath + os.sep + self.filename)  
    self.title = audiofile.title if not audiofile.title == None else ''
    self.artist = audiofile.artist if not audiofile.artist == None else ''
    self.album = audiofile.album if not audiofile.album == None else ''
  