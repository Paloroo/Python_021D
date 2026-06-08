from operaciones import menu,calcular
salir = False
while not salir:
                     
    menu()
    opcion = int(input("Ingrese una opcion: "))
    if opcion == 6:
        salir = True
    else:
        try:
            numero1 = int(input("Ingrese el primer numero:"))
            numero2 = int(input("Ingrese el segundo numero:"))
        except ValueError:
            print("Solo se permiten numeros, intente nuevamente.")        
        else:
            calcular(numero1,numero2,opcion)    