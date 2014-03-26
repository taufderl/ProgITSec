#!/usr/bin/env python
# this is a python 2.x file due to pdfminer dependency
#
#  pdf_to_text.py
#
#  Copyright 2014 Tim auf der Landwehr <dev@taufderl.de>
#
#  This script converts a pdf file to a text file.
#
import sys
import getopt
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.pdfpage import PDFPage
from pdfminer.converter import TextConverter
from pdfminer.layout import LAParams

# pdf2text converter class
class PDF2Text:
  
  # converts a pdf file to text and writes it to the output stream
  def convertPDF(self, filename, output):
    # open pdf
    pdf_file = open(filename, 'rb')
    
    # create pdf resource manager
    rsrcmgr = PDFResourceManager()
    text_converter = TextConverter(rsrcmgr, output, codec='utf-8', laparams=LAParams())
    
    # create page interpreter and ..
    page_interpreter = PDFPageInterpreter(rsrcmgr, text_converter)
    # .. go through all the pages of the document .. 
    for page in PDFPage.get_pages(pdf_file,
                                  set(),
                                  maxpages=0, 
                                  password='',
                                  caching=True,
                                  check_extractable=True):
      # .. and process them to text
      page_interpreter.process_page(page)
    
    # close pdf file
    pdf_file.close()

# usage
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

# main
def main():
  try:
    opts, args = getopt.gnu_getopt(sys.argv[1:],"ho:v",["help", "in=", "out="])
  except (getopt.GetoptError, NameError):
    usage()
    sys.exit()

  # defaults
  input_file = ''
  output_file = 'out.txt'

  # get parameters
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
    # create converter instance
    converter = PDF2Text()
    # open output file
    with open(output_file, 'w') as output:
      # run conversion
      converter.convertPDF(input_file, output)
      
if __name__ == "__main__":
  main()
