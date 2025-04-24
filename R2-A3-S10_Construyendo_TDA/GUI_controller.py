from GUI_model import ListaClientesDoble

class Controlador:
    def __init__(self, vista):
        self.modelo = ListaClientesDoble()
        self.vista = vista
        
    def agregar_cliente(self, cedula, nombre):
        self.modelo.insertar_cliente(cedula, nombre)
        
    def listar_derecha(self):
        return self.modelo.listar_derecha()
    
    def listar_izquierda(self):
        return self.modelo.listar_izquierda()