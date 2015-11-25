import os
# from audiosamples import mp3s

curr_file = 'dracula_transcription.txt'
out_file_trns = 'only_transcript.txt'
out_file_time = 'only_timestamp.txt'


def scrape_text(in_file, out_file):
	lines = []
	with open(in_file, "r") as f:
	    for line in curr_file:
	    	if not any(char.isdigit() for char in line):
	    		# print(line)
	    		# maybe I need to write to the output file here, instead of in another function?
	    		line.append
	    		return lines

# commented out for testing purposes

# def scrape_timestamps(in_file, out_file):
#     # line = []
#     with open(in_file, "r") as f:
#         for line in f:
#             if any(char.isdigit() for char in line):
#                 print(line)
#                 # open(out_file_time, "w")
#                 # out_file_time.append(line)



def store_timestamps(timestamps, out):
    with open(out_file, "w") as f:
        for lines in timestamps:
            f.write(lines)

scrape_text(curr_file, out_file_trns)
scrape_timestamps(curr_file, out_file_time)
# store_timestamps(scrape_timestamps, out_file)
