def mostrar_menu():
    print("\nMENÚ")
    print("1. Insertar por la derecha")
    print("2. Insertar por la izquierda")
    print("3. Atender por la derecha")
    print("4. Atender por la izquierda")
    print("5. Listar")
    print("6. Salir")

def insertar_derecha(bicola):
    valor = input("Ingrese el valor a insertar por la derecha: ")
    bicola.append(valor)
    print(f"'{valor}' insertado por la derecha.")

def insertar_izquierda(bicola):
    valor = input("Ingrese el valor a insertar por la izquierda: ")
    bicola.insert(0, valor)
    print(f"'{valor}' insertado por la izquierda.")

def atender_derecha(bicola):
    if bicola:
        valor = bicola.pop()
        print(f"Se atendió por la derecha: '{valor}'")
    else:
        print("Bicola vacía. No hay nada que atender.")

def atender_izquierda(bicola):
    if bicola:
        valor = bicola.pop(0)
        print(f"Se atendió por la izquierda: '{valor}'")
    else:
        print("Bicola vacía. No hay nada que atender.")

def listar_bicola(bicola):
    if bicola:
        print("\nContenido actual de la bicola:")
        print(" <- ".join(bicola))
    else:
        print("La bicola está vacía.")

def main():
    bicola = []
    while True:
        mostrar_menu()
        opcion = input("Seleccione una opción (1-6): ")
        
        if opcion == "1":
            insertar_derecha(bicola)
        elif opcion == "2":
            insertar_izquierda(bicola)
        elif opcion == "3":
            atender_derecha(bicola)
        elif opcion == "4":
            atender_izquierda(bicola)
        elif opcion == "5":
            listar_bicola(bicola)
        elif opcion == "6":
            print("¡Hasta luego!")
            break
        else:
            print("Opción no válida. Intente nuevamente.")

if __name__ == "__main__":
    main()
