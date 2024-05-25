# Algoritmo FCFS (first come, first served)

def fcfs(cola, posicion_inicial):

    # Inicializar la posición actual de la cabeza
    posicion_actual = posicion_inicial

    # Inicializar el número de desplazamientos
    desplazamientos = 0

    # Lista para almacenar los pares [desplazamiento, solicitud]
    lista_solicitudes_atendidas = []

    # Agregar el desplazamiento inicial
    lista_solicitudes_atendidas.append([desplazamientos, posicion_inicial])

    # Iterar sobre la cola
    for solicitud in cola:
        # Calcular el desplazamiento hasta la nueva solicitud
        desplazamientos += abs(solicitud - posicion_actual)

        # Agregar el par [desplazamiento, solicitud] a la lista
        lista_solicitudes_atendidas.append([desplazamientos, solicitud])

        # Actualizar la posición actual de la cabeza
        posicion_actual = solicitud

    return desplazamientos, lista_solicitudes_atendidas