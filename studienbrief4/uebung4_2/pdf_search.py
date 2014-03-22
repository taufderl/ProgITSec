#!/usr/bin/env python
# this is a python 2.x file due to pdfminer dependency
import sys, os
sys.path.append(os.path.join(os.path.dirname(__file__), '..'))
import getopt
import mmap
from uebung4_1.pdf_to_text import PDF2Text

class SearchPDF:
  
  def __init__(self, input_file):
    self.input_file = input_file
    
  def searchPDF(self, temp_file, keyword):
    output = open(temp_file, 'w')
    converter = PDF2Text()
    converter.convertPDF(self.input_file, output)
    output.close()
    
    # start search
    with open(temp_file, "r+b") as f:
      mm = mmap.mmap(f.fileno(), 0)
      
      # find first occurence
      result = mm.find(keyword)
      while (result > 0):
        #print("Found \'%s\' in [%s] at position %i"%(keyword, input_file, result))
        
        # find beginning of line and print the whole line
        linestart = mm.rfind('\n', 0, result)
        mm.seek(linestart+1)
        
        line = self.__get_line_number(mm, result)
        
        # find line number
        print("Line %i: %s"%(line, mm.readline().strip()))
        
        # find next occurence
        result = mm.find(keyword, result+1)
        
  def __get_line_number(self, mm, index, current_line = 1):
    new_index = mm.rfind('\n', 0, index)
    if new_index == -1:
      return current_line;
    else:
      return self.__get_line_number(mm, new_index, current_line+1)
    
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
  keyword = ''

  for o,v in opts:
    if o in ['--in']:
      input_file = v
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
  if keyword == '':
      print('Please specify a keyword.')
      sys.exit(1)
  else:
    temp_file = "out.txt.tmp"
    searchPDF = SearchPDF(input_file)
    searchPDF.searchPDF(temp_file, keyword)
    os.remove(temp_file)
      
if __name__ == "__main__":
  main()
