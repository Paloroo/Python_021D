def menu():

    print("##### Calculadora #####")
    print("1. Sumar")
    print("2. Restar")
    print("3. Multiplicar")
    print("4. Dividir")
    print("5. Potencia")
    print("6. Salir")

def calcular(numero1,numero2,opcion):
    if opcion == 1:
        resultado = numero1+numero2
        print(f"El resultado es: {resultado}")
    elif opcion == 2:
        resultado = numero1-numero2
        print(f"El resultado es: {resultado}")
    elif opcion == 3:
        resultado = numero1 * numero2
        print(f"el resultado es: {resultado}")
    elif opcion == 4:
        while numero2 != 0:
            resultado = numero1 / numero2
        else:    
            print("No se puede dividir por cero.")
        print(f"El resultado es: {resultado}")  
    elif opcion == 5:
        resultado = numero1**numero2
    print(f"El resultado es: {resultado}")              