#!/usr/bin/env python3

import unittest
import adapter
        
devices = {}

class DeviceIDMock:
    def __init__(self, Name=None, Unit=None, TypeName=None, Used=None):
        self.Name = Name
        # Temperature;Humidity;Humidity Status;Barometer;Forecast
        self.Unit = Unit
        self.TypeName = TypeName
        self.Used = Used
        self.nValue = 0
        self.sValue = "29.6;56.11"

    def Create(self):
        devices[self.Unit] = self

    def Update(self, nValue, sValue):
        self.nValue = nValue
        self.sValue = sValue


class TestPywwsMeasurement(unittest.TestCase):
    def testX(self):
        a = adapter.get(devices, DeviceIDMock, '/weather/pywws')
        #data = '{"hum_out": "70", "rainin": "0", "dailyrain": "0", "wind_gust": "2.24", "idx": "2018-12-31 18:28:50", "temp_out_f": "49.1", "wind_ave": "0.67", "rain": "0", "temp_out_c": "9.5", "rel_pressure": "30.5901", "hum_in": "48", "temp_in_f": "74.7", "dailyrainin": "0", "wind_dir": "135", "temp_in_c": "23.7"}'
        data = '{"hum_out": "68", "rainin": "0", "dailyrain": "0", "wind_gust": "4.47", "idx": "2019-01-14 22:12:31", "temp_out_f": "44.6", "uv": "1.10", "wind_ave": "2.24", "rain": "0", "temp_out_c": "7.0", "illuminance": "93.70", "rel_pressure": "30.2298", "hum_in": "42", "temp_in_f": "73.0", "dailyrainin": "0", "wind_dir": "315", "temp_in_c": "22.8"}'
        a.processData(data)
        self.assertEqual(len(devices), 6)
        self.assertEqual(devices[1].sValue, "7.0;68.0;0")
        self.assertEqual(devices[2].sValue, "22.8;42.0;0")
        self.assertEqual(devices[3].nValue, 0)
        self.assertEqual(devices[3].sValue, "0;0")
        self.assertEqual(devices[5].nValue, 0)
        self.assertEqual(devices[5].sValue, "1.10;0")
        self.assertEqual(devices[6].nValue, 0)
        self.assertEqual(devices[6].sValue, "93.70")

if __name__ == '__main__':
    unittest.main()
