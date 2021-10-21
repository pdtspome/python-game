from random import randint
from colorama import init
from pyfiglet import Figlet
from termcolor import colored

init()

font = Figlet(font='standard')
welcome = colored(font.renderText(
    "TIC - TOC - TOE !"), color='white')

print(welcome)

board = ['*' for x in range(9)]

isWin = False
winner = ''
positions = []


def table():
    print(f" {board[0]} | {board[1]} | {board[2]} ")
    print("-----------")
    print(f" {board[3]} | {board[4]} | {board[5]} ")
    print("-----------")
    print(f" {board[6]} | {board[7]} | {board[8]} ")
    print("-----------")


def add_move(val, pos):
    pos -= 1
    board[pos] = val


def player_move():
    global board, positions

    pos = input('Position you wanna move: ')

    while int(pos) not in [1, 2, 3, 4, 5, 6, 7, 8, 9] or int(pos) in positions:
        pos = input("That position was chosen or invalid num, only (1 -> 9): ")

    pos = int(pos)
    positions.append(pos)
    add_move('X', pos)


def computer_move():
    global positions
    pos = randint(1, 9)

    while(pos in positions):
        pos = randint(1, 9)

    positions.append(pos)
    add_move('O', pos)


def isWinner(board):
    global isWin, winner
    # horizontally
    for cursor in range(0, 7, 3):
        if(board[cursor] == board[cursor + 1] == board[cursor + 2] != '*'):
            isWin = True
            winner = board[cursor]
    # vertically
    for cursor in range(3):
        if(board[cursor] == board[cursor + 3] == board[cursor + 6] != '*'):
            isWin = True
            winner = board[cursor]
    # diagnally
    if(board[0] == board[4] == board[8] != '*'):
        isWin = True
        winner = board[0]
    if(board[2] == board[4] == board[6] != '*'):
        isWin = True
        winner = board[2]


def display_winner():
    global winner
    if(winner == 'X'):
        return "Player"
    else:
        return "Computer"


first_move = input(
    "Computer or Player go first?\n(c/p) or (computer/player): ")
first_move = first_move[0].upper()

while not isWin:

    if(first_move == 'C'):
        computer_move()
        table()
        isWinner(board)
        if(winner):
            break
        player_move()
    elif(first_move == 'P'):
        table()
        player_move()
        isWinner(board)
        if (winner):
            break
        computer_move()
    isWinner(board)

table()

congrat = colored(font.renderText(
    f"{display_winner()} wins.\nCongrats !!!"), color='cyan')
print(congrat)
