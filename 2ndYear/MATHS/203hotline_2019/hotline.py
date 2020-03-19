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

from time import time
from sys import argv
from compute import Math
from math import *

class Hotline():

    """
    Main class that allows computation and output printing.
    """

    def __init__(self):
        self._n = False
        self._k = False
        self._d = False

    def computeBinomial(self):

        """
        Run computations and process output printing for the first case.
        """

        math = Math()
        result = math.binomialCoef(self._n, self._k)
        print("%d-combinations of a set of size %d:\n%d" %(self._k, self._n, result))

    def computeDistributions(self):

        """
        Run computations and process output printing for the second case.
        """

        maths = Math()

        def computeOverload(l:list) -> float:
            res = 0
            for i in range(26):
                res += l[i]
            return 1 - res

        def binomialDistributions():
            init = time()
            p = self._d / (3600 * 8)
            bi = []
            for i in range (0, 51):
                bi.append(maths.binomial(3500, i, p))
                print("{:d} -> {:.3f}".format(i, bi[-1]), end='')
                if (i+1) % 5 == 0:
                    print()
                elif i != 50:
                    print("\t", end='')
            if self._d > 320:
                print("\nOverload: 100%")
            else:
                print("\nOverload: {:.1f}%".format(computeOverload(bi) * 100))
            print("Computation time: {:.2f}ms".format(((time()-init) * 100)))

        def poissonDistributions():
            init = time()
            people = 3500 * (self._d / (3600 * 8))
            bi = []
            for i in range (0, 51):
                bi.append(exp(-people) * pow(people, i) / factorial(i))
                print("{:d} -> {:0.3f}".format(i, bi[-1]), end='')
                if (i+1) % 5 == 0:
                    print()
                elif i != 50:
                    print("\t", end='')
            if self._d > 320:
                print("\nOverload: 100%")
            else:
                print("\nOverload: {:.1f}%".format(computeOverload(bi) * 100))
            print("Computation time: {:.2f}ms".format((time() - init) * 100))

        print("Binomial distribution:")
        binomialDistributions()
        print("\nPoisson distribution:")
        poissonDistributions()

    def run(self):

        """
        Redirect to the right function.
        """

        if len(argv) == 2:
            self._d = int(argv[1])
            self.computeDistributions()
        elif len(argv) == 3:
            self._n = int(argv[1])
            self._k = int(argv[2])
            self.computeBinomial()
