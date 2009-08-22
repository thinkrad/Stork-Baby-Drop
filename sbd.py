#!/usr/bin/env python

import sys

root = sys.path[0]
sys.path.append('%s/lib' %root)

from Game import *

if __name__ == '__main__':
    game = Game()
    game.displayMenu()
