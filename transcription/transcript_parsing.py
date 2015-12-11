# transcription/transcript_parsing.py

import os

output_file_trns = 'only_transcript.txt'
output_file_time = 'only_timestamp.txt'
folder = 'mp3s'

# each file needs a disclaimer regarding variable transcript quality

def scrape_text(in_file):
	transcript_lines = []
	with open(in_file, "r") as f:
	    for line in f:
	        if not any(char.isdigit() for char in line):
	            transcript_lines.append(line)
	return transcript_lines

def scrape_timestamps(in_file):
    timestamp_lines = []
    with open(in_file, "r") as f:
        for line in f:
            if any(char.isdigit() for char in line):
                timestamp_lines.append(line)
    return timestamp_lines


def store_text(transcript, out):
	with open(out, "w") as f:
		for transcript_lines in transcript:
			f.write(transcript_lines)


def store_timestamps(timestamps, out):
	with open(out, "w") as f:
	    for timestamp_lines in timestamps:
	    	f.write(timestamp_lines)

def store_xml(timestamps, out):
	with open(out, "w") as f:
		for timestamp_lines in timestamps:
			f.write(timestamp_lines)

for files in os.listdir(folder):
	input_file = os.path.join(folder, files)
	if 'transcription.txt' in files:
		filestart = os.path.splitext(files)[0]

		transcript_output = os.path.join(folder, filestart + '_only_transcript.txt')
		timestamp_output = os.path.join(folder, filestart + '_only_timestamp.txt')
		timestamp_xml_out = os.path.join(folder, filestart + '_only_timestamp.xml')

		text_lines = scrape_text(input_file)
		time_lines = scrape_timestamps(input_file)

		store_text(text_lines, transcript_output)
		store_timestamps(time_lines, timestamp_output)
		store_xml(time_lines, timestamp_xml_out)
	else:
		pass