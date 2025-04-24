import tkinter as tk
from tkinter import ttk
from tkinter import messagebox

class Vista:
    def __init__(self, controlador):
        self.controlador = controlador
        self.ventana = tk.Tk()
        self.ventana.title('Menú clientes')
        self.ventana.geometry('700x500')
        self.ventana.resizable(False, False)

        self.cont_superior = tk.Frame(self.ventana)
        self.cont_superior.pack(side='top', expand=True)
        self.cont_Inferior = tk.Frame(self.ventana)
        self.cont_Inferior.pack(side='bottom', expand=True)

        self.etiqueta_cedula = tk.Label(self.cont_superior, text='Cedula: ')
        self.etiqueta_cedula.pack(pady=5)

        self.entrada_cedula = tk.Entry(self.cont_superior)
        self.entrada_cedula.pack(pady=5)

        self.etiqueta_nombre = tk.Label(self.cont_superior, text='Nombre: ')
        self.etiqueta_nombre.pack(pady=5)

        self.entrada_nombre = tk.Entry(self.cont_superior)
        self.entrada_nombre.pack(pady=5)
            
        self.btn_agregar = tk.Button(self.cont_superior, text='Agregar', command=self.agregar_cliente)
        self.btn_agregar.pack(side='left', pady=5)

        self.btn_lista_derecha = tk.Button(self.cont_superior, text='Lista derecha', command=self.listar_derecha)
        self.btn_lista_derecha.pack(side='left', pady=5)

        self.btn_lista_izquierda = tk.Button(self.cont_superior, text='Lista izquierda', command=self.listar_izquierda)
        self.btn_lista_izquierda.pack(side='left', pady=5)

        self.tabla = ttk.Treeview(self.cont_Inferior, columns=("cedula", "nombre"), show='headings')
        self.tabla.heading("cedula", text="Cédula")
        self.tabla.heading("nombre", text="Nombre")
        self.tabla.pack(pady=5)
        
    def agregar_cliente(self):
        cedula = self.entrada_cedula.get()
        nombre = self.entrada_nombre.get()
        if cedula and nombre:
            self.controlador.agregar_cliente(cedula, nombre)
            self.entrada_cedula.delete(0, tk.END)
            self.entrada_nombre.delete(0, tk.END)
            messagebox.showinfo('Cliente agregado', f'El cliente {nombre} con cedula {cedula} fue agregado')
        else:
            messagebox.showerror('Error', 'Ingresa los datos requeridos')
            
    def listar_derecha(self):
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)
        
        clientes = self.controlador.listar_derecha()
        for cedula, nombre in clientes:
            self.tabla.insert("", "end", values=(cedula, nombre))
        
    def listar_izquierda(self):
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)
        
        clientes = self.controlador.listar_izquierda()
        for cedula, nombre in clientes:
            self.tabla.insert("", "end", values=(cedula, nombre))
        
    def ejecutar(self):
        self.ventana.mainloop()