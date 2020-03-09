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

def help():

    """
    Show usage of the program.
    """

    print("USAGE\n"
            "\t./101pong x0 y0 z0 x1 y1 z1 n\n\n"
            "DESCRIPTION\n"
            "\tx0   ball abscissa at time t - 1\n"
            "\ty0   ball ordinate at time t - 1\n"
            "\tz0   ball altitude at time t - 1\n"
            "\tx1   ball abscissa at time t\n"
            "\ty1   ball ordinate at time t\n"
            "\tz1   ball altitude at time t\n"
            "\tn    time shift (greater than or equal to zero, integer)")
