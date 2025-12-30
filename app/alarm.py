
from dataclasses import dataclass
from typing import Dict, List, Optional


@dataclass
class AlarmEntry:
    timestamp: float
    sensor: str
    value: float
    alarm_type: str   # "LOW" or "HIGH"


class AlarmEngine:
    def __init__(self, limits: Dict[str, Dict[str, float]]):
        self.limits = limits
        self.alarm_log: List[AlarmEntry] = []

    def check_value(
        self,
        sensor_name: str,
        value: float,
        timestamp: float
    ) -> Optional[AlarmEntry]:

        if sensor_name not in self.limits:
            return None

        low = self.limits[sensor_name]["low"]
        high = self.limits[sensor_name]["high"]

        if value < low:
            alarm = AlarmEntry(timestamp, sensor_name, value, "LOW")
            self.alarm_log.append(alarm)
            return alarm

        if value > high:
            alarm = AlarmEntry(timestamp, sensor_name, value, "HIGH")
            self.alarm_log.append(alarm)
            return alarm

        return None
