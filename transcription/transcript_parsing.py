# transcription/transcript_parsing.py

import os

output_file_trns = 'only_transcript.txt'
output_file_time = 'only_timestamp.txt'
folder = 'mp3s'

# finds all the text-only lines from an audiogrep output file and append them into a list that gets returned
def scrape_text(in_file):
	transcript_lines = []
	with open(in_file, "r") as f:
	    for line in f:
	        if not any(char.isdigit() for char in line):
	            transcript_lines.append(line)
	return transcript_lines

# finds all the lines with timestamp info from an audiogrep output file and append them into a list that gets returned
def scrape_timestamps(in_file):
    timestamp_lines = []
    with open(in_file, "r") as f:
        for line in f:
            if any(char.isdigit() for char in line):
                timestamp_lines.append(line)
    return timestamp_lines


# writes the text returned from scrape_text to a file
def store_text(transcript, out):
	with open(out, "w") as f:
		for transcript_lines in transcript:
			f.write(transcript_lines)

# writes the timestamp lines returned from scrape_timestamps to a text file
def store_timestamps(timestamps, out):
	with open(out, "w") as f:
	    for timestamp_lines in timestamps:
	    	f.write(timestamp_lines)

# writes the timestamp lines returned from scrape_timestamps to an xml file
def store_xml(timestamps, out):
	with open(out, "w") as f:
		for timestamp_lines in timestamps:
			f.write(timestamp_lines)

# loops through files in a directory; looks for transcription text files, and executes writing the new files
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