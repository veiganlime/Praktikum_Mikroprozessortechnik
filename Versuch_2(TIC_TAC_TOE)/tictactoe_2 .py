from machine import Pin, SPI,SoftI2C
import ili9342c
import axp202c
import focaltouch
#import tictactoe_2 #import* #der Import wird als Modul-name Error gemeldet

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
i2c = SoftI2C(scl=Pin(22), sda=Pin(21))
touch = focaltouch.FocalTouch(i2c)

class Button:
    def __init__(self,x,y,breite,höhe,farbe,tft):
        self.x=x
        self.y=y
        self.breite=breite
        self.höhe=höhe
        self.farbe=farbe
        self.tft=tft
        
    def setFarbe(self,farbe):
        self.farbe = farbe
    def getFarbe(self):
        return self.farbe
    def draw(self):
        tft.fill_rect(self.x,self.y,self.breite,self.höhe,self.farbe)
    def test(self,px,py):
        if(px >= self.x and px <= self.breite and py >=self.y and py <= self.höhe):
            return True
        else:
            return False
        
        
#für den ersten Button
button_obj = Button(10,10,100,100,ili9342c.YELLOW,tft)
button_obj.draw()
#für das zweite Button
button2_obj = Button(130,10,100,100,ili9342c.MAGENTA,tft)
button2_obj.draw()

while True:
    if(touch.touched > 0):
        if(button_obj.test(touch.touches[0]['x'],touch.touches[0]['y'])):
            button_obj.setFarbe(ili9342c.RED)
            button_obj.draw()
        else:
            button_obj.setFarbe(ili9342c.BLUE)
            button_obj.draw()
        #Für das zweite Button kann eine andere Farbe gewählt werden   
        if(button2_obj.test(touch.touches[0]['x'],touch.touches[0]['y'])):
            button2_obj.setFarbe(ili9342c.BLUE)
            button2_obj.draw()
        else:
            button2_obj.setFarbe(ili9342c.RED)
            button2_obj.draw()



        
    
