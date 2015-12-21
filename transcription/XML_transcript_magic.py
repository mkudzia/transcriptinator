# transcription/XML_transcript_magic.py

from lxml import etree as etree

# folder = 'mp3s'

def create_root(in_file):
	root = etree.Element('cues')
	disclaimer = etree.SubElement(root, 'disclaimer')
	disclaimer.text = 'These transcripts were created by a software program; we make no guarantees as to the quality of the output. We know some of the words are incorrect.'
	return root

# call this inside iterator?
def create_cues(root, beginning, ending, transcript_text):
	cue = etree.SubElement(root, 'cue')
	start = etree.SubElement(cue, 'start')
	end = etree.SubElement(cue, 'end')
	transcript = etree.SubElement(cue, 'transcript')
	
	start.text = str(beginning)
	end.text = str(ending)
	transcript.text = transcript_text

# regex to remove (digits):
# /\W\d+\W/g

def iterator(in_file):
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
	tree.write('output.xml', pretty_print=True, xml_declaration=True)

# root = create_root('test_xml.xml')
iterator(open('test_xml.xml'))
