def buscar_en_matriz(matriz, valor):
    """Busca un valor en la matriz y devuelve su posición."""
    for fila in range(len(matriz)):
        for columna in range(len(matriz[fila])):
            if matriz[fila][columna] == valor:
                return fila, columna
    return None

# Definir la matriz 3x3
matriz = [
    [1, 2, 3],
    [4, 5, 6],
    [7, 8, 9]
]

# Definir el valor a buscar
valor_buscado = 9

# Buscar el valor en la matriz
posicion = buscar_en_matriz(matriz, valor_buscado)

# Mostrar el resultado
if posicion:
    print(f"El número {valor_buscado} se encuentra en la posición (fila: {posicion[0] + 1}, columna: {posicion[1] + 1}).")
else:
    print(f"El número {valor_buscado} no está en la matriz.")