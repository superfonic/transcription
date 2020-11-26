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
from superf.OutClass import OutClass
from superf.ProcSound import ProcSound
from superf.Plotting import Plotting
from superf.utilities import get_note

##############################################################################
# SETTINGS
##############################################################################

disable_plot = True        #  turns off all plots
disable_processing = True  #  turns off the repeat processing, only processes one

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
        file_path = input("Enter path to music file: ")
    else:
        file_path = args.file

    # Read the file name from input file path
    file_name = os.path.basename(file_path)

    # Initialze plotting class
    my_plot = Plotting()
    my_plot.setup(file_name)

    # Initialize notemaster and output data class
    my_note = NoteMaster()
    my_out = OutClass(file_name)

    # Read audio file, split the data into frames, and setup output vals
    my_note.read_audio(file_path)
    my_note.split_frames()
    my_out.setup_with_note(my_note)

    # Set the bottom plot in plotting:
    if not disable_plot:
        my_plot.plot(my_note.data, None, 3)

    # Get a working copy of framed data
    framed_data = copy.deepcopy(my_note.framed_data)

    # Intialize proc sound class and iterate over frames
    my_proc = ProcSound()
    if not disable_plot:
        my_plot.show()

    if disable_processing:
        frame = framed_data[30] #takes the 30th frame
        note_freq = my_proc.find_all_peaks(my_plot, frame, my_note.fs) #gets all of the frequencies in the selected sound frame
        note = get_note(note_freq) #determines the note associated with the frame
        my_out.add_peaks(0, note_freq)
        if not disable_plot:
                my_plot.patch(0, my_note.height, my_note.ymin, frame)
                my_plot.fig.canvas.draw()
    else:
        for i in range(my_note.num_frames): #loops through all the sound frames
            frame = framed_data.pop(0) #takes the first frame
            note_freq = my_proc.find_all_peaks(my_plot, frame, my_note.fs) #gets all of the frequencies in the selected sound frame
            note = get_note(note_freq) #determines the note associated with the frame
            my_out.add_peaks(i, note_freq)
            #print(str(i) + 'note: ' + str(note)) #print the result
            # Update plotting cavas
            if not disable_plot:
                my_plot.patch(i, my_note.height, my_note.ymin, frame)
                my_plot.fig.canvas.draw()

    input('Press Enter to continue....')
    my_plot.close()
    my_out.print_json()
