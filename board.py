#!/usr/bin/env python
# -*- coding:utf-8 -*-

"""
    module for tiles and a board that contain tiles
"""

from typing import List, Tuple


class Tile:
    """
        a tile of a maze
        
        attributes
        ----------
        x : int
            the x coordinate
        y : int
            the y coordinate
        paths : list
            coordinates of accessibles neighbors
        visited : bool
            the state of the tile (unvisited or visited)
        
        methods
        -------
        visit() -> None:
            mark the tile as visited
        pos() -> Tuple[int, int]:
            the pos of the tile
    """
    
    def __init__(self, x: int, y: int) -> None:
        """
            Tile class' constructor
            
            parameters
            ----------
            None
            
            returns
            -------
            None
        """
        self.x = x
        self.y = y
        self.paths = list()
        self.visited = False
    
    def visit(self) -> None:
        """
            mark the tile as visited
            
            parameters
            ----------
            None
            
            returns
            -------
            None
        """
        self.visited = True
    
    def pos(self) -> Tuple[int, int]:
        """
            get the pos of the tile as a tuple
            
            parameters
            ----------
            None
            
            returns
            -------
            Tuple[int, int]
                the pos
        """
        return (self.x, self.y)


class Board:
    """
        a board that contain cells
        
        attributes
        ----------
        grid: list[list[Tile]]
            the grid that contain tiles
        
        methods
        -------
        neighborhood(x: int, y: int) -> tuple
            find the direct neighbors of a tile
        unvisited(x: int, y: int) -> tuple
            find the unvisited neighbors of a tile
    """
    
    def __init__(self, width: int, height: int) -> None:
        """
            Board class' constructor
            
            parameters
            ----------
            width : int
                the width of the board
            height : int
                the height of the board
        """
        self.grid: List[List[Tile]] = [
            [
                Tile(x, y) for x in range(width)
            ]
            for y in range(height)
        ]
        self.width = width
        self.height = height
    
    def __getitem__(self, value: Tuple[int, int]) -> Tile:
        """
            allows to pick tiles using index
            
            parameters
            ----------
            value : (int, int)
                the coordinates of the tile
            
            returns
            -------
            list
                the row at the index
        """
        return self.grid[value[1]][value[0]]
    
    def __iter__(self):
        """
            allows to iterate the board to pick each tile one by one
            pick tiles horizontally, the vertically
            
            parameters
            ----------
            None
            
            returns
            -------
            Tile
                each tile one at a time
        """
        for row in self.grid:
            for tile in row:
                yield tile

    def clear(self):
        """
            clear the board by setting all the tiles as unvisited

            parameters
            ----------
            None

            returns
            -------
            None
        """
        for tile in self:
            tile.visited = False
    
    def neighborhood(self, x: int, y: int) -> tuple:
        """
            find the directs neighbors of a tile
            
            parameters
            ----------
            x: int
                x coordinate of the tile
            y: int
                y coordinate of the tile
            
            returns
            -------
            tuple
                the neighbors
        """
        result = list()
        for xadd in (1, -1):
            if (x+xadd >= 0) and (x+xadd < self.width):
                result.append(self.grid[y][x+xadd])
        for yadd in (1, -1):
            if (y+yadd >= 0) and (y+yadd < self.height):
                result.append(self.grid[y+yadd][x])
        return tuple(result)
    
    def unvisited(self, x: int, y: int) -> tuple:
        """
            find unvisited neighbors of a tile
            
            parameters
            ----------
            x: int
                x coordinate of the tile
            y: int
                y coordinate of the tile
            
            returns
            -------
            tuple
                the unvisited neighbors
        """
        result = list()
        for tile in self.neighborhood(x, y):
            if not tile.visited:
                result.append(tile)
        return tuple(result)


class Path:
    """
        represent a path across a maze using a tree structure
        
        attributes
        ----------
        cell : tuple(int, int)
            coordinates of the current tile
        paths: list
            all accessible tiles
        
        methods
        -------
        add_path(path: Path) -> None
            add a new sub-path
    """
    
    def __init__(self, tile: Tuple[int, int]) -> None:
        """
            constructor of the Path class
            
            parameters
            ----------
            tile: tuple(int, int)
                the coordinates stored at the Node
            paths: list
                list of all paths starting at this tile
            
            returns
            -------
            None
        """
        self.tile = tile
        self.paths = list()
    
    def add_path(self, path) -> None:
        """
            function to add a new sub-path to a path
            
            parameters
            ----------
            path: Path
                the sub-path to add
            
            returns
            -------
            None
        """
        self.paths.append(path)

