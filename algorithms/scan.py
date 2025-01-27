# Algoritmo SCAN

def scan(cola, posicion_inicial):
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

    # Lista adicional para almacenar las solicitudes ya atendidas
    solicitudes_atendidas = set()

    # Moverse hacia el inicio cumpliendo las solicitudes antes de la posición actual
    for solicitud in reversed(cola_ordenada):
        if solicitud <= posicion_actual:
            desplazamientos += abs(solicitud - posicion_actual)
            posicion_actual = solicitud

            # Agregar el par [desplazamiento, solicitud] a la lista
            lista_solicitudes_atendidas.append([desplazamientos, solicitud])

            # Marcar la solicitud como atendida
            solicitudes_atendidas.add(solicitud)

    # Moverse al cilindro inicial
    desplazamientos += abs(0 - posicion_actual)
    posicion_actual = 0
    lista_solicitudes_atendidas.append([desplazamientos, 0])

    # Moverse hacia el extremo cumpliendo las solicitudes después de la posición actual
    for solicitud in cola_ordenada:
        if solicitud > posicion_actual and solicitud not in solicitudes_atendidas:
            desplazamientos += abs(solicitud - posicion_actual)
            posicion_actual = solicitud

            # Agregar el par [desplazamiento, solicitud] a la lista
            lista_solicitudes_atendidas.append([desplazamientos, solicitud])

            # Marcar la solicitud como atendida
            solicitudes_atendidas.add(solicitud)

    return desplazamientos, lista_solicitudes_atendidas