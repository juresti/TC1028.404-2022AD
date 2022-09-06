def creaLinea(ancho):
    linea = ""
    for veces in range(ancho):
        linea += "$"
    return linea

def creaRectangulo(ancho,alto):
    salida = ""
    for veces in range(alto):
        salida += creaLinea(ancho) + "\n"
    return salida

def main():
    #Ejercicio 1
    print("*** Ejercicio 1 ***")
    num = int(input("Dime el ancho de la linea: "))
    line = creaLinea(num)
    print(line)
    
    #Ejercicio 2
    print("\n*** Ejercicio 2 ***")
    wide = int(input("Dime el ancho del rectangulo: "))
    leng = int(input("Dime el alto del rectangulo: "))
    rect = creaRectangulo(wide,leng)
    print(rect)
    