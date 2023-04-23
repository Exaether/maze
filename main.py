#!/usr/bin/env python
#-*- coding:utf-8 -*-

import pygame
import sys
from random import randint

from display import draw_maze, draw_maze_iter
from gen import gen, gen_iter
from board import Board
from character import Character

BLACK = 0, 0, 0
RED = 255, 0, 0

pygame.init()

size = width, height = 1800, 1000
size_tile = sizex, sizey = 50, 50
deadend = False
board = Board(width//sizex, height//sizey)

screen = pygame.display.set_mode(size)

running = True
while running:
    for event in pygame.event.get():
        match event.type:
            case pygame.QUIT:
                running = False
            case pygame.KEYDOWN:
                match event.key:
                    case pygame.K_SPACE:
                        screen.fill(BLACK)
                        board.clear()
                        pos = (
                            randint(0, width//sizex - 1),
                            randint(0, height//sizey - 1)
                        )
                        player = Character(*pos, RED, sizex//2 - 4)
                        path = gen_iter(board, pos)
                        draw_maze_iter(screen, path, size_tile, deadend)
                        player.draw(screen, size_tile)
                    case pygame.K_z:
                        player.erase(screen, size_tile)
                        player.move(board, "up")
                        player.draw(screen, size_tile)
                    case pygame.K_q:
                        player.erase(screen, size_tile)
                        player.move(board, "left")
                        player.draw(screen, size_tile)
                    case pygame.K_s:
                        player.erase(screen, size_tile)
                        player.move(board, "down")
                        player.draw(screen, size_tile)
                    case pygame.K_d:
                        player.erase(screen, size_tile)
                        player.move(board, "right")
                        player.draw(screen, size_tile)
    pygame.display.flip()

sys.exit()

