# Python Plugin pywws MQTT
#
# Author: michlv
#
"""
Adapter objects for dealing with MQTT and Domoticz Device objects.
"""
import json

def get(devices, createDevice, topic):
    return Adapter(devices, createDevice)

class Adapter:
    def __init__(self, devices, createDevice):
        self.devices = devices
        self.createDevice = createDevice
        self.checkDevices()

    devs = [
        ['Temp+Hum Outside', 'Temp+Hum'],
        ['Temp+Hum Inside', 'Temp+Hum'],
        ['Rain', 'Rain'],
        ['Wind', 'Wind'],
        ['UV', 'UV'],
        ['Illumination', 'Illumination'],
        ['Solar Radiation Est', 'Solar Radiation'],
        ['Solar Radiation Disp', 'Solar Radiation']
    ]
        
    def checkDevices(self):
        for i in range(1, len(self.devs)+1):
            if i not in self.devices:
                x = self.devs[i-1]
                self.createDevice(Unit=i, Name=x[0], TypeName=x[1], Used=1).Create()

    def updateTempHum(self, unit, temp, hum):
        v = [str(float(temp)), str(float(hum)), '0']
        self.devices[unit].Update(0, ";".join(v))

    def getJsonData(self, jdata, name):
        try:
            return jdata[name]
        except KeyError:
            return None

    def toFloat(self, data):
        if data is None:
            return None
        return float(data)

    def toInt(self, data):
        if data is None:
            return None
        return int(data)

    def toStr(self, data):
        if data is None:
            return None
        return str(data)

    def update(self, unit, nValue, sValue):
        if nValue is None or sValue is None:
            return
        self.devices[unit].Update(nValue, sValue)
        
    def adjWind(self, data):
        return str(float(data)*10.0)

    def adjRainRate(self, data):
        return str(float(data)*100.0)
        
    def processData(self, data):
        jdata = json.loads(data)
        self.updateTempHum(1, jdata['temp_out_c'], jdata['hum_out'])
        self.updateTempHum(2, jdata['temp_in_c'], jdata['hum_in'])
        self.devices[3].Update(0, ";".join([self.adjRainRate(jdata['rain_last_hour_mm']), jdata['rain_mm']]))
        self.devices[4].Update(0, ";".join([jdata['wind_dir_degrees'],
                                            jdata['wind_dir_text'],
                                            self.adjWind(jdata['wind_ave_mps']),
                                            self.adjWind(jdata['wind_gust_mps']),
                                            jdata['temp_out_c'],
                                            jdata['wind_chill_c']]))
        self.devices[5].Update(0, ";".join([jdata['uv'], '0']))
        self.devices[6].Update(0, jdata['illuminance_lux'])
        self.devices[7].Update(0, jdata['illuminance_wm2'])
        self.devices[8].Update(0, str(float(jdata['illuminance_lux'])/683.0))
