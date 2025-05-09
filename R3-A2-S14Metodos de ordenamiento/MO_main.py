from MO_view import Vista
from MO_controller import Controlador

def main():
    vista = Vista(None)
    controlador = Controlador(vista)
    vista.controlador = controlador
    vista.ejecutar()
    
main()