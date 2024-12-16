print("Projekt: Větrák spínaný z hlediska teploty")
import machine, onewire, ds18x20, time         #import knihoven (machine = práce s piny mikrokontroleru, ds18x20 = komunikace s teplotními senzory DS18B20, onewire = sériová komunikace s více zařízeními[např.: teplotními čidly] pomocí jediné datové linky, time = časové prodlevy)

rele = machine.Pin(16, machine.Pin.OUT)        #inicializace relé - pin 16 je nastaven jako výstup pro ovládání relé
teplomer_pin = machine.Pin(21)                       #proměnná teplomer_pin je nastavena na pin 21
teplomer_sensor = ds18x20.DS18X20(onewire.OneWire(teplomer_pin))    #promena teplomer_pin(pin 21) je použita pro onewire komunikaci s teplotním senzorem

#funkce rele_zap() a rele_vyp() zde jsou jen pro přehlednost
def rele_zap():
    rele.value(1)    #nastaví hodnotu pinu 16 na 1
    
def rele_vyp():
    rele.value(0)    #nastaví hodnotu pinu 16 ba 0
    

roms = teplomer_sensor.scan()    #sken dostupných zařízení na onewire sběrnici
print('Found DS devices: ', roms)    #výpis najitých zařízení

#Hlavní smyčka kódu
while True:
  teplomer_sensor.convert_temp()        #převod hodnoty na teplotu
  time.sleep_ms(750)
  for rom in roms:
    print(rom)
    temp = teplomer_sensor.read_temp(rom)
    print('temperature (ºC):', "{:.2f}".format(temp))
    print()
    if temp > 30:    #pokud je naměřená teplota vyšší než 30 stupňů tak sepni relé
        rele_zap()
    else:            #pokud je naměřená teplota nižší než 30 stupňů tak rozepni relé
        rele_vyp()
  time.sleep(5)
