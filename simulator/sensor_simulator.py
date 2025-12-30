import socket
import json
import time
import random

HOST = "127.0.0.1"
PORT = 9000

SENSORS = [
    {"name": "temp1", "min": 15, "max": 30},
    {"name": "vib1", "min": 0, "max": 5},
    {"name": "speed1", "min": 1000, "max": 3000},
    {"name": "press1", "min": 1, "max": 5},
    {"name": "opt1", "min": 0, "max": 100},
]

def generate_value(sensor):
    """
    generated values is 90% right 

    """
    if random.random() < 0.1:
        return sensor["max"] * random.uniform(0.2, 1.5)
    return random.uniform(sensor["min"], sensor["max"])


def main():
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as server:
        server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        server.bind((HOST, PORT))
        server.listen(1)

        print(f" Sensor Simulator running on {HOST}:{PORT}")
        print(" Waiting for client...")

        conn, addr = server.accept()
        with conn:
            print(f" Client connected from {addr}")

            while True:
                for sensor in SENSORS:
                    data = {
                        "sensor": sensor["name"],
                        "value": round(generate_value(sensor), 2),
                        "timestamp": time.time()
                    }

                    message = json.dumps(data) + "\n"
                    conn.sendall(message.encode("utf-8"))

                    time.sleep(0.2) 


if __name__ == "__main__":
    main()
