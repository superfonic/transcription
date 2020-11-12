#!/usr/bin/env python3
#
# main.py
#
# VERSION 0.0.1
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
import os
from superf.ProcSound import ProcSound
from superf.Plotting import Plotting
from superf.utilities import get_note

import numpy as np
from scipy.io import wavfile

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

    my_plot = Plotting()
    my_plot.setup(filename)

    # reads the selected WAV file and returns
    # sampling rate (int) and the sound data (numpy.array)
    fs, data = wavfile.read(filename)

    # TODO: deal with mono/stereo
    # e.g., G.wav --- left only or average channels or else?
    if len(data.shape) > 1:
        print("Input file has {} channels".format(data.shape[1]))
        # For now, just take one channel
        data = data[:, 0]
    else:
        print("Input file has {} channels".format(1))

    my_plot.plot(data,data,3)

    split = int(int(len(data))/(fs/48)) #calculate how large of a sample window to process, 48 is based on a 16th note at 180 beats per minute

    framed_data = np.array_split(data,split,0) #splits the sound data into smaller frames

    my_proc = ProcSound()
    for i in range(split): #loops through all the sound frames
        frame = framed_data.pop(0) #takes the first frame
        note_freq = my_proc.find_all_peaks(my_plot, frame, fs) #gets all of the frequencies in the selected sound frame
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
