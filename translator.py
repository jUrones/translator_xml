
from __future__ import print_function

from googletrans import Translator
import xml.etree.ElementTree as ET  
import pprint # Para poder hacer uso de PrettyPrinter		
def main():
	translator = Translator()
	tree = ET.parse('book.xml')
	root = tree.getroot()

	translated = tree

	for elem in root:
		for subelem in elem:
			#subelem.text = translator.translate(subelem.text, dest='es').text
			print(subelem.text)
	tree.write("XMLtranslated.xml")

if __name__ == '__main__':
    main()
