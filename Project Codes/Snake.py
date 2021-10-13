import pygame as p
from pygame.locals import *
import time
import random

SIZE = 40
Background=(17, 79, 99)

class Apple:
    def __init__(self, parent_screen):
        self.image = p.image.load("Snake/apple.jpg").convert()
        self.parent_screen = parent_screen
        self.x = SIZE * 3
        self.y = SIZE * 3

    def draw(self):
        self.parent_screen.blit(self.image, (self.x, self.y))
        p.display.flip()

    def move(self):
        self.x=random.randint(1,30)* SIZE
        self.y=random.randint(1,25)* SIZE


class Snake:
    def __init__(self, parent_screen, length):
        self.length = length
        self.parent_screen = parent_screen
        self.block = p.image.load("Snake/block.jpg").convert()
        self.x = [SIZE] * length
        self.y = [SIZE] * length
        self.direction = 'down'
    def increase_length(self):
        self.length+=1
        self.x.append(-1)
        self.y.append(-1)
    def draw(self):

        for i in range(self.length):
            self.parent_screen.blit(self.block, (self.x[i], self.y[i]))
        p.display.update()

    def move_up(self):
        self.direction = 'up'

    def move_down(self):
        self.direction = 'down'

    def move_left(self):
        self.direction = 'left'

    def move_right(self):
        self.direction = 'right'

    def walk(self):
        for i in range(self.length - 1, 0, -1):
            self.x[i] = self.x[i - 1]
            self.y[i] = self.y[i - 1]
        if self.direction == 'down':
            self.y[0] += SIZE
        if self.direction == 'left':
            self.x[0] -= SIZE
        if self.direction == 'up':
            self.y[0] -= SIZE
        if self.direction == 'right':
            self.x[0] += SIZE
        self.draw()


class Game:
    def __init__(self):
        p.init()
        p.mixer.init()

        self.display = p.display.set_mode((1920, 1080),p.FULLSCREEN)
        p.display.set_caption('Snake Game')
        self.background_music()
        self.snake = Snake(self.display, 1)
        self.snake.draw()
        self.apple = Apple(self.display)
        self.apple.draw()

    def collide(self, x1, y1, x2, y2):
        if x2 <= x1 < x2 + SIZE:
            if y2 <= y1 < y2 + SIZE:
                return True
        return False
    def limit(self,x1,x2,y1,y2):
        if x1>=x2 or x1<0 or y1>=y2 or y1<0:
            return True

    def display_score(self):
        font=p.font.SysFont('arial',30)
        score=font.render(f"Score: {self.snake.length-1}",True,(200,200,200))
        self.display.blit(score,(1300,10))

    def background_music(self):
        p.mixer.music.load('Snake/music.mp3')
        p.mixer.music.play(-1,0)

    def sound(self,song):
        sound = p.mixer.Sound(f"Snake/{song}.mp3")
        p.mixer.Sound.play(sound)

    def play(self):
        self.background_image()
        self.snake.walk()
        self.apple.draw()
        self.display_score()
        p.display.update()

        if self.collide(self.snake.x[0], self.snake.y[0], self.apple.x, self.apple.y):
            self.sound("eat")
            self.snake.increase_length()
            self.apple.move()
        if self.limit(self.snake.x[0],1080,self.snake.y[0],1920):
            raise "Game Over"

        for i in range(2,self.snake.length):
            if self.collide(self.snake.x[0],self.snake.y[0],self.snake.x[i],self.snake.y[i]):
                self.sound("crash")
                raise "Game Over"

    def show_game_over(self):
        self.background_image()
        font = p.font.SysFont('arial', 60)
        Final_score = font.render(f" Game over!! Your Final Score is: {self.snake.length - 1}", True, (214, 20, 6))
        self.display.blit(Final_score,(400,300))
        Again=font.render("To Play again Press Enter.To exit press Escape",True,(255,255,255))
        self.display.blit(Again, (400, 350))
        p.display.update()
        p.mixer.music.pause()
    def background_image(self):
        img=p.image.load("Snake/background.jpg")
        self.display.blit(img,(0,0))
    def  reset(self):
        self.snake = Snake(self.display, 1)
        self.apple = Apple(self.display)

    def run(self):
        game_run = True
        pause=False
        while game_run:
            for events in p.event.get():
                if events.type == KEYDOWN:
                    if events.key == K_ESCAPE:
                        game_run = False
                    if events.key == K_RETURN:
                        p.mixer.music.unpause()
                        pause = False
                    if not pause:
                        if events.key == K_UP:
                            self.snake.move_up()
                        if events.key == K_DOWN:
                            self.snake.move_down()
                        if events.key == K_LEFT:
                            self.snake.move_left()
                        if events.key == K_RIGHT:
                            self.snake.move_right()
                elif events.type == QUIT:
                    game_run = False
            try:
                if not pause:
                    self.play()
            except Exception as e:
                self.show_game_over()
                pause= True
                self.reset()
            time.sleep(0.2)


if __name__ == "__main__":
    game = Game()
    game.run()
