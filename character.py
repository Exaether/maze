#!/usr/bin/env python
#-*- coding:utf-8 -*-

"""
    module to create a character and move it through a maze
"""

import pygame
from typing import Tuple


MOVES = {
    'right': (1, 0),
    'left': (-1, 0),
    'up': (0, -1),
    'down': (0, 1)
}

class Character:
    """
        character class
        modelize a little guy that can move in a maze
        
        attributes
        ----------
        x: int
            x pos of the character
        y: int
            y pos of the character
        
        methods
        -------
        goto(destination: tuple[int, int]) -> None:
            move the character to the given position
        move(board, direction) -> None:
            move the character to the given direction
        erase(screen) -> None:
            erase the character from the screen
        draw(screen) -> None:
            draw the character at its current position
    """
    
    def __init__(self, x: int, y: int,
            color: Tuple[int, int, int],
            size: int) -> None:
        """
            character's class constructor
            set up the attributes
            
            parameters
            ----------
            x: int
                starting x pos
            y: int
                starting y pos
            color: Tuple[int, int, int]
                the color of the character
            size: int
                the radius of the character circle
            
            returns
            -------
            None
        """
        self.x = x
        self.y = y
        self.color = color
        self.size = size
    
    def goto(self, destination: Tuple[int, int]) -> None:
        """
            move the character to the given position
            this is a teleportation and do not take in count 
            the walls of the maze
            
            parameters
            ----------
            destination: tuple[int, int]
                coordinates of the destination
            
            returns
            -------
            None
        """
        self.x = destination[0]
        self.y = destination[1]
        return None
    
    def move(self, board, direction) -> None:
        """
            move the character to the given direction
            do not move if there is a wall in the way
            
            parameters
            ----------
            board: Board
                the board the character is on
            direction: str
                right, left, up, or down
                the direction to move the character by
            
            returns
            -------
            None
        """
        movex, movey = MOVES[direction]
        #calculate the coordinates of the destination
        destination = (
            self.x + movex,
            self.y + movey
        )
        # test if the destiantion is accessible
        if destination in board[self.x, self.y].paths:
            # then move to it
            self.goto(destination)
        
        return None
    
    def erase(self, screen, tile):
        """
            erase the character from the screen
            
            parameters
            ----------
            screen
                the screen
            tile: Tuple[int, int]
                the size of a tile
            
            returns
            -------
            None
        """
        posx = self.x*tile[0] + tile[0]//2
        posy = self.y*tile[1] + tile[1]//2
        pos = (posx, posy)
        radius = self.size
        pygame.draw.circle(screen, (255, 255, 255), pos, radius)
    
    def draw(self, screen, tile):
        """
            draw the character at its currnet position
            
            parameters
            ----------
            screen
                the screen to draw on
            tile: Tuple[int, int]
                the size of a tile
            
            returns
            -------
            None
        """
        posx = self.x*tile[0] + tile[0]//2
        posy = self.y*tile[1] + tile[1]//2
        pos = (posx, posy)
        radius = self.size
        pygame.draw.circle(screen, self.color, pos, radius)

