class Nodo:
    def __init__(self, cedula, nombre):
        self.cedula = cedula
        self.nombre = nombre
        self.siguiente = None
        
class ListaClientes:
    def __init__(self):
        self.clientes = []
        self.inicio = None

    def insertar_cliente(self, cedula, nombre):
        nuevo = Nodo(cedula, nombre)
        
        if nuevo:
            nuevo.siguiente = self.inicio
            self.inicio = nuevo
    
    # Recorre cada nodo de la lista ordenando de menor a mayor
    def ordenar_burbuja(self):
        
        if not self.inicio or not self.inicio.siguiente:
            return self.clientes

        cambiado = True
        while cambiado:
            cambiado = False
            actual = self.inicio
            while actual.siguiente:
                if actual.cedula > actual.siguiente.cedula:
                    actual.cedula, actual.siguiente.cedula = actual.siguiente.cedula, actual.cedula
                    actual.nombre, actual.siguiente.nombre = actual.siguiente.nombre, actual.nombre
                    cambiado = True
                actual = actual.siguiente
                
        actual = self.inicio
        while actual:
            self.clientes.append((actual.cedula, actual.nombre))
            actual = actual.siguiente

        return self.clientes
    
    # Recorre la lista varias veces seleccionando el elemento mas pequello
    def ordenar_secuencial(self):
        if not self.inicio or not self.inicio.siguiente:
            return

        actual = self.inicio
        while actual:
            menor = actual
            siguiente = actual.siguiente
            while siguiente:
                if siguiente.cedula < menor.cedula:
                    menor = siguiente
                siguiente = siguiente.siguiente

            actual.cedula, menor.cedula = menor.cedula, actual.cedula
            actual.nombre, menor.nombre = menor.nombre, actual.nombre

            actual = actual.siguiente
            
        actual = self.inicio
        while actual:
            self.clientes.append((actual.cedula, actual.nombre))
            actual = actual.siguiente
        
        return self.clientes
    
    # De dividen en dos sublistas los numero pequeños a la izquierda y los grandes a la derecha, 
    def ordenar_quicksort(self):
        def partition(start, end):
            if start == end or not start or not end:
                return start, end

            pivot = start
            prev = start
            curr = start.siguiente

            while curr != end.siguiente:
                if curr.cedula < pivot.cedula:
                    prev = prev.siguiente
                    prev.cedula, curr.cedula = curr.cedula, prev.cedula
                    prev.nombre, curr.nombre = curr.nombre, prev.nombre
                curr = curr.siguiente

            pivot.cedula, prev.cedula = prev.cedula, pivot.cedula
            pivot.nombre, prev.nombre = prev.nombre, pivot.nombre

            return prev, prev.siguiente

        def quicksort_recursive(start, end):
            if start == end or not start or not end:
                return

            pivot, next_start = partition(start, end)
            quicksort_recursive(start, pivot)
            quicksort_recursive(next_start, end)

        if not self.inicio or not self.inicio.siguiente:
            return self.clientes

        end = self.inicio
        while end.siguiente:
            end = end.siguiente

        quicksort_recursive(self.inicio, end)
        
        actual = self.inicio
        while actual:
            self.clientes.append((actual.cedula, actual.nombre))
            actual = actual.siguiente
            
        return self.clientes