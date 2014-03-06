#I. A. a. Violent Python
import PyPDF2
import argparse
from PyPDF2 import PdfFileReader
def printMeta(fileName):
    pdfFile = PdfFileReader(open(fileName, 'rb'))
    docInfo = pdfFile.getDocumentInfo()
    print('[*] PDF MetaData For: ' + str(fileName))
    for metaItem in docInfo:
        print('[+] '+ metaItem + ':' + docInfo[metaItem])
def main():
    parser = argparse.ArgumentParser()
    parser.add_argument('-F', dest='fileName', type=str, 
        required=True, help='specify PDF file name')
    args = parser.parse_args()
    printMeta(args.fileName)
if __name__ == '__main__':
    main()