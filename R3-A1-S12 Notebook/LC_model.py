class Nodo:
    def __init__(self, cedula, nombre):
        self.cedula = cedula
        self.nombre = nombre
        self.siguiente = None

class ListaCircular:
    def __init__(self):
        self.cabeza = None

    def agregar(self, cedula, nombre):
        nuevo_nodo = Nodo(cedula, nombre)

        if not self.cabeza:
            self.cabeza = nuevo_nodo
            nuevo_nodo.siguiente = nuevo_nodo
        else:
            temp = self.cabeza
            while temp.siguiente != self.cabeza:
                temp = temp.siguiente
            temp.siguiente = nuevo_nodo
            nuevo_nodo.siguiente = self.cabeza
            
    def listar(self):
        datos = []
        if self.cabeza:
            temp = self.cabeza
            while temp:
                datos.append((temp.cedula, temp.nombre))
                temp = temp.siguiente
                if temp == self.cabeza:
                    break
        return datos