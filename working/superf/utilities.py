def get_note(freq):
    """
    Name:     get_note
    Input:    array, array of frequencies (freq)
    Output:   str, the musical note
    Features: Finds the musical note corresponding to the given frequency
    """
    from mingus.containers import Note

    freq.sort() #sorts the frequencies in ascending order
    freq = list(dict.fromkeys(freq)) #removes all duplicates from the list

    if len(freq) > 1: #list size is greater than 1
        if freq[0]<12: #first value in the list is less than 12
            freq=freq[1:] #if there are more than 1 member in the list and the first value is less than 12 eliminate it

    #Below is a list of conditionals check to see if the minimum frequency is within a range, if it is note is equal to it's corresponding note value
    mfreq = min(freq) # calculate min frequency once
    if mfreq <= 15:
        note = 'REST' #if the frequency is less than 12 assume it was a Rest
    else:
        try:
           note = str(Note().from_hertz(mfreq))
        except:
           note = 'Unknown'

    return(note) #return the found note
