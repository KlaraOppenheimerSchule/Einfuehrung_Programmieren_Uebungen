import random

class BNE_Sensor:
    def __init__(self, id):
        self.__id=id
    
    def getTempData(self):
        #Zufallswert erzeugen
        return (random.randrange(-40,60))


#sensor1=BNE_Sensor(1)
#print(sensor1.getTempData())