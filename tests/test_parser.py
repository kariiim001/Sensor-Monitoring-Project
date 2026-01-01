import json

def test_sensor_parsing():
    raw = '{"sensor":"temp1","value":25,"timestamp":1}'
    data = json.loads(raw)
    assert data["sensor"] == "temp1"
