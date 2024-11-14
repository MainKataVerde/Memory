from board import Board
from player import Player
from cpu import Cpu
import os
import time

# clase es el motor del juego
class Engine:
    def __init__(self):
        self.game_board = Board
        self.player1 = Player
        self.player2 = Player
        self.cpu = Cpu
        self.cpu2 = Cpu
        
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
        
        modo = int(input("Bien ahora que tenemos el tablero , ¿qué modo de juego quieres jugar?\n 1.Modo Jugador contra jugador\n 2.Modo Jugador contra Maquina\n 3.Modo Maquina contra Maquina\n  --> "))        
        self.game_board = Board(columns , rows)
        self.game_board.fillBoard()
        
        match modo :
            case 1 :
                #mientras el jugaro este poniendo las cosas bien se sigue jugando
                print("Modo seleccionado : Jugador contra jugador\nDisfrutad y suerte!! :)")
                self.player1 = Player(input("Introduce el nombre del jugador 1 :"))
                self.player2 = Player(input("Introduce el nombre del jugador 2 :"))
                print("El primero en jugar es " , self.player1.getname())
                while acabado != True :
                    turno1 = False
                    turno2 = False
                    while turno1 != True:
                        os.system('cls')
                        print("Puntos\n", self.player1.getname() , ": ", self.player1.getpoints(),"\n", self.player2.getname() , ": ", self.player2.getpoints(),"\n\n")
                        self.game_board.boarOutPrint()
                        print("¿Dónde crees que esta el primero ",self.player1.getname() , "?")
                        p1col1 = int(input("Columnas: "))
                        p1rws1 = int(input("Filas: "))
                        if self.game_board.checkPosition(p1col1 , p1rws1) == False:
                            while self.game_board.checkPosition(p1col1 , p1rws1) == False:
                                print("Esa posicion ya ha sido adivinada elige una correcta")
                                p1col1 = int(input("Columnas: "))
                                p1rws1 = int(input("Filas: "))
                        os.system('cls')
                        print("Puntos\n", self.player1.getname() , ": ", self.player1.getpoints(),"\n", self.player2.getname() , ": ", self.player2.getpoints(),"\n\n")
                        self.game_board.discover(p1col1 , p1rws1)
                        print("¿Y el segundo?")
                        p1col2 = int(input("Columnas: "))
                        p1rws2 = int(input("Filas: "))
                        if self.game_board.checkPosition(p1col2 , p1rws2) == False:
                            while self.game_board.checkPosition(p1col2 , p1rws2) == False:
                                print("Esa posicion ya ha sido adivinada elige una correcta")
                                p1col1 = int(input("Columnas: "))
                                p1rws1 = int(input("Filas: "))
                        os.system('cls')
                        self.game_board.discover(p1col2 ,p1rws2)
                        if self.game_board.checkPairs(p1col1,p1rws1,p1col2,p1rws2):
                            print("Muy bien " , self.player1.getname() , ", has ganado 2 puntos")
                            self.player1.addpoints()
                            if (self.player1.getpoints() + self.player2.getpoints()) == self.game_board.maxPoint :
                                if self.player1.getpoints() > self.player2.getpoints() :
                                    print(f"¡Enhorabuena {self.player1.getname()}! , eres el ganador\n Con una puntuacion de {self.player1.getpoints()}")
                                elif self.player1.getpoints() < self.player2.getpoints():
                                    print(f"¡Enhorabuena {self.player2.getname()}! , eres el ganador\n Con una puntuacion de {self.player2.getpoints()}")
                                elif self.player1.getpoints() == self.player2.getpoints():
                                    print("¡TENEMOS UN EMPATEEEEEE!")
                                acabado = True
                                turno1 = True
                                turno2 = True
                        else:
                            print("!Que mal¡ , mas suerte la proxima ronda")
                            turno1 = True
                    while turno2 != True:
                        time.sleep(1.3)
                        os.system('cls')
                        print("Puntos\n", self.player1.getname() , ": ", self.player1.getpoints(),"\n", self.player2.getname() , ": ", self.player2.getpoints(),"\n\n")
                        self.game_board.boarOutPrint()
                        print("Ahora tu  ",self.player2.getname() , "¿Dónde crees que esta el primero?")
                        p2col1 = int(input("Columnas: "))
                        p2rws1 = int(input("Filas: "))
                        if self.game_board.checkPosition(p2col1 , p2rws1) == False:
                            while self.game_board.checkPosition(p2col1 , p2rws1) == False:
                                print("Esa posicion ya ha sido adivinada elige una correcta")
                                p1col1 = int(input("Columnas: "))
                                p1rws1 = int(input("Filas: "))
                        os.system('cls')
                        print("Puntos\n", self.player1.getname() , ": ", self.player1.getpoints(),"\n", self.player2.getname() , ": ", self.player2.getpoints(),"\n\n")
                        self.game_board.discover(p2col1 , p2rws1)
                        print("¿Y el segundo?")
                        p2col2 = int(input("Columnas: "))
                        p2rws2 = int(input("Filas: "))
                        if self.game_board.checkPosition(p2col2 , p2rws2) == False:
                            while self.game_board.checkPosition(p2col2 , p2rws2) == False:
                                print("Esa posicion ya ha sido adivinada elige una correcta")
                                p1col1 = int(input("Columnas: "))
                                p1rws1 = int(input("Filas: "))
                        os.system('cls')
                        self.game_board.discover(p2col2 ,p2rws2)
                        if self.game_board.checkPairs(p2col1,p2rws1,p2col2,p2rws2):
                            print("Muy bien " , self.player2.getname() , ", has ganado 2 puntos")
                            self.player2.addpoints()
                            if (self.player1.getpoints() + self.player2.getpoints()) == self.game_board.maxPoint :
                                if self.player1.getpoints() > self.player2.getpoints() :
                                    print(f"¡Enhorabuena {self.player1.getname()}! , eres el ganador\n Con una puntuacion de {self.player1.getpoints()}")
                                elif self.player1.getpoints() < self.player2.getpoints():
                                    print(f"¡Enhorabuena {self.player2.getname()}! , eres el ganador\n Con una puntuacion de {self.player2.getpoints()}")
                                elif self.player1.getpoints() == self.player2.getpoints():
                                    print("¡TENEMOS UN EMPATEEEEEE!")
                                acabado = True
                                turno2 = True
                                turno1 = True
                        else:
                            print("!Que mal¡ , mas suerte la proxima ronda")
                            turno2 = True
                        time.sleep(1.3)
            case 2 :
                print("Modo seleccionado : Jugador contra maquina\nDisfrutad y suerte!! :)")
                self.player1 = Player(input("Introduce tu nombre :"))
                dificultad = int(input("¿En que dificultad quieres a la maquina?\n1.Facil\n2.Intermedia\n3.Dificil\n --> "))
                self.cpu= Cpu(dificultad)
                match dificultad:
                    case 1 :
                        print("Maquina en dificultadad Facil\n¡Disfuta!") 
                    case 2 :
                        print("Maquina en dificultadad Intermedia\n¡Disfuta!")
                    case 3 : 
                        print("Maquina en dificultadad Dificil\n¡Disfuta!")
                time.sleep(1.3) 
                while acabado != True :
                    turno1 = False
                    turno2 = False
                    while turno1 != True:
                        os.system('cls')
                        print("Puntos\n", self.player1.getname() , ": ", self.player1.getpoints(),"\n", self.cpu.getname() , ": ", self.cpu.getpoints(),"\n\n")
                        self.game_board.boarOutPrint()
                        print("¿Dónde crees que esta el primero ",self.player1.getname() , "?")
                        p1col1 = int(input("Columnas: "))
                        p1rws1 = int(input("Filas: "))
                        if self.game_board.checkPosition(p1col1 , p1rws1) == False:
                            while self.game_board.checkPosition(p1col1 , p1rws1) == False:
                                print("Esa posicion ya ha sido adivinada elige una correcta")
                                p1col1 = int(input("Columnas: "))
                                p1rws1 = int(input("Filas: "))
                        os.system('cls')
                        print("Puntos\n", self.player1.getname() , ": ", self.player1.getpoints(),"\n", self.cpu.getname() , ": ", self.cpu.getpoints(),"\n\n")
                        self.game_board.discover(p1col1 , p1rws1)
                        print("¿Y el segundo?")
                        p1col2 = int(input("Columnas: "))
                        p1rws2 = int(input("Filas: "))
                        if self.game_board.checkPosition(p1col2 , p1rws2) == False:
                            while self.game_board.checkPosition(p1col2 , p1rws2) == False:
                                print("Esa posicion ya ha sido adivinada elige una correcta")
                                p1col1 = int(input("Columnas: "))
                                p1rws1 = int(input("Filas: "))
                        os.system('cls')
                        print("Puntos\n", self.player1.getname() , ": ", self.player1.getpoints(),"\n", self.cpu.getname() , ": ", self.cpu.getpoints(),"\n\n")
                        self.game_board.discover(p1col2 ,p1rws2)
                        if self.game_board.checkPairs(p1col1,p1rws1,p1col2,p1rws2):
                            print("Muy bien " , self.player1.getname() , ", has ganado 2 puntos")
                            self.player1.addpoints()
                            if (self.player1.getpoints() + self.cpu.getpoints()) == self.game_board.maxPoint :
                                if self.player1.getpoints() > self.cpu.getpoints() :
                                    print(f"¡Enhorabuena {self.player1.getname()}! , eres el ganador\n Con una puntuacion de {self.player1.getpoints()}")
                                elif self.player1.getpoints() < self.cpu.getpoints():
                                    print(f"¡Enhorabuena {self.cpu.getname()}! , eres el ganador\n Con una puntuacion de {self.cpu.getpoints()}")
                                elif self.player1.getpoints() == self.cpu.getpoints():
                                    print("¡TENEMOS UN EMPATEEEEEE!")
                                acabado = True
                                turno1 = True
                                turno2 = True
                        else:
                            print("!Que mal¡ , mas suerte la proxima ronda")
                            turno1 = True
                        #turno de la cpu
                    while turno2 != True:
                        time.sleep(1.3)
                        os.system('cls')
                        print("Puntos\n", self.player1.getname() , ": ", self.player1.getpoints(),"\n", self.cpu.getname() , ": ", self.cpu.getpoints(),"\n\n")
                        self.game_board.boarOutPrint()
                        print("Ahora tu ", self.cpu.getname() , "¿Dónde crees que esta el primero?")
                        time.sleep(1.3)
                        postions1 = self.cpu.cpuPlay(columns,rows , self.game_board.boardOut)
                        if self.game_board.checkPosition(*postions1) == False:
                            while self.game_board.checkPosition(*postions1) == False:
                                print("Esa posicion ya ha sido adivinada elige una correcta")
                                postions1 = self.cpu.cpuPlay(columns,rows,self.game_board.boardOut)
                                os.system('cls')
                        self.cpu.remind(postions1 , self.game_board.boardIn[postions1[1] - 1][postions1[0] - 1])
                        os.system('cls')
                        print("Puntos\n", self.player1.getname() , ": ", self.player1.getpoints(),"\n", self.cpu.getname() , ": ", self.cpu.getpoints(),"\n\n")
                        self.game_board.discover(*postions1)
                        print("¿Y el segundo?")
                        time.sleep(1.3)
                        postions2 = self.cpu.cpuPlay(columns,rows, self.game_board.boardOut)
                        if self.game_board.checkPosition(*postions2) == False:
                            while self.game_board.checkPosition(*postions2) == False:
                                print("Esa posicion ya ha sido adivinada elige una correcta")
                                postions2 = self.cpu.cpuPlay(columns,rows, self.game_board.boardOut)
                                os.system('cls')
                        self.cpu.remind(postions1 , self.game_board.boardIn[postions1[1] - 1][postions1[0] - 1])
                        os.system('cls')
                        print("Puntos\n", self.player1.getname() , ": ", self.player1.getpoints(),"\n", self.cpu.getname() , ": ", self.cpu.getpoints(),"\n\n")
                        self.game_board.discover(*postions2)
                        if self.game_board.checkPairs(*postions1,*postions2):
                            print("Muy bien " , self.cpu.getname() , ", has ganado 2 puntos")
                            self.cpu.addpoints()
                            if (self.player1.getpoints() + self.cpu.getpoints()) == self.game_board.maxPoint :
                                if self.player1.getpoints() > self.cpu.getpoints() :
                                    print(f"¡Enhorabuena {self.player1.getname()}! , eres el ganador\n Con una puntuacion de {self.player1.getpoints()}")
                                elif self.player1.getpoints() < self.cpu.getpoints():
                                    print(f"¡Enhorabuena {self.cpu.getname()}! , eres el ganador\n Con una puntuacion de {self.cpu.getpoints()}")
                                elif self.player1.getpoints() == self.cpu.getpoints():
                                    print("¡TENEMOS UN EMPATEEEEEE!")
                                acabado = True
                                turno2 = True
                                turno1 = True
                        else:
                            print("!Que mal¡ , mas suerte la proxima ronda")
                            turno2 = True
                        time.sleep(1.3)   
            case 3 : 
                print("Modo seleccionado : Maquina contra maquina\nDisfrutad y suerte!! :)")
                self.cpu= Cpu(1)
                self.cpu2= Cpu(1)
                self.cpu.setname("Makinon1")
                self.cpu2.setname("Makinon2")
                while acabado != True :
                    turno1 = False
                    turno2 = False
                    #turno de la maquina1
                    while turno1 != True:
                        time.sleep(1.3)
                        os.system('cls')
                        print("Puntos\n", self.cpu.getname() , ": ", self.cpu.getpoints(),"\n", self.cpu2.getname() , ": ", self.cpu2.getpoints(),"\n\n")
                        self.game_board.boarOutPrint()
                        print("Ahora tu ", self.cpu.getname() , "¿Dónde crees que esta el primero?")
                        time.sleep(1.3)
                        postions1 = self.cpu.cpuPlay(columns,rows , self.game_board.boardOut)
                        if self.game_board.checkPosition(*postions1) == False:
                            while self.game_board.checkPosition(*postions1) == False:
                                print("Esa posicion ya ha sido adivinada elige una correcta")
                                postions1 = self.cpu.cpuPlay(columns,rows,self.game_board.boardOut)
                                os.system('cls')
                        self.cpu.remind(postions1 , self.game_board.boardIn[postions1[1] - 1][postions1[0] - 1])
                        os.system('cls')
                        print("Puntos\n", self.cpu.getname() , ": ", self.cpu.getpoints(),"\n", self.cpu2.getname() , ": ", self.cpu2.getpoints(),"\n\n")
                        self.game_board.discover(*postions1)
                        print("¿Y el segundo?")
                        time.sleep(1.3)
                        postions2 = self.cpu.cpuPlay(columns,rows, self.game_board.boardOut)
                        if self.game_board.checkPosition(*postions2) == False:
                            while self.game_board.checkPosition(*postions2) == False:
                                print("Esa posicion ya ha sido adivinada elige una correcta")
                                postions2 = self.cpu.cpuPlay(columns,rows, self.game_board.boardOut)
                                os.system('cls')
                        self.cpu.remind(postions1 , self.game_board.boardIn[postions1[1] - 1][postions1[0] - 1])
                        os.system('cls')
                        print("Puntos\n", self.cpu.getname() , ": ", self.cpu.getpoints(),"\n", self.cpu2.getname() , ": ", self.cpu2.getpoints(),"\n\n")
                        self.game_board.discover(*postions2)
                        if self.game_board.checkPairs(*postions1,*postions2):
                            print("Muy bien " , self.cpu.getname() , ", has ganado 2 puntos")
                            self.cpu.addpoints()
                            if (self.cpu2.getpoints() + self.cpu.getpoints()) == self.game_board.maxPoint :
                                if self.cpu2.getpoints() > self.cpu.getpoints() :
                                    print(f"¡Enhorabuena {self.cpu2.getname()}! , eres el ganador\n Con una puntuacion de {self.player1.getpoints()}")
                                elif self.cpu2.getpoints() < self.cpu.getpoints():
                                    print(f"¡Enhorabuena {self.cpu.getname()}! , eres el ganador\n Con una puntuacion de {self.cpu.getpoints()}")
                                elif self.cpu2.getpoints() == self.cpu.getpoints():
                                    print("¡TENEMOS UN EMPATEEEEEE!")
                                acabado = True
                                turno1 = True
                                turno2 = True
                        else:
                            print("!Que mal¡ , mas suerte la proxima ronda")
                            turno1 = True
                        time.sleep(1.3)  
                    #turno de la maquina2  
                    while turno2 != True:
                        time.sleep(1.3)
                        os.system('cls')
                        print("Puntos\n", self.cpu.getname() , ": ", self.cpu.getpoints(),"\n", self.cpu2.getname() , ": ", self.cpu2.getpoints(),"\n\n")
                        self.game_board.boarOutPrint()
                        print("Ahora tu ", self.cpu2.getname() , "¿Dónde crees que esta el primero?")
                        time.sleep(1.3)
                        postions1 = self.cpu2.cpuPlay(columns,rows , self.game_board.boardOut)
                        if self.game_board.checkPosition(*postions1) == False:
                            while self.game_board.checkPosition(*postions1) == False:
                                print("Esa posicion ya ha sido adivinada elige una correcta")
                                postions1 = self.cpu2.cpuPlay(columns,rows,self.game_board.boardOut)
                                os.system('cls')
                        self.cpu2.remind(postions1 , self.game_board.boardIn[postions1[1] - 1][postions1[0] - 1])
                        os.system('cls')
                        print("Puntos\n", self.cpu.getname() , ": ", self.cpu.getpoints(),"\n", self.cpu2.getname() , ": ", self.cpu2.getpoints(),"\n\n")
                        self.game_board.discover(*postions1)
                        print("¿Y el segundo?")
                        time.sleep(1.3)
                        postions2 = self.cpu2.cpuPlay(columns,rows, self.game_board.boardOut)
                        if self.game_board.checkPosition(*postions2) == False:
                            while self.game_board.checkPosition(*postions2) == False:
                                print("Esa posicion ya ha sido adivinada elige una correcta")
                                postions2 = self.cpu2.cpuPlay(columns,rows, self.game_board.boardOut)
                                os.system('cls')
                        self.cpu2.remind(postions1 , self.game_board.boardIn[postions1[1] - 1][postions1[0] - 1])
                        os.system('cls')
                        print("Puntos\n", self.cpu.getname() , ": ", self.cpu.getpoints(),"\n", self.cpu2.getname() , ": ", self.cpu2.getpoints(),"\n\n")
                        self.game_board.discover(*postions2)
                        if self.game_board.checkPairs(*postions1,*postions2):
                            print("Muy bien " , self.cpu2.getname() , ", has ganado 2 puntos")
                            self.cpu2.addpoints()
                            if (self.cpu2.getpoints() + self.cpu.getpoints()) == self.game_board.maxPoint :
                                if self.cpu2.getpoints() > self.cpu.getpoints() :
                                    print(f"¡Enhorabuena {self.cpu2.getname()}! , eres el ganador\n Con una puntuacion de {self.cpu2.getpoints()}")
                                elif self.cpu2.getpoints() < self.cpu.getpoints():
                                    print(f"¡Enhorabuena {self.cpu.getname()}! , eres el ganador\n Con una puntuacion de {self.cpu.getpoints()}")
                                elif self.cpu2.getpoints() == self.cpu.getpoints():
                                    print("¡TENEMOS UN EMPATEEEEEE!")
                                acabado = True
                                turno2 = True
                                turno1 = True
                        else:
                            print("!Que mal¡ , mas suerte la proxima ronda")
                            turno2 = True
                        time.sleep(1.3) 

                    

                
        

