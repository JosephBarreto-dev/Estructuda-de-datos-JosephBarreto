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
        
    def listar_derecha(self):
        clientes = []
        actual = self.inicio
        while actual:
            clientes.append((actual.cedula, actual.nombre))
            actual = actual.siguiente
        return clientes

    def listar_izquierda(self):
        clientes = []
        actual = self.inicio
        while actual and actual.siguiente:
            actual = actual.siguiente

        while actual:
            clientes.append((actual.cedula, actual.nombre))
            actual = actual.anterior
        return clientes