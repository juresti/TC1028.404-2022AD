def reversa(pal):
    salida = ""
    for letra in pal:
        salida = letra + salida
    return salida

def reversaV2(pal):
    salida = ""
    for pos in range(-1,-len(pal)-1,-1):
        salida += pal[pos]
    return salida
