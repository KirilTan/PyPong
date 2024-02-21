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

# Movement variables
player_direction = 0
player_speed = 5

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

    # Game loop logic
    for event in pygame.event.get():

        # Pressing the close button closes the game
        if event.type == pygame.QUIT:
            running = False

        # Y axis movement
        if event.type == pygame.KEYDOWN:  # The player presses a key

            if event.key == pygame.K_w:   # The player pressed 'W' -> Go up
                player_direction = -5

            if event.key == pygame.K_s:   # The player pressed 'S' -> Go down
                player_direction = 5

        if event.type == pygame.KEYUP:   # The player releases a key

            if event.key == pygame.K_w or event.key == pygame.K_s:   # The player released 'W' or 'S'
                player_direction = 0

        # Place the player on the new location
        player_y += player_speed * player_direction






    pygame.display.flip()  # Update the screen

pygame.quit()  # Close the pygame
