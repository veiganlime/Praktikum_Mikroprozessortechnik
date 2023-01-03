from machine import Pin, SPI,SoftI2C
import ili9342c
import axp202c
import focaltouch
from sht30 import SHT30  # Klasse SHT30 aus Datei-sht30 importieren
from bmp280 import BMP280
import vga2_16x32 as font

# initialisieren das Display und setzen Sie die Hintergrundfarbe auf WHITE
axp = axp202c.PMU(address=0x34) # PMU einbinden
axp.enablePower(axp202c.AXP192_LDO2) # Display anschalten
axp.setDC3Voltage(3000) # Hintergrundbeleuchtung einstellen
spi = SPI(2,baudrate=60000000,sck=Pin(18),mosi=Pin(23)) # SPI init
tft = ili9342c.ILI9342C(spi,320,240,reset=Pin(33, Pin.OUT),
     cs=Pin(5, Pin.OUT),dc=Pin(15, Pin.OUT),rotation=0) # Display init
tft.init() # Initialisiert und löscht das Display
tft.fill(ili9342c.WHITE) # füllt das Bild weiß

#initialisieren die I2C-Schnittstelle
i2c = SoftI2C(scl=Pin(33), sda=Pin(32))
axp.enablePower(axp202c.AXP192_EXTEN)#VBus Betriebsspannung aktivieren

print( axp.getVbusVoltage())
print(axp.getVbusCurrent())
print(i2c.scan())
#print(hex(id(68)))

# Erzeugung eines SHT30-Objekt
mysht = SHT30(i2c,0,0)
print(mysht.is_present())
temp,luft=mysht.measure()
print(temp,'  ',luft)

#Luftdruck und Temperatur hier als Property des BMP280-Objekts
mybmp = BMP280(i2c)
t = mybmp.temperature
l = mybmp.pressure
print(t,"  ",l)

#Werte auf dem Display anzeigen
var1="SHT30:temp="+str(temp)
var2="SHT30:Luft"+str(luft)
var3=str(t)
var4=str(l)
tft.text(font,var1,50,20,ili9342c.GREEN,ili9342c.BLACK) 
tft.text(font,var2,50,60,ili9342c.RED,ili9342c.BLACK) 
tft.text(font,var3,150,100,ili9342c.BLUE,ili9342c.BLACK) 
tft.text(font,var4,150,140,ili9342c.YELLOW,ili9342c.BLACK) 
        




