
#-*-coding: UTF-8 -*-
# XML translator version 0.1
# AUTHOR : jUrones
# CONTRIBUTORS: Itu26, SamuelCifuentes, enolgargon
from __future__ import print_function

from googletrans import Translator
import xml.etree.ElementTree as ET  
import sys

def main():
	translator = Translator()
	tree = getTree()
	root = tree.getroot()

	language = getLanguage()

	for elem in root:
            elem.text = translator.translate(elem.text, dest=language).text
            for subelem in elem:
                subelem.text = translator.translate(subelem.text, dest=language).text

	tree.write("XMLtranslated_"+language+".xml")


def getTree():
	fileName = raw_input("Insert the name of XML file or the file path: \n")
	return ET.parse(fileName);

def getLanguage():
    showOptions()
    try:
        language = int(raw_input('Select language number (1...4)\n'))
	if(language < 1 or language > 4):
	    print('No valid option')
	    print('Closing program....')
	    sys.exit()
	if(language == 1):
            return 'es'
        if(language== 2):
            return 'fr'
        if(language == 3):
            return 'it'
        if(language== 4):
            return 'en'           
    except:
	 print('No valid option')
	 print('Closing program....')
	 sys.exit()

def showOptions():
    print('---------Select the language to translate--------')
    print('\t1...Spanish')
    print('\t2...French')
    print('\t3...Italian')
    print('\t4...English')



if __name__ == '__main__':
    main()
