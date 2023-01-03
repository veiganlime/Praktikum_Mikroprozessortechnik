from machine import Pin, SPI,SoftI2C
import ili9342c
import axp202c
import focaltouch
#import tictactoe_2 #der Import wird als Modul-name Error gemeldet oder direkt auf dem Microkrontroller speichern

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
#eine Liste um Button_objekt zu speichern
mylist=[]
# 3*3 Matrix erzeugen 
for x in range(5,310,100):
    for j in range(5,220,75):
        mylist.append(Button(x,j,90,70,ili9342c.CYAN,tft))

# eine Variable, die durch die Liste(mylist) laüft um auszugeben
for btn in mylist:
    btn.draw()
        
