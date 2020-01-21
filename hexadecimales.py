#-------------------------------------------------------------------------------
# Name:        Conversion_Hexadecimale
# Purpose:     Conversion Numerique
#
# Author:      Benito
#
# Created:     17-07-2019
# Copyright:   (c) Benito 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# Fonction conversion en hexadecimal

def Conversion_en_hexadecimal(n):
    hexa = {10:'A', 11:'B', 12:'C', 13:'D', 14:'E', 15:'F'}
    t = list()
    if(n < 16):
        if(n > 9):
            return hexa[n]
        elif(n <= 9):
            return n
    if(n > 15):
        while n != 0:
            percent=(n%16)
            if(percent > 9):
                t.append(hexa[percent])
            else:
                t.append(percent)
            n //= 16
    return t[::-1]
