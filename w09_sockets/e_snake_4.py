# inspirace: https://zetcode.com/javagames/snake/

# Vytvořte síťovou verzi hry snake. Zde jsou pozice jablka a instance hráčů uloženy ve statických proměnných třídy Snake. Pro picklink
# (serializace dat pomocí nakládání) je však potřeba mít vše v objektu. Příklad s použitím nakládání zde:
# ..\w07_oop\examples\Image.py

import pygame
from enum import Enum
from pygame.locals import *
from random import randrange
import sys
import socket
import pickle

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
    # délka překážky
    N_OBSTACLE_DOTS = 3
    # max pozice jablka v libovolné ose
    APPLE_MAX_POS = 29
    OBSTACLES =[
            [[10,10], [10,11], [10,12]],
            [[24,24], [25,24], [26,24]],
            [[13,12], [13,13], [13,14], [12,13], [14,13]]
        ]

    def __init__(self, app, y_init):
        # body = tělo hada, reprezentované seznamem bodů (n-tic) jednotlivých stavebních kamenů o šířce Snake.DOT_SIZE
        self._body = []
        # aktuální pohyb
        self._movement = Movement.RIGHT
        
        
        # hlava hada
        self._image_head = None
        # stav. kámen hada
        self._image_body = None
        # jablko
        self._image_apple = None
        # Snake running
        self._running = True
        self._y_init = y_init
        self._app = app
        self._app.respawn_apple()
        self._app.snakes.append(self)
        
    def init_snake(self):
        for z in range(Snake.N_DOTS):
            self._body.append([50 - z * Snake.DOT_SIZE, self._y_init])
        self._image_head = pygame.image.load("../resources/head.png").convert()
        self._image_body = pygame.image.load("../resources/dot.png").convert()
        self._image_apple = pygame.image.load("../resources/apple.png").convert()
        
    def pohyb(self, movement):
        head = [self._body[0][0], self._body[0][1]]
        if movement == Movement.LEFT:
            head[0] -= Snake.DOT_SIZE
        if movement == Movement.RIGHT:
            head[0] += Snake.DOT_SIZE
        if movement == Movement.UP:
            head[1] -= Snake.DOT_SIZE
        if movement == Movement.DOWN:
            head[1] += Snake.DOT_SIZE
        if head == self._app.apple_position:
            self._body = [head] + self._body
            self._app.respawn_apple()
            self._app.speed += 0.5
            if self._app.speed >= App.SPEED_LEVEL_LIMIT:
                self._app.level += 1
                App.play_music(self._app.level)
                self._app.speed = 8
        else:
            self._body = [head] + self._body[:-1]
    def is_collided(self):
        # možné body kolize sám se sebou a spoluhráči
        bodies = self._app.get_bodies()
        bodies.remove(self._body[0])
        # S koncem obrazovky
        if (self._body[0][0] == 0
            or self._body[0][0] == App.B_WIDTH-Snake.DOT_SIZE
            or self._body[0][1] == App.SCORE_SCREEN_HEIGHT
            or self._body[0][1] == App.B_HEIGHT-Snake.DOT_SIZE
            # sám se sebou, či s ostatními
            or self._body[0] in bodies
            # s překážkami:
            or self._body[0] in map(
                lambda p: [p[0] * Snake.DOT_SIZE, p[1] * Snake.DOT_SIZE], 
                sum(Snake.OBSTACLES[:self._app.level-1],[]))):

            self._running = False



    def draw_obstacles(self, surface):
        cnt = 0
        for obstacle in Snake.OBSTACLES:
            cnt += 1
            if cnt == self._app.level:
                break
            for p in obstacle:
                pygame.draw.rect(surface, (0,0,255), pygame.Rect(
                    Snake.DOT_SIZE * p[0], Snake.DOT_SIZE * p[1], Snake.DOT_SIZE, Snake.DOT_SIZE), 3)
            

    def draw(self, surface):
        #draw apple
        surface.blit(self._image_apple, self._app.apple_position)
        #draw snake
        surface.blit(self._image_head, self._body[0])
        #draw obstacles
        self.draw_obstacles(surface)
        
        for i in range(len(self._body) - 1):
            surface.blit(self._image_body, self._body[i + 1])
    def setMovement(self, movement):
        self._movement = movement
    
    def getScore(self):
        return len(self._body) - Snake.N_DOTS

