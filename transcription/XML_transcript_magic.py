# mp3s/XML_transcript_magic.py

import os

folder = 'mp3s'

# def input_xml(in_file):
# 	input_files = []
# 	for files in os.listdir(folder):
# 		input_file = os.path.join(folder, files)
# 		if '.xml' in files:
# 			# 
# 	return input_files

def insert_xml_start(in_file):
	for files in os.listdir(folder):
		if '.xml' in files:
			with open(in_file, "r") as original:
				data = original.read()
			with open(in_file, "w") as modified:
				modified.write('<?xml version="1.0" encoding="UTF-8"?>\n' + data)