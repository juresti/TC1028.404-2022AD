import os
print(os.getcwd())
os.chdir("C:\\Users\\L00423103\\Desktop")
print(os.getcwd())

def abrirArchivoRead(nombre):
    miArchivo = open(nombre + ".txt","r")
    contenido = miArchivo.read()
    miArchivo.close()
    
    print(contenido)
    return contenido

def abrirArchivoReadlines(nombre):
    miArchivo = open(nombre + ".txt","r")
    contenido = miArchivo.readlines()
    miArchivo.close()
    
    print(contenido)
    return contenido

def abrirArchivoReadline(nombre):
    miArchivo = open(nombre + ".txt","r")
    
    linea = miArchivo.readline()
    while(linea != ""):
        print(linea)
        linea = miArchivo.readline()
        
    miArchivo.close()

def escribirArchivoWrite(nombre):
    miArchivo = open(nombre + ".txt","w")
    miArchivo.write("esto va a estar en el archivo. De verdad que si")
    miArchivo.close()
    print("Archivo escrito a disco")

def escribirArchivoWritelines(nombre):
    miArchivo = open(nombre + ".txt","w")
    miArchivo.writelines(["Data 1\n","Dato 2\n","Dato 3\n","Dato 4\n"])
    miArchivo.close()
    print("Archivo escrito a disco")
