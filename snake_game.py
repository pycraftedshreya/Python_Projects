import pygame 
import time
import random

# to start the pygame :
pygame.init()

# hex color  :
red = (255,0,0)
blue = (51,153,255)
grey = (192,192,192)
green = (51,102,0)

# to give the box , windows of game  :
win_width = 600
win_height = 400

# to display the output : 
window = pygame.display.set_mode((win_width,win_height))

# title of game  :
pygame.display.set_caption("Snake Game")

# 5 min mate screen rese : 
time.sleep(5)

# snake : 
snake = 10
snake_speed = 15

# it display all fonts provide my pygame :
# fonts = pygame.font.get_fonts()
# print(fonts)     

font_style = pygame.font.SysFont("calibri",26)
score_font = pygame.font.SysFont('comicsansms',30)

def user_score(score):
    number = score_font.render("Score :",score,True,red)
    window.blit(number,[0,0])

def game_snake():
    pass

def message(msg):
    msg = font_style.render(msg,True,red)
    # display :
    window.blit(msg,[win_width/6,win_height/3])

def game_loop():
    gameOver = False
    gameClose = False    #game continue

# snake Positon :
    x1 = win_width/2
    y1 = win_height/2

# length of Snake  :
    x1_change = 0
    y1_change = 0

# increase the length of snake when it start eat : 
    snake_length_list = []
    snake_length = 1

    foodx = round(random.randrange(0,win_width - snake)/10.0) * 10.0 
    foody = round(random.randrange(0,win_height - snake)/10.0) * 10.0 

    while not gameOver : 
        while gameClose == True :
            window.fill(grey)
            message("Oh no ! press P to play again & press Q to quit  ")          