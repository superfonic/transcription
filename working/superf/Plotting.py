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

class Plotting:

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
        Name:     Plotting.setup
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
        Name:     Plotting.plot
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

    def show(self):
        plt.show(block=False)
        
        
    def close(self):    
        plt.close()