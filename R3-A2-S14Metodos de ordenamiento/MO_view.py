import tkinter as tk
from tkinter import messagebox, ttk

class Vista:
    def __init__(self, controlador):
        self.controlador = controlador
        self.ventana = tk.Tk()
        self.ventana.title("Ordenamiento de Clientes")
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
            
        self.btn_agregar = tk.Button(self.cont_superior, text='Agregar', command=self.insertar_cliente)
        self.btn_agregar.pack(side='left', pady=5)

        self.btn_ordenar_burbuja = tk.Button(self.cont_superior, text='Burbuja', command=self.ordenar_burbuja)
        self.btn_ordenar_burbuja.pack(side='left', pady=5)
        
        self.btn_ordenar_secuencial = tk.Button(self.cont_superior, text='Secuencial', command=self.ordenar_secuencial)
        self.btn_ordenar_secuencial.pack(side='left', pady=5)
        
        self.btn_ordenar_quicksort = tk.Button(self.cont_superior, text='Quicksort', command=self.ordenar_quicksort)
        self.btn_ordenar_quicksort.pack(side='left', pady=5)

        self.tabla = ttk.Treeview(self.cont_Inferior, columns=("cedula", "nombre"), show='headings')
        self.tabla.heading("cedula", text="Cédula")
        self.tabla.heading("nombre", text="Nombre")
        self.tabla.pack(pady=5)
        
    def insertar_cliente(self):
        cedula = self.entrada_cedula.get()
        nombre = self.entrada_nombre.get()        
        if cedula and nombre:
            self.controlador.insertar_cliente(cedula, nombre)
            self.entrada_cedula.delete(0, tk.END)
            self.entrada_nombre.delete(0, tk.END)
            messagebox.showinfo('Cliente agregado', f'El cliente {nombre} con cedula {cedula} fue agregado')
            self.tabla.insert("", tk.END, values=(cedula, nombre))
        else:
            messagebox.showerror('Error', 'Ingresa los datos')
            
    def ordenar_burbuja(self):
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)
            
        clientes = self.controlador.ordenar_burbuja()
        for cedula, nombre in clientes:
            self.tabla.insert("", tk.END, values=(cedula, nombre))
            
    def ordenar_secuencial(self):
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)
            
        self.controlador.ordenar_secuencial()
        clientes = self.controlador.ordenar_secuencial()
        for cedula, nombre in clientes:
            self.tabla.insert("", tk.END, values=(cedula, nombre))
            
    def ordenar_quicksort(self):
        for fila in self.tabla.get_children():
            self.tabla.delete(fila)
            
        clientes = self.controlador.ordenar_quicksort()
        for cedula, nombre in clientes:
            self.tabla.insert("", tk.END, values=(cedula, nombre))

    
    def ejecutar(self):
        self.ventana.mainloop()