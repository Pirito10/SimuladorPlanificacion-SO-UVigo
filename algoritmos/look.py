# Algoritmo LOOK

def look(cola, posicion_inicial):
    # Ordenar la cola de solicitudes
    cola_ordenada = sorted(cola)

    # Inicializar el número de desplazamientos
    desplazamientos = 0

    # Inicializar la posición actual de la cabeza
    posicion_actual = posicion_inicial

    # Lista para almacenar los pares [desplazamiento, solicitud]
    lista_solicitudes_atendidas = []

    # Agregar el desplazamiento inicial
    lista_solicitudes_atendidas.append([desplazamientos, posicion_inicial])

    # Filtrar las solicitudes que están antes y después de la posición actual
    solicitudes_antes = [solicitud for solicitud in cola_ordenada if solicitud < posicion_actual]
    solicitudes_despues = [solicitud for solicitud in cola_ordenada if solicitud >= posicion_actual]

    # Moverse hacia el inicio atendiendo las solicitudes antes de la posición actual
    for solicitud in reversed(solicitudes_antes):
        desplazamientos += abs(solicitud - posicion_actual)
        posicion_actual = solicitud

        # Agregar el par [desplazamiento, solicitud] a la lista
        lista_solicitudes_atendidas.append([desplazamientos, solicitud])

    # Moverse hacia el otro extremo atendiendo las solicitudes
    for solicitud in solicitudes_despues:
        desplazamientos += abs(solicitud - posicion_actual)
        posicion_actual = solicitud

        # Agregar el par [desplazamiento, solicitud] a la lista
        lista_solicitudes_atendidas.append([desplazamientos, solicitud])

    return desplazamientos, lista_solicitudes_atendidas