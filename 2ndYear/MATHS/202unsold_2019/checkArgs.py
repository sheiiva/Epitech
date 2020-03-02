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

class ArgumentManager():

    def checkArgs(self, argv):

        """
        Check for arguments validity.
        """

        def isNum(value):

            """
            Return True if value is a digit.
            """

            try:
                int(value)
            except:
                False
            else:
                return True

        if (len(argv) != 3):
            print("This program works with 3 arguments! For more information execute ./202unsold -h")
            return 84
        if not isNum(argv[1]) or not isNum(argv[2]):
            print("Values must be integers! For more information execute ./202unsold -h")
            return 84
        if (int(argv[1]) <= 50 or int(argv[2]) <= 50):
            print("The values must be greater than 50! For more information execute ./202unsold -h")
            return 84

    def needHelp(self, argv):

        """
        Check if the user is asking for help.
        """

        if "-h" in argv or "--help" in argv:
            return True
        return False
