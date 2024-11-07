#clase orientada a el bot , todo lo que sepa el bot es aqui
import random
import player  # Importamos el módulo 'player' que debe tener la clase 'Player'

class Cpu(player.Player):  # Usamos 'player.Player' si Player está en el módulo 'player'
    def __init__(self, difficulty):
        super().__init__("Makinon")
        self.difficulty = difficulty
        self.colmRm = 0
        self.rowRm = 0
        self.round = 1
    def cpuPlay(self, colm, row , boardIn):
        match self.difficulty:
            case 1:
                colmn = random.randint(0, colm - 1)
                rows = random.randint(0, row - 1)
                if boardIn[self.rowRm][self.colmRm] == boardIn[rows][colmn]:
                        return (self.colmRm , self.rowRm)
                else :
                    return(colmn , rows)

    def remind(self,colm, row):
        self.colmRm = colm
        self.rowRm = row
        
    #implementar un diccionario en vez de esto
    
    #al fallar una pareja se guarda en un diccionario, luego la maquina elige una posicion, 
    # busca en el diccionario si esta esa misma cara, 
    # si esta pues pone la posicion que esta guardad en el diccionario, si no, pues pone una aleatoria
