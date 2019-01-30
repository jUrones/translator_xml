# coding: utf-8
from __future__ import print_function

from googletrans import Translator
import xml.etree.ElementTree as ET  
import pprint # Para poder hacer uso de PrettyPrinter
		
def main():
	translator = Translator()
	tree = getTree()  
	root = tree.getroot()
	
	translated = tree
	pp = pprint.PrettyPrinter(indent=2)
	
	for elem in root:
		for subelem in elem:
			subelem.text = translator.translate(subelem.text, dest='es').text
	tree.write("XMLtranslated.xml")

def getTree():
	fileName = raw_input("Insert the name of XML file or the file path: \n")
	return ET.parse(fileName);
if __name__ == '__main__':
    main()
