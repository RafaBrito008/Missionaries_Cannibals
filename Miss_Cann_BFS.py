# PRUEBA DE MEDIO PARCIAL
# RAFAEL BRITO

from collections import deque


# Función que valida si un estado de (Monjes, Caníbales) es seguro o no.
def es_estado_valido(M, C):
    # Si hay más caníbales que monjes en una orilla y hay monjes en esa orilla, no es un estado válido.
    if (M < C and M > 0) or (M > C and M < 3):
        return False
    # Validación para valores fuera de los límites aceptables.
    if M < 0 or C < 0 or M > 3 or C > 3:
        return False
    return True


# Función que genera todos los movimientos posibles desde un estado dado.
def movimientos_posibles(M, C, B):
    # Posibles movimientos: (Monjes, Caníbales)
    movimientos = [(-1, -1), (-2, 0), (0, -2), (-1, 0), (0, -1)]
    posibilidades = []

    for m, c in movimientos:
        # Calcula el nuevo estado después de aplicar el movimiento.
        new_M = M + m * B - m * (1 - B)
        new_C = C + c * B - c * (1 - B)
        new_B = 1 - B

        # Si el nuevo estado es válido, lo añade a las posibilidades.
        if es_estado_valido(new_M, new_C):
            posibilidades.append((new_M, new_C, new_B))

    return posibilidades


# Función que devuelve el estado de la orilla derecha a partir de un estado de la orilla izquierda.
def estado_derecha(M, C, B):
    return (3 - M, 3 - C, 1 - B)


# Algoritmo de búsqueda en anchura.
def bfs():
    estado_inicial = (3, 3, 1)
    estado_final = (0, 0, 0)

    visitados = set()  # Conjunto para mantener un registro de los estados visitados.
    cola = deque(
        [(estado_inicial, [])]
    )  # Cola que contiene el estado actual y el camino recorrido.

    # Mientras haya elementos en la cola.
    while cola:
        # Extraer el estado y el camino hasta ahora.
        (M, C, B), ruta = cola.popleft()

        # Si el estado actual es el estado objetivo.
        if (M, C, B) == estado_final:
            return ruta + [(M, C, B)]  # Devuelve el camino completo.

        # Explorar estados vecinos.
        for estado_siguiente in movimientos_posibles(M, C, B):
            if estado_siguiente not in visitados:
                visitados.add(estado_siguiente)
                # Añade el estado siguiente a la cola y actualiza el camino.
                cola.append((estado_siguiente, ruta + [(M, C, B)]))

    return None  # Si no se encuentra una solución.


if __name__ == "__main__":
    solucion = bfs()
    if solucion:
        print("SOLUCIÓN ENCONTRADA:")
        # Imprime cada estado en la solución.
        for estado in solucion:
            M, C, B = estado
            M_d, C_d, B_d = estado_derecha(M, C, B)
            print(
                f"Orilla Izquierda -> Monjes={M}, Caníbales={C}, Bote={B} || Orilla Derecha -> Monjes={M_d}, Caníbales={C_d}, Bote={B_d}"
            )
    else:
        print("No hay solución.")
