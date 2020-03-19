#!/usr/bin/env python3
#coding: utf-8

############################################
#                MATHEMATICS               #
############################################
#                                          #
#  MONFA-MATAS Patricica & ROZET Corentin  #
#                                          #
#         Project : 203hotline_2019        #
#                                          #
############################################

from math import factorial

class Math():

    def binomialCoef(self, n, k):
        
        """
        Returns binomial coefficients of (n k)
            return n! / k!(n - k)!
        """

        return factorial(n) // (factorial(k) * factorial(n-k))

    def binomial(self, n, k, p):

        """
        Returns binomial
        """

        return self.binomialCoef(n, k) * pow(p, k) * pow((1-p), (n - k))
