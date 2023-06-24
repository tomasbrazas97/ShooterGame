import pygame as pg
import sys
from settings import *
from map import *

class Game:
    #methods
    def __init__(self):
        pg.init()
        self.screen = pg.display.set_mode(RES) #screen for resolution
        self.clock = pg.time.Clock()
        self.new_game()

    def new_game(self):
       self.map = Map(self)

    def update(self): #update screen and display current frames in window caption
        pg.display.flip()
        self.clock.tick(FPS)
        pg.display.set_caption(f'{self.clock.get_fps() :.1f}')

    def draw(self): #each iteration paint screen black
        self.screen.fill('black')
        self.map.draw()

    def check_events(self): #Check if user presses closes window or presses esc
        for event in pg.event.get():
            if event.type == pg.QUIT or (event.type == pg.KEYDOWN and event.key == pg.K_ESCAPE):
                pg.quit()
                sys.exit()

    def run(self): # main loop of the game
        while True:
            self.check_events()
            self.update()
            self.draw()

if __name__ == '__main__': #instance of game
    game = Game()
    game.run()    
    