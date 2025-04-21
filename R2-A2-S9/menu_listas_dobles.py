class Nodo:
    def __init__(self, cedula, nombre):
        self.cedula = cedula
        self.nombre = nombre
        self.anterior = None
        self.siguiente = None

class ListaClientesDoble:
    def __init__(self):
        self.inicio = None

    def insertar_cliente(self, cedula, nombre):
        nuevo = Nodo(cedula, nombre)

        # Si la lista está vacía
        if self.inicio is None:
            self.inicio = nuevo
            print("Cliente insertado correctamente.")
            return

        actual = self.inicio
        anterior = None

        # Buscar la posición correcta para insertar
        while actual and cedula > actual.cedula:
            anterior = actual
            actual = actual.siguiente

        if anterior is None:
            # Insertar al principio
            nuevo.siguiente = self.inicio
            self.inicio.anterior = nuevo
            self.inicio = nuevo
        else:
            # Insertar en medio o al final
            nuevo.siguiente = actual
            nuevo.anterior = anterior
            anterior.siguiente = nuevo
            if actual:
                actual.anterior = nuevo

        print("Cliente insertado correctamente.")

    def listar_derecha(self):
        actual = self.inicio
        if actual is None:
            print("La lista está vacía.")
            return
        print("\nClientes (inicio → fin):")
        while actual:
            print(f"Cédula: {actual.cedula} | Nombre: {actual.nombre}")
            actual = actual.siguiente

    def listar_izquierda(self):
        actual = self.inicio
        if actual is None:
            print("La lista está vacía.")
            return

        # Ir al último nodo
        while actual.siguiente:
            actual = actual.siguiente

        print("\nClientes (fin → inicio):")
        while actual:
            print(f"Cédula: {actual.cedula} | Nombre: {actual.nombre}")
            actual = actual.anterior

# Menú de la aplicación
def menu():
    lista_clientes = ListaClientesDoble()

    while True:
        print("\n--- Menú ---")
        print("1. Insertar cliente")
        print("2. Listar clientes hacia la derecha")
        print("3. Listar clientes hacia la izquierda")
        print("4. Salir")

        opcion = input("Seleccione una opción: ")

        if opcion == "1":
            cedula = int(input("Ingrese la cédula del cliente: "))
            nombre = input("Ingrese el nombre del cliente: ")
            lista_clientes.insertar_cliente(cedula, nombre)

        elif opcion == "2":
            lista_clientes.listar_derecha()

        elif opcion == "3":
            lista_clientes.listar_izquierda()

        elif opcion == "4":
            print("Aplicación finalizada.")
            break
        else:
            print("Opción no válida. Intente de nuevo.")

# Ejecutar la aplicación
if __name__ == "__main__":
    menu()
