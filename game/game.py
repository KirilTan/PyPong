from core import *  # Import the core module ('*' is a bad practice but here it works)

if __name__ == "__main__":  # Only run the module if this is the main module
    pygame.init()           # Initialize the pygame module

# Make the screen and caption
screen = pygame.display.set_mode(screen_dimensions)
pygame.display.set_caption("PyPong")

# Start the game loop
while True:

    timer.tick(framerate)          # Set the framerate
    screen.fill(colours['black'])  # Fill the screen with a colour

    # Create the players
    player = pygame.draw.rect(screen, colours['white'], [10, player_y, 10, player_size])
    opponent = pygame.draw.rect(screen, colours['white'], [580, opponent_y, 10, opponent_size])

    # Create the ball
    ball = pygame.draw.rect(screen, colours['white'], [ball_x, ball_y, ball_size, ball_size])

    # Opponent movement
    opponent_y = update_ai(ball_y, opponent_y)

    # Game loop logic
    for event in pygame.event.get():

        # Pressing the close button closes the game
        if event.type == pygame.QUIT:
            close_game()  # Close the game

        # Y axis movement
        elif event.type == pygame.KEYDOWN:  # The player presses a key

            if event.key == pygame.K_w:     # The player pressed 'W' -> Go up
                player_direction = -5

            if event.key == pygame.K_s:     # The player pressed 'S' -> Go down
                player_direction = 5

        elif event.type == pygame.KEYUP:    # The player releases a key

            if event.key == pygame.K_w or event.key == pygame.K_s:  # The player released 'W' or 'S'
                player_direction = 0

        # Place the player on the new location
        player_y += player_speed * player_direction

    pygame.display.flip()  # Update the screen

