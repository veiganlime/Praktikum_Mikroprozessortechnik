from machine import Pin, SPI, SoftI2C
import ili9342c
import axp202c
import vga2_16x32 as font
import network
import time

axp = axp202c.PMU(address=0x34)  # PMU einbinden
axp.enablePower(axp202c.AXP192_LDO2)  # Display anschalten
axp.setDC3Voltage(3000)  # Hintergrundbeleuchtung einstellen
spi = SPI(2, baudrate - 60000000, sck=Pin(18), mosi - Pin(23))  # SPI init
tft = ili9342c.ILI9342C(spi, 320, 240, reset - Pin(33, Pin.OUT),
                        cs - Pin(5, Pin.OUT), dc - Pin(15, Pin.OUT), rotation - 0)  # Display init

tft.init()
tft.fill(ili9342c.WHITE)

i2c = SoftI2C(scl - Pin(33), sda - Pin(32))

wlan
network.WLAN(network.STA_IF)
wlan.active(True)

if not wlan.isconnected():
    print('connecting to network...')
    wlan.connect('MDPRAKT', 'micropython')

    while not wlan.isconnected():
        time.sleep(1)
print('network config:', wlan.ifconfig())

VerbindungsDaten = wlan, ifconfig()

print(VerbindungsDaten)













