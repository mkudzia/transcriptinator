# transcription/transcript_parsing.py

import os
import shutil
from lxml import etree as etree
import re
from datetime import timedelta

'''this is the folder you're keeping your source audio files in; replace
if you're using a different audio file folder name'''
folder = '/mp3s'

'''this is the whole file path to the source audio file folder; replace
to match your circumstances '''
path = 'path/to/your/mp3/folder'


def create_cues(root, beginning, ending, transcript_text):
    cue = etree.SubElement(root, 'cue')
    start = etree.SubElement(cue, 'start')
    end = etree.SubElement(cue, 'end')
    transcript = etree.SubElement(cue, 'transcript')

    start.text = str(beginning)
    end.text = str(ending)
    transcript.text = remove_numbers(transcript_text)


def create_root(in_file):
    root = etree.Element('cues')
    return root


def file_names(folder):
    for dirpath, dirnames, filenames in os.walk(folder):
        for f in filenames:
            if f.endswith('.transcription_only_timestamp.txt'):
                input_file = os.path.join(dirpath, f)
                iterator(input_file)


def iterator(in_file):
    root = create_root(in_file)
    count = 0
    start_time = 0
    beginsplit = os.path.splitext(in_file)[0]
    basefile = beginsplit.split('.')[0]
    out_file = basefile + '_transcript.xml'
    vtt_out_file = basefile + '_vtt.vtt'
    with open(in_file) as transcriptfile:
        # start a new cue string
        cue_string = 'WEBVTT \n\n'
        for line in transcriptfile:
            if line[0].isalpha():
                split_vals = line.split()
                if count == 0:
                    transcript_words = []
                    # grab the start time of the first word
                    start_time = (split_vals[1])
                    # save the first word to the list
                    transcript_words.append(split_vals[0])
                    count += 1

                elif count == 6:
                    end_time = (split_vals[2])
                    transcript_words.append(split_vals[0])
                    transcript_text = " ".join(transcript_words) 
                    create_cues(
                        root, start_time, end_time, transcript_text)

                    cue_string += generate_caption(start_time, end_time, transcript_text)
                    count = 0  # reset the count

                else:
                    # save the intervening words to the list
                    transcript_words.append(split_vals[0])
                    count += 1

    tree = etree.ElementTree(root)
    tree.write(out_file, pretty_print=True,
               xml_declaration=True, encoding='UTF-8')
    # print(vtt_out_file)
    write_vtt(cue_string, vtt_out_file)

def generate_caption(start, end, text):
    """Create vtt-formatted caption.

    args:
        start(str): time in seconds e.g. 1.534
        end(str): time in seconds e.g. 5.342
        text(str): full text of caption
    """
    start_time = update_time_format(start)
    end_time = update_time_format(end)
    caption_text = remove_numbers(text)
    return "{0} --> {1}\n{2}\n\n".format(start_time, end_time, caption_text)

def update_time_format(time):
    """Change time format from s.ss to hh:mm:ss.ss.
    * Megan's note: should be hh:mm:ss.sss

    args:
        time(str): time in s.ss format
    """
    total_seconds = float(time)
    milliseconds = time.split(".")[1]
    hours, remainder = divmod(total_seconds, 60*60)
    minutes, seconds = divmod(remainder, 60)

    hours_format = str(int(hours)).zfill(2)
    minutes_format = str(int(minutes)).zfill(2)
    seconds_format = str(int(seconds)).zfill(2)
    milliseconds_format = str(int(milliseconds)).zfill(3)
    return "{0}:{1}:{2}.{3}".format(hours_format, minutes_format, seconds_format, milliseconds_format)


def write_vtt(cue_string, out):
    with open(out, "w") as f:
        # print(cue_string, "in write_vtt")
        f.write(cue_string)


def make_folders(path):
    file_count = 0
    for dirpath, dirnames, filenames in os.walk(path):
        for f in filenames:
            input_file = os.path.join(dirpath, f)
            if 'transcription.txt' in f:
                file_count += 1
                print("{0}. Processing file: {1}".format(file_count, f))
                filestart = os.path.splitext(f)[0]

                transcript_output = os.path.join(
                    dirpath, filestart + '_only_transcript.txt')
                timestamp_output = os.path.join(
                    dirpath, filestart + '_only_timestamp.txt')
                timestamp_xml_out = os.path.join(
                    dirpath, filestart + '_only_timestamp.xml')

                text_lines = scrape_text(input_file)
                time_lines = scrape_timestamps(input_file)

                store_text(text_lines, transcript_output)
                store_timestamps(time_lines, timestamp_output)
                iterator(timestamp_output)
            else:
                pass
        


def remove_numbers(text_string):
    return re.sub(r'\W\d+\W', '', text_string)


def scrape_text(in_file):
    transcript_lines = []
    with open(in_file, "r") as f:
        for line in f:
            if not any(char.isdigit() for char in line):
                transcript_lines.append(line)
    return transcript_lines


# finds all the lines with timestamp info from an audiogrep output file,
# and appends them into a list that gets returned
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



make_folders(path)