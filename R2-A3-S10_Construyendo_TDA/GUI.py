import tkinter as tk

def mostrar_resultado():
    resultado = eval(entrada.get())
    etiqueta_resultado.config(text=f'Resultado:{resultado}')

ventana = tk.Tk()
ventana.title('Menú lista doble')

entrada = tk.Entry(ventana)
entrada.pack()

boton = tk.Button(ventana, text='Calcular', command=mostrar_resultado)
boton.pack()

etiqueta_resultado = tk.Label(ventana, text='Resultado: ')
etiqueta_resultado.pack()

ventana.mainloop()