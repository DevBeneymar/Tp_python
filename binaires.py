
#-------------------------------------------------------------------------------
# Name:        Conversion_Binaire
# Purpose:     Conversion Numerique
#
# Author:      Benito
#
# Created:     17-07-2019
# Copyright:   (c) Benito 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# # Fonction Conversion en Binaire

def Conversion_en_binaire(n):
    t = []
    if(n < 2):
        return n
    elif(n > 1):
        while n != 0:
            t.append(n%2)
            n//= 2
    return t[::-1]
