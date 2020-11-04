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
#
##############################################################################
# REQUIRED MODULES
##############################################################################
import argparse
import os

import matplotlib
gui_env = ['TKAgg','GTKAgg','Qt4Agg','WXAgg']
for gui in gui_env:
    try:
        print("testing {}".format(gui))
        matplotlib.use(gui,warn=False, force=True)
        from matplotlib import pyplot as plt
        break
    except:
        continue
print("Using: {}".format(matplotlib.get_backend()))

import numpy as np
from scipy.io import wavfile


##############################################################################
# CLASSES
##############################################################################
class _ProcSound:
    """takes the input numpy file and performs the Fourier Transform analysis to then finds all of the frequencies corresponding to the peaks in the transform"""
    # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    # Class Initialization
    # ////////////////////////////////////////////////////////////////////////
    def __init__(self):
        """
        Name:     _ProcSound.__init__
        Inputs:   None
        Outputs:  None
        Features: Basic intialization
        """
        pass

    # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    # Class Function Definitions
    # ////////////////////////////////////////////////////////////////////////
    def find_all_peaks(self, sample_plot, sound_data, sample_rate):
        """
        Name:     _ProcSound.find_all_peaks
        Inputs:   - _Plotting, this our plotter (sample_plot)
                  - array, audio data (sound_data)
                  - float, sampling rate of audio file (sample_rate)
        Outputs:  - list, list of frequencies
        Features: Returns all of the peaks of the Fourier Transform
        Depends:  - find_peak
        """
        N = int(sound_data.size) #finds the size of the sample data
        dur = int((N/1)) #calculate the time duration of the sample data
        freq = abs(np.fft.fftfreq(dur, 1/sample_rate)) #calculate the sample frequencies for the specific time duration

        ft = np.fft.fft(sound_data[:]) #perform a Fourier Transform of the sample data
        fdata = abs(np.around(ft.real**2 + ft.imag**2,decimals = 2)) #formatting the data

        #plt.ion
        sample_plot.plot(freq,fdata,1)

        #plt.show(block=False)

        # - - - Rework this Section - - -

        #This section of the logic is working with the data to eliminate noise and increase the accuracy of the output
        #fsub = np.roll(fdata, -1)  #shift the data by 1 position
        fdata = fdata-(np.mean(fdata)*10) #subtracting the mean of the entire data from the individual values
        fdata[fdata<0] = 0 #setting any values less than 0 equal to 0
        #print(fdata)

        #plt.ion
        #ax2.plot(freq, fdata)
        #plt.show(block=False)
        #input('Pause for plotting...')
        #time.sleep(5)

        # - - - End of Rework Section - - -

        peaks = [] #list of frequencies of the peaks
        (new_peaks, fdata, freq) = self.find_peak(fdata, freq) #find_peak finds the largest peak in the data set then is sent to it and will return the corresponding frequency and the data set with that value set to 0
        peaks.append(new_peaks) #add the frequency to the list of peaks

        while np.max(fdata) > 5: #loop while any peak is greater than 5 (5 is just a value selected to be a reasonable height, this might need adjusted for accuracy)

            (new_peaks, fdata, freq) = self.find_peak(fdata, freq) #loop through the dataset until all peaks are found
            peaks.append(new_peaks) #add the return frequencies to the list

        #input('Pause for plotting...')
        sample_plot.plot(peaks,fdata,2)

        return(peaks) #return the list of frequencies


    def find_peak(self, fft_data, fft_freq):
        """
        Names:    _ProcSound.find_peak
        Inputs:   - (fft_data)
                  - (fft_freq)
        Outputs:  tuple of values
                  - float, peak frequency
                  - list, original data (edited)
                  - float, original frequency
        Features: finds the maximum value of the given dataset,
                  relates that to it's corresponding frequency,
                  and removes that value from the dataset.
                  Returned are the found frequency, the altered data set, and the dataset containing the frequencies
        """
        note = np.max(fft_data) #find the maximum value in the dataset
        nposition = np.where(fft_data == note) #find it's position in the dataset
        nposition = list(nposition) #converts the location to a list
        position = nposition[0] #gets the value of the position
        peak_freq = fft_freq[position[0]] #find the frequency at the corresponding position
        fft_data[position[0]] = 0 #set the max value in the dataset equal to zero

        return(peak_freq,fft_data,fft_freq) #returns the frequency, the dataset, and the frequencies


