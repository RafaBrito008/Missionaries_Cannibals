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


# Realiza una búsqueda bidireccional desde el inicio y el objetivo.
def busqueda_bidireccional():
    inicio = (3, 3, 1)
    objetivo = (0, 0, 0)

    # Diccionarios para controlar los nodos visitados desde el inicio y desde el objetivo.
    visitados_inicio = {inicio: None}
    visitados_fin = {objetivo: None}

    # Colas para controlar los estados pendientes de visitar.
    cola_inicio = deque([(inicio, [])])
    cola_fin = deque([(objetivo, [])])

    # Mientras haya estados por visitar en ambas direcciones.
    while cola_inicio and cola_fin:
        # Expande la cola desde el inicio.
        estado_actual_inicio, camino_inicio = expandir_cola(
            cola_inicio, visitados_inicio
        )
        # Si se encuentra un estado ya visitado desde el final, se ha encontrado una conexión.
        if estado_actual_inicio in visitados_fin:
            camino_desde_fin = list(reversed(visitados_fin[estado_actual_inicio]))
            return camino_inicio, camino_desde_fin

        # Lo mismo, pero empezando desde el final.
        estado_actual_fin, camino_fin = expandir_cola(cola_fin, visitados_fin)
        if estado_actual_fin in visitados_inicio:
            camino_desde_inicio = visitados_inicio[estado_actual_fin]
            return camino_desde_inicio, camino_fin

    return [], []


# Función que expande la cola de estados a visitar.
def expandir_cola(cola, visitados):
    estado_actual, camino = cola.popleft()
    M, C, B = estado_actual
    for m, c, b in movimientos_posibles(M, C, B):
        nuevo_estado = (m, c, b)
        # Si el estado no ha sido visitado previamente, se añade a la cola.
        if nuevo_estado not in visitados:
            nuevo_camino = camino + [estado_actual]
            cola.append((nuevo_estado, nuevo_camino))
            visitados[nuevo_estado] = camino + [estado_actual]
    return estado_actual, camino


# Punto de entrada principal.
if __name__ == "__main__":
    camino_desde_inicio, camino_desde_fin = busqueda_bidireccional()

    # Si se ha encontrado una solución, se imprime.
    if camino_desde_inicio or camino_desde_fin:
        print("Camino desde el inicio:")
        for paso in camino_desde_inicio:
            print(paso)

        print("\nCamino desde el objetivo (invertido):")
        for paso in camino_desde_fin:
            print(paso)

        print("\nCamino completo de solución:")
        camino_completo = camino_desde_inicio + list(reversed(camino_desde_fin))
        for paso in camino_completo:
            print(paso)
    else:
        print("No hay solución")
