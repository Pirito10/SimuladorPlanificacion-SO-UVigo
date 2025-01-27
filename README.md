# About The Project

Hard Disk Scheduling Algorith Simulator project for "[Sistemas Operativos](https://secretaria.uvigo.gal/docnet-nuevo/guia_docent/?centre=305&ensenyament=V05G301V01&assignatura=V05G301V01303)" subject in Telecommunications Engineering Degree at Universidad de Vigo (2023 - 2024)

# How To Run

### Requirements
Make sure you have Python installed on your system. Then install the required dependencies with:

```bash
pip install -r requirements.txt
```

### Usage
To execute the simulator, run the following commands:

```bash
cd src
python simulator.py [OPTIONS]
```

| Option                         | Short | Description                                         |
|--------------------------------|-------|-----------------------------------------------------|
| `--cilindros CILINDROS`        | `-c`  | Number of cylinders in the disk                    |
| `--cola COLA [COLA ...]`       | `-q`  | Queue of requests to the cylinders                 |
| `--algoritmos ALGORITMOS [...]`| `-a`  | Algorithm(s) to simulate                           |
| `--posicion_inicial POSICION`  | `-p`  | Initial position of the head                       |
| `--tiempo_arranque`            | `-ta` | Startup time in milliseconds                       |
| `--tiempo_desplazamiento`      | `-tds`| Time to move between cylinders in milliseconds     |
| `--tiempo_detencion`           | `-td` | Stop time in milliseconds                          |
| `--tiempo_latencia`            | `-tl` | Latency time in milliseconds                       |
| `--tiempo_transferencia`       | `-tt` | Transfer time in milliseconds                      |
| `--help`                       | `-h`  | Show the help message                    |

### Algorithms
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

### Example
Simulate a disk with 200 cylinders, an initial head position at cylinder 50, and a queue of requests [10, 30, 150, 190], using the FCFS and SSTF algorithms:

```bash
python simulator.py -c 200 -p 50 -q 10 30 150 190 -a FCFS SSTF
```