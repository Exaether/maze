#!/usr/bin/env python
#-*- coding:utf-8 -*-

from random import choice
from typing import Tuple

from board import Path, Board
from stack import Stack

"""
    moteur permettant de generer un labyrinthe
"""


def gen(board: Board, start: Tuple[int, int]) -> Path:
    """
        permet de generer un labyrinthe
        a partir d'un tableau et une case de départ
        
        parametres
        ----------
        board: Board
            le tableau
        x: int
            coordonnée x de départ
        y: int
            coordonnée y de départ
        
        retours
        -------
        le chemin permettant de dessiner le labyrinthe
    """
    
    path = Path((start))  # create a new sub-maze
    board[start].visited = True
    
    while board.unvisited(*start) != ():
        # choose a random direction
        n = choice(board.unvisited(*start))
        
        # update the board
        board[start].paths.append((n.x, n.y))
        board[n.x, n.y].paths.append(start)
        
        # add the new sub-maze
        path.add_path(gen(board, (n.x, n.y)))
    
    return path


def gen_iter(board: Board, start: Tuple[int, int]) -> Path:
    """
        generate a maze in a given board
        and start at the given point
        
        parameters
        ----------
        board: Board
            the board to create the maze on
        start: Tuple[int, int]
            the starting tile
        
        returns
        -------
        ...: Path
            the completed maze's path
    """
    stack = Stack()
    board[start].visit()
    stack.push(Path(start))
    
    while not stack.is_empty():
        pos = stack.top().tile
        # test if there is an accessible path from here
        if board.unvisited(*pos) == ():
            # then if not, add the path to the previous
            tile = stack.pop()
            if not stack.is_empty():
                stack.top().add_path(tile)
        else:
            # if yes, choose a random path
            next = choice(board.unvisited(*pos))
            # mark it as visited
            board[next.pos()].visit()
            # update the board
            board[next.pos()].paths.append(pos)
            board[pos].paths.append(next.pos())
            # create a new path
            sub_path = Path(next.pos())
            # and add it to the stack
            stack.push(sub_path)
    return tile

