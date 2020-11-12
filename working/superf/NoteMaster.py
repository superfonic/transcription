class NoteMaster:
    """
    """
    # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    # Class Parameters
    # ////////////////////////////////////////////////////////////////////////
    num_samples = 0   # read from audio file
    num_frames = 0    # manually set
    sample_rate = 0   # read from audio file
    frame_size = 0    # calculated based on  number of frames / samples
    frame = []        # holds indexes for each frame
    notes = []        # holds notes corresponding to each frame

    # \\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\\
    # Class Initialization
    # ////////////////////////////////////////////////////////////////////////
    def __init__(self):
        """
        """
        pass
