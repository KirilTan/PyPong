import pygame

# Library of colours
colours = {
    'black': (0, 0, 0),
    'white': (255, 255, 255),
    'red': (255, 0, 0),
}

# Timer and fps variables
timer = pygame.time.Clock()
framerate = 120

# Player location variables
player_y = 150
opponent_y = 150

# Ball location variables
ball_x = 300
ball_y = 300

# Movement variables
player_direction = 0
player_speed = 5

