import pygame
from enum import Enum
from pygame.locals import *
from random import randrange
class Movement(Enum):
    LEFT   = 1 
    RIGHT  = 2 
    UP     = 3
    DOWN   = 4 

class Snake:
    # šířka hada
    DOT_SIZE = 10
    # délka hada při startu (počet stavebních kamenů)
    N_DOTS = 3
    # max pozice jablka v libovolné ose
    APPLE_MAX_POS = 29
    def __init__(self):
        # body = tělo hada, reprezentované seznamem bodů (n-tic) jednotlivých stavebních kamenů o šířce Snake.DOT_SIZE
        self._body = []
        # aktuální pohyb
        self._movement = Movement.RIGHT
        # pozice jablka
        self._apple_position = ()
        self._respawn_apple()
        # hlava hada
        self._image_head = None
        # stav. kámen hada
        self._image_body = None
        # jablko
        self._image_apple = None


    def init_snake(self):
        for z in range(Snake.N_DOTS):
            self._body.append((50 - z * 10, 50))
        self._image_head = pygame.image.load("../resources/head.png").convert()
        self._image_body = pygame.image.load("../resources/dot.png").convert()
        self._image_apple = pygame.image.load("../resources/apple.png").convert()

    def _respawn_apple(self):
        self._apple_position = (randrange(Snake.APPLE_MAX_POS), randrange(Snake.APPLE_MAX_POS))
    
    def draw(self, surface):
        #draw apple
        surface.blit(self._image_apple, self._apple_position)
        #draw snake
        cnt = 0
        for p in self._body:
            if cnt == 0:
                surface.blit(self._image_head, p)
            else:
                surface.blit(self._image_body, p)
            cnt += 1
    def move(self):
        self._body = [(self._body[0][0], self._body[0][1])] + self._body
        if self._movement == Movement.LEFT:
            self._body[0][0] -= Snake.DOT_SIZE
        elif self._movement == Movement.RIGHT:
            self._body[0][0] += Snake.DOT_SIZE
        elif self._movement == Movement.UP:
            self._body[0][1] += Snake.DOT_SIZE
        elif self._movement == Movement.DOWN:
            self._body[0][1] += Snake.DOT_SIZE
    def set_movement(self, mvmt):
        self._movement = mvmt

class App:
    B_WIDTH  = 300
    B_HEIGHT = 300

    
    def __init__(self):
        # hra neskončena
        self._running = True 
        self._display_surf = None
        self._snake = Snake()
        self.size = self.width, self.height = App.B_WIDTH, App.B_HEIGHT
        self._display_surf = None
        self._clock = None
 
    def on_init(self):
        # inicializace PyGame modulů
        pygame.init()   
        # nastavení velikosti okna, pokus o nastavení HW akcelerace, pokud nelze, použije se DOUBLEBUF
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        self._clock = pygame.time.Clock()
        self._snake.init_snake()
    def on_input_focus(self):
        pass
    def on_key_down(self, event):
        print("key down...")
        print(event)
        if event.key == pygame.K_LEFT:
            self._snake.set_movement(Movement.LEFT)
        if event.key == pygame.K_RIGHT:
            self._snake.set_movement(Movement.RIGHT)
        if event.key == pygame.K_UP:
            self._snake.set_movement(Movement.UP)
        if event.key == pygame.K_DOWN:
            self._snake.set_movement(Movement.DOWN)          
    def on_key_up(self, event):
        pass
    def on_event(self, event):
        if event.type == QUIT:
            self._running = False
            #self.on_exit()
        elif event.type == KEYUP:
            self.on_key_up(event)
        elif event.type == KEYDOWN:
            self.on_key_down(event)

    def on_loop(self):
        self._snake.move
        self._clock.tick(250) 

    def on_render(self):
            pygame.draw.rect(self._display_surf, (0xff, 0xff, 0xff), pygame.Rect(0, 0, App.B_WIDTH, App.B_HEIGHT))
            self._snake.draw(self._display_surf)
            pygame.display.flip()
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        self.on_init()
        # game loop
        while( self._running ):
            # zpracování všech typů událostí
            for event in pygame.event.get():
                self.on_event(event)
            self.on_loop()
            self.on_render()
        self.on_cleanup()
 
if __name__ == "__main__" :
    theApp = App()
    theApp.on_execute()