#chartcsv.py
#plots graphs from time series or folded phase data
#see test.csv for format of data file
#Ray Sanders - info@dearastronomer.com
#
#importing the required libraries
# coding: utf-8
import matplotlib
import pylab
from matplotlib.backends.backend_agg import FigureCanvasAgg as FigureCanvas
from matplotlib.figure import Figure
import matplotlib.mlab as mlab
import matplotlib.pyplot as plt

# Read data from a CSV file. Click here to download.
# IMPORTANT!!!! THE FILE NEEDS TO BE IN X,Y FORMAT!!!
r = mlab.csv2rec('./test.csv')

# Create a figure with size in inches.
# format is width, height
fig = Figure(figsize=(8,4))

# Create a canvas and add the figure to it.
canvas = FigureCanvas(fig)

# Create a subplot.
ax = fig.add_subplot(111)

# Set the title.
#ax.set_title('Test',fontsize=14)

# Set the X Axis label.
ax.set_xlabel('X',fontsize=12)

# Set the Y Axis label.
ax.set_ylabel('Y',fontsize=12)

# Display Grid.
#ax.grid(True,linestyle='-',color='0.75')

# Generate the Scatter Plot.

ax.scatter(r.x,r.y, c='black', marker='o',s=1);
# this sets limits on y axis if needed
ax.set_ylim(5.0, 8.5)
# this inverts the y axis
ax.set_ylim(ax.get_ylim()[::-1])
#
# set x limit if needed
ax.set_xlim(0.0, 2.0)
#
plt.show()
# Save the generated Scatter Plot to a PNG file.
canvas.print_figure('test.png',dpi=300)
