import glob
import os
import pyfits
from sys import argv

# this needs to change to a command-line parameter - /path/to/fits/*.fits or /path/to/fts/*.fts
# something like dir = argv ???

dir = "./"

# we can use any filter value in the FITS header to sort by.
# WHAT I'm interested in, is sorting a bunch of images into separate directories based on what filter was used
# BVRI, RGB, JHK, etc.

keys = ['FILTER']
hdu = 0

header_value = []
file_names = []

# this needs to take input from the parameter above since sometimes files are *.fts, and sometimes they are *.fits
# should just pass full path to files

for file_name in glob.glob(dir+'*.fts'):
    header = pyfits.getheader(file_name, hdu)
    header_value.append([header.get(key) for key in keys])
    file_names.append(file_name)


#this prints the filter values
print header_value[0]
print file_names[0]


# okay, now we get a list which corresponds to the filter used for each image.
#would be nice to then move each file into a subdirectory in the directory specified.

#example: move "R" into subdir R, "V" into subdir "V", etc.
# since I have my output from header_value and file_names it should be a matter of combining them into a file move operation.
