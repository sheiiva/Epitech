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

class Unsold():

    """
    Main class that allows computation and output printing.
    """

    def __init__(self):
        self._a = int(argv[1])
        self._b = int(argv[2])
        self._total = 0
        self._z = [0, 0, 0, 0, 0, 0, 0, 0, 0]
        self._x = [0, 0, 0, 0, 0]
        self._y = [0, 0, 0, 0, 0]
        self._expected = dict()
        self._variance = dict()

    def printSerparator(self):
      
        """
        Print a formatted separator.
        """
      
        print("----------------------------------------------------------------------------------")


    def join_and_marginal(self):

        def probabilities(x, y):
            """
            Compute and print probabilities of selling items.
            """

            return ((self._a - x) * (self._b - y)) / ((5 * self._a - 150) * (5 * self._b - 150))

        print("\tX=10\tX=20\tX=30\tX=40\tX=50\tY law")
        
        for i in range(10, 51, 10):
            print("Y=" + str(i), end="\t")
            for j in range(10, 51, 10):
                print("%0.3f" % probabilities(j, i), end="\t")
            print("%0.3f" % self._y[int(i / 10) - 1])
        print("X law", end="\t")
        for x in self._x:
            print("%0.3f" % x, end="\t")
        print("%0.3f" % self._total)


    def zRull(self):
        
        """
        Compute and print probabilities of selling complete suits.
        """

        print("z\t20\t30\t40\t50\t60\t70\t80\t90\t100\np(Z=z)", end='')

        for z in self._z:
            print("\t%0.3f" % z, end='')
        print()


    def expectedAndVariance(self):
        
        """
        Print expected values and their variance.
        """

        for variable in ['X', 'Y', 'Z']:
            print("expected value of "+variable+":\t", end='')
            print("%0.1f" % self._expected[variable])
            print("variance of "+variable+": \t\t", end='')
            print("%0.1f" % self._variance[variable])


    def run(self):

        """
        Run computations and process output printing.
        """

        self.printSerparator()
        self.join_and_marginal()
        self.printSerparator()
        self.zRull()
        self.printSerparator()
        self.expectedAndVariance()
        self.printSerparator()
