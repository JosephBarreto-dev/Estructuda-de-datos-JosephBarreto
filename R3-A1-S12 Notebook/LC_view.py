import tkinter as tk

class vista:
    def __init__(self):
        self.ventana = tk.Tk()
        self.ventana.title('Menú clientes')
        self.ventana.geometry('700x500')
        self.ventana.resizable(False, False)

        self.continer = tk.Frame(self.ventana)

        self.lista_c = tk.Text()