#!/usr/bin/env python3
#
# Plotting.py
#
# VERSION 0.0.2
#
# LAST EDIT: 2020-11-17
#
# This module is a part of the Superf package.

##############################################################################
# REQUIRED MODULES
##############################################################################
import matplotlib
gui_env = ['TKAgg','GTKAgg','Qt4Agg','WXAgg']
for gui in gui_env:
    try:
        print("testing {}".format(gui))
        matplotlib.use(gui, force=True)
        from matplotlib import pyplot as plt
        break
    except:
        continue
print("Using: {}".format(matplotlib.get_backend()))
from matplotlib.patches import Rectangle


##############################################################################
# CLASSES
##############################################################################
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
                  +----+----+----+----+
                  |         |         |
                  +   ax1   +   ax2   +
                  |         |         |
                  +----+----+----+----+
                  |        ax3        |
                  +----+----+----+----+
        """
        self.fig = plt.figure(figsize=(12, 8))
        self.ax1 = plt.subplot2grid(
            self.gridsize, (0, 0), colspan=2, rowspan=2)
        self.ax2 = plt.subplot2grid(
            self.gridsize, (0, 2), colspan=2, rowspan=2)
        self.ax3 = plt.subplot2grid(
            self.gridsize, (2, 0), colspan=4, rowspan=1)
        self.fig.suptitle(title)

    def patch(self, index, height, ymin, fdata):
        """
        Draw a rectangle around frame data
        """
        x1 = int(index) * len(fdata)
        w = len(fdata)
        self.ax3.add_patch(
            Rectangle((x1, ymin), w, height,
                facecolor='yellow',
                fill = True,
                alpha=0.5
            )
        )

    def plot(self, data1, data2, pos):
        """
        Name:     Plotting.plot
        Inputs:   - list/array, data to plot (data1)
                  - list/array, data to plot (data2)
                  - int, the trend plot you are assigning (pos)
        Features: plots the data provided
        """
        if pos == 1:
            self.ax1.clear()
            self.ax1.plot(data1, data2) #Optional Data Plot to show the Fourier Transform of the data
        elif pos == 2:
            self.ax2.clear()
            self.ax2.hist(data1, bins='auto')
        elif pos == 3:
            self.ax3.plot(data1)
        else:
            print("You have chosen poorly.")

    def show(self):
        """
        Turn on interactive mode and show plot
        """
        plt.ion()
        plt.show(block=False)


    def close(self):
        plt.close()
