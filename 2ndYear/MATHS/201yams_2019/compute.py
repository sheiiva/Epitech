#!/usr/bin/env python3
#coding: utf-8

############################################
#                MATHEMATICS               #
############################################
#                                          #
#  MONFA-MATAS Patricica & ROZET Corentin  #
#                                          #
#           Project : 201yams_2019         #
#                                          #
############################################

from math import factorial

class Math():

    def binomialCoef(self, n, k):
        
        """
        Returns binomial coefficients of (n k)
            return n! / k!(n -k)!
        """

        return factorial(n) / (factorial(k) * factorial(n-k))

    def binomial(self, n, k):

        """
        Returns binomial
        """

        return self.binomialCoef(n, k) * pow(1/6, k) * pow(5/6, (n - k))
