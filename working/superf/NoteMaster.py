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
    frame_size = 0    # calculated based on  number of samples / frame

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
    def height(self):
        return int(float(self.ymax) - float(self.ymin))

    @property
    def num_samples(self):
        return len(self.sample_data)

    @property
    def ymax(self):
        return numpy.max(self.sample_data)

    @property
    def ymin(self):
        return numpy.min(self.sample_data)

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
        Calculates the number of frames in the 
        wave file based on a set number of samples per frame

        """
        self.frame_size = 200
        self.num_frames = int(len(self.sample_data)/self.frame_size)
        self.framed_data = numpy.array_split(
            self.sample_data, self.num_frames, 0
        )
