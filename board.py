import random

# clase destinada a elavorar el tablero donde se va a jugar
class Board:
    def __init__(self, width, height):
        self.width = width # número de columnas
        self.height = height # número de filas
        self.boardOut = [["*" for i in range(width)] for j in range(height)] # lista 2D para el jugador (oculta)
        self.boardIn = [[] for j in range(height)] # lista 2D con todas las figuras (oculta)
        self.maxPoint = self.width * self.height # puntos maximos que puede alcanzar la partida cada jugador o entre los dos
        self.elementos = ["🎃", "👻", "👽", "🐍", "🦄", "🍕", "🌈", "🚀", "🐸", "💎", "🔥", "🍄", "🌻", "⚽", "🎲"]# array con los emoji que vamos a usar
        self.posicionesCorrectas = []
    # metodo que imprime la array que va a ver el usuario    
    def boarOutPrint(self):
        num = 1
        print("  " , end='')
        for i in range(1 , self.width + 1):
            print(i , end="   ")
        print("")
        for i in self.boardOut:
            print( num , end="  ")
            num+=1
            for j in i:
                print(j , end="   ")
            print()

    # metodo que imprime la array interna con todas las repuestas     
    def boarInPrint(self):
        for i in self.boardIn:
            for j in i :
                print(j , end="  ")
            print()
       
    # metodo que rellena de parejas la array     
    def fillBoard(self): 
        # seleccionamos un conjunto de elementos aleatorios en pares , 
        # lo que esta entre parentesis es el numero maximo de parejas posibles
        pairs = random.sample(self.elementos, ((self.width * self.height)//2)) * 2 
        # mezclamos los elementos de la lista
        random.shuffle(pairs) 
        
        # añadimos los elementos a la lista
        for i in range(self.height):
            for j in range(self.width):
                self.boardIn[i].append(pairs.pop())
    
    # metodo nos muestra las repuesta que hemos elegido         
    def discover(self , colum , row):
        self.boardOut[(row-1)][(colum - 1)] = self.boardIn[(row-1)][(colum - 1)]
        self.boarOutPrint()
    # metod que comprueba que la pareja que hemos elegido es correcta
    def checkPairs(self , colm1 , rw1 , colm2 , rw2):    
        if self.boardIn[(rw1 -1)][(colm1 - 1)] == self.boardIn[(rw2 -1)][(colm2 - 1)] :
            self.posicionesCorrectas.append((rw1 -1))
            self.posicionesCorrectas.append((colm1 -1))
            self.posicionesCorrectas.append((rw2 -1))
            self.posicionesCorrectas.append((colm2 -1))
            return True
        else:
            self.boardOut[(rw1-1)][(colm1 - 1)] = "*"
            self.boardOut[(rw2-1)][(colm2 - 1)] = "*"
            return False
    
    def checkPosition(self , colm , rows):
        if colm > (self.width * self.height) or rows > (self.width * self.height) : 
            return False
        elif self.boardOut[(rows -1)][(colm - 1)] != "*":
            return False
        else: 
            return True
            
            


        
