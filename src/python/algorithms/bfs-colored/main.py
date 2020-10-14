#! /usr/bin/env python

"""Implementation of BFS algorithm with colored map."""

import os

__author__ = "Pedro Arias Perez and Juan G. Victores"


LOCAL_PATH = os.path.dirname(os.path.abspath(__file__)).split("master-ipr")[0]
FILE_NAME = LOCAL_PATH + "master-ipr/map1/map1.csv"
START_X = 2
START_Y = 2
END_X = 7
END_Y = 2


class Colors:
    """
    ANSI color codes (source: https://en.wikipedia.org/wiki/ANSI_escape_code).
    """

    ESC = "\033"
    BLINK = "5"
    FG_BLACK = "30"
    FG_RED = "31"
    FG_GREEN = "32"
    FG_YELLOW = "33"
    FG_BLUE = "34"
    FG_MAGENTA = "35"
    FG_CYAN = "36"
    FG_WHITE = "37"
    BG_BLACK = "40"
    BG_RED = "41"
    BG_GREEN = "42"
    BG_YELLOW = "43"
    BG_BLUE = "44"
    BG_MAGENTA = "45"
    BG_CYAN = "46"
    BG_WHITE = "47"


class CharMapCell:
    """
    Wrapper for chars that allows formatting at printing.
    """

    RESET = Colors.ESC + "[0m"
    CURRENT = Colors.ESC + "[" + Colors.BLINK + ";" + Colors.BG_BLUE + "m"
    EMPTY = Colors.ESC + "[" + Colors.FG_WHITE + ";" + Colors.BG_WHITE + "m"
    WALL = Colors.ESC + "[" + Colors.FG_BLACK + ";" + Colors.BG_BLACK + "m"
    VISITED = Colors.ESC + "[" + Colors.FG_BLUE + ";" + Colors.BG_BLUE + "m"
    START = Colors.ESC + "[" + Colors.FG_GREEN + ";" + Colors.BG_GREEN + "m"
    END = Colors.ESC + "[" + Colors.FG_RED + ";" + Colors.BG_RED + "m"

    def __init__(self, c):
        self.c = str(c)

    def __eq__(self, o):
        if isinstance(o, CharMap):
            return self.c == o.c
        elif isinstance(o, int):
            return self.c == str(o)
        elif isinstance(o, str):
            return self.c == o
        else:
            return False

    def __add__(self, o):
        if isinstance(o, CharMap):
            return  str(self) + str(o)
        else:
            raise TypeError("invalid operation between", type(self), "and", type(o))

    def __str__(self):
        if self.c == "0":
            return self.EMPTY + self.c + self.RESET
        elif self.c  == "1":
            return self.WALL + self.c + self.RESET
        elif self.c == "2":
            return self.VISITED + self.c + self.RESET
        elif self.c == "3":
            return self.START + self.c + self.RESET
        elif self.c == "4":
            return self.END + self.c + self.RESET
        elif self.c == "5":
            return self.CURRENT + "X" + self.RESET
        else:
            return self.c


class CharMap:
    """
    A map that represents the C-Space.
    """

    def __init__(self, filename, start=None, end=None):
        self.charMap = []
        self.nodes = []

        self.read(filename)
        self.start = start
        self.end = end

    @property
    def start(self):
        return self.__start

    @start.setter
    def start(self, s):
        if s is not None:
            self.charMap[s[0]][s[1]] = CharMapCell(3)
            self.nodes.append(Node(s[0], s[1], 0, -2))
        self.__start = s

    @property
    def end(self):
        return self.__end

    @end.setter
    def end(self, e):
        if e is not None:
            self.charMap[e[0]][e[1]] = CharMapCell(4)
        self.__end = e

    def read(self, filename):
        """
        Reads map from file and save it at charMap attribute.

        filename: path to file.
        """

        with open(FILE_NAME) as f:
            line = f.readline()
            while line:
                charLine = line.strip().split(',')
                l = []
                for c in charLine:
                    l.append(CharMapCell(c))
                self.charMap.append(l)
                line = f.readline()

    def dump(self):
        """
        Prints colored map.
        """

        for line in self.charMap:
            l = ""
            for char in line:
                l += str(char)
            print(l)
        print()  # empty line behind map

    def check(self, cell, node):
        """
        Check if cell is end or not visited and add it to tree nodes.

        cell: current cell
        node: parent node

        return: parent id if end else -1
        """

        if( self.charMap[cell[0]][cell[1]] == '4' ):  # end
            return node.myId
        elif ( self.charMap[cell[0]][cell[1]] == '0' ):  # empty
            newNode = Node(cell[0], cell[1], len(self.nodes), node.myId)
            self.charMap[cell[0]][cell[1]] = CharMapCell(2)
            self.nodes.append(newNode)
        return -1


class Node:
    """
    Node: visited cell of the map.
    """

    def __init__(self, x, y, myId, parentId):
        self.x = x
        self.y = y
        self.myId = myId
        self.parentId = parentId

    def dump(self):
        print("---------- x", str(self.x), "| y", str(self.y), "| id",\
              str(self.myId), "| parentId", str(self.parentId))


def main():
    map = CharMap(FILE_NAME, [START_X, START_Y], [END_X, END_Y])

    map.dump()

    done = False
    goalParentId = -1
    while not done:
        print("--------------------- number of nodes: ", len(map.nodes))
        for node in map.nodes:
            node.dump()

            old = map.charMap[node.x][node.y]
            map.charMap[node.x][node.y] = CharMapCell(5)

            # up
            tmpX = node.x - 1
            tmpY = node.y
            if map.check([tmpX, tmpY], node) != -1:
                map.dump()
                done = True
                goalParentId = node.myId
                break

            # down
            tmpX = node.x + 1
            tmpY = node.y
            if map.check([tmpX, tmpY], node) != -1:
                map.dump()
                done = True
                goalParentId = node.myId
                break

            # right
            tmpX = node.x
            tmpY = node.y + 1
            if map.check([tmpX, tmpY], node) != -1:
                map.dump()
                done = True
                goalParentId = node.myId
                break

            # left
            tmpX = node.x
            tmpY = node.y - 1
            if map.check([tmpX, tmpY], node) != -1:
                map.dump()
                done = True
                goalParentId = node.myId
                break

            map.dump()
            if old == 0:
                map.charMap[node.x][node.y] = CharMapCell(2)
            else:
                map.charMap[node.x][node.y] = old


    print("%%%%%%%%%%%%%%%%%%%")
    ok = False
    while not ok:
        for node in map.nodes:
            if( node.myId == goalParentId ):
                node.dump()
                goalParentId = node.parentId
                if( goalParentId == -2):
                    print("%%%%%%%%%%%%%%%%%")
                    ok = True

if __name__ == "__main__":
    main()
