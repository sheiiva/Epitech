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

from math import pow

from check_args import ArgumentManager
from compute import Math

class Yams():

    """
    Main class that allows computation and output printing.
    """

    def __init__(self, argsManager):
        self._combinationType = argsManager._combinationType
        self._a = argsManager._a
        self._b = argsManager._b
        self._chances = None
        self._dices = argsManager._dices

    def printOutput(self):
        
        """
        Print output following a special format.
            "Chances to get a '_a' '_type'( of '_b'): 'chances'%"
        """

        def getType(combinationType):
            
            """
            Returns a formated combination type.
            """

            formated = ["pair", "three-of-a-kind", "four-of-a-kind",
                            "straight", "full", "yams"]
            combinations = ["pair", "three", "four",
                            "straight", "full", "yams"]

            for i in range (0, len(combinations)):
                if (combinationType == combinations[i]):
                    return formated[i]
            return None

        output = ""

        output += "Chances to get a "+str(self._a)+" "+getType(self._combinationType)
        if self._b != None:
            output += " of "+str(self._b)
        output += ": %0.2f%%" % (self._chances * 100)

        print(output)


    def compute(self):

        """
        Main computation function.
        """

        maths = Math()

        def computeCombination(required, value):

            """
            Returns the probability of having 'required' time the same dice.
            """

            res = 0
            occurences = self._dices.count(value)
            if occurences >= required:
                return 1
            else:
                for dice in range(required - occurences, 5 - occurences + 1):
                    res += maths.binomial(5 - occurences, dice)
                return res
        
        def computeStraight():

            """
            Returns the probability of having a straight.
            """

            def isAll():
                if ((self._dices.count("1") == 1
                    and self._dices.count("2") == 1
                    and self._dices.count("3") == 1
                    and self._dices.count("4") == 1
                    and self._dices.count("5") == 1)
                    or
                    (self._dices.count("2") == 1
                    and self._dices.count("3") == 1
                    and self._dices.count("4") == 1
                    and self._dices.count("5") == 1
                    and self._dices.count("6") == 1)):
                    return True
                return False
            
            if isAll():
                return 1
            return pow(1/6, self._dices.count(self._a))

        def computeFull():

            """
            Returns the probability of having a full.
            """

            occurences_a = self._dices.count(self._a)
            occurences_b = self._dices.count(self._b)
            if (occurences_a == 3 and occurences_b == 2):
                return 1
            if (occurences_a > 3):
                occurences_a = 3
            if (occurences_b > 2):
                occurences_b = 2
            return maths.binomialCoef(5 - occurences_a - occurences_b, 3 - occurences_a) * pow(1/6, 5 - occurences_a - occurences_b)

        if (self._combinationType == "pair"):
            self._chances = computeCombination(2, self._a)
        elif (self._combinationType == "three"):
            self._chances= computeCombination(3, self._a)
        elif (self._combinationType == "four"):
            self._chances = computeCombination(4, self._a)
        elif (self._combinationType == "yams"):
            self._chances = computeCombination(5, self._a)
        elif (self._combinationType == "straight"):
            self._chances = computeStraight()
        elif (self._combinationType == "full"):
            self._chances = computeFull()
