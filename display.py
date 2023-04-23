#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
    a module to draw and display a maze using pygame
"""

import pygame
from typing import Tuple

from stack import Stack
from queue import Queue

WHITE = (255, 255, 255)
RED = 255, 0, 0
WALL = 2

def draw_maze(screen, maze, size: Tuple[int, int]) -> None:
    """
        draw a maze from a tree sctructure
        
        parameters
        ----------
        screen
            the screen to draw on
        maze: Path
            the maze
        size: int
            size of a tile in pixels
            (size of the window divided by size of the maze)
        
        returns
        -------
        None
    """
    sizex, sizey = size
    x = maze.tile[0] * sizex + WALL//2
    y = maze.tile[1] * sizey + WALL//2
    #draw the tile
    pygame.draw.rect(
        screen,
        WHITE,
        pygame.Rect(x, y, sizex - WALL, sizey - WALL)
    )
    pygame.display.flip()
    
    #draw all sub-mazes
    if maze.paths != []:
        
        for sub_maze in maze.paths:
            pygame.draw.rect(
                screen,
                WHITE,
                pygame.Rect(
                    x + ((sizex - WALL) * (sub_maze.tile[0] - maze.tile[0])),
                    y + ((sizey - WALL) * (sub_maze.tile[1] - maze.tile[1])),
                    sizex - WALL,
                    sizey - WALL
                )
            )
            pygame.display.flip()
            draw_maze(screen, sub_maze, size)

def draw_maze_iter(screen, maze, size: Tuple[int, int], deadend=False) -> None:
    """
        draw a maze from a tree sctructure
        
        parameters
        ----------
        screen
            the screen to draw on
        maze: Path
            the maze
        size: int
            size of a tile in pixels
            (size of the window divided by size of the maze)
        deadend: bool
            enable the deadends (default False)
        
        returns
        -------
        None
    """
    sizex, sizey = size
    queue = Queue()
    queue.enqueue(maze)
    
    while not queue.is_empty():
        maze = queue.dequeue()
        
        x = maze.tile[0] * sizex + WALL//2
        y = maze.tile[1] * sizey + WALL//2
        #draw the tile
        pygame.draw.rect(
            screen,
            WHITE,
            pygame.Rect(x, y, sizex - WALL, sizey - WALL)
        )
        pygame.display.flip()
        
        # add all the submazes to the stack
        if maze.paths != []:
            
            for sub_maze in maze.paths:
                # draw the link
                pygame.draw.rect(
                    screen,
                    WHITE,
                    pygame.Rect(
                        x + ((sizex - WALL) * (sub_maze.tile[0] - maze.tile[0])),
                        y + ((sizey - WALL) * (sub_maze.tile[1] - maze.tile[1])),
                        sizex - WALL,
                        sizey - WALL
                    )
                )
                # add the maze to the stack
                queue.enqueue(sub_maze)
        elif deadend:
            pygame.draw.rect(
                screen,
                RED,
                pygame.Rect(x, y, sizex - WALL, sizey - WALL)
            )

