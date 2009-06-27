import pygame
from pygame.locals import *

from Constants import *
from Tools import *

class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        pygame.mouse.set_visible(0)
        self.clock = pygame.time.Clock()
        pygame.mixer.init()

    def displayMenu(self):
        newSong('ftg.mp3')

        count = 0
        bgCount = 0

        bg = imageLoad('logo%i.png' %bgCount)

        while True:
            count += 1
            if count == 30:
                count = 0
                bg = imageLoad('logo%i.png' %bgCount)
                bgCount += 1
                if bgCount > 6:
                    count = 500
                    bgCount = 0

            self.screen.blit(bg, (0,0)) 

            pygame.display.flip()
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit(0)

