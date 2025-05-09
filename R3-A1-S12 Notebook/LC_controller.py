from LC_model import ListaCircular

class Controlador:
    def __init__(self, vista):
        self.modelo = ListaCircular()
        self.vista = vista
        
    def agregar(self, cedula, nombre):
        self.modelo.agregar(cedula, nombre)
        
    def listar(self):
        return self.modelo.listar()
        