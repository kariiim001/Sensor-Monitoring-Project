
# ===============================
# Network configuration
# ===============================
HOST = "127.0.0.1" #local host
PORT = 9000 


# ===============================
# Sensor limits (for alarms)
# ===============================
SENSOR_LIMITS = {
    "temp1": {
        "low": 15.0,
        "high": 30.0
    },
    "vib1": {
        "low": 0.0,
        "high": 5.0
    },
    "speed1": {
        "low": 1000.0,
        "high": 3000.0
    },
    "press1": {
        "low": 1.0,
        "high": 5.0
    },
    "opt1": {
        "low": 0.0,
        "high": 100.0
    }
}


# ===============================
# UI update settings
# ===============================
UI_REFRESH_RATE_HZ = 2   
MAX_GRAPH_POINTS = 100 