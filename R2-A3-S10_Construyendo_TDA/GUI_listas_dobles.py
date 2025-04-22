import tkinter as tk

class Nodo:
    def __init__(self, cedula, nombre):
        self.cedula = cedula
        self.nombre = nombre
        self.anterior = None
        self.siguiente = None

class ListaClientesDoble:
    def __init__(self):
        self.inicio = None

    def insertar_cliente(self, cedula, nombre):
        nuevo = Nodo(cedula, nombre)

        # Si la lista está vacía
        if self.inicio is None:
            self.inicio = nuevo
            print("Cliente insertado correctamente.")
            return

        actual = self.inicio
        anterior = None

        # Buscar la posición correcta para insertar
        while actual and cedula > actual.cedula:
            anterior = actual
            actual = actual.siguiente

        if anterior is None:
            # Insertar al principio
            nuevo.siguiente = self.inicio
            self.inicio.anterior = nuevo
            self.inicio = nuevo
        else:
            # Insertar en medio o al final
            nuevo.siguiente = actual
            nuevo.anterior = anterior
            anterior.siguiente = nuevo
            if actual:
                actual.anterior = nuevo

        print("Cliente insertado correctamente.")
        
    def listar_derecha(self):
        actual = self.inicio
        if actual is None:
            print("La lista está vacía.")
            return
        print("\nClientes (inicio → fin):")
        while actual:
            print(f"Cédula: {actual.cedula} | Nombre: {actual.nombre}")
            actual = actual.siguiente

    def listar_izquierda(self):
        actual = self.inicio
        if actual is None:
            print("La lista está vacía.")
            return

        # Ir al último nodo
        while actual.siguiente:
            actual = actual.siguiente

        print("\nClientes (fin → inicio):")
        while actual:
            print(f"Cédula: {actual.cedula} | Nombre: {actual.nombre}")
            actual = actual.anterior
    
# Menú de la aplicación
lista_clientes = ListaClientesDoble()

ventana = tk.Tk()
ventana.title('Menú clientes')

etiqueta_cedula = tk.Label(ventana, text='Cedula: ')
etiqueta_cedula.pack()

entrada_cedula = tk.Entry(ventana)
entrada_cedula.pack()

etiqueta_nombre = tk.Label(ventana, text='Nombre: ')
etiqueta_nombre.pack()

entrada_nombre = tk.Entry(ventana)
entrada_nombre.pack()

def agregar_cliente_vista():
    cedula = entrada_cedula.get()
    nombre = entrada_nombre.get()
    lista_clientes.insertar_cliente(cedula, nombre)
    entrada_cedula.delete(0, tk.END)
    entrada_nombre.delete(0, tk.END)
    
btn_agregar = tk.Button(ventana, text='Agregar', command= lambda: agregar_cliente_vista())
btn_agregar.pack()

btn_lista_derecha = tk.Button(ventana, text='Lista derecha', command=lista_clientes.listar_derecha)
btn_lista_derecha.pack()

btn_lista_izquierda = tk.Button(ventana, text='Lista izquierda', command=lista_clientes.listar_izquierda)
btn_lista_izquierda.pack()

ventana.mainloop()
