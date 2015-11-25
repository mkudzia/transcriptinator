# run using: python scripts/transcript_parsing.py mp3s/dracula_transcription.txt mp3s/only_transcript.txt

import os
# from audiosamples import mp3s

curr_file = 'dracula_transcription.txt'
out_file_trns = 'only_transcript.txt'
out_file_time = 'only_timestamp.txt'


# opening the file I'm feeding into the program so that it can be parsed
#curr_file = open(input_file)

def scrape_text(in_file, out_file):
	lines = []
	with open(in_file, "r") as f:
	    for line in curr_file:
	    	if not any(char.isdigit() for char in line):
	    		# print(line)
	    		# maybe I need to write to the output file here, instead of in another function?
	    		line.append
	    		return lines


# def scrape_timestamps(in_file, out_file):
#     # line = []
#     with open(in_file, "r") as f:
#         for line in f:
#             if any(char.isdigit() for char in line):
#                 print(line)
#                 # open(out_file_time, "w")
#                 # out_file_time.append(line)



def store_timestamps(scrape_timestamps, out):
    with open(out_file, "w") as f:
        for lines in scrape_timestamps:
            f.write(lines)

scrape_text(curr_file, out_file_trns)
scrape_timestamps(curr_file, out_file_time)
# store_timestamps(scrape_timestamps, out_file)

# examples
# def CreateDirs(output_path, collection_pid, today):
#     """Create directory for storing data about ingest processing"""
#     log_root = os.path.join(output_path, "logs", collection_pid + "-" + today)
#     if not os.path.exists(log_root):
#         os.makedirs(log_root)
#     if not os.path.exists(os.path.join(output_path, "fails")):
#         os.makedirs(os.path.join(output_path, "fails"))
#     return log_root

# def StoreOutcomes(outcomes, directory):
#     with open(os.path.join(directory, "results.txt"), "w") as f:
#         for o in outcomes:
#             f.write(o["File"] + ": " + o["Outcome"])

# def LoadJson(ffile):
#     """Grab selected JSON file from static directory and load into memory."""
#     with open(os.path.join(static_dir, ffile), "r") as f:
#         data = json.load(f)
#     return data 

# def store_data_in_file(data_object):
#     """
#     Store arbitrary python object in JSON file for later access.
#     args:
#     data_object(any) -- arbitrary object that can be serialized.
#     """
#     current_date_time = datetime.datetime.today().isoformat()
#     fielname = "data_object_{0}.json".format(current_date_time)
#     with codecs.open(os.path.join(static_dir, filename), "w", "utf-8") as output:
#         json.dump(data_object, output)

#     return filename

# current_path = os.path.dirname(os.path.realpath(__file__))
# static_dir = os.path.join(current_path, "static")