class App:
    HOST = "127.0.0.1"  # Standard loopback interface address (localhost)
    PORT = 65432  # Port to listen on (non-privileged ports are > 1023)  
    B_WIDTH  = 300
    B_HEIGHT = 300
    SCORE_SCREEN_HEIGHT = 40
    SPEED_LEVEL_LIMIT = 10

    d_level_mid = {
        1: "../resources/tetris.mid",
        2: "../resources/mortal_kombat.mid",
        3: "../resources/popcorn.mid",
        4: "../resources/beat_it.mid",
    }
    _display_surf = pygame.display.set_mode((B_WIDTH, B_HEIGHT), pygame.HWSURFACE | pygame.DOUBLEBUF)
    _clock = pygame.time.Clock()
    pygame.font.init()
    pygame.mixer.init()

    @staticmethod
    def play_music(level):
        pygame.mixer.music.stop()
        pygame.mixer.music.load(App.d_level_mid.get(level))
        pygame.mixer.music.play()
        
    def __init__(self):
        # instance hráčú
        self.snakes = []
        # pozice jablka
        self.apple_position = []

        # hra neskončena
        self._running = True 
        self.size = self.width, self.height = App.B_WIDTH, App.B_HEIGHT
        self.speed = 8
        self.level = 1
        
        # inicializace PyGame modulů
        pygame.init()
        # nastavení velikosti okna, pokus o nastavení HW akcelerace, pokud nelze, použije se DOUBLEBUF
        self._running = True
        self._snake = Snake(self, 50)
        #App.play_music(self.level)

        
    def get_bodies(self):
        bodies = []
        for snake in self.snakes:
            bodies += snake._body
        return bodies

    def respawn_apple(self):
        while True:
            self.apple_position = [randrange(1,Snake.APPLE_MAX_POS-1)*Snake.DOT_SIZE,
                                    randrange(int(App.SCORE_SCREEN_HEIGHT/Snake.DOT_SIZE + 1), Snake.APPLE_MAX_POS-1)*Snake.DOT_SIZE]
            if self.apple_position not in self.get_bodies() and self.apple_position not in sum(Snake.OBSTACLES[:self.level-1],[]):
                break
    def on_input_focus(self):
        pass
    def on_key_down(self, event):
        if event.key == pygame.K_LEFT:
            self._snake.setMovement(Movement.LEFT)
        if event.key == pygame.K_RIGHT:
            self._snake.setMovement(Movement.RIGHT)
        if event.key == pygame.K_UP:
            self._snake.setMovement(Movement.UP)
        if event.key == pygame.K_DOWN:
            self._snake.setMovement(Movement.DOWN)          

    def on_event(self, event):
        if event.type == QUIT:
            self._running = False
        elif event.type == KEYDOWN:
            self.on_key_down(event)
    def game_over(self):
        pygame.mixer.music.stop()
        pygame.font.init()
        App._display_surf.fill((0, 0, 0))
        font = pygame.font.SysFont("Arial", 50)
        font2 = pygame.font.SysFont("Arial", 20)
        render = font.render("Game Over", 1, (255, 0, 0))
        render2 = font2.render("Score: {}".format(self._snake.getScore()), 1, (0, 255, 0))
        App._display_surf.blit(render, (self.B_WIDTH/2 - render.get_width()/2, self.B_WIDTH/2 - render.get_height()/2))
        App._display_surf.blit(render2, (self.B_WIDTH/2 - render2.get_width()/2, self.B_WIDTH/2 - render2.get_height()/2 + 35))
        pygame.display.flip()
        while True:
            for event in pygame.event.get():
                if event.type == KEYDOWN and event.key == pygame.K_SPACE:
                    self.on_cleanup()
                    
    def draw_score_screen(self):
        font = pygame.font.SysFont("Arial", 25 )
        render = font.render("Score: {}".format(self._snake.getScore()), 1, (255, 0, 0))
        App._display_surf.blit(render, (20, self.SCORE_SCREEN_HEIGHT/2 - render.get_height()/2))
        
        render = font.render("Speed: {}".format(self.speed), 1, (0, 255, 0))
        App._display_surf.blit(render, (100, self.SCORE_SCREEN_HEIGHT/2 - render.get_height()/2))
        
        render = font.render("Level: {}".format(self.level), 1, (0, 0, 255))
        App._display_surf.blit(render, (200, self.SCORE_SCREEN_HEIGHT/2 - render.get_height()/2))
        
    def on_loop(self):
        App._clock.tick(self.speed)
        self._snake.pohyb(self._snake._movement)
        self._snake.is_collided()
    def on_render(self):
            App._display_surf.fill((0, 0, 0))
            self.draw_score_screen()
            self._snake.draw(self._display_surf)
            pygame.draw.rect(self._display_surf, (255,0,0), pygame.Rect(
                0, App.SCORE_SCREEN_HEIGHT, App.B_WIDTH, App.B_HEIGHT-App.SCORE_SCREEN_HEIGHT), 10)
            pygame.display.flip()
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self, isObserver = False):
        # had
        if not isObserver:
            self._snake.init_snake()
        # game loop
        while self._snake._running:
            # zpracování všech typů událostí (netýká se serveru, resp. pozorovtele - observer)
            if not isObserver:
                for event in pygame.event.get():
                    self.on_event(event)
            self.on_loop()
            self.on_render()
        self.game_over()

 
if __name__ == "__main__" :
    theApp = None
    if len(sys.argv) > 1 and sys.argv[1] == "s":
        theApp = App()
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.bind((App.HOST, App.PORT))
            s.listen()
            conn, addr = s.accept()
            with conn:
                print(f"Connected by {addr}")
                while True:
                    data = pickle.dumps(theApp)
                    #data = conn.recv(1024)
                    #print(f"Received {data!r}")
                    conn.sendall(data)
        theApp.on_execute(True)
    else:
        with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
            s.connect((App.HOST, App.PORT))
            while True:
                #s.sendall(b"Hello, world")
                data = s.recv(1024)
                theApp = pickle.loads(data)
                break
                print(f"Received {data!r}")
    theApp.on_execute()
        