from GUI_view import Vista
from GUI_controller import Controlador

def main():
    vista = Vista(None)
    controlador = Controlador(vista)
    vista.controlador = controlador
    vista.ejecutar()

main()