#!/usr/bin/env python
# this is a python 2.x file due to pdfminer dependency
import sys
import getopt
import mmap
from uebung4_1.pdf_to_text import PDF2Text
from StringIO import StringIO

def searchPDF(filename, keyword):
  text = StringIO()
  
  converter = PDF2Text()
  converter.convertPDF(filename, text)
  print(text)
  
  
  # start search
  with open(output_filename, "r+b") as f:
    mm = mmap.mmap(f.fileno(), 0)
    result = mm.find(keyword)
  
  print(result)
      
def usage():
  print("\n pdf_to_text.py by Tim auf der Landwehr")
  print('')
  print(' Usage: pdf_to_text.py')
  print('   > Convert PDF file to text file')
  print('')
  print(' --in [filename]')
  print(' \tSet the PDF file to be converted')
  print(' --out [filename]')
  print(' \tSet the output filename, default: out.txt')
  print(' --search [keyword]')
  print(' \tSet the output filename, default: out.txt')
  print(' -h --help')
  print(' \tShow this information')

def main():
  try:
    opts, args = getopt.gnu_getopt(sys.argv[1:],"ho:v",["help", "in=", "out=", "search="])
  except (getopt.GetoptError, NameError):
    usage()
    sys.exit()

  # defaults
  input_file = ''
  output_file = 'out.txt'
  keyword = ''

  for o,v in opts:
    if o in ['--in']:
      input_file = v
    elif o in ['--out']:
      output_file = v
    elif o in ['--search']:
      keyword = v
    elif o in ['-h','--help']:
      usage()
      sys.exit(1)
    else:
      print('unknown parameter %s'%o)
      sys.exit(1)

  if input_file == '':
      print('Please specify an input file.')
      sys.exit(1)
  else:
    searchPDF(input_file, output_file, keyword)

      
if __name__ == "__main__":
  main()
