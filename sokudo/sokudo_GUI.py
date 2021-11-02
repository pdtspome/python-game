import pygame
import time

from sokudo_grid import Grid, Button

pygame.init()

def format_time(secs):
    sec = secs % 60
    minute = secs//60
    hour = minute//60

    return f"{str(minute)}: {str(sec)}"

def redraw_window(game, board, button, time, incorrects):
    game.fill((255,255,255))

    #draw time
    fnt = pygame.font.SysFont("calibri", 28)
    text = fnt.render("Time: " + format_time(time), 1, (0,0,0))
    game.blit(text, (540 - text.get_width() - 10, 560))

    #draw btn
    pos = pygame.mouse.get_pos()
    if button.isOver(pos):
        button = Button((200,200,200), 540/2 - 50, 600-60 + 15, 100, 30)
    button.draw(game)

    # Draw incorrects
    text = fnt.render("X " * incorrects, 1, (255,0,0))
    game.blit(text, (10, 560))

    #draw grid and board
    board.draw_board(game)

def main():
    WIDTH, HEIGHT = 543, 600
    game = pygame.display.set_mode((WIDTH,HEIGHT))
    board = Grid(9, 9, 540, 540)
    btn = Button((242,242,242), 540/2 - 50, 600-60 + 15, 100, 30)
    key = None
    running = True
    start = time.time() #returns cur time in secs
    incorrects = 0
    while running:
        play_time = round(time.time() - start)
        
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_1:
                    key = 1
                if event.key == pygame.K_2:
                    key = 2
                if event.key == pygame.K_3:
                    key = 3
                if event.key == pygame.K_4:
                    key = 4
                if event.key == pygame.K_5:
                    key = 5
                if event.key == pygame.K_6:
                    key = 6
                if event.key == pygame.K_7:
                    key = 7
                if event.key == pygame.K_8:
                    key = 8
                if event.key == pygame.K_9:
                    key = 9
                if event.key == pygame.K_BACKSPACE:
                    board.clear()
                    key = None
                if event.key == pygame.K_RETURN:
                    i, j = board.selected
                    if board.cubes[i][j].temp != 0:
                        if board.display_answer(board.cubes[i][j].temp):
                            print("Success!")
                        else:
                            print("Wrong answer!")
                            incorrects += 1
                        key = None
                        if board.is_finished():
                            print("Game over")
            
            if event.type == pygame.MOUSEBUTTONDOWN:
                pos = pygame.mouse.get_pos() #return (x-axis, y-axis)
                clicked = board.click(pos)
                if clicked:
                    board.select(clicked[0], clicked[1])
                    key = None

                if btn.isOver(pos):
                    board.solution(Grid.board)
                    print("ClickED")


            if board.selected and key != None:
                board.display_pre_answer(key)

            redraw_window(game, board, btn, play_time, incorrects)

        pygame.display.update()


if __name__ == "__main__":
    main()
pygame.quit()

