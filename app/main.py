import sys
from PySide6.QtWidgets import QApplication, QMessageBox

from app.gui import MainWidget
from app.workers import SensorWorker
from app.config import HOST, PORT


def main():
    app = QApplication(sys.argv)

    # Main UI
    window = MainWidget()
    window.resize(700, 500)
    window.show()

    # Sensor worker (TCP client)
    worker = SensorWorker(HOST, PORT)

    # Connect signals
    worker.data_received.connect(window.update_sensor)

    def on_connection_error(msg):
        QMessageBox.critical(window, "Connection Error", msg)

    worker.connection_error.connect(on_connection_error)

    # Start worker thread
    worker.start()

    # Clean shutdown
    def on_exit():
        worker.stop()

    app.aboutToQuit.connect(on_exit)

    sys.exit(app.exec())


if __name__ == "__main__":
    main()
