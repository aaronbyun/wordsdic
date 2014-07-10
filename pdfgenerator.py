#!/usr/bin/env python
# -*- coding: utf8 -*-

from fpdf import FPDF
from datamanager import DataManager
import sys
import codecs

reload(sys)  # Reload does the trick!
sys.setdefaultencoding('UTF8')

datamanager = DataManager('127.0.0.1', 27017) 

pdf = FPDF()

pdf.add_page()
pdf.set_author('GRE Master')
pdf.set_title('GRE Word')
#pdf.set_font('Arial', 'B', 16)

pdf.add_font('eunjin', '', 'Eunjin.ttf', uni=True)
pdf.set_font('eunjin', '', 16)

pdf.add_font('bangwool', '', 'Bangwool.ttf', uni=True)
pdf.set_font('bangwool', '', 16)

#pdf.add_font('DejaVu', '', 'DejaVuSansCondensed.ttf', uni=True)
#pdf.set_font('DejaVu', '', 16)

for row in datamanager.find():
    text = row['text']
    meanings = row['meaning']
    synonyms = row['synonyms']

    meaning = ','.join(meanings)
    synonym = u','.join(synonyms)

    line = '%s : %s \n synonyms : %s' % (text, meaning, synonym)

    #pdf.cell(20, 10, row['text'], 0, 0)# + '  ' + ','.join(row['meaning']))
    pdf.multi_cell(0, 8, line, 1, 'J')
pdf.output('gre_words.pdf', 'F')
