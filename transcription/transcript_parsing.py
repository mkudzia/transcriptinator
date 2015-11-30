import os
# from audiosamples import mp3s

curr_file = 'dracula_transcription.txt'
output_file_trns = 'only_transcript.txt'
output_file_time = 'only_timestamp.txt'


def scrape_text(in_file, out_file):
	transcript_lines = []
	with open(in_file, "r") as f:
	    for line in f:
	        if not any(char.isdigit() for char in line):
	            transcript_lines.append(line)
	return transcript_lines

def scrape_timestamps(in_file, out_file):
    timestamp_lines = []
    with open(in_file, "r") as f:
        for line in f:
            if any(char.isdigit() for char in line):
                timestamp_lines.append(line)
    return timestamp_lines


def store_timestamps(timestamps, out):
	with open(output_file_time, "w") as f:
	    for timestamp_lines in timestamps:
	    	f.write(timestamp_lines)

def store_text(transcript, out):
	with open(output_file_trns, "w") as f:
		for transcript_lines in transcript:
			f.write(transcript_lines)


text_lines = scrape_text(curr_file, output_file_trns)
time_lines = scrape_timestamps(curr_file, output_file_time)

store_text(text_lines, output_file_trns)
store_timestamps(time_lines, output_file_time)
