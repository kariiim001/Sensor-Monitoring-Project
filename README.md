# Real-Time Sensor Monitoring System

## Overview
This project is a **real-time sensor monitoring desktop application** developed in Python.  
It simulates sensors, monitors in real time, and generates alarms when values exceed predefined safety limits.

---

## Features
- Real-time sensor data monitoring
- TCP-based sensor simulator
- Multithreaded data acquisition
- Alarm detection (HIGH / LOW)

---

## System Architecture
```
Sensor Simulator (TCP Server)
SensorWorker (QThread) >> Alarm Engine >> Qt GUI
```

### Architecture Layers
- **Simulation Layer**: Simulates sensors and sends data over TCP connection
- **Communication Layer**: Handles TCP communication in a separate thread
- **Presentation Layer**: Graphical user interface (Qt)

---

## Technologies Used
- Python 3.9+
- PySide6 (Qt for Python)
- TCP/IP Sockets
- Multithreading
- JSON-based protocol

---

## Project Structure
```
siware-project/
├── app/
│   ├── __init__.py
│   ├── main.py          # Application entry point
│   ├── gui.py           # GUI logic
│   ├── workers.py       # TCP client 
│   ├── alarm.py         # Alarm logic
│   └── config.py        # Configuration
├── simulator/
│   └── sensor_simulator.py  # Sensor simulator
├── requirements.txt
└── README.md
```

---

## Sensor Data Format
The simulator sends **line-based JSON messages** over TCP:
```json
{
  "sensor": "temp1",
  "value": 32.5,
  "timestamp": 1690000000.25
}
```

---

## Alarm Logic
Each sensor has predefined limits:
- If value < LOW → LOW Alarm
- If value > HIGH → HIGH Alarm
- Otherwise → OK

Alarm handling is isolated in a dedicated module `alarm.py` to ensure testability and scalability.

---

## Setup & Installation

### 1. Clone the project
```bash
git clone https://github.com/kariiim001/Sensor-Monitoring-Project.git
cd project
```

### 2. Create virtual environment
```bash
python3 -m venv venv
source venv/bin/activate
```

### 3. Install dependencies
```bash
pip install -r requirements.txt
```

---

## Running the Project

### Step 1: Run the Sensor Simulator
Open a terminal and run:
```bash
python simulator/sensor_simulator_tcp.py
```

Expected output:
```
Sensor Simulator running on 127.0.0.1:9000
Waiting for client...
```

---

### Step 2: Run the Application
Open another terminal (with virtual environment activated):
```bash
python -m app.main
```

---

## Expected Behavior
- GUI window opens
- Sensor table fills automatically
- Values update in real time
- Alarm rows turn red when limits are exceeded
- Alarm log displays triggered alarms