# detrend.py
#
# this takes a simple csv of time-series data and applies a 2nd or 3rd order polynomial fit.
# useful for "detrending" astronomical time series data before processing.
#
# Ray Sanders - info@dearastronomer.com
#
import pprint
import os
import sys
import numpy
from matplotlib import pyplot
from scipy.optimize import curve_fit
_general_function = None

# 2nd order poly
def fittingFunction(x, a, b, c,):
     return a*x**2 + b*x + c

# 3rd order poly
#def fittingFunction(x, a, b, c, d):
#     return a*x**3 + b*x**2 + c*x + d

# import the data file
# unpack=True below means split up columns into separate variables
dataX, dataY = numpy.loadtxt('test.dat.csv', unpack=True)
coeffs, covar = curve_fit(fittingFunction, dataX, dataY)

#This will print coeffs, which is a list of the values of a,b, and c as optimized by curve_fit.
#print coeffs
#print "\n"

#Print fitted data
data1 = fittingFunction(dataX, *coeffs)
#data2 = fittingFunction(dataY, *coeffs)
#print fittingFunction(dataX, *coeffs)
#print fittingFunction(dataY, *coeffs)


# easier to use a for loop than learn how to assemble fitted values in a two column format or csv. 
#
# print Original Timestamps
print "\n"
print "Timestamp Values (x-axis)"
for item in dataX:
  print item

# print original magnitude values
#print "\n"
#print "Data Y: Original magnitude data:"
#for item in dataY:
#	print item

# print fitted data (original minus corrected)
print "\n"
print "Magnitude data minus correction (y-axis):"
fitted = dataY - data1
for item in fitted:
	print item

# This just plots the fitting line, can comment out the print statements above and uncomment this when testing. 
pyplot.plot(dataX,dataY)
pyplot.plot(dataX,data1)
pyplot.show()
