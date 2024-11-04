class Player: 
    def __init__(self, name):
        self.name = name
        self.points = 0
    #metodo que cambiar o pone el nombre del jugador  
    def setname(self, name):
        self.name = name
    #metodo que añade 2 puntos al jugador
    def addpoints(self):
        self.points += 2
    #metodo que nos devuelve el nombre dle jugador
    def getname(self):
        return self.name
    #netodo que nos devuelve el numero de puntos que tiene el jugador
    def getpoints(self):
        return self.points