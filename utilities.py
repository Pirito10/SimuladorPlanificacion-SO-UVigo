import random
import matplotlib.pyplot as plt

# Genera una cola aleatorio, del tamaño indicado, y para el número de cilindros indicado
def generar_cola(tamano, cilindros):
    return [random.randint(0, cilindros - 1) for _ in range(tamano)]

# Verifica que ninguna solicitud de una cola se salga del rango de cilindros
def verificar_solicitudes_en_rango(cilindros, cola):
    for solicitud in cola:
        if not (0 <= solicitud < cilindros):
            print(f"Error: Solicitud {solicitud} fuera del rango de cilindros (0-{cilindros - 1})")
            exit()

# Verifica que la posición inicial de la cabeza se encuentra dentro del rango de cilindros
def verificar_posicion_en_rango(posicion, cilindros):
    if not (0 <= posicion < cilindros):
        print(f"Error: Posición inicial de la cabeza fuera del rango de cilindros (0-{cilindros - 1})")
        exit()

# Calcula el tiempo total de simulación
def simular_tiempo_total(tamano_cola, desplazamientos, TIEMPO_ARRANQUE, TIEMPO_DESPLAZAMIENTO, TIEMPO_DETENCION, TIEMPO_LATENCIA, TIEMPO_TRANSFERENCIA):
    tiempo_total = 0
    tiempo_total += desplazamientos * TIEMPO_DESPLAZAMIENTO
    tiempo_total += TIEMPO_ARRANQUE  # Sumar una sola vez
    tiempo_total += TIEMPO_DETENCION  # Sumar una sola vez

    for i in range(tamano_cola):
        tiempo_total += TIEMPO_LATENCIA  # Sumar una vez por cada solicitud
        tiempo_total += TIEMPO_TRANSFERENCIA  # Sumar una vez por cada solicitud

    return tiempo_total

# Dibuja una gráfica con las solicitudes atendidas
def dibujar_grafica(algoritmo, lista_solicitudes_atendidas):
    # Extraer las posiciones de cabeza y desplazamientos desde la lista de solicitudes
    posiciones_cabeza = [par[1] for par in lista_solicitudes_atendidas]
    desplazamientos = [par[0] for par in lista_solicitudes_atendidas]

    # Crear gráfica con color personalizado
    plt.figure(facecolor='#5A5C6C')
    plt.axes().set_facecolor("#5A5C6C")

    # Dibujar los ejes horizontal y vertical
    plt.plot(desplazamientos, posiciones_cabeza, marker='o', color='red')

    # Configurar la gráfica
    plt.title(f'Gráfica de {algoritmo.upper()}', color='#FFFFCC', fontsize=30)
    plt.xlabel('Número de desplazamientos', color='white')
    plt.ylabel('Número de cilindros', color='white')
    plt.xticks(color='white')
    plt.yticks(color='white')
    plt.grid(axis='y', color='white')
    plt.ylim(bottom=0)

    # Agregar etiquetas a cada solicitud
    for solicitud in lista_solicitudes_atendidas:
        plt.annotate(
            text=str(solicitud[1]), 
            xy=(solicitud[0], solicitud[1]), 
            xytext=(-10, 5), 
            textcoords='offset points', 
            bbox=dict(boxstyle='round,pad=0.3', edgecolor='white', facecolor='#666699'),
            color='white',
            ha='right',
            va='bottom'
        )

    # Mostrar la gráfica
    plt.show()