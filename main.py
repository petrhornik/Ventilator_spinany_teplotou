print("Projekt: Větrák spínaný z hlediska teploty")
import machine, onewire, ds18x20, time

rele = machine.Pin(16, machine.Pin.OUT)
ds_pin = machine.Pin(21)
ds_sensor = ds18x20.DS18X20(onewire.OneWire(ds_pin))

def rele_zap():
    rele.value(1)
    
def rele_vyp():
    rele.value(0)
    

roms = ds_sensor.scan()
print('Found DS devices: ', roms)

while True:
  ds_sensor.convert_temp()
  time.sleep_ms(750)
  for rom in roms:
    print(rom)
    tempC = ds_sensor.read_temp(rom)
    print('temperature (ºC):', "{:.2f}".format(tempC))
    print()
    if tempC > 30:
        rele_zap()
    else:
        rele_vyp()
  time.sleep(5)