class _Plotting:
    """sets up and plots the inputs on 3 different plots"""
    # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    # Class Initialization
    # ////////////////////////////////////////////////////////////////////////
    def __init__(self):
        """TBA"""
        self.gridsize = (3, 4)

    # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    # Class Function Definitions
    # ////////////////////////////////////////////////////////////////////////
    def setup(self, title):
        """
        Name:     _Plotting.setup
        Input:    str, title of plot
        Outputs:  None
        Features: initializes the plots and sets the title name
        """
        self.fig = plt.figure(figsize=(12, 8))
        self.ax1 = plt.subplot2grid(
            self.gridsize, (0, 0), colspan=2, rowspan=2)
        self.ax2 = plt.subplot2grid(
            self.gridsize, (0, 2), colspan=2, rowspan=2)
        self.ax3 = plt.subplot2grid(
            self.gridsize, (2, 0), colspan=4, rowspan=1)
        self.ax1.set_title(title, fontsize = 14)

    def plot(self, data1, data2, pos):
        """
        Name:     _Plotting.plot
        Inputs:   - list/array, data to plot (data1)
                  - list/array, data to plot (data2)
                  - int, the trend plot you are assigning (pos)
        Features: plots the data provided
        """
        if pos == 1:
            self.ax1.plot(data1, data2) #Optional Data Plot to show the Fourier Transform of the data
        elif pos == 2:
            self.ax2.hist(data1, bins='auto')
        elif pos == 3:
            self.ax3.plot(data1)
        else:
            print("You have chosen poorly.")



