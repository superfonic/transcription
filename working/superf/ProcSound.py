import numpy as np

class ProcSound:
    """takes the input numpy file and performs the Fourier Transform analysis to then finds all of the frequencies corresponding to the peaks in the transform"""
    # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    # Class Initialization
    # ////////////////////////////////////////////////////////////////////////
    def __init__(self):
        """
        Name:     ProcSound.__init__
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
        Name:     ProcSound.find_all_peaks
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
        Names:    ProcSound.find_peak
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