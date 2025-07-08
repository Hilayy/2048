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
        self.score = 0

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

    def immediate_merge(self):
        for i in range(4):
            for j in range(4):
                vs = self.immediate_tiles_values([i, j])
                if self.board[i][j].value in vs:
                    return True
        return False


    def immediate_tiles_values(self, t):
        vs = []
        if t[0] < 3:
            vs.append(self.board[t[0] + 1][t[1]].value)
        if t[0] > 0:
            vs.append(self.board[t[0] - 1][t[1]].value)
        if t[1] < 3:
            vs.append(self.board[t[0]][t[1] + 1].value)
        if t[1] > 0:
            vs.append(self.board[t[0]][t[1] - 1].value)
        return vs

    def make_move(self):
        has_moved = False
        while has_moved is False:
            direction = 'x'
            if direction.lower() not in 'wasd':
                direction = input()

            if direction == 'w':  # upward
                for i in range(4):
                    for j in range(4):
                        if isinstance(self.board[i][j], Block):
                            last = [i, j]
                            while True and last[0] > 0:
                                if isinstance(self.board[last[0] - 1][last[1]], Block):
                                    if self.board[i][j].value == self.board[last[0] - 1][last[1]].value:
                                        self.merge_blocks([i, j], [last[0] - 1, last[1]])
                                        has_moved = True
                                        last = None
                                    break
                                last[0] -= 1

                            if last:
                                if last != [i, j]:
                                    self.move_block([i, j], last)
                                    has_moved = True

            if direction == 's':  # downward
                for i in range(3, -1, -1):
                    for j in range(4):
                        if isinstance(self.board[i][j], Block):
                            last = [i, j]
                            while True and last[0] < 3:
                                if isinstance(self.board[last[0] + 1][last[1]], Block):
                                    if self.board[i][j].value == self.board[last[0] + 1][last[1]].value:
                                        self.merge_blocks([i, j], [last[0] + 1, last[1]])
                                        last = None
                                        has_moved = True
                                    break
                                last[0] += 1

                            if last:
                                if last != [i, j]:
                                    self.move_block([i, j], last)
                                    has_moved = True

            if direction == 'a':  # left
                for j in range(4):
                    for i in range(4):
                        if isinstance(self.board[i][j], Block):
                            last = [i, j]
                            while True and last[1] > 0:
                                if isinstance(self.board[last[0]][last[1] - 1], Block):
                                    if self.board[i][j].value == self.board[last[0]][last[1] - 1].value:
                                        self.merge_blocks([i, j], [last[0], last[1] - 1])
                                        last = None
                                        has_moved = True
                                    break
                                last[1] -= 1

                            if last:
                                if last != [i, j]:
                                    self.move_block([i, j], last)
                                    has_moved = True

            if direction == 'd':  # right
                for j in range(3, -1, -1):
                    for i in range(4):
                        if isinstance(self.board[i][j], Block):
                            last = [i, j]
                            while True and last[1] < 3:
                                if isinstance(self.board[last[0]][last[1] + 1], Block):
                                    if self.board[i][j].value == self.board[last[0]][last[1] + 1].value:
                                        self.merge_blocks([i, j], [last[0], last[1] + 1])
                                        last = None
                                        has_moved = True
                                    break
                                last[1] += 1

                            if last:
                                if last != [i, j]:
                                    self.move_block([i, j], last)
                                    has_moved = True

            if has_moved is False:
                print("no tiles can move in this direction, choose another move")

    def move_block(self, current, new):
        x = copy.deepcopy(self.board[current[0]][current[1]])
        x.pos = [new[0], new[1]]
        self.board[current[0]][current[1]] = None
        self.board[new[0]][new[1]] = x

    def merge_blocks(self, t1, t2):
        self.board[t2[0]][t2[1]].value *= 2
        self.board[t1[0]][t1[1]] = None
        self.score += self.board[t2[0]][t2[1]].value

    def cant_continue(self):
        return self.empty_tiles() == [] and self.immediate_merge() is False

    def check_won(self):
        for i in range(4):
            for j in range(4):
                if isinstance(self.board[i][j], Block):
                    if self.board[i][j].value == 2048:
                      return True
        return False
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

    def announce_score(self):
        print(f"score:{self.score}")


def game():
    res = None
    b = Board()
    while True:
        b.announce_score()
        b.print_board()
        b.make_move()
        b.create_block()
        b.print_board()
        if b.cant_continue():
            res = 0
            break
        if b.check_won():
            res = 1
            break
    if res == 1:
        print("Congratulations! You Won!")
    if res == 0:
        print("You Lost :(")




game()
