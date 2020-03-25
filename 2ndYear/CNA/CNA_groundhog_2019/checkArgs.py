#!/usr/bin/env python3
#coding: utf-8

############################################
#                 B-CNA-410                #
############################################
#                                          #
#  MONFA-MATAS Patricica & ROZET Corentin  #
#                                          #
#            Project : Groundhog           #
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

        if (len(argv) != 2):
            print("Please enter one, and only one period!\nFor more informations, please execute\n\t./groundhog -h")
            return 84
        if not isNum(argv[1]):
            print("Period's value must be an integer!\nFor more informations, please execute:\n\t./groundhog -h")
            return 84

    def needHelp(self, argv):

        """
        Check if the user is asking for help.
        """

        if "-h" in argv or "--help" in argv:
            return True
        return False
