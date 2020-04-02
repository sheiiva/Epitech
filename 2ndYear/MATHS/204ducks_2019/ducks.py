#!/usr/bin/env python3
#coding: utf-8

############################################    __(o )
#                MATHEMATICS               #    ===  |
############################################        | \___/|
#                                          #        \ \=== |
#  MONFA-MATAS Patricica & ROZET Corentin  #         \_\==/
#                                          #           ||
#          Project : 204ducks_2019         #          ===
#                                          #---------------------
############################################---------------------

from math import exp, sqrt
from sys import argv

class Ducks():

    """
    Main class that allows computation and output printing.
    """

    def __init__(self):
        self._constant = float(argv[1])


    def probability(self, t, state=0):
        
        """
        Return chances that a duck will come back after *t* minutes.
   
        int time        a time in minute.s
        """

        if state == 1:
            return (-self._constant * exp(-t) - (4 - 3 * self._constant) / 2 * exp(-2 * t) - (2 * self._constant - 4) / 4 * exp(-4 * t))
        else:
            return ((self._constant * exp(-t))
                    + ((4 - (3 * self._constant)) * exp(-2 * t))
                    + (((2 * self._constant) - 4) * exp(-4 * t)))

    def digitToTime(self, digit):

        """
        Convert a digit into a time.
        """

        minutes = int(digit)
        secondes = round((digit - int(digit)) * 60 + 0.5)

        return minutes, secondes

    def average(self):

        """
        Compute and print the average time after which ducks come back.
        """

        av = 0.

        for t in range (0, 10000):
            av += self.probability((t / 1000)) * (t / 1000) / 1000

        minutes, secondes = self.digitToTime(av)

        print("Average return time: {}m {}s".format(minutes, secondes))
        
        return av

    def std_deviation(self, average):
        
        """
        Compute and print the standard deviation of the ducks’ return time.
        """

        std = 0.

        for t in range (0, 100000):
            std += (((t / 1000) - average) ** 2) * self.probability((t / 1000)) / 1000

        std = round(sqrt(std), 3)

        print("Standard deviation: {}".format(std))


    def partial_return(self, p):

        """
        Compute and print the time after which p% of all of the ducks are back
        
        int p       a percentage
        """

        i = 1.0
        while (1):
            if (self.probability(i / 60, 1)) - (self.probability(0, 1)) >= p:
                break
            i += 0.01
        minutes = i % 60 /10
        units = i % 10
        total = i / 60
        print("Time after which {}% of the ducks are back: {}m {}{}s" .format(int(p*100), int(total), int(minutes), round(units)))

    def how_much_ducks_after(self, time, unit):

        """
        The percentage of ducks that come back after 'time' minute.s.
        
        int time        a time in minute.s
        str unit        a string corresponding to the time's unit
        """

        res = (self.probability(time, 1) - self.probability(0, 1)) * 100 + 0.2
        print("Percentage of ducks back after {} {}: {:.1f}%".format(time, unit, (res - 0.2)))

    def run(self):

        """
        Run computations and process output printing.
        """
        
        av = self.average()
        self.std_deviation(av)
        self.partial_return(0.50)
        self.partial_return(0.99)
        self.how_much_ducks_after(1, "minute")
        self.how_much_ducks_after(2, "minutes")
        return 0
