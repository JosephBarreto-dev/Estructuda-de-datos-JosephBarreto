class Nodo:
    def __init__(self, valor):
        self.valor = valor
        self.izquierda = None
        self.derecha = None

class ArbolBinario:
    def __init__(self):
        self.raiz = None

    def insertar(self, valor):
        if self.raiz is None:
            self.raiz = Nodo(valor)
        else:
            self._insertar_recursivo(self.raiz, valor)

    def _insertar_recursivo(self, nodo, valor):
        if valor < nodo.valor:
            if nodo.izquierda is None:
                nodo.izquierda = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.izquierda, valor)
        elif valor > nodo.valor:
            if nodo.derecha is None:
                nodo.derecha = Nodo(valor)
            else:
                self._insertar_recursivo(nodo.derecha, valor)
        # Si el valor ya existe, no lo insertamos (opcional)

    def inorden(self):
        print("Recorrido Inorden:")
        self._inorden_recursivo(self.raiz)
        print()

    def _inorden_recursivo(self, nodo):
        if nodo:
            self._inorden_recursivo(nodo.izquierda)
            print(nodo.valor, end=" ")
            self._inorden_recursivo(nodo.derecha)

    def preorden(self):
        print("Recorrido Preorden:")
        self._preorden_recursivo(self.raiz)
        print()

    def _preorden_recursivo(self, nodo):
        if nodo:
            print(nodo.valor, end=" ")
            self._preorden_recursivo(nodo.izquierda)
            self._preorden_recursivo(nodo.derecha)

    def postorden(self):
        print("Recorrido Postorden:")
        self._postorden_recursivo(self.raiz)
        print()

    def _postorden_recursivo(self, nodo):
        if nodo:
            self._postorden_recursivo(nodo.izquierda)
            self._postorden_recursivo(nodo.derecha)
            print(nodo.valor, end=" ")

# Menú principal
def menu():
    arbol = ArbolBinario()
    while True:
        print("\n--- MENÚ ---")
        print("1. Insertar dato")
        print("2. Imprimir en In orden")
        print("3. Imprimir en Post orden")
        print("4. Imprimir en Pre orden")
        print("5. Salir")
        opcion = input("Selecciona una opción: ")

        if opcion == "1":
            try:
                valor = int(input("Ingresa un número: "))
                arbol.insertar(valor)
            except ValueError:
                print("Por favor, ingresa un número válido.")
        elif opcion == "2":
            arbol.inorden()
        elif opcion == "3":
            arbol.postorden()
        elif opcion == "4":
            arbol.preorden()
        elif opcion == "5":
            print("¡Hasta luego!")
            break
        else:
            print("Opción inválida. Intenta de nuevo.")

# Ejecutar el menú
if __name__ == "__main__":
    menu()