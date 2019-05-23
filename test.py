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
        data = '{"wind_ave_mps": "2.40", "wind_ave_mph": "5.37", "hum_in": "40", "pressure_rel_inhg": "29.9966", "temp_out_f": "48.2", "wind_chill_c": "7.70", "wind_dir_text": "N", "rain_last_hour_mm": "0.3", "temp_out_c": "9.0", "rain_day_mm": "0.6", "illuminance_wm2": "0.53", "pressure_abs_inhg": "29.9966", "pressure_rel_hpa": "1015.8000", "pressure_abs_hpa": "1015.8000", "rain_mm": "3.9", "wind_dir_degrees": "0", "temp_in_f": "73.0", "temp_in_c": "22.8", "hum_out": "65", "illuminance_lux": "105.00", "rain_last_24hours_mm": "0.6", "idx": "2019-04-27 21:58:16", "dew_point_c": "2.8", "wind_gust_mph": "9.84", "uv": "1.00", "wind_gust_mps": "4.40", "temp_out_realfeel_c": "5.8"}'
        a.processData(data)
        self.assertEqual(len(devices), 7)
        self.assertEqual(devices[1].sValue, "9.0;65.0;0")
        self.assertEqual(devices[2].sValue, "22.8;40.0;0")
        self.assertEqual(devices[3].nValue, 0)
        self.assertEqual(devices[3].sValue, "30.0;3.9")
        self.assertEqual(devices[4].nValue, 0)
        self.assertEqual(devices[4].sValue, "0;N;24.0;44.0;9.0;7.70")
        self.assertEqual(devices[5].nValue, 0)
        self.assertEqual(devices[5].sValue, "1.00;0")
        self.assertEqual(devices[6].nValue, 0)
        self.assertEqual(devices[6].sValue, "105.00")
        self.assertEqual(devices[7].nValue, 0)
        self.assertEqual(devices[7].sValue, "0.53")

if __name__ == '__main__':
    unittest.main()
