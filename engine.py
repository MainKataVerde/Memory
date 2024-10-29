from board import Board
from player import Player
from cpu import Cpu
import os
import time

class Engine:
    def __init__(self):
        self.game_board = Board
        self.player1 = Player
        self.player2 = Player
        
    def start(self):
        self.play()
        
    def play(self):
        acabado = False
        print("Bienvenudo al juego de las parejas\nPara iniciar el juego indicanos el numero de columnas y filas que quieres")
        columns = int(input("Columnas: "))
        rows = int(input("Filas: "))
        #Si el el tablero que le damos es impar o es mas grande de 30 
        # Hacemos que nos vuelva a dar los datos hasta que cumpla las condiciones
        if (columns * rows) >= 30 or (columns * rows)%2 != 0 :
            while (columns * rows) > 30 or (columns * rows)%2 != 0:
                print("Parece que te has pasado del maximo de (6x5) o tu multiplicacion da impar")
                columns = int(input("Columnas: "))
                rows = int(input("Filas: "))
        
        modo = int(input("Bien ahora que tenemos el tablero , ¿qué modo de juego quieres jugar?\n 1.Modo Jugador contra jugador\n 2.Modo Jugador contra CPU\n --> "))        
        self.game_board = Board(columns , rows)
        self.game_board.fillBoard()
        
        match modo :
            case 1 :
                
                print("Modo seleccionado : Jugador contra jugador\nDisfrutad y suerte!! :)")
                self.player1 = Player(input("Introduce el nombre del jugador 1 :"))
                self.player2 = Player(input("Introduce el nombre del jugador 2 :"))
                print("El primero en jugar es " , self.player1.getname())
                while acabado != True :
                    os.system('cls')
                    print("Puntos\n", self.player1.getname() , ": ", self.player1.getpoints(),"\n", self.player2.getname() , ": ", self.player2.getpoints(),"\n\n")
                    self.game_board.boarOutPrint()
                    print("¿Dónde crees que esta el primero ",self.player1.getname() , "?")
                    p1col1 = int(input("Columnas: "))
                    p1rws1 = int(input("Filas: "))
                    #Limpia la consola
                    os.system('cls')
                    print("Puntos\n", self.player1.getname() , ": ", self.player1.getpoints(),"\n", self.player2.getname() , ": ", self.player2.getpoints(),"\n\n")
                    self.game_board.discover(p1col1 , p1rws1)
                    print("¿Y el segundo?")
                    p1col2 = int(input("Columnas: "))
                    p1rws2 = int(input("Filas: "))
                    os.system('cls')
                    self.game_board.discover(p1col2 ,p1rws2)
                    if self.game_board.checkPairs(p1col1,p1rws1,p1col2,p1rws2):
                        print("Muy bien " , self.player1.getname() , ", has ganado 2 puntos")
                        self.player1.addpoints()
                    else:
                        print("!Que mal¡ , mas suerte la proxima ronda")
                    time.sleep(1.3)
                    os.system('cls')
                    print("Puntos\n", self.player1.getname() , ": ", self.player1.getpoints(),"\n", self.player2.getname() , ": ", self.player2.getpoints(),"\n\n")
                    self.game_board.boarOutPrint()
                    print("Ahora tu  ",self.player2.getname() , "¿Dónde crees que esta el primero?")
                    p2col1 = int(input("Columnas: "))
                    p2rws1 = int(input("Filas: "))
                    os.system('cls')
                    print("Puntos\n", self.player1.getname() , ": ", self.player1.getpoints(),"\n", self.player2.getname() , ": ", self.player2.getpoints(),"\n\n")
                    self.game_board.discover(p2col1 , p2rws1)
                    print("¿Y el segundo?")
                    p2col2 = int(input("Columnas: "))
                    p2rws2 = int(input("Filas: "))
                    os.system('cls')
                    self.game_board.discover(p2col2 ,p2rws2)
                    if self.game_board.checkPairs(p2col1,p2rws1,p2col2,p2rws2):
                        print("Muy bien " , self.player2.getname() , ", has ganado 2 puntos")
                        self.player2.addpoints()
                    else:
                        print("!Que mal¡ , mas suerte la proxima ronda")
                    time.sleep(1.3)
                    if (self.player1.getpoints() + self.player2.getpoints()) == self.game_board.maxPoint :
                        if self.player1.getpoints() > self.player2.getpoints() :
                            print(f"¡Enhorabuena {self.player1.getname()}! , eres el ganador\n Con una puntuacion de {self.player1.getpoints()}")
                        elif self.player1.getpoints() < self.player2.getpoints():
                            print(f"¡Enhorabuena {self.player2.getname()}! , eres el ganador\n Con una puntuacion de {self.player2.getpoints()}")
                        elif self.player1.getpoints() == self.player2.getpoints():
                            print("¡TENEMOS UN EMPATEEEEEE!")
                        acabado = True

                    

                    

                
        

