class Nodo:
    def __init__(self, cedula, nombre):
        self.cedula = cedula
        self.nombre = nombre
        self.siguiente = None
        
class ListaClientes:
    def __init__(self):
        self.inicio = None

    def insertar_cliente(self, cedula, nombre):
        nuevo = Nodo(cedula, nombre)
        
        if self.inicio is None or cedula<self.inicio.cedula:
            nuevo.siguiente = self.inicio
            self.inicio = nuevo
        else:
            actual = self.inicio
            while actual.siguiente and actual.siguiente.cedula < cedula:
                actual = actual.siguiente
            nuevo.siguiente = actual.siguiente
            actual.siguiente = nuevo
            
    def mostrar_clientes(self):
        actual = self.inicio
        if not actual:
            print("La lista está vacía.")
            return
        print("\nListado de clientes:")
        while actual:
            print(f"Cédula: {actual.cedula}, Nombre: {actual.nombre}")
            actual = actual.siguiente

def menu():
    lista_clientes = ListaClientes()
    while True:
        print("\nMenú:")
        print("1. Insertar cliente")
        print("2. Mostrar clientes")
        print("3. Salir")
        
        opcion = input("Elija una opción: ")
        
        if opcion == "1":
            try:
                cedula = int(input("Ingrese la cédula del cliente: "))
                nombre = input("Ingrese el nombre del cliente: ")
                lista_clientes.insertar_cliente(cedula, nombre)
                print("Cliente insertado correctamente.")
            except ValueError:
                print("cedula invalida. Debe se un numero")
        elif opcion == "2":
            lista_clientes.mostrar_clientes()
        elif opcion == "3":
            print("Saliendo del programa.")
            break
        else:
            print("Opción inválida.")
            
menu()