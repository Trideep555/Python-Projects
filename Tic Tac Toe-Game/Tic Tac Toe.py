import pygame as p
from pygame.locals import * 
import time
import numpy as np

class Game:    
    def __init__(self):    
        p.init()
        p.mixer.init()
        self.background_music()
        self.display=p.display.set_mode((900,675))
        p.display.set_caption("Tic Tac Toe")
        self.circle=[]
        self.line=[]
        self.mat=[[0 for i in range(3)] for j in range(3)]
    
    def first_screen(self):
        font=p.font.SysFont('segoeuisymbol',55)
        write=font.render('TIC TAC TOE',True,(255,255,255))
        img=p.image.load("Tic tac toe/background.jpg")
        self.display.blit(img,(0,0))
        self.display.blit(write,(260,220))
        write2=font.render('Press Enter to Continue....',True,(255,255,255))
        self.display.blit(write2,(130,295))
        ab=True
        p.display.update()
        while ab:
            for event in p.event.get():
                if event.type==KEYDOWN:
                    if event.key==K_RETURN:
                        ab=False
    def score_screen(self,x):
        p.mixer.music.pause()
        sound=p.mixer.Sound("Tic tac toe/finish.wav")
        p.mixer.Sound.play(sound)
        
        font=p.font.SysFont('segoeuisymbol',55)
        if(x!=3):
            write=font.render(f'Player {x} Wins',True,(255,255,255))
        else:
            write=font.render(f'Game Draw',True,(255,255,255))
        img=p.image.load("Tic tac toe/background.jpg")
        self.display.blit(img,(0,0))
        self.display.blit(write,(260,220))
        write2=font.render('Press Enter to Exit....',True,(255,255,255))
        self.display.blit(write2,(180,295))
        ab=True
        p.display.update()
        while ab:
            for event in p.event.get():
                if event.type==KEYDOWN:
                    if event.key==K_RETURN:
                        ab=False
    def background_music(self):
        p.mixer.music.load('Tic tac toe/Background Song.mp3')
        p.mixer.music.play(-1,0)
        
    def sound(self,x):
        if(x==1):
            sound=p.mixer.Sound("Tic tac toe/click.wav")
        else:
            sound=p.mixer.Sound("Tic tac toe/click2.wav")
        p.mixer.Sound.play(sound)
        

    def check(self,x,y):
        x1=0
        y1=0
        if(0<=x<300):
            x1=0
        elif(300<=x<600):
            x1=300
        else:
            x1=600
        if 0<=y<225:
            y1=0
        elif 225<=y<450:
            y1=225
        else:
            y1=450
        return x1,y1
    def checkRows(self,board):
        for row in board:
            if len(set(row)) == 1:   
                return row[0]
        return 0
    def checkDiagonals(self,board):
        if len(set([board[i][i] for i in range(len(board))])) == 1:
            return board[0][0]
        if len(set([board[i][len(board)-i-1] for i in range(len(board))])) == 1:
            return board[0][len(board)-1]
        return 0

    def checkWin(self,board):
        for newBoard in [board, np.transpose(board)]:
            result = self.checkRows(newBoard)
            if result:
                return result
        return self.checkDiagonals(board)
    def checkDraw(self,board):
        if(np.count_nonzero(board)==9):
            return True
        return False
    def play(self):
        game_run=True
        i=0
        while game_run:
            self.display.fill((255,255,255))
            p.draw.line(self.display,(0,0,0),[300,0],[300,675],2)
            p.draw.line(self.display,(0,0,0),[600,0],[600,675],2)
            p.draw.line(self.display,(0,0,0),[0,225],[900,225],2)
            p.draw.line(self.display,(0,0,0),[0,450],[900,450],2)
            for event in p.event.get():
                if event.type == QUIT:
                    game_run = False
                elif event.type == MOUSEBUTTONDOWN:
                    x,y = event.pos
                    x1,y1=self.check(x,y)
                    if i%2==0:
                        if(self.mat[x1//300][y1//225]==0):   
                            self.mat[x1//300][y1//225]=1
                            self.circle.append((x1,y1))
                            i+=1
                            self.sound(1)
                    else:
                        if(self.mat[x1//300][y1//225]==0):
                            self.mat[x1//300][y1//225]=2
                            self.line.append((x1,y1))
                            i+=1
                            self.sound(2)
                    x=self.checkWin(self.mat)
                    if(x!=0):
                        self.score_screen(x)
                        game_run=False
                        
                    elif(self.checkDraw(self.mat)):
                        self.score_screen(3)
                        game_run=False
                                          
                for position in self.line:
                    img=p.image.load("Tic tac toe/X.PNG")
                    self.display.blit(img,position)
                for position in self.circle:
                    img=p.image.load("Tic tac toe/O.PNG")
                    self.display.blit(img,position)
                p.display.update()
    
    
    
if __name__=='__main__':
    Tictac=Game()
    Tictac.first_screen()
    Tictac.play()