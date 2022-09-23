def listaPersonas(num):
    lista = []
    for veces in range(num):
        nombre = input(f"Dime el nombre de la persona {veces+1}: ")
        #lista += [nombre]
        lista.append(nombre)
    return lista

def imprimePersonas(listaP):
    for persona in listaP:
        print(persona)
        
def menu():
    print("\n1. Dar de alta personas")
    print("2. Consultar lista completa de personas")
    print("3. Fin")
    op = int(input("Dime la opcion deseada: "))
    return op

def main():
    listaPer = []
    opcion = 0
    while (opcion != 3):
        opcion = menu()
        if (opcion == 1):
            cuantas = int(input("Cuantas personas vas a capturar? "))
            listaPer = listaPersonas(cuantas)
        elif (opcion == 2):
            imprimePersonas(listaPer)
        elif (opcion == 3):
            print("Hasta luego")
        else:
            print("Opcion no valida")
        
main()
