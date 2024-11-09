#clase orientada a el bot , todo lo que sepa el bot es aqui
import random
import player  # Importamos el módulo 'player' que debe tener la clase 'Player'

class Cpu(player.Player):  
    def __init__(self, difficulty):
        super().__init__("Makinon")
        self.difficulty = difficulty
        self.memory = {}  # Diccionario para recordar cartas vistas y sus posiciones
        self.last_position = None  # Última posición seleccionada por la CPU

    def cpuPlay(self, columns, rows, boardOut):
        # Si tiene una carta previa que puede emparejar
        if self.last_position:
            last_row, last_col = self.last_position
            last_card = boardOut[last_row - 1][last_col - 1]

            # Busca una pareja conocida en memoria
            for pos, card in self.memory.items():
                if card == last_card and pos != self.last_position:
                    # Limpiar last_position después de intentar emparejarla
                    self.last_position = None
                    return pos  # Devuelve la posición de la carta que coincide

        # Si no tiene pareja, elige una carta "boca abajo" aleatoria
        row, col = random.randint(1, rows), random.randint(1, columns)
        while boardOut[row - 1][col - 1] != "*":  # Evitar cartas ya descubiertas
            row, col = random.randint(1, rows), random.randint(1, columns)
        
        # Guardar la última posición seleccionada
        self.last_position = (row, col)
        return (col,row)

    def remind(self, pos, card):
        # Guardar en memoria la posición y carta vista
        self.memory[pos] = card
        # Limpiar last_position si ya hemos encontrado una pareja para evitar emparejar con ella misma
        if pos == self.last_position:
            self.last_position = None

