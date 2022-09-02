def cuentaPNC(cuantos):
    contPos = 0
    contNeg = 0
    contCero = 0
    while(cuantos > 0):
        num = int(input("Dime un numero: "))
        if (num > 0):
            contPos += 1
        elif (num < 0):
            contNeg += 1
        else:
            contCero += 1
        cuantos -= 1
    return contPos,contNeg,contCero

def aPositivo(cuantos):
    while (cuantos > 0):
        num = int(input("Dime un numero negativo para pasarlo a positivo: "))
        while (num >= 0):
            num = int(input("Dime un numero negativo para pasarlo a positivo: "))    
        
        print(-1*num)
        cuantos -= 1
        

def main():
    #Problema 1
    print("*** Problema 1 - Cuenta20 ***")
    nume = int(input("Dime cuantos numeros analizar: "))
    pos,neg,cero = cuentaPNC(nume)
    print(f"Fueron {pos} positivos, {neg} negativos y {cero} ceros")
    
    #Problema 2
    print("\n*** Problema 2 - A positivo")
    nume = int(input("Dime cuantos numeros: "))
    aPositivo(nume)
    