# transcription/XML_transcript_magic.py


import os

folder = 'mp3s'

# these functions are defined in the order that they need to show up in the result file here
# they'll be called in the correct order in the for-loop below


# this function is to insert the XML doctype declaration at the beginning of the file
def insert_xml_start(in_file):
	with open(in_file, "r") as original:
		data = original.read()
	with open(in_file, "w") as modified:
		modified.write('<?xml version="1.0" encoding="UTF-8"?>\n' + data)
	return modified

# this function is to insert a disclaimer into each file that we make no guarantees about transcription quality
def insert_disclaimer(in_file):
	with open(in_file, "r") as original:
		data = original.read()
	with open(in_file, "w") as disclaimed:
		disclaimed.write('<disclaimer>These transcripts were created by a software program; we make no guarantees as to the quality of the output. We know some of the words are incorrect.</disclaimer>' + data)
	return disclaimed

# this function is to divide the transcript into 6-word chunks to make reading and scrolling easier
def xml_chunks(in_file):
	with open(in_file, "r") as original:
		data = original.read()
	with open(in_file, "w") as chunked:
		# rewind? index[0]? tell python to start at the beginning of the transcription text
		# count six lines
		# insert newline \n
		# repeat every six lines

for files in os.listdir(folder):
	input_xml = os.path.join(folder, files)
	if '.xml' in files:
		start_filename = os.path.splitext(files)[0]

		xml_output = os.path.join(folder, start_filename + '_transcript.xml')

		insert_xml_start() # what args does this need?

	else:
		pass
