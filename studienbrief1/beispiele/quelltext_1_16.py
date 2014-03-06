#http://www.lfd.uci.edu/~gohlke/pythonlibs/#pil
from PIL import Image
import math
from file import File

class Picture(File):
    def __init__(self, filename, filepath):
        File.__init__(self, filename, filepath)

        self.width, self.height = self.dimensions()
        self.entropy = self.entropy()

    def dimensions(self):
        img= Image.open(self.filepath+'\\'+self.filename)
        return img.size

    def entropy(self):
        img= Image.open(self.filepath+'\\'+self.filename)
        histogram = img.histogram()
        histogram_length = sum(histogram)

        samples_probability = [float(h) /
            histogram_length for h in histogram]

        return -sum([p * math.log(p, 2) for p in
            samples_probability if p != 0])          