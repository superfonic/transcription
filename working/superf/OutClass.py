#!/usr/bin/env python3
#
# OutClass.py
#
# VERSION 0.0.0
#
# LAST EDIT: 2020-11-25
#
# This module is a part of the Superf package.

##############################################################################
# REQUIRED MODULES
##############################################################################
import json

from .utilities import get_note

##############################################################################
# CLASSES
##############################################################################
class OutClass(object):
    """
    Name:     OutClass
    Features: Class organizer for writing to output format(s)
    """
    # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    # Class Parameters
    # ////////////////////////////////////////////////////////////////////////
    filename = ""      # basename for a given audio file
    samplerate = 0     # sampling rate of the audio file (Hz)
    framecount = 0     # number of frames used to process audio file
    framesize = 0      # number of samples per frame
    samplecount = 0    # number of samples in an audio file
    data = dict()      # empty data dictionary

    # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    # Class Initialization
    # ////////////////////////////////////////////////////////////////////////
    def __init__(self, file_name=None):
        """
        Name:     OutClass.__init__
        Inputs:   None
        Features: Initializes the OutClass class
        """
        if file_name is not None:
            self.filename = file_name

    # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    # Class Function Definitions
    # ////////////////////////////////////////////////////////////////////////
    def print_json(self):
        """
        TODO: build the data dictionary + get the note
        """
        self.json = {
            "properties": {
                "filename": self.filename,
                "samplerate": self.samplerate,
                "framecount": self.framecount,
                "framesize": self.framesize
            },
            "data": [
                    {
                        "index": 0,
                        "peaks": self.data[0],
                        "note": get_note(self.data[0])
                    }
            ]
        }
        #js_obj = json.dumps(self.data, indent = 2)
        js_obj = json.dumps(self.json, indent = 2)
        print(js_obj)


    def add_peaks(self, frame_index, peak_list):
        """Add peak data to data dictionary"""
        if frame_index in self.data.keys():
            print("Data index, {}, already exists!".format(frame_index))
        else:
            self.data[frame_index] = peak_list


    def setup_with_note(self, note_class):
        """
        Name:     OutClass.setup_with_note
        Inputs:   NoteMaster
        Outputs:  None
        Features: Sets class values using the NoteMaster class
        TODO:     _ update with Tim's framesize in NoteMaster
        """
        self.samplerate = note_class.sample_rate
        self.framecount = note_class.num_frames
        self.samplecount = note_class.num_samples
        self.framesize = note_class.frame_size
