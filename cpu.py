#clase orientada a el bot , todo lo que sepa el bot es aqui
import random
import player  # Importamos el módulo 'player' que debe tener la clase 'Player'

class Cpu(player.Player):  # Usamos 'player.Player' si Player está en el módulo 'player'
    def __init__(self, difficulty):
        super().__init__("Makinon")
        self.difficulty = difficulty
        self.memory = {}
        self.last_position = None  # Última posición seleccionada por la CPU
    def cpuPlay(self, columns, rows, boardOut):
        # Si tiene una carta previa que puede emparejar
        if self.last_position:
            last_row, last_col = self.last_position
            last_card = boardOut[last_row - 1][last_col - 1]

            # Busca una pareja conocida en memoria
            for pos, card in self.memory.items():
                if card == last_card and pos != self.last_position:
                    return pos  # Devuelve la posición de la carta que coincide

        # Si no tiene pareja, elige una carta al azar
        row, col = random.randint(1, rows), random.randint(1, columns)
        while boardOut[row - 1][col - 1] != "*":  # Evitar cartas ya recordadas
            row, col = random.randint(1, rows), random.randint(1, columns)
        
        # Guardar la última posición seleccionada
        self.last_position = (row, col)
        return (row, col)

    def remind(self,pos , card):
        self.memory[pos] = card
        
    #implementar un diccionario en vez de esto
    
    #al fallar una pareja se guarda en un diccionario, luego la maquina elige una posicion, 
    # busca en el diccionario si esta esa misma cara, 
    # si esta pues pone la posicion que esta guardad en el diccionario, si no, pues pone una aleatoria
