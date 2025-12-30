from PySide6.QtWidgets import (
    QWidget, QVBoxLayout, QTableWidget, QTableWidgetItem,
    QLabel, QListWidget
)
from PySide6.QtGui import QColor
from PySide6.QtCore import Slot

from app.alarm import AlarmEngine
from app.config import SENSOR_LIMITS


class MainWidget(QWidget):
    def __init__(self):
        super().__init__()

        self.setWindowTitle("Monitor")

        # Alarm
        self.alarm_engine = AlarmEngine(SENSOR_LIMITS)

        # UI elements
        self.status_label = QLabel("System Status: OK")

        self.table = QTableWidget(0, 4)
        self.table.setHorizontalHeaderLabels(
            ["Sensor", "Value", "Status", "Timestamp"]
        )

        self.alarm_list = QListWidget()

        layout = QVBoxLayout()
        layout.addWidget(self.status_label)
        layout.addWidget(self.table)
        layout.addWidget(QLabel("Alarm Log"))
        layout.addWidget(self.alarm_list)

        self.setLayout(layout)

        # Store last values
        self.sensor_rows = {}

    @Slot(dict)
    def update_sensor(self, data: dict):
        """
        Slot to recieve sensor data from SensorWorker
        """
        sensor = data["sensor"]
        value = float(data["value"])
        ts = data["timestamp"]

        # Add new row if sensor not exists
        if sensor not in self.sensor_rows:
            row = self.table.rowCount()
            self.table.insertRow(row)
            self.sensor_rows[sensor] = row

            self.table.setItem(row, 0, QTableWidgetItem(sensor))
            self.table.setItem(row, 1, QTableWidgetItem(""))
            self.table.setItem(row, 2, QTableWidgetItem(""))
            self.table.setItem(row, 3, QTableWidgetItem(""))

        row = self.sensor_rows[sensor]

        # Update value
        self.table.item(row, 1).setText(f"{value:.2f}")
        self.table.item(row, 3).setText(f"{ts:.2f}")

        # Check alarm
        alarm = self.alarm_engine.check_value(sensor, value, ts)

        status_item = self.table.item(row, 2)

        if alarm:
            status_item.setText(alarm.alarm_type)
            status_item.setBackground(QColor("red"))

            self.alarm_list.addItem(
                f"{alarm.sensor} {alarm.alarm_type} @ {alarm.timestamp:.2f}"
            )

            self.status_label.setText("System Status: ALARM")
            self.status_label.setStyleSheet("color: red;")

        else:
            status_item.setText("OK")
            status_item.setBackground(QColor("lightgreen"))

            self.status_label.setText("System Status: OK")
            self.status_label.setStyleSheet("color: green;")
