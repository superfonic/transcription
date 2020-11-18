#!/usr/bin/env python3
#
# NoteMaster.py
#
# VERSION 0.0.0
#
# LAST EDIT: 2020-11-17
#
# This module is a part of the Superf package.

##############################################################################
# REQUIRED MODULES
##############################################################################
import os.path

import numpy
from scipy.io import wavfile


##############################################################################
# CLASSES
##############################################################################
class NoteMaster(object):
    """
    Name:     NoteMaster
    Features: Class organizer for music files and notes
    """
    # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    # Class Parameters
    # ////////////////////////////////////////////////////////////////////////
    sample_data = []  # read from audio file
    framed_data = []  # manually split
    num_frames = 0    # manually set
    sample_rate = 0   # sampling rate read from audio file (Hz)
    frame_size = 0    # calculated based on  number of frames / samples
    frame = []        # holds indexes for each frame
    notes = []        # holds notes corresponding to each frame

    # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    # Class Initialization
    # ////////////////////////////////////////////////////////////////////////
    def __init__(self):
        """
        Name:     NoteMaster.__init__
        Inputs:   None
        Features: Initializes the NoteMaster class
        """
        pass

    # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    # Class Property Definitions
    # ////////////////////////////////////////////////////////////////////////
    @property
    def data(self):
        return self.sample_data

    @property
    def fs(self):
        return self.sample_rate

    @property
    def num_samples(self):
        return len(self.sample_data)

    @property
    def split(self):
        return self.num_frames

    # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    # Class Function Definitions
    # ////////////////////////////////////////////////////////////////////////
    def read_audio(self, audio_file):
        """
        Name:     NoteMaster.read_audio
        Inputs:   str, file path to audio file (audio_file)
        Features: Reads in audio data and sets sampling data and rate
        Depends:  scipy.io.wavfile
        Throws:   IOError
        TODO:     - deal with stereo sound files
        """
        if not os.path.isfile(audio_file):
            warn_msg = "Audio file, {}, not found!".format(audio_file)
            raise IOError(warn_msg)
        else:
            _, fext = os.path.splitext(audio_file)
            if fext == ".wav":
                self.sample_rate, self.sample_data = wavfile.read(audio_file)

                # TODO: deal with mono/stereo
                # e.g., G.wav --- left only or average channels or else?
                if len(self.sample_data.shape) > 1:
                    print(
                        "WARNING: input file has {} channels".format(
                            self.sample_data.shape[1])
                    )
                    # For now, just take one channel
                    self.sample_data = self.sample_data[:, 0]
                else:
                    print("Input file has {} channels".format(1))
            else:
                raise IOError("Only wav audio files are currently supported!")

    def split_frames(self):
        """
        Calculates how large of a sample window to process;
        48 is based on a 16th note at 180 beats per minute.
        Saves the data into split frames.
        """
        self.num_frames = int(int(len(self.sample_data))/(self.sample_rate/48))
        self.framed_data = numpy.array_split(
            self.sample_data, self.num_frames, 0
        )
