#!/usr/bin/env python
# this is a python 2.x file due to pdfminer dependency
import sys
import getopt

from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams

class PDF2Text:
  def convertPDF(self, filename, output):
    pdf_file = open(filename, 'rb')
    
    rsrcmgr = PDFResourceManager()
    text_converter = TextConverter(rsrcmgr, output, codec='utf-8', laparams=LAParams())
    
    page_interpreter = PDFPageInterpreter(rsrcmgr, text_converter)
    for page in PDFPage.get_pages(pdf_file,
                                  set(),
                                  maxpages=0, 
                                  password='',
                                  caching=True,
                                  check_extractable=True):
      page_interpreter.process_page(page)
      
    pdf_file.close()
    
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
  print(' -h --help')
  print(' \tShow this information')

def main():
  try:
    opts, args = getopt.gnu_getopt(sys.argv[1:],"ho:v",["help", "in=", "out="])
  except (getopt.GetoptError, NameError):
    usage()
    sys.exit()

  # defaults
  input_file = ''
  output_file = 'out.txt'

  for o,v in opts:
    if o in ['--in']:
      input_file = v
    elif o in ['--out']:
      output_file = v
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
    converter = PDF2Text()
    output = open(output_file, 'w')
    converter.convertPDF(input_file, output)
    output.close()

      
if __name__ == "__main__":
  main()
