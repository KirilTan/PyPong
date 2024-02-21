import pygame  # Import the pygame module

pygame.init()  # Initialize the pygame module

# Make the screen
screen = pygame.display.set_mode((600, 600))
pygame.display.set_caption("PyPong")

# Timer and fps variables
timer = pygame.time.Clock()
framerate = 60

# Library of colours
colours = {
    'black': (0, 0, 0),
    'white': (255, 255, 255),
    'red': (255, 0, 0),
}

# Player location variables
player_y = 150
opponent_y = 150

# Ball location variables
ball_x = 300
ball_y = 300

# Start the game loop
running = True
while running:

    timer.tick(framerate)  # Set the framerate
    screen.fill(colours['black'])  # Fill the screen with a colour

    # Create the players
    player = pygame.draw.rect(screen, colours['white'], [10, player_y, 10, 100])
    opponent = pygame.draw.rect(screen, colours['white'], [580, opponent_y, 10, 100])

    # Create the ball
    ball = pygame.draw.rect(screen, colours['white'], [ball_x, ball_y, 15, 15])

    # Exiting the game loop logic
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    pygame.display.flip()  # Update the screen

pygame.quit()  # Close the pygame
