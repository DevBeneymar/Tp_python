# Fonction Conversion en Octal

def Conversion_en_Octal(n):
    t=list() 
    if(n<8):
        return n 
    elif(n>7):
        while n!=0:
            t.append(n%8)
            n//=8
    return t[::-1]