##############################################################################
# FUNCTIONS
##############################################################################
def get_note(freq):
    """
    Name:     get_note
    Input:    array, array of frequencies (freq)
    Output:   str, the musical note
    Features: Finds the musical note corresponding to the given frequency
    """
    freq.sort() #sorts the frequencies in ascending order
    freq = list(dict.fromkeys(freq)) #removes all duplicates from the list

    if len(freq) > 1: #list size is greater than 1
        if freq[0]<12: #first value in the list is less than 12
            freq=freq[1:] #if there are more than 1 member in the list and the first value is less than 12 eliminate it

    #Below is a list of conditionals check to see if the minimum frequency is within a range, if it is note is equal to it's corresponding note value
    if min(freq) <= 16.835: note = 'REST' #if the frequency is less than 12 assume it was a Reset
    if 15.865 <= min(freq) <= 16.835: note = 'C0'
    if 16.835 <= min(freq) <= 17.835: note = 'C#0/Db0'
    if 17.835 <= min(freq) <= 18.9: note = 'D0'
    if 18.9 <= min(freq) <= 20.025: note = 'D#0/Eb0'
    if 20.025 <= min(freq) <= 21.215: note = 'E0'
    if 21.215 <= min(freq) <= 22.475: note = 'F0'
    if 22.475 <= min(freq) <= 23.81: note = 'F#0/Gb0'
    if 23.81 <= min(freq) <= 25.23: note = 'G0'
    if 25.23 <= min(freq) <= 26.73: note = 'G#0/Ab0'
    if 26.73 <= min(freq) <= 28.32: note = 'A0'
    if 28.32 <= min(freq) <= 30.005: note = 'A#0/Bb0'
    if 30.005 <= min(freq) <= 31.785: note = 'B0'
    if 31.785 <= min(freq) <= 33.675: note = 'C1'
    if 33.675 <= min(freq) <= 35.68: note = 'C#1/Db1'
    if 35.68 <= min(freq) <= 37.8: note = 'D1'
    if 37.8 <= min(freq) <= 40.045: note = 'D#1/Eb1'
    if 40.045 <= min(freq) <= 42.425: note = 'E1'
    if 42.425 <= min(freq) <= 44.95: note = 'F1'
    if 44.95 <= min(freq) <= 47.625: note = 'F#1/Gb1'
    if 47.625 <= min(freq) <= 50.455: note = 'G1'
    if 50.455 <= min(freq) <= 53.455: note = 'G#1/Ab1'
    if 53.455 <= min(freq) <= 56.635: note = 'A1'
    if 56.635 <= min(freq) <= 60.005: note = 'A#1/Bb1'
    if 60.005 <= min(freq) <= 63.575: note = 'B1'
    if 63.575 <= min(freq) <= 67.355: note = 'C2'
    if 67.355 <= min(freq) <= 71.36: note = 'C#2/Db2'
    if 71.36 <= min(freq) <= 75.6: note = 'D2'
    if 75.6 <= min(freq) <= 80.095: note = 'D#2/Eb2'
    if 80.095 <= min(freq) <= 84.86: note = 'E2'
    if 84.86 <= min(freq) <= 89.905: note = 'F2'
    if 89.905 <= min(freq) <= 95.25: note = 'F#2/Gb2'
    if 95.25 <= min(freq) <= 100.915: note = 'G2'
    if 100.915 <= min(freq) <= 106.915: note = 'G#2/Ab2'
    if 106.915 <= min(freq) <= 113.27: note = 'A2'
    if 113.27 <= min(freq) <= 120.005: note = 'A#2/Bb2'
    if 120.005 <= min(freq) <= 127.14: note = 'B2'
    if 127.14 <= min(freq) <= 134.7: note = 'C3'
    if 134.7 <= min(freq) <= 142.71: note = 'C#3/Db3'
    if 142.71 <= min(freq) <= 151.195: note = 'D3'
    if 151.195 <= min(freq) <= 160.185: note = 'D#3/Eb3'
    if 160.185 <= min(freq) <= 169.71: note = 'E3'
    if 169.71 <= min(freq) <= 179.805: note = 'F3'
    if 179.805 <= min(freq) <= 190.5: note = 'F#3/Gb3'
    if 190.5 <= min(freq) <= 201.825: note = 'G3'
    if 201.825 <= min(freq) <= 213.825: note = 'G#3/Ab3'
    if 213.825 <= min(freq) <= 226.54: note = 'A3'
    if 226.54 <= min(freq) <= 240.01: note = 'A#3/Bb3'
    if 240.01 <= min(freq) <= 254.285: note = 'B3'
    if 254.285 <= min(freq) <= 269.405: note = 'C4'
    if 269.405 <= min(freq) <= 285.42: note = 'C#4/Db4'
    if 285.42 <= min(freq) <= 302.395: note = 'D4'
    if 302.395 <= min(freq) <= 320.38: note = 'D#4/Eb4'
    if 320.38 <= min(freq) <= 339.43: note = 'E4'
    if 339.43 <= min(freq) <= 359.61: note = 'F4'
    if 359.61 <= min(freq) <= 380.995: note = 'F#4/Gb4'
    if 380.995 <= min(freq) <= 403.65: note = 'G4'
    if 403.65 <= min(freq) <= 427.65: note = 'G#4/Ab4'
    if 427.65 <= min(freq) <= 453.08: note = 'A4'
    if 453.08 <= min(freq) <= 480.02: note = 'A#4/Bb4'
    if 480.02 <= min(freq) <= 508.565: note = 'B4'
    if 508.565 <= min(freq) <= 538.81: note = 'C5'
    if 538.81 <= min(freq) <= 570.85: note = 'C#5/Db5'
    if 570.85 <= min(freq) <= 604.79: note = 'D5'
    if 604.79 <= min(freq) <= 640.75: note = 'D#5/Eb5'
    if 640.75 <= min(freq) <= 678.855: note = 'E5'
    if 678.855 <= min(freq) <= 719.225: note = 'F5'
    if 719.225 <= min(freq) <= 761.99: note = 'F#5/Gb5'
    if 761.99 <= min(freq) <= 807.3: note = 'G5'
    if 807.3 <= min(freq) <= 855.305: note = 'G#5/Ab5'
    if 855.305 <= min(freq) <= 906.165: note = 'A5'
    if 906.165 <= min(freq) <= 960.05: note = 'A#5/Bb5'
    if 960.05 <= min(freq) <= 1017.135: note = 'B5'
    if 1017.135 <= min(freq) <= 1077.615: note = 'C6'
    if 1077.615 <= min(freq) <= 1141.695: note = 'C#6/Db6'
    if 1141.695 <= min(freq) <= 1209.585: note = 'D6'
    if 1209.585 <= min(freq) <= 1281.51: note = 'D#6/Eb6'
    if 1281.51 <= min(freq) <= 1357.71: note = 'E6'
    if 1357.71 <= min(freq) <= 1438.445: note = 'F6'
    if 1438.445 <= min(freq) <= 1523.98: note = 'F#6/Gb6'
    if 1523.98 <= min(freq) <= 1614.6: note = 'G6'
    if 1614.6 <= min(freq) <= 1710.61: note = 'G#6/Ab6'
    if 1710.61 <= min(freq) <= 1812.33: note = 'A6'
    if 1812.33 <= min(freq) <= 1920.095: note = 'A#6/Bb6'
    if 1920.095 <= min(freq) <= 2034.265: note = 'B6'
    if 2034.265 <= min(freq) <= 2155.23: note = 'C7'
    if 2155.23 <= min(freq) <= 2283.39: note = 'C#7/Db7'
    if 2283.39 <= min(freq) <= 2419.17: note = 'D7'
    if 2419.17 <= min(freq) <= 2563.02: note = 'D#7/Eb7'
    if 2563.02 <= min(freq) <= 2715.425: note = 'E7'
    if 2715.425 <= min(freq) <= 2876.895: note = 'F7'
    if 2876.895 <= min(freq) <= 3047.96: note = 'F#7/Gb7'
    if 3047.96 <= min(freq) <= 3229.2: note = 'G7'
    if 3229.2 <= min(freq) <= 3421.22: note = 'G#7/Ab7'
    if 3421.22 <= min(freq) <= 3624.655: note = 'A7'
    if 3624.655 <= min(freq) <= 3840.19: note = 'A#7/Bb7'
    if 3840.19 <= min(freq) <= 4068.54: note = 'B7'
    if 4068.54 <= min(freq) <= 4310.465: note = 'C8'
    if 4310.465 <= min(freq) <= 4566.775: note = 'C#8/Db8'
    if 4566.775 <= min(freq) <= 4838.33: note = 'D8'
    if 4838.33 <= min(freq) <= 5126.035: note = 'D#8/Eb8'
    if 5126.035 <= min(freq) <= 5430.845: note = 'E8'
    if 5430.845 <= min(freq) <= 5753.78: note = 'F8'
    if 5753.78 <= min(freq) <= 6095.92: note = 'F#8/Gb8'
    if 6095.92 <= min(freq) <= 6458.405: note = 'G8'
    if 6458.405 <= min(freq) <= 6842.44: note = 'G#8/Ab8'
    if 6842.44 <= min(freq) <= 7249.31: note = 'A8'
    if 7249.31 <= min(freq) <= 7680.375: note = 'A#8/Bb8'
    if 7680.375 <= min(freq) <= 8252.13: note = 'B8'

    return(note) #return the found note


