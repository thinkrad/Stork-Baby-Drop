import pygame
import os
import sys

pygame.mixer.init()
root = sys.path[0]
data = root + '/data/'
sounds = {}

def imageLoad(name):
    image = pygame.image.load(data + name).convert()
    image = image.convert()
    return image
    
def playSong():
    pygame.mixer.music.play(-1)

def newSong(filename):
    pygame.mixer.music.load(data + filename)
    playSong()

def loadSound(filename, soundName):
    global sounds
    sounds[soundName] = pygame.mixer.Sound(filename)

def playSound(soundName):
    global sounds
    pygame.mixer.Sound.play(sounds[soundName])
