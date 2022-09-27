def mayoresX(listaNom,listaEdad,Edad):
    salida = []
    for pos in range(len(listaNom)):
        if (listaEdad[pos] >= Edad):
            salida.append(listaNom[pos])
    return salida

def altaEmpleado():
    """Regresa una lista con los empleados dados de alta.
    Debe de preguntar si quiere dar de alta otro empleado.
    Cada elemento de la lista tiene la siguiente estructura:
        (Nombre,Edad,Antiguedad,Salario)
    """
    salida = []
    res = input("Quieres añadir un empleado (Si/No)? ").lower()
    while (res == "si"):
        nombre = input("Dime el nombre: ")
        edad = int(input("Dime la edad: "))
        ant = int(input("Dime la antiguedad: "))
        salario = float(input("Dime el salario: "))
        tuplaInfo = (nombre,edad,ant,salario)
        salida.append(tuplaInfo)
        res = input("Quieres añadir otro empleado (Si/No)? ").lower()
    
    return salida

def promedioSalarios(listaEmp):
    """Recibe una lista con tuplas con la siguiente informacion:
            (Nombre,Edad,Antiguedad,Salario)
        Regresa el promedio de los salarios de los empleados
    """
    suma = 0
    for infoEmpleado in listaEmp:
        suma += infoEmpleado[3]
    promedio = suma / len(listaEmp)
    return promedio