##############################################################################
# MAIN
##############################################################################
if __name__ == "__main__":
    # Create an ArgumentParser class object for dealing with commandline args
    p = argparse.ArgumentParser(
        description="Transcribes an audio file to music notes.")
    p.add_argument("-f", "--file", default="../audio/G.wav",
        help="Path to your music file")

    # Read any commandline arguements sent to the program
    # NOTE: if -h or --help, the program stops here
    args = p.parse_args()

    if not os.path.isfile(args.file):
        filename = input("Enter path to music file: ")
    else:
        filename = args.file

    my_plot = _Plotting()
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

    split = int(int(data.size)/(fs/48)) #calculate how large of a sample window to process, 48 is based on a 16th note at 180 beats per minute

    framed_data = np.array_split(data,split,0) #splits the sound data into smaller frames

    #for i in range(split): #loops through all the sound frames
    #    frame = framed_data.pop(0) #takes the first frame
    #    note_freq = _ProcSound.find_all_peaks(frame, fs) #gets all of the frequencies in the selected sound frame
    #    note = get_note(note_freq) #determines the note associated with the frame
    #    print(str(i) + 'note: ' + str(note)) #print the result


    frame = framed_data.pop(30) #takes the first frame

    my_proc = _ProcSound()
    note_freq = my_proc.find_all_peaks(my_plot, frame, fs) #gets all of the frequencies in the selected sound frame
    print(note_freq)
    note = get_note(note_freq) #determines the note associated with the frame
    print(note) #print the result

    plt.show(block=False)
    input('Press Enter to continue....')
    plt.close()
