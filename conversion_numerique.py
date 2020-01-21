#-------------------------------------------------------------------------------
# Purpose Name:        Conversion_Numerique : de Decimal .....
# 
# Author:      Petit-Homme Ben-Jacques
# E-Mail:      pbenjacques@gmail.com
#
# Created:     17-07-2019
# Copyright:   (c) Beneymar 2019
# Licence:     <your licence>
#-------------------------------------------------------------------------------
# from binaires import Conversion_en_binaire
import binaires
from octales import Conversion_en_Octal
from hexadecimales import Conversion_en_hexadecimal

n=17
affichage = 'La conversion numerique de "{}" '.format(n)
print("{}".format(affichage.upper()))

if(isinstance(n,int)):
    f = binaires.Conversion_en_binaire(n)
    o = Conversion_en_Octal(n)
    h = Conversion_en_hexadecimal(n)
    # print(h)
    # tg = " ".join('{0}'.format(n) for n in f)
    if(isinstance(f,list)):
        tg = " ".join(map(str, f))
    if(isinstance(o,list)):
        cotg=" ".join(map(str,o))
    if(isinstance(h,list)):
        cosec=" ".join(map(str,h))
    if(isinstance(f,int)):
        tg=f
    if(isinstance(o,int)):
        cotg=o
    if(isinstance(h, int) or isinstance(h, str)):
        cosec=" ".join(map(str,h))
    print('En binaire donne: '+str(tg))
    print('En Octal donne: '+str(cotg))
    print('En Hexadecimal donne: '+str(cosec))
else:
    print("Cet Expression ne peut etre convertie!!!")
