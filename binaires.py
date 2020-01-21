# Fonction Conversion en Binaire

def Conversion_en_binaire(n):
    t = []
    if(n < 2):
        return n
    elif(n > 1):
        while n != 0:
            t.append(n%2)
            n//= 2
    return t[::-1]
