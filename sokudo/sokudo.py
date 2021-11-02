from random import randint, shuffle
# '//' operator: floor division


def create_board():

    board = [[0 for col in range(9)] for row in range(9)]
    # challenge = input("Hard or easy? ")

    #generate board diagnally
    for box in range(0, 7, 3):
        ran_nums = [num for num in range(1,10)]
        shuffle(ran_nums)
        for row in range(box, box + 3):
            for col in range(box, box + 3):
                board[row][col] = ran_nums.pop()

    #finish whole board
    bot_solver(board)

    #remove a certain element
    for box_y in range(0, 7, 3):
        for box_x in range(0, 7, 3):
            ele_removed_each_box = randint(5,6)
            selected = []
            while ele_removed_each_box > 0:
                row = randint(box_y, box_y + 2)
                col = randint(box_x, box_x + 2)
                while [row,col] in selected:
                    row = randint(box_y, box_y + 2)
                    col = randint(box_x, box_x + 2)
                selected.append([row, col])
                board[row][col] = 0

                ele_removed_each_box -= 1
    return board


def display_board(board):
    for i in range(len(board)):
        if i % 3 == 0 and i != 0: 
            print("- - - - - - - - - - -")

        for j in range(len(board[i])):
            if j % 3 == 0 and j != 0:
                print(" | ", end="")
            if j == 8:
                print(board[i][j])
            elif j == 2 or j == 5:
                print(board[i][j] , end="")
            else:
                print(board[i][j] , end=" ")

# #////////////////////////////GAME/////////////////////////
def find_empty(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 0:
                return (i,j)
    return None

def check_valid(board, num, pos):
    #check horizontally
    for arrow in range(len(board)):
        if board[pos[0]][arrow] == num and arrow != pos[1]:
            return False
        
    #check vertically
        if board[arrow][pos[1]] == num and arrow != pos[0]:
            return False
   
    box_y = (pos[0] // 3)* 3
    box_x = (pos[1] // 3)* 3

    for i in range(box_y, box_y + 3):
        for j in range(box_x, box_x + 3):
            if board[i][j] == num and i != pos[0] and j != pos[1]:
                return False
    
    return True

def bot_solver(board):
    if not find_empty(board):
        return True # end recursion!
    else: 
        idx = find_empty(board)
        row, col = idx
    for num in range(1,10):
        if check_valid(board, num, idx):
            board[row][col] = num

            if bot_solver(board):
                return True #end backtracking

            board[row][col] = 0 # backtracking........
    # return False   

        
board = create_board()
display_board(board)

bot_solver(board)
print("_____________________")
display_board(board)
# # print(find_empty(board))
















# board = [
#     [0,0,0,0,0,0,6,0,9],
#     [1,0,0,0,0,4,0,0,0],
#     [0,0,5,3,0,6,8,2,1],
#     [0,0,4,6,7,0,0,5,0],
#     [0,0,7,0,0,0,9,0,0],
#     [0,0,0,5,4,0,0,0,0],
#     [3,7,0,4,0,5,2,0,6],
#     [0,0,0,0,0,0,5,1,0],
#     [0,6,0,0,2,0,0,3,7],
# ]