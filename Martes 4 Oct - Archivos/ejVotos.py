def leeVotos():
    with open("votos.txt","r") as archivo:
        contenido = archivo.readlines()
        
    print(contenido)
    
    #Metodo 1. Creando otra lista
    limpia = []
    for voto in contenido:
        limpia.append(voto.rstrip())
    print(limpia)
    
    #Metodo 2. Saca, limpia y guarda
    for pos in range(len(contenido)):
        contenido[pos] = contenido[pos].rstrip()
    print(contenido)
    