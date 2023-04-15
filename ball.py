import pygame
import random

# Initialize Pygame
pygame.init()

# Set the screen size
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set the clock
clock = pygame.time.Clock()

# Set the font
font = pygame.font.SysFont('Arial', 30)

# Set the colors
white = (255, 255, 255)
black = (0, 0, 0)
red = (255, 0, 0)

# Set the ball properties
ball_size = 30
ball_color = white
ball_speed = [5, 5]
ball_pos = [random.randint(0, screen_width-ball_size), 0]

# Set the hoop properties
hoop_width = 100
hoop_height = 100
hoop_color = white
hoop_pos = [screen_width//2-hoop_width//2, screen_height-hoop_height-10]
hoop_speed = 10

# Set the score
score = 0

# Set the game over flag
game_over = False

# The main game loop
while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                hoop_pos[0] -= hoop_speed
            if event.key == pygame.K_RIGHT:
                hoop_pos[0] += hoop_speed
    
    # Move the ball
    ball_pos[0] += ball_speed[0]
    ball_pos[1] += ball_speed[1]

    # Bounce the ball
    if ball_pos[0] < 0 or ball_pos[0] > screen_width - ball_size:
        ball_speed[0] = -ball_speed[0]
    if ball_pos[1] < 0 or ball_pos[1] > screen_height - ball_size:
        ball_speed[1] = -ball_speed[1]

    # Check if the ball goes through the hoop
    if ball_pos[1] + ball_size > hoop_pos[1] and ball_pos[0] > hoop_pos[0] and ball_pos[0] < hoop_pos[0] + hoop_width:
        score += 1
        ball_pos = [random.randint(0, screen_width-ball_size), 0]
        ball_speed = [random.randint(-5, 5), random.randint(5, 10)]

    # Draw the background
    screen.fill(black)

    # Draw the ball
    pygame.draw.circle(screen, ball_color, ball_pos, ball_size)

    # Draw the hoop
    pygame.draw.rect(screen, hoop_color, (hoop_pos[0], hoop_pos[1], hoop_width, hoop_height))

    # Draw the score
    score_text = font.render("Score: " + str(score), True, red)
    screen.blit(score_text, (screen_width//2-score_text.get_width()//2, 10))

    # Update the screen
    pygame.display.update()

    # Set the FPS
    clock.tick(60)

# Quit Pygame
pygame.quit()
