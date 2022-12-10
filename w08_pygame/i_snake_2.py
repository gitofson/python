# inspirace: https://zetcode.com/javagames/snake/

# Snake is an older classic video game. 
# It was first created in late 70s. Later it was brought to PCs. In this game the player controls a snake. 
# The objective is to eat as many apples as possible. Each time the snake eats an apple its body grows.
# The snake must avoid the walls and its own body. This game is sometimes called Nibbles.

# 1. pomocí 2 obdelníků rozdělte obrazovku na herní část a informační část (score, speed, level),
# 2. v informační části zobrazte aktuální score, speed a level,
# 3. po snědení N jablek zvyšte rychlost hry,
# 4. připravte další 2 úrovně hry v podobě zvyšujícího se počtu překážek (seznam seznamů seznamu bodů),
# 5. naprogramujte hru tak, aby s překážkami bylo v kolizích počítáno.
import pygame
from enum import Enum
from pygame.locals import *
from random import randrange
import time

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
        self._apple_position = []
        self._respawn_apple()
        # hlava hada
        self._image_head = None
        # stav. kámen hada
        self._image_body = None
        # jablko
        self._image_apple = None
        # Snake running
        self._running = True

    def init_snake(self):
        for z in range(Snake.N_DOTS):
            self._body.append([50 - z * Snake.DOT_SIZE, 50])
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
        if head == self._apple_position:
            self._body = [head] + self._body
            self._respawn_apple()
        else:
            self._body = [head] + self._body[:-1]
    def is_collided(self):
        # S koncem obrazovky
        if (self._body[0][0] == -Snake.DOT_SIZE
            or self._body[1][0] == App.B_WIDTH
            or self._body[0][1] == -Snake.DOT_SIZE
            or self._body[1][1] == App.B_HEIGHT
            or self._body[0] in self._body[1:]):
            self._running = False

    def _respawn_apple(self):
        while True:
            self._apple_position = [randrange(Snake.APPLE_MAX_POS)*Snake.DOT_SIZE,
                                    randrange(Snake.APPLE_MAX_POS)*Snake.DOT_SIZE]
            if self._apple_position not in self._body:
                break
    
    def draw(self, surface):
        #draw apple
        surface.blit(self._image_apple, self._apple_position)
        #draw snake
        surface.blit(self._image_head, self._body[0])
            
        for i in range(len(self._body) - 1):
            surface.blit(self._image_body, self._body[i + 1])

    def setMovement(self, movement):
        self._movement = movement
    
    def getScore(self):
        return len(self._body) - Snake.N_DOTS

class App:
    B_WIDTH  = 300
    B_HEIGHT = 300

    def __init__(self):
        # hra neskončena
        self._running = True 
        self._display_surf = None
        self._snake = Snake()
        self.size = self.width, self.height = App.B_WIDTH, App.B_HEIGHT
        self._clock = None
        self._level = 1
        self._levels = [None, 10, 20, 35, 55, 75, 90, 100]
        self._menu = True

        # inicializace PyGame modulů
        pygame.init()
        pygame.font.init()
        # nastavení velikosti okna, pokus o nastavení HW akcelerace, pokud nelze, použije se DOUBLEBUF
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._display_surf.fill((255, 255, 255))
        self._running = True
        self._clock = pygame.time.Clock()
    def on_input_focus(self):
        pass
    def UI(self):
        font = pygame.font.SysFont("Arial", 20)
        render = font.render(f"Skóre: {len(self._snake._body) - Snake.N_DOTS}    Level: {self._level}", 1, (0, 0, 0))
        self._display_surf.blit(render, (self.B_WIDTH/2 - render.get_width()/2, self.B_WIDTH - render.get_height() - 280))
    def menu(self):
        self._display_surf.fill((255, 255, 255))
        font = pygame.font.SysFont("Arial", 70)
        font2 = pygame.font.SysFont("Arial", 35)
        nazev = font.render("Snake", 1, (0, 0, 0))
        ukoncit = font2.render("Ukončit", 1, (0, 0, 0))
        render_levelu = [font2.render(f"Level {i}", 1, (0, 0, 0)) for i in range(1, 5)]
        self._display_surf.blit(nazev, (self.B_WIDTH/2 - nazev.get_width()/2, self.B_HEIGHT - nazev.get_height() - 220))
        for i in range(4):
            self._display_surf.blit(render_levelu[i], (self.B_WIDTH - render_levelu[i].get_width()/2 - (220 if i % 2 == 0 else 80), self.B_HEIGHT/4 - render_levelu[i].get_height()/2 + (35 if i <= 1 else 85)))
        self._display_surf.blit(ukoncit, (self.B_WIDTH/2 - ukoncit.get_width()/2, self.B_HEIGHT - ukoncit.get_height() - 50))
        pygame.display.flip()
    def on_key_down(self, event):
        if event.key == pygame.K_LEFT and self._snake._movement != Movement.RIGHT:
            self._snake._movement = Movement.LEFT
        if event.key == pygame.K_RIGHT and self._snake._movement != Movement.LEFT:
            self._snake._movement = Movement.RIGHT
        if event.key == pygame.K_UP and self._snake._movement != Movement.DOWN:
            self._snake._movement = Movement.UP
        if event.key == pygame.K_DOWN and self._snake._movement != Movement.UP:
            self._snake._movement = Movement.DOWN
    def on_event(self, event, mouse):
        if event.type == QUIT:
            self._running = False
        elif event.type == MOUSEBUTTONDOWN:
            if 25 <= mouse[0] <= 130 and 100 <= mouse[1] <= 120 and self._menu:
                self._menu = False
                self._snake.init_snake()
        elif event.type == KEYDOWN and not self._menu:
            self.on_key_down(event)
    def konec(self, text, skore):
        self._display_surf.fill((255, 255, 255))
        font = pygame.font.SysFont("Arial", 50)
        font2 = pygame.font.SysFont("Arial", 20)
        render = font.render(f"{text}", 1, (0, 0, 0))
        render2 = font2.render(f"Skóre: {skore}" if text == "PROHRA" else f" {self._level}. level dokončen!", 1, (0, 0, 0))
        self._display_surf.blit(render, (self.B_WIDTH/2 - render.get_width()/2, self.B_HEIGHT/2 - render.get_height()/2))
        self._display_surf.blit(render2, (self.B_WIDTH/2 - render2.get_width()/2, self.B_HEIGHT/2 - render2.get_height()/2 + 35))
        pygame.display.flip()
        time.sleep(5)
        self._menu = True
        start()
    def on_loop(self, skore):
        self._clock.tick(8)
        self._snake.pohyb(self._snake._movement)
        self._snake.is_collided()
        if skore == self._levels[self._level]:
            self.konec("VÝHRA", skore)
    def on_render(self):
            self._display_surf.fill((0, 0, 0))
            self._snake.draw(self._display_surf)
            self.UI()
            pygame.display.flip()
    def on_cleanup(self):
        pygame.quit()
 
    def on_execute(self):
        # game loop
        while self._snake._running:
            # zpracování všech typů událostí
            for event in pygame.event.get():
                mouse = pygame.mouse.get_pos()
                self.on_event(event, mouse)
            if not self._menu:
                skore = len(self._snake._body) - Snake.N_DOTS
                self.on_loop(skore)
                self.on_render()
            else:
                self.menu()
        if not self._menu:
            self.konec("PROHRA", skore)
        self.on_cleanup()
def start():
    theApp = App()
    theApp.on_execute()
if __name__ == "__main__":
    start()