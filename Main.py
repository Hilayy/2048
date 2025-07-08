import copy
import random
import os


class Block:
    def __init__(self, position, value=(2 if random.randint(1, 10) < 10 else 4)):
        self.value = value
        self.position = position


class Board:
    def __init__(self):
        self.board = [[None for _ in range(4)] for _ in range(4)]
        self.create_block()



    def create_block(self):
        pos = random.choice(self.empty_tiles())
        block = Block(pos)
        self.board[pos[0]][pos[1]] = block

    def empty_tiles(self):
        empty = []
        for i in range(4):
            for j in range(4):
                if self.board[i][j] is None:
                    empty.append([i, j])
        return empty

    def make_move(self):
        direction = 'x'
        if direction.lower() not in 'wasd':
            direction = input()

        if direction == 'w':
            for i in range(4):
                for j in range(4):
                    if isinstance(self.board[i][j], Block):
                        last = [i, j]
                        while True and last[0] > 0:
                            if isinstance(self.board[last[0] - 1][last[1]], Block):
                                break
                            last[0] -= 1
                        pos = last
                        print(pos)
                        self.move_block([i, j], last)


    def move_block(self, current, new):
        x = copy.deepcopy(self.board[current[0]][current[1]])
        x.pos = [new[0], new[1]]
        self.board[current[0]][current[1]] = None
        self.board[new[0]][new[1]] = x
        self.print_board()











    def print_board(self):
        print("-------------")
        for i in self.board:
            s = ""
            for j in i:
                if isinstance(j, Block):
                    s += str(j.value)
                else:
                    s += " "
                s += ' |'
            print('|' + s)
        print("-------------")


b = Board()
b.print_board()
b.make_move()
