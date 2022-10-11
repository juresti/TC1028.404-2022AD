def crearMatriz(numRen,numCol,valor):
    matriz = []
    for ren in range(numRen):
        renglon = []
        for col in range(numCol):
            renglon.append(valor) #renglon += [valor]
        matriz.append(renglon)
    
    return matriz

def imprimirMatriz(matriz):
    salida = ""
    for renglon in matriz:
        for valor in renglon:
            salida += str(valor) + " "
        salida += "\n"
        
    print(salida)
    
def imprimirMatrizVP(matriz):
    salida = ""
    for ren in range(len(matriz)):
        for col in range(len(matriz[ren])):
            salida += str(matriz[ren][col]) + " "
        salida += "\n"
        
    print(salida)

def tamanoMatriz(matriz):
    numRen = len(matriz)
    numCol = len(matriz[0])
    
    for renglon in matriz:
        if (len(renglon) != numCol):
            print("ERROR!!! Numero de columnas diferente")
            return -1,-1
    
    return numRen,numCol

def mismoTamano(mat1,mat2):
    datos1 = tamanoMatriz(mat1)
    datos2 = tamanoMatriz(mat2)
    return (datos1 == datos2)

def mismoTamanoInfo(mat1,mat2):
    numRen1,numCol1 = tamanoMatriz(mat1)
    numRen2,numCol2 = tamanoMatriz(mat2)
    
    renglones = False #True si ambas matrices tienen mismo numero renglones
    columnas = False #True mismo numero de columnas
    
    if (numRen1 == numRen2):
        renglones = True
    else:
        print("El numero de renglones no es igual")
        
    if (numCol1 == numCol2):
        columnas = True
    else:
        print("El numero de columnas no es igual")
        
    return (renglones and columnas)

                