import pygame
import random

# Initialize Pygame
pygame.init()

# Define colors
WHITE = (255, 255, 255)
BLACK = (0, 0, 0)
GREEN = (0, 255, 0)
RED = (255, 0, 0)

# Define screen dimensions
SCREEN_WIDTH = 600
SCREEN_HEIGHT = 600

# Create the game window
screen = pygame.display.set_mode((SCREEN_WIDTH, SCREEN_HEIGHT))
pygame.display.set_caption("Snake Game")

# Initialize snake position and body
snake_pos = [100, 50]
snake_body = [[100, 50], [90, 50], [80, 50]]

# Initialize food position
food_pos = [random.randrange(1, (SCREEN_WIDTH // 10)) * 10, random.randrange(1, (SCREEN_HEIGHT // 10)) * 10]
food_spawn = True

# Define directions
UP = 0
DOWN = 1
LEFT = 2
RIGHT = 3
dir = RIGHT

# Initialize score, level, snake speed, and game over status
score = 0
level = 1
snake_speed = 15
game_over = False

# Initialize clock for controlling game speed
clock = pygame.time.Clock()

# Main game loop
while not game_over:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP and dir != DOWN:
                dir = UP
            elif event.key == pygame.K_DOWN and dir != UP:
                dir = DOWN
            elif event.key == pygame.K_LEFT and dir != RIGHT:
                dir = LEFT
            elif event.key == pygame.K_RIGHT and dir != LEFT:
                dir = RIGHT

    # Move the snake based on its direction
    if dir == UP:
        snake_pos[1] -= 10
    elif dir == DOWN:
        snake_pos[1] += 10
    elif dir == LEFT:
        snake_pos[0] -= 10
    elif dir == RIGHT:
        snake_pos[0] += 10

    # Check for collision with the screen boundaries
    if snake_pos[0] < 0 or snake_pos[0] > SCREEN_WIDTH - 10 or snake_pos[1] < 0 or snake_pos[1] > SCREEN_HEIGHT - 10:
        game_over = True

    # Check if the snake eats the food
    if snake_pos[0] == food_pos[0] and snake_pos[1] == food_pos[1]:
        score += 1
        food_spawn = False
    else:
        snake_body.pop()

    # Spawn new food if needed
    if not food_spawn:
        food_pos = [random.randrange(1, (SCREEN_WIDTH // 10)) * 10, random.randrange(1, (SCREEN_HEIGHT // 10)) * 10]
        food_spawn = True

    # Update snake body
    snake_body.insert(0, list(snake_pos))

    # Draw game elements
    screen.fill(BLACK)
    for pos in snake_body:
        pygame.draw.rect(screen, WHITE, pygame.Rect(pos[0], pos[1], 10, 10))
    pygame.draw.rect(screen, RED, pygame.Rect(food_pos[0], food_pos[1], 10, 10))

    # Display score and level
    font = pygame.font.SysFont(None, 25)
    text = font.render("Score: " + str(score) + "   Level: " + str(level), True, WHITE)
    screen.blit(text, (10, 10))

    # Update display
    pygame.display.update()

    # Increase level and snake speed based on score
    if score > level * 3:
        level += 1
        snake_speed += 5

    # Control game speed
    clock.tick(snake_speed)

# Quit Pygame
pygame.quit()
