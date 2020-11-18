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
    mfreq = min(freq) # calculate min frequency once
    if mfreq <= 16.835:
        note = 'REST' #if the frequency is less than 12 assume it was a Rest
    elif 15.865 <= mfreq <= 16.835:
        note = 'C0'
    elif 16.835 <= mfreq <= 17.835:
        note = 'C#0/Db0'
    elif 17.835 <= mfreq <= 18.9:
        note = 'D0'
    elif 18.9 <= mfreq <= 20.025:
        note = 'D#0/Eb0'
    elif 20.025 <= mfreq <= 21.215:
        note = 'E0'
    elif 21.215 <= mfreq <= 22.475:
        note = 'F0'
    elif 22.475 <= mfreq <= 23.81:
        note = 'F#0/Gb0'
    elif 23.81 <= mfreq <= 25.23:
        note = 'G0'
    elif 25.23 <= mfreq <= 26.73:
        note = 'G#0/Ab0'
    elif 26.73 <= mfreq <= 28.32:
        note = 'A0'
    elif 30.005 <= mfreq <= 31.785:
        note = 'B0'
    elif 28.32 <= mfreq <= 30.005:
        note = 'A#0/Bb0'
    elif 31.785 <= mfreq <= 33.675:
        note = 'C1'
    elif 33.675 <= mfreq <= 35.68:
        note = 'C#1/Db1'
    elif 35.68 <= mfreq <= 37.8:
        note = 'D1'
    elif 37.8 <= mfreq <= 40.045:
        note = 'D#1/Eb1'
    elif 40.045 <= mfreq <= 42.425:
        note = 'E1'
    elif 42.425 <= mfreq <= 44.95:
        note = 'F1'
    elif 47.625 <= mfreq <= 50.455:
        note = 'G1'
    elif 44.95 <= mfreq <= 47.625:
        note = 'F#1/Gb1'
    elif 50.455 <= mfreq <= 53.455:
        note = 'G#1/Ab1'
    elif 53.455 <= mfreq <= 56.635:
        note = 'A1'
    elif 56.635 <= mfreq <= 60.005:
        note = 'A#1/Bb1'
    elif 60.005 <= mfreq <= 63.575:
        note = 'B1'
    elif 63.575 <= mfreq <= 67.355:
        note = 'C2'
    elif 67.355 <= mfreq <= 71.36:
        note = 'C#2/Db2'
    elif 71.36 <= mfreq <= 75.6:
        note = 'D2'
    elif 75.6 <= mfreq <= 80.095:
        note = 'D#2/Eb2'
    elif 80.095 <= mfreq <= 84.86:
        note = 'E2'
    elif 84.86 <= mfreq <= 89.905:
        note = 'F2'
    elif 89.905 <= mfreq <= 95.25:
        note = 'F#2/Gb2'
    elif 95.25 <= mfreq <= 100.915:
        note = 'G2'
    elif 100.915 <= mfreq <= 106.915:
        note = 'G#2/Ab2'
    elif 106.915 <= mfreq <= 113.27:
        note = 'A2'
    elif 113.27 <= mfreq <= 120.005:
        note = 'A#2/Bb2'
    elif 120.005 <= mfreq <= 127.14:
        note = 'B2'
    elif 127.14 <= mfreq <= 134.7:
        note = 'C3'
    elif 134.7 <= mfreq <= 142.71:
        note = 'C#3/Db3'
    elif 142.71 <= mfreq <= 151.195:
        note = 'D3'
    elif 151.195 <= mfreq <= 160.185:
        note = 'D#3/Eb3'
    elif 160.185 <= mfreq <= 169.71:
        note = 'E3'
    elif 169.71 <= mfreq <= 179.805:
        note = 'F3'
    elif 179.805 <= mfreq <= 190.5:
        note = 'F#3/Gb3'
    elif 190.5 <= mfreq <= 201.825:
        note = 'G3'
    elif 201.825 <= mfreq <= 213.825:
        note = 'G#3/Ab3'
    elif 213.825 <= mfreq <= 226.54:
        note = 'A3'
    elif 226.54 <= mfreq <= 240.01:
        note = 'A#3/Bb3'
    elif 240.01 <= mfreq <= 254.285:
        note = 'B3'
    elif 254.285 <= mfreq <= 269.405:
        note = 'C4'
    elif 269.405 <= mfreq <= 285.42:
        note = 'C#4/Db4'
    elif 285.42 <= mfreq <= 302.395:
        note = 'D4'
    elif 302.395 <= mfreq <= 320.38:
        note = 'D#4/Eb4'
    elif 320.38 <= mfreq <= 339.43:
        note = 'E4'
    elif 339.43 <= mfreq <= 359.61:
        note = 'F4'
    elif 359.61 <= mfreq <= 380.995:
        note = 'F#4/Gb4'
    elif 380.995 <= mfreq <= 403.65:
        note = 'G4'
    elif 403.65 <= mfreq <= 427.65:
        note = 'G#4/Ab4'
    elif 427.65 <= mfreq <= 453.08:
        note = 'A4'
    elif 453.08 <= mfreq <= 480.02:
        note = 'A#4/Bb4'
    elif 480.02 <= mfreq <= 508.565:
        note = 'B4'
    elif 508.565 <= mfreq <= 538.81:
        note = 'C5'
    elif 538.81 <= mfreq <= 570.85:
        note = 'C#5/Db5'
    elif 570.85 <= mfreq <= 604.79:
        note = 'D5'
    elif 604.79 <= mfreq <= 640.75:
        note = 'D#5/Eb5'
    elif 640.75 <= mfreq <= 678.855:
        note = 'E5'
    elif 678.855 <= mfreq <= 719.225:
        note = 'F5'
    elif 719.225 <= mfreq <= 761.99:
        note = 'F#5/Gb5'
    elif 761.99 <= mfreq <= 807.3:
        note = 'G5'
    elif 807.3 <= mfreq <= 855.305:
        note = 'G#5/Ab5'
    elif 855.305 <= mfreq <= 906.165:
        note = 'A5'
    elif 906.165 <= mfreq <= 960.05:
        note = 'A#5/Bb5'
    elif 960.05 <= mfreq <= 1017.135:
        note = 'B5'
    elif 1017.135 <= mfreq <= 1077.615:
        note = 'C6'
    elif 1077.615 <= mfreq <= 1141.695:
        note = 'C#6/Db6'
    elif 1141.695 <= mfreq <= 1209.585:
        note = 'D6'
    elif 1209.585 <= mfreq <= 1281.51:
        note = 'D#6/Eb6'
    elif 1281.51 <= mfreq <= 1357.71:
        note = 'E6'
    elif 1357.71 <= mfreq <= 1438.445:
        note = 'F6'
    elif 1438.445 <= mfreq <= 1523.98:
        note = 'F#6/Gb6'
    elif 1523.98 <= mfreq <= 1614.6:
        note = 'G6'
    elif 1614.6 <= mfreq <= 1710.61:
        note = 'G#6/Ab6'
    elif 1710.61 <= mfreq <= 1812.33:
        note = 'A6'
    elif 1812.33 <= mfreq <= 1920.095:
        note = 'A#6/Bb6'
    elif 1920.095 <= mfreq <= 2034.265:
        note = 'B6'
    elif 2034.265 <= mfreq <= 2155.23:
        note = 'C7'
    elif 2155.23 <= mfreq <= 2283.39:
        note = 'C#7/Db7'
    elif 2283.39 <= mfreq <= 2419.17:
        note = 'D7'
    elif 2419.17 <= mfreq <= 2563.02:
        note = 'D#7/Eb7'
    elif 2563.02 <= mfreq <= 2715.425:
        note = 'E7'
    elif 2715.425 <= mfreq <= 2876.895:
        note = 'F7'
    elif 2876.895 <= mfreq <= 3047.96:
        note = 'F#7/Gb7'
    elif 3047.96 <= mfreq <= 3229.2:
        note = 'G7'
    elif 3229.2 <= mfreq <= 3421.22:
        note = 'G#7/Ab7'
    elif 3421.22 <= mfreq <= 3624.655:
        note = 'A7'
    elif 3624.655 <= mfreq <= 3840.19:
        note = 'A#7/Bb7'
    elif 3840.19 <= mfreq <= 4068.54:
        note = 'B7'
    elif 4068.54 <= mfreq <= 4310.465:
        note = 'C8'
    elif 4310.465 <= mfreq <= 4566.775:
        note = 'C#8/Db8'
    elif 4566.775 <= mfreq <= 4838.33:
        note = 'D8'
    elif 4838.33 <= mfreq <= 5126.035:
        note = 'D#8/Eb8'
    elif 5126.035 <= mfreq <= 5430.845:
        note = 'E8'
    elif 5430.845 <= mfreq <= 5753.78:
        note = 'F8'
    elif 5753.78 <= mfreq <= 6095.92:
        note = 'F#8/Gb8'
    elif 6095.92 <= mfreq <= 6458.405:
        note = 'G8'
    elif 6458.405 <= mfreq <= 6842.44:
        note = 'G#8/Ab8'
    elif 6842.44 <= mfreq <= 7249.31:
        note = 'A8'
    elif 7249.31 <= mfreq <= 7680.375:
        note = 'A#8/Bb8'
    elif 7680.375 <= mfreq <= 8252.13:
        note = 'B8'
    else:
        note = 'Unknown'

    return(note) #return the found note
