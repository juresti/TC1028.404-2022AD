""" Ejercicios para recordar el for
y también para recordar el range
Fin
"""
def cuenta4en4(inicio,fin):
    for numero in range(inicio,fin + 1,4):
        print(numero)
        
def divisibles7(inicio,fin):
    "Imprime los divisibles entre 7 en el rango recibido. Regresa cuantos fueron"
    cont = 0
    for dato in range(fin,inicio-1,-1):
        res = dato % 7
        if (res == 0):
            print(dato)
            cont += 1
    return cont
