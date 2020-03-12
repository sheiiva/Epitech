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


class ArgumentManager():

    def checkArgs(self, argv):

        """
        Check for arguments validity.
        """

        def isNum(value):

            """Return True if value is a digit."""

            try:
                int(value)
            except:
                False
            else:
                return True

        if len(argv) == 3:
            if not isNum(argv[1]) or not isNum(argv[2]):
                print("Arguments might be digits. Please retry with -h.")
                return 84
        elif len(argv) == 2:
            if not isNum(argv[1]):
                print("Arguments might be digits. Please retry with -h.")
                return 84
        else:
            print("Wrong number of arguments. Please retry with -h.")
            return 84

    def needHelp(self, argv):

        """
        Check if the user is asking for help.
        """

        if "-h" in argv or "--help" in argv:
            return True
        return False
