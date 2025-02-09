# Simulador de Planificación
_Simulador de Planificación_ is a **Hard Disk Drive Scheduling Algorith Simulator** developed as part of the course "[Sistemas Operativos](https://secretaria.uvigo.gal/docnet-nuevo/guia_docent/?centre=305&ensenyament=V05G301V01&assignatura=V05G301V01303&any_academic=2023_24)" in the Telecommunications Engineering Degree at the Universidad de Vigo (2023 - 2024).

## About The Project
This project simulates various disk scheduling algorithms to demonstrate how operating systems handle I/O requests in a hard disk drive. It incorporates theoretical concepts of operating systems and algorithms, showcasing:
- Simulation of real-world hard disk scheduling algorithms.
- Modular and extensible design.
- Customizable parameters for cylinder requests, head position, and timing.

## How To Run

### Requirements
Make sure you have [Python](https://www.python.org/downloads/) installed on your system. Then install the required dependencies with:

```bash
pip install -r requirements.txt
```

### Usage
Once the dependencies are installed, you can execute the simulator by running:

```bash
python src/simulator.py [--cilindros CYLINDERS] [--cola QUEUE] [--algoritmos ALGORITHMS] [--posicion_inicial POSITION] [--tiempo_arranque TIME] [--tiempo_desplazamiento TIME] [--tiempo_detencion TIME] [--tiempo_latencia TIME] [--tiempo_transferencia TIME] [--help]
```

| Option                         | Short | Description                                         | Example |
|--------------------------------|-------|-----------------------------------------------------|---------|
| `--cilindros CYLINDERS`        | `-c`  | Number of cylinders in the disk                    | `-c 200` |
| `--cola QUEUE`       | `-q`  | Queue of requests to the cylinders                 | `-q 10 30 150 190` |
| `--algoritmos ALGORITHMS`| `-a`  | Algorithm(s) to simulate                           | `-a FCFS SSTF` |
| `--posicion_inicial POSITION`  | `-p`  | Initial position of the head                       | `-p 50` |
| `--tiempo_arranque TIME`            | `-ta` | Startup time in milliseconds                       | `-ta 3` |
| `--tiempo_desplazamiento TIME`      | `-tds`| Time to move between cylinders in milliseconds     | `-tds 0.2` |
| `--tiempo_detencion TIME`           | `-td` | Stop time in milliseconds                          | `-td 1` |
| `--tiempo_latencia TIME`            | `-tl` | Latency time in milliseconds                       | `-tl 4` |
| `--tiempo_transferencia TIME`       | `-tt` | Transfer time in milliseconds                      | `-tt 0.5` |
| `--help`                       | `-h`  | Show the help message                    | `-h` |

#### Algorithms
- **FCFS (First Come, First Served)**  
   The simplest algorithm where requests are handled in the order they arrive. It does not optimize the movement of the disk head and can lead to high seek times.

- **SSTF (Shortest Seek Time First)**  
   This algorithm selects the request that requires the least movement of the disk head from its current position, reducing seek time. However, it may cause starvation for requests far from the current head position.

- **SCAN**  
   The disk head moves in one direction, fulfilling all requests until it reaches the end of the disk. It then reverses direction and processes requests in the opposite direction.

- **C-SCAN (Circular SCAN)**  
   Similar to SCAN, but instead of reversing direction, the disk head jumps back to the start of the disk after reaching the end, processing requests only in one direction.

- **LOOK**  
   A variation of SCAN where the disk head only travels as far as the last request in each direction, avoiding unnecessary movement to the physical end of the disk.

- **C-LOOK (Circular LOOK)**  
   Similar to LOOK, but the head jumps back to the start of the request queue instead of reversing direction.

#### Example
```bash
python simulator.py -c 200 -p 50 -q 10 30 150 190 -a FCFS SSTF
```

## About The Code
There is no dedicated documentation for this project. Refer to [`Presentación.pdf`](docs/Presentación.pdf) for a high-level overview and results, or inspect the code for a deeper understanding of the system and how it works.
