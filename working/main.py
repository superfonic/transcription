#!/usr/bin/env python3
#
# main.py
#
# VERSION 0.0.2
#
#
# LEXICON
# -------
# wavefile: full audio frequency data set
# frame: subset of the wavefile
# sample: the smallest subset of a audio file's data; read from audio file
# sample rate: number of samples per second (Hz); read from the audio file
#
##############################################################################
# REQUIRED MODULES
##############################################################################
import argparse
import copy
import os

from superf.NoteMaster import NoteMaster
from superf.ProcSound import ProcSound
from superf.Plotting import Plotting
from superf.utilities import get_note


##############################################################################
# MAIN
##############################################################################
if __name__ == "__main__":
    # Create an ArgumentParser class object for dealing with commandline args
    print(os.getcwd())
    p = argparse.ArgumentParser(
        description="Transcribes an audio file to music notes.")
    p.add_argument("-f", "--file", default= "../audio/piano-G5.wav",
        help="Path to your music file")

    # Read any commandline arguements sent to the program
    # NOTE: if -h or --help, the program stops here
    args = p.parse_args()

    if not os.path.isfile(args.file):
        filename = input("Enter path to music file: ")
    else:
        filename = args.file

    # Initialze plotting class
    my_plot = Plotting()
    my_plot.setup(filename)

    # Initialize notemaster class
    my_note = NoteMaster()

    # Read audio file and split the data into frames
    my_note.read_audio(filename)
    my_note.split_frames()

    # Set the bottom plot in plotting:
    my_plot.plot(my_note.data, None, 3)

    # Get a working copy of framed data
    framed_data = copy.deepcopy(my_note.framed_data)

    # Intialize proc sound class and iterate over frames
    my_proc = ProcSound()
    for i in range(my_note.num_frames): #loops through all the sound frames
        frame = framed_data.pop(0) #takes the first frame
        note_freq = my_proc.find_all_peaks(my_plot, frame, my_note.fs) #gets all of the frequencies in the selected sound frame
        note = get_note(note_freq) #determines the note associated with the frame
        print(str(i) + 'note: ' + str(note)) #print the result


    #frame = framed_data.pop(30) #takes the first frame
    #my_proc = ProcSound()
    #note_freq = my_proc.find_all_peaks(my_plot, frame, fs) #gets all of the frequencies in the selected sound frame
    #print(note_freq)
    #note = get_note(note_freq) #determines the note associated with the frame
    #print(note) #print the result

    my_plot.show()
    input('Press Enter to continue....')
    my_plot.close()
