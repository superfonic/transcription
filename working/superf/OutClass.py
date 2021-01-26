#!/usr/bin/env python3
#
# OutClass.py
#
# VERSION 0.0.1
#
# LAST EDIT: 2020-11-30
#
# This module is a part of the Superf package.
#
# CHANGELOG
# 2020-11-30    Create JSON
#               Create time-stamped log file
# 2020-11-25    Original draft
#
##############################################################################
# REQUIRED MODULES
##############################################################################
import datetime
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
    logfile = "superf-log.json"  # dummy log file

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
    def create_log_file(self):
        """Append timestamp to the log file"""
        now = datetime.datetime.now()
        self.logfile = now.strftime("superf-log_%Y-%m-%d-%H%M%S.json")

    def create_json(self):
        """
        Name:     OutClass.create_json
        Inputs:   None
        Outputs:  None
        Features: Creates the JSON version of the data
        Depends:  get_note
        """
        # Initialize the dictionary with file properties and empty data list
        self.json = {
            "properties": {
                "filename": self.filename,
                "samplerate": self.samplerate,
                "framecount": self.framecount,
                "framesize": self.framesize
            },
            "data": []
        }
        # Iterate through the key-value pairs in the data dictionary,
        # create minidicts and append them to the JSON dictionary
        for k,v in self.data.items():
            minidict = {
                "index": k,
                "peaks": v,
                "note": get_note(v)
            }
            self.json["data"].append(minidict)

    def print_json(self):
        """
        Name:     OutClass.print_json
        Inputs:   None
        Outputs:  None
        Features: Prints to console the JSON version of the data
        Depends:  create_json
        """
        self.create_json()
        js_obj = json.dumps(self.json, indent = 2)
        print(js_obj)

    def save_to_json(self):
        """
        Name:     OutClass.save_to_json
        Inputs:   None
        Outputs:  None
        Features: Saves the json to the log file
        Depends:  - create_log_file
                  - create_json
        """
        self.create_log_file()
        self.create_json()
        with open(self.logfile, 'w') as f:
            js_obj = json.dump(self.json, f, indent=2)

    def add_peaks(self, frame_index, peak_list):
        """Add list of peak data to data dictionary"""
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
        """
        self.samplerate = note_class.sample_rate
        self.framecount = note_class.num_frames
        self.samplecount = note_class.num_samples
        self.framesize = note_class.frame_size
