import json
import unittest
from datetime import datetime


def convertFromFormat1(data):
    ts = to_millis(data["timestamp"])

    return {
        "deviceId": data["deviceId"],
        "timestamp": ts,
        "temperature": data["measurements"]["temperature"],
        "humidity": data["measurements"]["humidity"],
        "pressure": data["measurements"]["pressure"],
        "status": data["status"]
    }


def convertFromFormat2(data):
    ts = to_millis(data["time"])

    values = {item["type"]: item["value"] for item in data["data"]}

    return {
        "deviceId": data["device"]["id"],
        "timestamp": ts,
        "temperature": values.get("temperature"),
        "humidity": values.get("humidity"),
        "pressure": values.get("pressure"),
        "status": data["device"]["state"]
    }


# 🔥 Smart universal converter (bonus)
def convert(data):
    if "deviceId" in data:
        return convertFromFormat1(data)
    return convertFromFormat2(data)


def to_millis(iso_time):
    dt = datetime.fromisoformat(iso_time.replace("Z", "+00:00"))
    return int(dt.timestamp() * 1000)


# ✅ Tests
class TestTelemetryConversion(unittest.TestCase):

    def setUp(self):
        with open("data-1.json") as f:
            self.d1 = json.load(f)

        with open("data-2.json") as f:
            self.d2 = json.load(f)

        with open("data-result.json") as f:
            self.expected = json.load(f)

    def test_format1(self):
        self.assertEqual(convertFromFormat1(self.d1), self.expected)

    def test_format2(self):
        self.assertEqual(convertFromFormat2(self.d2), self.expected)

    def test_auto(self):
        self.assertEqual(convert(self.d1), self.expected)
        self.assertEqual(convert(self.d2), self.expected)


if __name__ == "__main__":
    unittest.main()