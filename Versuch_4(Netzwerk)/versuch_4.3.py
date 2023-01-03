import network
import time
import urequests

axp = axp202c.PMU(address=0x34) # PHU einbinden
axp.enablePower (axp202c.AXP192_L002) # Display anschalten
axp.setDC3Voltage(3000) #Hintergrundbeleuchtung einstellen
spi = SPI(2, baudrate-60000000,sck-Pin(18), mosi-Pin(23)) # SPI init
tft = ili9342c.ILI9342C(spi,320,240, reset-Pin(33, Pin.OUT),
cs = Pin(5, Pin.OUT), dc-Pin(15, Pin.OUT), rotation=  0) # Display init

tft.init()
tft.fill(il19342c.WHITE)

i2c = Soft120(scl-Pin(33), sda-Pin(32))
wlan = network.WLAN(network.STA IF)
wlan.active(True)

if not wlan.isconnected():
    print('connecting to network...")
    wlan.connect('MCPRAKT', 'micropython")
    while not wlan.isconnected():
        time.sleep(1)
print('network config:', wlan.ifconfig())


r = urequests.get("http://ip-api.com/json/")
rj = r.json()

for i in rj:
    print(i, "/", ri[i])

print("")
print("--------")
print("Variable r ist von Type:", type(r))
print("Variable rj ist von Type:", type(rj))
print("--------")
