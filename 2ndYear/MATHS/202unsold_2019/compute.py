#!/usr/bin/env python3
#coding: utf-8

############################################
#                MATHEMATICS               #
############################################
#                                          #
#  MONFA-MATAS Patricica & ROZET Corentin  #
#                                          #
#          Project : 202unsold_2019        #
#                                          #
############################################

from sys import argv
from unsold import Unsold

class Compute():

    """
    Computation class.
    """

    def __init__(self, unsold):
        self.join_and_marginal(unsold)
        self.zRull(unsold)
        self.expectedAndVariance(unsold)

    def join_and_marginal(self, unsold):

        def probabilities(x, y):

            """
            Compute and print probabilities of selling items.
            """

            return ((unsold._a - x) * (unsold._b - y)) / ((5 * unsold._a - 150) * (5 * unsold._b - 150))

        for i in range(10, 51, 10):
            for j in range(10, 51, 10):
                unsold._y[int(i / 10) - 1] += probabilities(j, i)
                unsold._x[int(j / 10) - 1] += probabilities(j, i)
                unsold._total += probabilities(j, i)

    def zRull(self, unsold):
        
        """
        Compute and print probabilities of selling complete suits.
        """

        for z in range (20, 101, 10):
            for y in range (10, 51, 10):
                for x in range (10, 51, 10):
                    if (x+y) == z and y < 60:
                        unsold._z[int(z / 10) - 2] += ((unsold._a - x) * (unsold._b - y)) / ((5 * unsold._a - 150) * (5 * unsold._b - 150))
    
    def expectedAndVariance(self, unsold):
        
        """
        Compute and print expected values and their variance.
        """

        def computeTotal(nlist, result=0):
            
            """
            Compute the sum of results.
            """

            for i in range (10, 51, 10):
                result += nlist[int(i/10) - 1] * i
            return result

        def computeVariance(nlist, value, result=0):
                 
            """
            Compute the variance of results.
            """

            for i in range (0, 5):
                result += ((((i + 1) * 10) - value) ** 2) * nlist[i]
            return result

        expected = {'X': computeTotal(unsold._x),
                    'Y':computeTotal(unsold._y),
                    'Z':computeTotal(unsold._x)+computeTotal(unsold._y)}
        variance = {'X': computeVariance(unsold._x, expected['X']),
                    'Y':computeVariance(unsold._y, expected['Y']),
                    'Z':computeVariance(unsold._x, expected['X'])+computeVariance(unsold._y, expected['Y'])}
        unsold._expected = expected
        unsold._variance = variance
