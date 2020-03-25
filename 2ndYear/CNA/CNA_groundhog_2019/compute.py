#!/usr/bin/env python3
#coding: utf-8

############################################
#                 B-CNA-410                #
############################################
#                                          #
#  MONFA-MATAS Patricica & ROZET Corentin  #
#                                          #
#            Project : Groundhog           #
#                                          #
############################################

from sys import argv
import numpy as np

class Compute():

    """
    Computation class.
    """

    def computeG(self, groundhog, periodIsPast):
 
        """
        Compute the temperature increase average (._g) observed on the last period.
        """

        if not periodIsPast:
            return
        i = len(groundhog._values) - groundhog._period
        groundhog._g = 0
        while i < len(groundhog._values):
            tmp = groundhog._values[i] - groundhog._values[i - 1]
            if tmp > 0:
                groundhog._g += tmp
            i += 1
        try :
            groundhog._g /= groundhog._period
        except ZeroDivisionError:
            groundhog._g = 0

    def computeR(self, groundhog, periodIsPast):

        """
        Compute the relative temperature evolution (._r)
        between the last giver temperature and the temperatureobserved n-days ago.
        """

        if not periodIsPast:
            return
        groundhog._r = ((groundhog._values[-1] / groundhog._values[-1-groundhog._period]) * 100) - 100
        groundhog._r = int(groundhog._r + (0.5 - int(groundhog._r < 0)))

    def computeS(self, groundhog, periodIsPast):

        """
        Compute the thestandard deviation (._s) of the temperatures observed during the last period.
        """

        if not periodIsPast:
            return
        tmp = groundhog._values.copy()
        tmp.reverse()
        tmp = tmp[:groundhog._period]
        tmp.reverse()
        groundhog._s = np.std(tmp)
        return

    def computeSwitch(self, groundhog, last, periodIsPast):
        
        """
        Look for important switches in global tendency.
        """
        
        def isSwitch(a, b):
            if a < 0 and b >= 0:
                return True
            elif b < 0 and a >= 0:
                return True
            else:
                return False

        if last == None or not periodIsPast:
            return
        if isSwitch(last, groundhog._r):
            groundhog._alerts = True
        else:
            groundhog._alerts = False

        # append in groundhog._switches.appen(X)
        return

    def process(self, groundhog, day):

        """
        Process all computations.
        """
        
        periodIsPast = (day>= groundhog._period)
        last = groundhog._r

        self.computeG(groundhog, periodIsPast)
        self.computeR(groundhog, periodIsPast)
        self.computeS(groundhog, (day>=(groundhog._period - 1)))
        self.computeSwitch(groundhog, last, periodIsPast)
