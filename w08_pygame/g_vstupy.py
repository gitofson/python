import pygame
from pygame.locals import *
 
class App:
    def __init__(self):
        self._running = True
        self._display_surf = None
        self._image_surf = None
        self.size = self.weight, self.height = 640, 400
        self._display_surf = None
        self._star_position_x = 0
        self._star_position_y = 0
 
    def on_init(self):
        # inicializace PyGame modulů
        pygame.init()   
        # nastavení velikosti okna, pokus o nastavení HW akcelerace, pokud nelze, použije se DOUBLEBUF
        self._display_surf = pygame.display.set_mode(self.size, pygame.HWSURFACE | pygame.DOUBLEBUF)
        self._running = True
        # načtení obrázku
        self._image_surf = pygame.image.load("../resources/star.png").convert()
    def on_input_focus(self):
        pass
    def on_input_blur(self):
        pass
    def on_key_down(self, event):
        print("key down...")
        print(event)
        if event.key == pygame.K_LEFT:
            self._star_position_x -= 1
        if event.key == pygame.K_RIGHT:
            self._star_position_x += 1
    def on_key_up(self, event):
        pass
    def on_mouse_focus(self):
        pass
    def on_mouse_blur(self):
        pass
    def on_mouse_move(self, event):
        pass
    def on_mouse_wheel(self, event):
        pass
    def on_lbutton_up(self, event):
        pass
    def on_lbutton_down(self, event):
        pass
    def on_rbutton_up(self, event):
        pass
    def on_rbutton_down(self, event):
        pass
    def on_mbutton_up(self, event):
        pass
    def on_mbutton_down(self, event):
        pass
    def on_minimize(self):
        pass
    def on_restore(self):
        pass
    def on_resize(self,event):
        pass
    def on_expose(self):
        pass
    def on_exit(self):
        pass
    def on_user(self,event):
        pass
    def on_joy_axis(self,event):
        pass
    def on_joybutton_up(self,event):
        pass
    def on_joybutton_down(self,event):
        pass
    def on_joy_hat(self,event):
        pass
    def on_joy_ball(self,event):
        pass
    def on_event(self, event):
        if event.type == QUIT:
            self._running = False
            #self.on_exit()
 
        elif event.type >= USEREVENT:
            self.on_user(event)
 
        elif event.type == VIDEOEXPOSE:
            self.on_expose()
 
        elif event.type == VIDEORESIZE:
            self.on_resize(event)
 
        elif event.type == KEYUP:
            self.on_key_up(event)
 
        elif event.type == KEYDOWN:
            self.on_key_down(event)
 
        elif event.type == MOUSEMOTION:
            self.on_mouse_move(event)
 
        elif event.type == MOUSEBUTTONUP:
            if event.button == 0:
                self.on_lbutton_up(event)
            elif event.button == 1:
                self.on_mbutton_up(event)
            elif event.button == 2:
                self.on_rbutton_up(event)
 
        elif event.type == MOUSEBUTTONDOWN:
            if event.button == 0:
                self.on_lbutton_down(event)
            elif event.button == 1:
                self.on_mbutton_down(event)
            elif event.button == 2:
                self.on_rbutton_down(event)
 
        elif event.type == ACTIVEEVENT:
            if event.state == 1:
                if event.gain:
                    self.on_mouse_focus()
                else:
                    self.on_mouse_blur()
            elif event.state == 2:
                if event.gain:
                    self.on_input_focus()
                else:
                    self.on_input_blur()
            elif event.state == 4:
                if event.gain:
                    self.on_restore()
                else:
                    self.on_minimize()

    def on_loop(self):
        pass
    def on_render(self):
            self._display_surf.blit(self._image_surf,(self._star_position_x, self._star_position_y))
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