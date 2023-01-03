from machine import Pin, SPI,SoftI2C
import ili9342c
import axp202c
import focaltouch


# initialisieren das Display und setzen Sie die Hintergrundfarbe auf WHITE
axp = axp202c.PMU(address=0x34) # PMU einbinden
axp.enablePower(axp202c.AXP192_LDO2) # Display anschalten
axp.setDC3Voltage(3000) # Hintergrundbeleuchtung einstellen
spi = SPI(2,baudrate=60000000,sck=Pin(18),mosi=Pin(23)) # SPI init
tft = ili9342c.ILI9342C(spi,320,240,reset=Pin(33, Pin.OUT),
     cs=Pin(5, Pin.OUT),dc=Pin(15, Pin.OUT),rotation=0) # Display init


tft.init() # Initialisiert und löscht das Display
tft.fill(ili9342c.WHITE) # füllt das Bild weiß
#tft.fill_rect(10,10,240,200,0x2f0)

#initialisieren die I2C-Schnittstelle
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
touch = focaltouch.FocalTouch(i2c)

while True:
    if(touch.touched >0):
        tft.rect(touch.touches[0]['x'],touch.touches[0]['y'],30,30,ili9342c.RED)
        
       

