def mostrar_menu():

    print("\n" + "="*50)
    print(" SISTEMA DE GESTIÓN DE PELÍCULAS")
    print("="*50)
    print("1. Agregar película")
    print("2. Listar todas las películas")
    print("3. Buscar película")
    print("4. Actualizar película")
    print("5. Eliminar película")
    print("6. Salir")
    print("="*50)
def agregar_pelicula(lista_peliculas):
    print("\n--- AGREGAR NUEVA PELÍCULA ---")

    nombre = input("Ingrese el nombre de la película: ").strip()
    if not nombre:
        print("⚠️ El nombre no puede estar vacío.")
    
    
        
try:
    año = int(input("Ingrese el año de estreno: "))
    if año < 1888 or año > 2024:
        print("⚠️ Año fuera de rango válido (1888 - 2024).")
        
except ValueError:
    print("⚠️ Entrada inválida. Debe ser un número entero.")
    

categoria = input("Ingrese la categoría: ").strip()
if not categoria:
    print("⚠️ La categoría no puede estar vacía.")


nueva_pelicula = {
   
    "año": año,
    "categoria": categoria
    }
