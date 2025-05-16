import os
import time

# Función para limpiar la pantalla según el sistema operativo
def limpiar_pantalla():
    os.system('cls' if os.name == 'nt' else 'clear')

# Función para dibujar las torres en consola
def mostrar_torres(torres, num_discos):
    limpiar_pantalla()
    print("\n🔁 Estado actual de las torres:\n")
    for nivel in reversed(range(num_discos)):
        for torre in ['A', 'B', 'C']:
            if nivel < len(torres[torre]):
                disco = torres[torre][nivel]
                relleno = "-" * disco
                espacio = " " * (num_discos - disco)
                print(espacio + relleno + "|" + relleno + espacio, end="  ")
            else:
                print(" " * num_discos + "|" + " " * num_discos, end="  ")
        print()
    print("   A" + " " * (num_discos*2) + "B" + " " * (num_discos*2) + "C\n")
    time.sleep(0.5)

# Algoritmo recursivo de Torres de Hanoi
def hanoi(n, origen, destino, auxiliar, torres, num_discos):
    if n == 1:
        disco = torres[origen].pop()
        torres[destino].append(disco)
        mostrar_torres(torres, num_discos)
    else:
        hanoi(n - 1, origen, auxiliar, destino, torres, num_discos)
        hanoi(1, origen, destino, auxiliar, torres, num_discos)
        hanoi(n - 1, auxiliar, destino, origen, torres, num_discos)

# Función principal
def main():
    num_discos = int(input("Ingrese el número de discos: "))
    torres = {
        'A': list(reversed(range(1, num_discos + 1))),
        'B': [],
        'C': []
    }
    mostrar_torres(torres, num_discos)
    hanoi(num_discos, 'A', 'C', 'B', torres, num_discos)
    print("✅ ¡Todos los discos se han movido correctamente!\n")

if __name__ == "__main__":
    main()
