## Introduction ##
This is a module that works with [audiogrep](https://github.com/antiboredom/audiogrep) to create timestamped transcripts of audio files. It is very experimental and in the early stages of development.

## Installation ##

This script also assumes you're getting a transcript from [audiogrep](https://github.com/antiboredom/audiogrep), so first you need to install that. 

Audiogrep requires [pip](https://pip.pypa.io/en/stable/installing/), [ffmpeg](http://ffmpeg.org/), and [pocketsphinx](http://cmusphinx.sourceforge.net/). DISCLAIMER: the audiogrep [installation instructions](https://github.com/antiboredom/audiogrep/blob/master/README.md) in general assume you're using a mac. 

## Creating Transcripts ##

Once you have audiogrep and its dependencies installed, download the make_transcripts project and save at least make_transcripts.py to the folder containing your transcript files.

If you don't have transcript files yet, use audiogrep to create the initial transcript files, like this (per audiogrep readme):

```
audiogrep --input path/to/*.mp3 --transcribe
```
This will transcribe all the audio files in a given directory. Budget some time for this; each transcript will take less than the total time of the audio recording, but could take up to half as long.

Then, using the command line, navigate to one directory above your transcripts, and type:

```
python3 foldername/transcript_parsing.py
```
You should get three derivative files for each transcript: 
* one with timestamp information (no chunks of text)
* one with just text
* an XML file with timestamp information

## Coming Soon -- Structured XML Output ##
See the branch xml_rewrite if you're interested in this functionality. The transcript output is intended to fit the [Islandora Oral Histories Module](https://github.com/digitalutsc/islandora_solution_pack_oralhistories).
The Oral Histories Module has the following dependencies (per their github page): 
* [Islandora](https://github.com/islandora/islandora)
* [Tuque](https://github.com/islandora/tuque) 
* [Islandora Solr Search](https://github.com/Islandora/islandora_solr_search)
* [Islandora Video Solution Pack](https://github.com/Islandora/islandora_solution_pack_video)
* [Islandora Audio Solution Pack](https://github.com/Islandora/islandora_solution_pack_audio)
* [Transcripts UI](https://github.com/Islandora/islandora_solution_pack_audio)
