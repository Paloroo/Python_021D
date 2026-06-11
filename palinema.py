peliculas = ["rey leon","el titanic", "rango"]
salida_menu = False
while not salida_menu:
    
    print("######Peliculas######")
    print("1. Guardar peliculas")
    print("2. Mostrar peliculas")
    print("3. Buscar pelicula")
    print("4. Eliminar peliculas")
    print("5. Actualizar peliculas")
    
    salir = False
    while not salir:
        try:
            opt = int(input("Seleccione una opción: "))
        except ValueError:
            print("Opción no valida, ingrese nuevamente. P")
        else:
            
            if opt == 1:
                pelicula_a_guardar = input("Ingrese el nombre de la pelicula: ").strip().lower()
                print("peli guardada")
                while pelicula_a_guardar == "":
                    print("Debe ingresar el nombre de una pelicula")
                    pelicula_a_guardar = input("Ingrese el nombre de la pelicula: ").strip().lower()

                peliculas.append(pelicula_a_guardar)
                print("pelicula guardada con exito")     
            elif opt == 2:
                for posicion,peliculas in enumerate(peliculas):
                    print(f"{posicion+1}) - {peliculas.title()} ") 

            elif opt == 3:
                print("buscar pelicula")
                buscar_pelicula = input("Ingrese la pelicula que quiere buscar: ").strip().lower()
                pelicula_agendada = False
                for pelicula in peliculas:
                    if peliculas == buscar_pelicula:  
                        print(f"la pelicula guardada es: {buscar_pelicula},{posicion+1}")
                        pelicula_agendada = True

                if not pelicula_agendada:
                     print("Pelicula no encontrada")

                elif opt == 4:
                    print("Eliminar")
                    peli_a_eliminar = input("Ingrese a la pelicula a eliminar: ")
                    peliculas.pop(posicion)           
                    print("Eliminación completa, ya no esta la pelicula")
                elif opt == 5:
                    print("actualización")
                    actualizacion_de_la_cartelera = input("la cartelera ha sido actualizada, esta es la cartelera: ")
                    actualizacion = peliculas.replace("rey leon", "el rey leon")
                    print(f"{peliculas}")