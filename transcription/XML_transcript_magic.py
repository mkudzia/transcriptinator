# transcription/XML_transcript_magic.py

from lxml import etree as etree
import re
import os

path = '/path/to/your/mp3s/'

# this is still not working, and it's producing weird output
# print statements are for troubleshooting
def folder_name(path):
	for folders in os.listdir(path):
		folderstart = path.split('/')[5]
		# print folderstart
		folder = folderstart + folders
		# print folder
		if os.path.isdir(folders):
			return folder
		else:
			pass

def file_names(folder):
	for files in os.listdir(folder):
		input_file = os.path.join(folder, files)
		for eachfile in files:
			iterator(open(input_file))
			
			filestart = os.path.splitext(files)[0]
			out_file = filestart + 'transcription.xml'

	return filestart
	return out_file

def create_root(in_file):
	root = etree.Element('cues')
	disclaimer = etree.SubElement(root, 'disclaimer')
	disclaimer.text = 'These transcripts were created by a software program; we make no guarantees as to the quality of the output. We know some of the words are incorrect.'
	return root

def remove_numbers(text_string):
	return re.sub(r'\W\d+\W', '', text_string)

def create_cues(root, beginning, ending, transcript_text):
	cue = etree.SubElement(root, 'cue')
	start = etree.SubElement(cue, 'start')
	end = etree.SubElement(cue, 'end')
	transcript = etree.SubElement(cue, 'transcript')
	
	start.text = str(beginning)
	end.text = str(ending)
	transcript.text = remove_numbers(transcript_text)

def iterator(in_file, out_file):
	root = etree.Element('cues')
	count = 0
	start_time = 0
	end_time = 0
	for line in in_file:
		if line[0].isalpha():
			split_vals = line.split()
			if count == 0: # for the first word
				transcript_words = [] # start a new list of words
				start_time = (split_vals[1]) # grab the start time of the first word
				transcript_words.append(split_vals[0]) # save the first word to the list
				count += 1
			elif count == 6: # for the sixth word	
				end_time = (split_vals[2]) # grab the stop time of the last word
				transcript_words.append(split_vals[0]) # save the last word to the list
				create_cues(root, start_time, end_time, " ".join(transcript_words)) # assemble the cue
				count = 0 # reset the count
			else:
				transcript_words.append(split_vals[0]) # save the intervening words to the list
				count += 1

	tree = etree.ElementTree(root)		
	tree.write(out, pretty_print=True, xml_declaration=True, encoding='UTF-8')

folder_name(path)
file_names(folder)
iterator(open(out_file))
