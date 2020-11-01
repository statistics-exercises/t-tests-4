import matplotlib.pyplot as plt
import numpy as np
import scipy.stats

# This bit of code generates points for our graph of the normal distribution
xvals = np.linspace( -4, 4, 200 )
gvals = ( 1 / np.sqrt(2*np.pi/3) )*np.exp( - xvals*xvals / np.sqrt(3) )

# Your code to generate the values for the t-distribution goes here
# set the variable called tvals so that it is an np-array of 
# values for the t-distribution probability distribution you need
tvals

## This bit of code will generate your graphs you should not need to modify
## the code from here
## The Gaussian is plotted as a blue line
plt.plot( xvals, gvals, 'b-')
## The t-distribution will be plotted as a red line once you set the values
## in tvals in the correct way.
plt.plot( xvals, tvals, 'r-')
plt.savefig("pdfs.png")
