
import socket
import json
from PySide6.QtCore import QThread, Signal


class SensorWorker(QThread):
    data_received = Signal(dict)       
    connection_error = Signal(str)    

    def __init__(self, host: str, port: int):
        super().__init__()
        self.host = host
        self.port = port
        self._running = True

    def run(self):
        try:
            with socket.create_connection((self.host, self.port), timeout=5) as sock:
                buffer = ""
                while self._running:
                    data = sock.recv(4096).decode("utf-8")
                    if not data:
                        break

                    buffer += data

                    while "\n" in buffer:
                        line, buffer = buffer.split("\n", 1)
                        try:
                            parsed = json.loads(line)
                            self.data_received.emit(parsed)
                        except json.JSONDecodeError:
                            print(" JSON parse error:", line)

        except Exception as e:
            self.connection_error.emit(str(e))

    def stop(self):
        self._running = False
        self.quit()
        self.wait()
