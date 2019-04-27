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
        data = '{"wind_ave_mps": "3.10", "rainin": "0", "wind_ave_mph": "6.93", "hum_in": "39", "dailyrainin": "0.023622", "pressure_rel_inhg": "29.9523", "dailyrain": "0.6", "temp_out_f": "52.0", "temp_out_c": "11.1", "illuminance": "97.50", "rain_day_mm": "0.6", "illuminance_wm2": "0.49", "rain_last_hour_mm": "0.0", "pressure_abs_hpa": "1014.3000", "rain": "0", "rain_mm": "3.9", "rel_pressure": "1014.3000", "pressure_abs_inhg": "29.9523", "temp_in_f": "74.3", "temp_in_c": "23.5", "hum_out": "50", "illuminance_lux": "97.50", "rain_last_24hours_mm": "0.6", "idx": "2019-04-27 19:28:16", "wind_gust_mph": "10.74", "uv": "1.00", "pressure_rel_hpa": "1014.3000", "wind_gust_mps": "4.80", "wind_dir_degrees": "0"}'
        a.processData(data)
        self.assertEqual(len(devices), 6)
        self.assertEqual(devices[1].sValue, "11.1;50.0;0")
        self.assertEqual(devices[2].sValue, "23.5;39.0;0")
        self.assertEqual(devices[3].nValue, 0)
        self.assertEqual(devices[3].sValue, "0;3.9")
        self.assertEqual(devices[4].nValue, 0)
        self.assertEqual(devices[4].sValue, "0;0;3.10;0;11.1;0")
        self.assertEqual(devices[5].nValue, 0)
        self.assertEqual(devices[5].sValue, "1.00;0")
        self.assertEqual(devices[6].nValue, 0)
        self.assertEqual(devices[6].sValue, "97.50")

if __name__ == '__main__':
    unittest.main()
