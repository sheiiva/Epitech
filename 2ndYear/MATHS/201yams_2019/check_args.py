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

class ArgumentManager():

    def __init__(self):
        self._combinationType = None
        self._a = 0
        self._b = None
        self._dices = None

    def isNum(self, n):

        """
        Returns True if n is a digit, returns False otherwise.
        """

        try:
            int(n)
        except:
            return False
        else:
            return True

    def isDiceDigit(self, value):

        """
        Return True if value is set between 1 and 6, returns False otherwise.
        """

        if int(value) < 1 or int(value) > 6:
            print("Digit might have a value between 1 and 6. Please retry with '-h'.")
            return False
        return True

    def isValid(self, combination):
        
        """
        Check for expected combination is valid.
        Returns True if the combination is valid, returns False otherwise.
        """

        elements = combination.split('_', combination.count('_'))
        combinations = ["pair", "three", "four",
                        "straight", "full", "yams", "None"]

        def assignments():
            self._combinationType = elements[0]
            if elements[0] == "full" and len(elements) == 3:
                if self.isDiceDigit(elements[1]) and self.isDiceDigit(elements[2]):
                    self._a = elements[1]
                    self._b = elements[2]
                    if (self._a == self._b):
                        return False
                else:
                    return False
            elif elements[0] != "full" and len(elements) == 2:
                if self.isDiceDigit(elements[1]):
                    self._a = elements[1]
                else:
                    return False
            else:
                return False
            if elements[0] == "straight":
                if self._a != '5' and self._a != '6':
                    return False
            return True

        for c in combinations:
            if elements[0] == c:
                break
            elif c == "None":
                return False
        for i in range (1, len(elements)):
            if not self.isNum(elements[i]):
                return False
        return assignments()


    def check_args(self, argv):

        """
        Check for arguments list validity.
            Returns 84 in case of error.
        """

        def fullZeroCheck(argv):
            if argv.count('0') != 0 and argv.count('0') != 5:
                return False
            return True

        if len(argv) != 7:
            print("Wrong number of arguments. Please retry with '-h'.")
            return 84
        if not fullZeroCheck(argv):
            return 84
        if argv.count('0') == 0:
            for i in range (1, 6):
                if not self.isNum(argv[i]):
                    print("One of dices value is not a digit. Please retry with '-h'.")
                    return 84
                elif not self.isDiceDigit(argv[i]):
                    return 84
        if not self.isValid(argv[6]):
            print("Wrong expected combination. Please retry with '-h'.")
            return 84
        # Assignement
        self._dices = [argv[1], argv[2], argv[3], argv[4], argv[5]]
        return 0

    def needHelp(self, argv):

        """
        Check if the user is asking for help.
        """

        if "-h" in argv or "--help" in argv:
            return True
        return False
