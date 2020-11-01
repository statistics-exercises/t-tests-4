import unittest
from main import *

class UnitTests(unittest.TestCase) :
    def test_plot(self) : 
        fighand=plt.gca()
        figdat = fighand.get_lines()[1].get_xydata()
        this_x, this_y = zip(*figdat)
        for i in range(len(this_x)) :
            yv = scipy.stats.t.pdf( this_x[i], 2 )
            self.assertTrue( np.abs( yv - this_y[i])<1e-7, "your plot of the t-distribution is not correct" )
