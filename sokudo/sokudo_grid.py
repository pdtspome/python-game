import pygame
from pygame.draw import line, rect

from sokudo_cube import Cube
from sokudo import bot_solver, check_valid, create_board, find_empty

class Grid:
    board = create_board()

    def __init__(self, rows, cols, width, height):
        self.rows = rows
        self.cols = cols

        self.cubes = [[Cube(self.board[row][col], row, col, width, height) for col in range(cols)] for row in range(rows)]

        self.width = width
        self.height = height
        self.board = None
        self.selected = None

    def update_board(self):
        self.board = [[self.cubes[row][col].value for col in range(self.cols)] for row in range(self.rows)]

    def solution(self, board):
        if not find_empty(board):
            return True
        else:
            row, col = find_empty(board)
        for num in range(1,10):
            if check_valid(board, num, (row,col)):
                board[row][col] = num
                self.cubes[row][col].set_val(num)
                self.update_board()
                # time.sleep(0.02)
                if self.solution(board):
                    return True
                
                board[row][col] = 0
                self.cubes[row][col].set_val(0)
                self.cubes[row][col].set_temp(0)
                self.update_board()
                

    def display_answer(self, val):
        row, col = self.selected
        if self.cubes[row][col].value == 0:
            self.cubes[row][col].set_val(val)
            self.update_board()

            if check_valid(self.board, val, (row,col)) and bot_solver(self.board):
                return True
            
            else:
                self.cubes[row][col].set_val(0)
                self.cubes[row][col].set_temp(0)
                self.update_board()
                return False
    
    def display_pre_answer(self, val):
        row, col = self.selected
        self.cubes[row][col].set_temp(val)

    def draw_board(self, game):
        # Draw Grid lines
        #(96,96,96)
        gap = self.width / 9
        for i in range(self.rows + 1):
            if i % 3 == 0:
                thick = 4
            else:
                thick = 1
            line(game, (64,64,64), (0, i * gap), (self.width, i * gap), thick) # draw line horizontally

            line(game, (64,64,64), (i * gap, 0), (i * gap, self.height), thick) # draw line vertically

        # Draw Cubes
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].draw_value(game)

    def select(self, row, col):
        # Reset all other
        for i in range(self.rows):
            for j in range(self.cols):
                self.cubes[i][j].selected = False

        self.cubes[row][col].selected = True
        self.selected = (row, col)

    def clear(self):
        row, col = self.selected
        if self.cubes[row][col].value == 0:
            self.cubes[row][col].set_temp(0)

    def click(self, pos):
        # Should return indexes of the board
        if pos[0] < self.width and pos[1] < self.height:
            gap = self.width / 9
            x = pos[0] // gap
            y = pos[1] // gap
            return (int(y), int(x))

        else:
            return None

    def is_finished(self):
        for i in range(self.rows):
            for j in range(self.cols):
                if self.cubes[i][j].value == 0:
                    return False
        return True


class Button:
    def __init__(self, color, x,y, width, height, text="SOLUTION"):
        self.color = color
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.text = text
    
    def draw(self, game):
        rect(game, self.color, (self.x, self.y, self.width, self.height), 0)

        font = pygame.font.SysFont('calibri', 15)
        text = font.render(self.text, 1, (32,32,32))
        game.blit(text, (self.x + (self.width/2 - text.get_width()/2), self.y +(self.height/2 -text.get_height()/2)))

    def isOver(self, pos):
        #Pos is the mouse position or a tuple of (x,y) coordinates
        if pos[0] > self.x and pos[0] < self.x + self.width:
            if pos[1] > self.y and pos[1] < self.y + self.height:
                return True
            
        return False