import pygame  # Import the pygame module
import sys  # Import the sys module


def close_game():
    """
    This function closes the game.

    """
    pygame.quit()  #
    sys.exit()


def update_ai(ball_location: int, opponent_location: int) -> int:
    """
    This function updates the location of the opponent based on the location of the ball and the size of the opponent.

    Parameters:
        ball_location (int): The current location of the ball
        opponent_location (int): The current location of the opponent

    Returns:
        int: The updated location of the opponent

    """
    if opponent_location + (opponent_size / 2) > ball_y + (ball_size / 2):  # Opponent is bellow the ball
        opponent_location -= opponent_speed  # Opponent goes up

    elif opponent_location + (opponent_size / 2) < ball_y + (ball_size / 2):  # Opponent is above the ball
        opponent_location += opponent_speed  # Opponent goes down

    return opponent_location  # Return the updated location of the opponent


# Game screen dimensions
screen_width = 600
screen_height = 600
screen_dimensions = (screen_width, screen_height)

# Library of colours
colours = {
    'black': (0, 0, 0),
    'white': (255, 255, 255),
    'red': (255, 0, 0),
}

# Timer and fps variables
timer = pygame.time.Clock()
framerate = 120

# Player, opponent, and ball size variables
player_size = opponent_size = 100
ball_size = player_size / 10

# Player location variables
player_y = 150
opponent_y = 150

# Ball location variables
ball_x = 300
ball_y = 300

# Movement variables
player_direction = 0
player_speed = 5
opponent_speed = player_speed - 2  # Slower than the player so that the player has an advantage
