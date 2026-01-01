from app.alarm import AlarmEngine

def test_high_alarm():
    limits = {"temp1": {"low": 10, "high": 20}}
    engine = AlarmEngine(limits)
    alarm = engine.check_value("temp1", 30, 123)
    assert alarm is not None
    assert alarm.alarm_type == "HIGH"
