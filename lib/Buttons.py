import pygame
import sys

from Tools import *

class Button(pygame.sprite.Sprite):
    ''' Base class for creating buttons. Should not be used
    directly. executeCommand should be overridden by subclasses. '''

    def __init__(self, image, position):
        pygame.sprite.Sprite.__init__(self)
        self.image = imageLoad(image)
        self.rect = self.image.get_rect()
        self.position = position
        self.rect.center = self.position
        self.clickable = True
        
    def toggleClickability(self):
        if self.clickable == True:
            self.clickable = False
        else:
            self.clickable = True

    def collide(self):
        if self.rect.collidepoint(pygame.mouse.get_pos()) and self.clickable == True:
            self.executeCommand()

    def executeCommand(self, args):
        pass

class StartButton(Button):
    def __init__(self, image, position, sprites):
        ''' The args should be a list of sprites that 
        the startButton affects.'''
        
        Button.__init__(self, image, position)
        loadSound('data/lets_drop_some.ogg', 'lets_drop')
        self.sprites = sprites

    def executeCommand(self):
        playSound('lets_drop')
        
        for sprite in self.sprites:
            sprite.startMoveContinuously(0, 10)
            
        self.toggleClickability()


    
