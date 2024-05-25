# Algoritmo SSTF (shortest seek time first)

def sstf(cola, posicion_inicial):
    # Clonar la cola para no modificar la original, y ordenarla por cercanía de solicitud
    cola_ordenada = sorted(cola, key=lambda x: abs(x - posicion_inicial))

    # Inicializar el número de desplazamientos
    desplazamientos = 0

    # Inicializar la posición actual de la cabeza
    posicion_actual = posicion_inicial

    # Lista para almacenar los pares [desplazamiento, solicitud]
    lista_solicitudes_atendidas = []

    # Agregar el desplazamiento inicial
    lista_solicitudes_atendidas.append([desplazamientos, posicion_inicial])

    # Iterar sobre la cola ordenada
    for solicitud in cola_ordenada:
        # Calcular el desplazamiento hasta la nueva solicitud
        desplazamientos += abs(solicitud - posicion_actual)

        # Actualizar la posición actual de la cabeza
        posicion_actual = solicitud

        # Agregar el par [desplazamiento, solicitud] a la lista
        lista_solicitudes_atendidas.append([desplazamientos, solicitud])

    return desplazamientos, lista_solicitudes_atendidas