import pygame
from pygame.locals import *

from Constants import *
from Tools import *
from Buttons import *

class Entity(pygame.sprite.Sprite):
    def __init__(self, imageName, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = imageLoad(imageName)
        self.rect = self.image.get_rect()
        self.position = position
        self.rect.center = self.position
        
class Movable(Entity):
    keepMoving = False
    xPerTurn = 0
    xPerTurn = 0
        
    def setPosition(self, x, y):
        ''' Set the entity to an absolute position on
        the screen. '''
        
        self.position(x, y)
        self.rect.center = self.position
        
    def move(self, offsetX, offsetY):
        ''' Move the entity relative to its current
        position. '''
        
        x = self.position[0]
        y = self.position[1]
        x += offsetX
        y += offsetY
        self.position = (x, y)
        self.rect.center = self.position
        
    def startMoveContinuously(self, xPerTurn, yPerTurn):
        self.keepMoving = True
        self.xPerTurn = xPerTurn
        self.yPerTurn = yPerTurn
        
    def stopMoveContinuously(self):
        self.keepMoving = False
        
    def update(self):
        self.rect.center = self.position
        if self.keepMoving:
            self.move(self.xPerTurn, self.yPerTurn)
            
class Game:
    def __init__(self):
        pygame.init()
        self.screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
        #pygame.mouse.set_visible(0)
        self.clock = pygame.time.Clock()
        pygame.mixer.init()
        self.sounds = {}
        self.sprites = pygame.sprite.Group() 

    def displayMenu(self):
        #newSong('ftg.mp3')

        count = 0
        bgCount = 0

        baby = Movable('baby.png', (100, 400))
        drop = Movable('drop.png', (370, 510))
        self.sprites.add(baby)
        self.sprites.add(drop)
        bg = imageLoad('logoNoBabbs.png')

        start = StartButton('start.png', (200, 500), (baby, drop))
        self.sprites.add(start)
        buttons = [start]

        while True:
            self.clock.tick(MAX_FPS)
            self.screen.blit(bg, (0,0)) 
            self.sprites.draw(self.screen)

            pygame.display.flip()
            
            self.sprites.update()
            
            for event in pygame.event.get():
                if event.type == QUIT:
                    sys.exit(0)
                if event.type == MOUSEBUTTONDOWN:
                    if event.button == 1:
                        for button in buttons:
                            button.collide()

