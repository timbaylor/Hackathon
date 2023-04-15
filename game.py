import pygame
import random


pygame.init()

# Set up the screen
screen_width = 800
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))

# Set up the fonts
font = pygame.font.Font(None, 36)

# Set up the colors
black = (0, 0, 0)
white = (255, 255, 255)
red = (255, 0, 0)
green = (0, 255, 0)
blue = (0, 0, 255)

# Set up the player
player_image = pygame.image.load("water.png").convert_alpha()
player_width = 50
player_height = 50
player_x = 50
player_y = screen_height - player_height
player_jump_vel = -20
player_fall_vel = 5
player_jump_count = 10
player_is_jumping = False

# Set up the obstacle
obstacle_width = 100
obstacle_height = 100
obstacle_x = screen_width
obstacle_y = screen_height - obstacle_height
obstacle_vel = 10
obstacle_countdown = 60
obstacle_color = red

# Set up the game loop
game_over = False
score = 0
clock = pygame.time.Clock()

# Set up the quit button
quit_button = pygame.Rect(screen_width // 2 - 50, screen_height // 2 + 50, 100, 50)

while not game_over:
    # Handle events
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE and not player_is_jumping:
                player_is_jumping = True
                player_jump_count = 10
        elif event.type == pygame.MOUSEBUTTONDOWN:
            mouse_pos = pygame.mouse.get_pos()
            if quit_button.collidepoint(mouse_pos):
                pygame.quit()

    # Update the player
    if player_is_jumping:
        player_y += player_jump_vel
        player_jump_count -= 1
        if player_jump_count == 0:
            player_is_jumping = False
    else:
        player_y += player_fall_vel

    # Update the obstacle
    obstacle_x -= obstacle_vel
    if obstacle_x < -obstacle_width:
        obstacle_x = screen_width
        obstacle_y = random.randint(screen_height // 2, screen_height - obstacle_height)
        score += 1
        obstacle_countdown -= 1
        if obstacle_countdown == 0:
            obstacle_vel += 1
            obstacle_countdown = 60
            obstacle_color = random.choice([red, green, blue])

    # Check for collision
    player_rect = pygame.Rect(player_x, player_y, player_width, player_height)
    obstacle_rect = pygame.Rect(obstacle_x, obstacle_y, obstacle_width, obstacle_height)
    if player_rect.colliderect(obstacle_rect):
        game_over = True

    # Draw the screen
    screen.fill(white)
    # Resize player image
    player_image_resized = pygame.transform.scale(player_image, (player_width, player_height))
    screen.blit(player_image_resized(player_x, player_y))
    pygame.draw.rect(screen, obstacle_color, (obstacle_x, obstacle_y, obstacle_width, obstacle_height))
    score_text = font.render("Score: " + str(score), True, black)
    screen.blit(score_text, (10, 10))
    if game_over:
        game_over_text = font.render("Game Over! Score: " + str(score), True, black)
        screen.blit(game_over_text, (screen_width//2 - 120, screen_height//2))
        pygame.draw.rect(screen, black, quit_button)
        quit_text = font.render("Quit", True, white)
        screen.blit(quit_text, (screen_width // 2 - 30, screen_height // 2 + 65))
        pygame.display.update()

# Set the frame rate
clock.tick(60)

# Clean up pygame
pygame.quit()

