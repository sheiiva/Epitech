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

class ArgumentManager():

    def checkArgs(self, argv):

        """
        Check for arguments validity.
        """

        def isNum(value):

            """ Return True if value is a digit."""

            try:
                float(value)
            except:
                False
            else:
                return True

        if (len(argv) != 2):
            print("This program works with 2 arguments!\nFor more information execute ./202unsold -h")
            return 84
        elif not isNum(argv[1]):
            print("Value must be a float!\nFor more information execute ./202unsold -h")
            return 84
        elif (float(argv[1]) < 0. or float(argv[1]) > 2.5):
            print("Wrong value!\nFor more information execute ./202unsold -h")
            return 84
        else:
            return 0

    def needHelp(self, argv):

        """
        Check if the user is asking for help.
        """

        if "-h" in argv or "--help" in argv:
            return True
        return False
