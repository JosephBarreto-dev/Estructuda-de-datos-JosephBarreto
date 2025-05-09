from MO_model import ListaClientes

class Controlador:
    def __init__(self, vista):
        self.modelo = ListaClientes()
        self.vista = vista
        
    def insertar_cliente(self, cedula, nombre):
        self.modelo.insertar_cliente(cedula, nombre)
        
    def ordenar_burbuja(self):
        return self.modelo.ordenar_burbuja()
    
    def ordenar_secuencial(self):
        return self.modelo.ordenar_secuencial()
    
    def ordenar_quicksort(self):
        return self.modelo.ordenar_quicksort()