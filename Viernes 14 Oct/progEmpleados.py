def menu():
    print("1) Leer datos del archivo empleados")
    print("2) Guardar datos en el archivo empleados")
    print("3) Reporte de todos los empleados")
    print("4) Alta de un empleado")
    print("5) Consulta de un empleado")
    print("6) Salir")
    
    return int(input("Dime la opcion que deseas: "))
    
def leerDatosArchivo():
    with open("Empleados.txt","r") as miArchivo:
        datosSucios = miArchivo.readlines()
    print(datosSucios)
    #Quita \n y genera listas
    for pos in range(len(datosSucios)):
        datosSucios[pos] = datosSucios[pos].rstrip()
        datosSucios[pos] = datosSucios[pos].split(",")
    print(datosSucios)
    #Convierte datos
    for lista in datosSucios:
        lista[1] = int(lista[1])
        lista[2] = float(lista[2])
    print(datosSucios)
        
    print("Datos leidos")
    return datosSucios #[["Diego",23,14.5],["Kenia",25,98.4],["Samuel",20,74.52]]

def guardarDatosArchivo(listaEmp):
    print("Se guardara la siguiente inforamacion")
    print(listaEmp)
    
    for lista in listaEmp:
        lista[1] = str(lista[1])
        lista[2] = str(lista[2])
    print(listaEmp)
    
    for pos in range(len(listaEmp)):
        listaEmp[pos] = ",".join(listaEmp[pos])
    print(listaEmp)
    print("Datos guardados")

def reporteEmpleados(lista):
    print("\n REPORTE DE LOS EMMPLEADOS \n")
    for empleado in lista:
        print(f"Nombre: {empleado[0]}")
        print(f"Edad: {empleado[1]}")
        print(f"Salario: {empleado[2]}\n")

def altaEmpleado(lista):
    nombre = input("Dime el nombre del nuevo empleado: ")
    edad = int(input("Dime la edad del nuevo empleado: "))
    salario = float(input("Dime el salario del nuevo empleado: "))
    lista.append([nombre,edad,salario])
    return lista

def consultaEmpleado(lista,nombre):
    encontrado = False
    for empleado in lista:
        if nombre in empleado: #if(empleado[0] == nombre):
            encontrado = True
            print(f"Nombre: {empleado[0]}")
            print(f"Edad: {empleado[1]}")
            print(f"Salario: {empleado[2]}\n")
            break
    
    if not(encontrado):
        print(f"La persona {nombre} no trabaja aqui")

def main():
    op = 0
    listaEmp = []
    while (op != 6):
        op = menu()
        if (op == 1):
            listaEmp = leerDatosArchivo()
        elif (op == 2):
            guardarDatosArchivo(listaEmp)
        elif (op == 3):
            reporteEmpleados(listaEmp)
        elif (op == 4):
            listaEmp = altaEmpleado(listaEmp)
        elif (op == 5):
            nom = input("Dime el nombre que buscas: ")
            consultaEmpleado(listaEmp,nom)
        elif (op == 6):
            print("Vuelva pronto")
        else:
            print("Opcion no valida. Vuelva a intentarlo")
            
main()
