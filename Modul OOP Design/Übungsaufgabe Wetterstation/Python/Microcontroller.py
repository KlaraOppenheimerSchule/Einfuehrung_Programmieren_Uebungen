import BNE_Sensor
import Display

class Microcontroller:
    def __init__(self):
        self.__myBNE_sensor=BNE_Sensor.BNE_Sensor(1)
            
    def getTempData(self):
        #Zufallswert erzeugen
        print(self.__myBNE_sensor.getTempData())

    def addDisplay(self, display):
        self.__myDisplay=display

microcontroller1=Microcontroller()
display1=Display.Display()
microcontroller1.addDisplay(display1)
microcontroller1.getTempData()