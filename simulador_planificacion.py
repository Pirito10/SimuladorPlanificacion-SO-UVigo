import argparse, random
from utilidades import generar_cola, verificar_solicitudes_en_rango, verificar_posicion_en_rango, simular_tiempo_total, dibujar_grafica
from algoritmos.fcfs import fcfs
from algoritmos.sstf import sstf
from algoritmos.scan import scan
from algoritmos.c_scan import c_scan
from algoritmos.look import look
from algoritmos.c_look import c_look

def main():
    # Manejo de parámetros de entrada
    parser = argparse.ArgumentParser(description="Simulador de Algoritmos de Planificación de Discos")
    parser.add_argument("--cilindros", "-c", type=int, help="Número de cilindros del disco")
    parser.add_argument("--cola", "-q", nargs="+", type=int, help="Cola de solicitudes a los cilindros")
    parser.add_argument("--algoritmos", "-a", nargs="+", help="Algoritmo(s) a simular")
    parser.add_argument("--posicion_inicial", "-p", type=int, help="Posición inicial de la cabeza")
    parser.add_argument("--tiempo_arranque", "-ta", type=float, default=3, help="Tiempo de arranque en milisegundos")
    parser.add_argument("--tiempo_desplazamiento", "-tds", type=float, default=0.2, help="Tiempo de desplazamiento entre cilindros en milisegundos")
    parser.add_argument("--tiempo_detencion", "-td", type=float, default=1, help="Tiempo de detención en milisegundos")
    parser.add_argument("--tiempo_latencia", "-tl", type=float, default=4, help="Tiempo de latencia en milisegundos")
    parser.add_argument("--tiempo_transferencia", "-tt", type=float, default=0.5, help="Tiempo de transferencia en milisegundos")
    args = parser.parse_args()

    # Comprobar si se indicaron número de cilindros y la cola
    if args.cilindros is not None and args.cola is not None:
        verificar_solicitudes_en_rango(args.cilindros, args.cola)
        cilindros = args.cilindros
        cola = args.cola
    else:
        # Si solo se proporciona uno de los valores
        if args.cola is not None:
            cola = args.cola
            # Generar cilindros de forma que sea válido para la cola indicada
            cilindros = max(cola) + random.randint(1, 100)
        elif args.cilindros is not None:
            cilindros = args.cilindros
            # Generar una cola válida para el número de cilindros indicado
            cola = generar_cola(random.randint(10, 50), cilindros)
        else:
            # Si no se proporciona ninguno, generar ambos de forma que tenga sentido
            cilindros = random.randint(50, 500)
            cola = generar_cola(random.randint(10, 50), cilindros)

    # Verificar si se indicó la posición inicial de la cabeza
    if args.posicion_inicial is not None:
        posicion_inicial = args.posicion_inicial
        verificar_posicion_en_rango(posicion_inicial, cilindros)
    else:
        # Si no se indicó, posicionarla en el medio
        posicion_inicial = cilindros // 2
        
    # Determinar algoritmos a simular
    algoritmos = args.algoritmos or ["fcfs", "sstf", "scan", "c-scan", "look", "c-look"]  # Usar todos los algoritmos si no se proporciona ninguno

    # Mostrar los datos usados
    print(f"\nNúmero de cilindros: {cilindros}")
    print(f"Cola de solicitudes: {', '.join(map(str, cola))}")
    print(f"Posición inicial: {posicion_inicial}\n")

    print(f"Tiempo de arranque: {args.tiempo_arranque}ms")
    print(f"Tiempo de desplazamiento: {args.tiempo_desplazamiento}ms")
    print(f"Tiempo de detención: {args.tiempo_detencion}ms")
    print(f"Tiempo de latencia: {args.tiempo_latencia}ms")
    print(f"Tiempo de transferencia: {args.tiempo_transferencia}ms\n")

    # Simular con los algoritmos indicados
    for algoritmo in algoritmos:
        if algoritmo.lower() == "fcfs":
            desplazamientos, lista_solicitudes_atendidas = fcfs(cola, posicion_inicial)
            tiempo = simular_tiempo_total(len(cola), desplazamientos, args.tiempo_arranque, args.tiempo_desplazamiento, args.tiempo_detencion, args.tiempo_latencia, args.tiempo_transferencia)
            print(f"- FCFS: {desplazamientos} desplazamientos // {round(tiempo, 2)}ms")
            dibujar_grafica(algoritmo, lista_solicitudes_atendidas)

        elif algoritmo.lower() == "sstf":
            desplazamientos, lista_solicitudes_atendidas = sstf(cola, posicion_inicial)
            tiempo = simular_tiempo_total(len(cola), desplazamientos, args.tiempo_arranque, args.tiempo_desplazamiento, args.tiempo_detencion, args.tiempo_latencia, args.tiempo_transferencia)
            print(f"- SSTF: {desplazamientos} desplazamientos // {round(tiempo, 2)}ms")
            dibujar_grafica(algoritmo, lista_solicitudes_atendidas)

        elif algoritmo.lower() == "scan":
            desplazamientos, lista_solicitudes_atendidas = scan(cola, posicion_inicial)
            tiempo = simular_tiempo_total(len(cola), desplazamientos, args.tiempo_arranque, args.tiempo_desplazamiento, args.tiempo_detencion, args.tiempo_latencia, args.tiempo_transferencia)
            print(f"- SCAN: {desplazamientos} desplazamientos // {round(tiempo, 2)}ms")
            dibujar_grafica(algoritmo, lista_solicitudes_atendidas)

        elif algoritmo.lower() == "c-scan":
            desplazamientos, lista_solicitudes_atendidas = c_scan(cilindros, cola, posicion_inicial)
            tiempo = simular_tiempo_total(len(cola), desplazamientos, args.tiempo_arranque, args.tiempo_desplazamiento, args.tiempo_detencion, args.tiempo_latencia, args.tiempo_transferencia)
            print(f"- C-SCAN: {desplazamientos} desplazamientos // {round(tiempo, 2)}ms")
            dibujar_grafica(algoritmo, lista_solicitudes_atendidas)

        elif algoritmo.lower() == "look":
            desplazamientos, lista_solicitudes_atendidas = look(cola, posicion_inicial)
            tiempo = simular_tiempo_total(len(cola), desplazamientos, args.tiempo_arranque, args.tiempo_desplazamiento, args.tiempo_detencion, args.tiempo_latencia, args.tiempo_transferencia)
            print(f"- LOOK: {desplazamientos} desplazamientos // {round(tiempo, 2)}ms")
            dibujar_grafica(algoritmo, lista_solicitudes_atendidas)
            
        elif algoritmo.lower() == "c-look":
            desplazamientos, lista_solicitudes_atendidas = c_look(cola, posicion_inicial)
            tiempo = simular_tiempo_total(len(cola), desplazamientos, args.tiempo_arranque, args.tiempo_desplazamiento, args.tiempo_detencion, args.tiempo_latencia, args.tiempo_transferencia)
            print(f"- C-LOOK: {desplazamientos} desplazamientos // {round(tiempo, 2)}ms\n")
            dibujar_grafica(algoritmo, lista_solicitudes_atendidas)

if __name__ == "__main__":
    main()