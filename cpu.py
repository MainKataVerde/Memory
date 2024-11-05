#clase orientada a el bot , todo lo que sepa el bot es aqui
import player
import random
class Cpu(player):
    def __init__(self,dificulty):
        super().__init__("Maquina")
        self.dificulty = dificulty
    
    def cpuPlay(self , colm , row):
        match self.dificulty:
            case 1 :
                colmn = random.randint(0,colm-1) 
                row = random.randint(0,row-1)
                return (colmn,row)
                