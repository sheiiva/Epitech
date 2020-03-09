#!/usr/bin/env python3
#coding: utf-8

############################################
#                MATHEMATICS               #
############################################
#                                          #
#       Verlhac Lilian & ROZET Corentin    #
#                                          #
#           Project : 101pong_2018         #
#                                          #
############################################

class ArgumentManager():

    def checkArgs(self, argv):

        """
        Check for arguments validity.
        """

        def isFloat(value):

            """
            Return True if value is a Float.
            """

            try:
                float(value)
            except:
                False
            else:
                return True

        def isInt(value):

            """
            Return True if value is an Int.
            """

            try:
                int(value)
            except:
                False
            else:
                return True

        if (len(argv) != 8):
            print("This program works with 8 arguments! For more information execute ./101pong -h")
            return 84
        for arg in argv:
            if (arg == "./101pong"):
                continue
            elif not isFloat(arg):
                print("Arguments should be digit! For more information execute ./101pong -h")
                return 84
        if not isInt(argv[7]):
            print("n time should be an integer! For more information execute ./101pong -h")
            return 84
        elif int(argv[7]) < 0:
            print("n time should be greater than or equal to zero! For more information execute ./101pong -h")
            return 84
        return 0


    def needHelp(self, argv):

        """
        Check if the user is asking for help.
        """

        if "-h" in argv or "--help" in argv:
            return True
        return False
