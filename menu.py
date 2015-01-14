import sys
import subprocess
from datamanager import DataManager
import pdfgenerator

def runWordSniffer():
    subprocess.Popen('sudo python ./word_capturer.py', shell=True)

def wordCount():
    datamanager = DataManager('127.0.0.1', 27017)
    print 'words count is :', datamanager.count()

def printToPDF():
    filename = raw_input('insert words filename : ')
    if filename == 'c' or filename == 'cancel':
        print 'canceled to print'
    else :
        pdfgenerator.generate(filename)

def quit():
    sys.exit(0)


options = {
    1 : runWordSniffer,
    2 : wordCount,
    3 : printToPDF,
    4 : quit
}

while True:
    try:
        print '----------------------------------------'
        print ' 1. run word sniffer'
        print ' 2. word count'
        print ' 3. print'
        print ' 4. quit'    
        print '----------------------------------------'

        selection = int(raw_input())
        options[selection]()
    except Exception, e:
        continue

