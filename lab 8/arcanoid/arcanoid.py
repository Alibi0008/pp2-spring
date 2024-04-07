import pygame 
import random

pygame.init()
pygame.mixer.init()

W, H = 1200, 800
FPS = 60

screen = pygame.display.set_mode((W, H), pygame.RESIZABLE)
clock = pygame.time.Clock()
done = False
bg = (0, 0, 0)

# Paddle
paddleW = 300
paddleH = 25
paddleSpeed = 20
paddle = pygame.Rect(W // 2 - paddleW // 2, H - paddleH - 30, paddleW, paddleH)

# Ball
ballRadius = 20
ballSpeed = 6
ball_rect = int(ballRadius * 2 ** 0.5)
ball = pygame.Rect(random.randrange(ball_rect, W - ball_rect), H // 2, ball_rect, ball_rect)
dx, dy = 1, -1

# Game score
game_score = 0
game_score_fonts = pygame.font.SysFont('comicsansms', 40)
game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (0, 0, 0))
game_score_rect = game_score_text.get_rect()
game_score_rect.center = (210, 20)

# Catching sound
collision_sound = pygame.mixer.Sound('lab 8/arcanoid/catch (1).mp3')

def detect_collision(dx, dy, ball, rect):
    if dx > 0:
        delta_x = ball.right - rect.left
    else:
        delta_x = rect.right - ball.left
    if dy > 0:
        delta_y = ball.bottom - rect.top
    else:
        delta_y = rect.bottom - ball.top

    if abs(delta_x - delta_y) < 10:
        dx, dy = -dx, -dy
    if delta_x > delta_y:
        dy = -dy
    elif delta_y > delta_x:
        dx = -dx
    return dx, dy

def increase_ball_speed():
    global ballSpeed
    ballSpeed += 0.1  # Increase the speed by 0.1 units per frame

def shrink_paddle():
    global paddle, paddleW
    paddleW -= 10  # Reduce the paddle width by 10 unit per frame
    paddle = pygame.Rect(paddle.x, paddle.y, paddleW, paddleH)  # Create a new paddle Rect with updated width

def create_bonus_bricks():
    bonus_block_list = [pygame.Rect(10 + 120 * i, 90, 100, 50) for i in range(10)]
    return bonus_block_list

def detect_bonus_collision(ball, bonus_blocks):
    for bonus_block in bonus_blocks:
        if ball.colliderect(bonus_block):
            return bonus_block
    return None

# Block settings
block_list = [pygame.Rect(10 + 120 * i, 150 + 70 * j, 100, 50) for i in range(10) for j in range(3)]
color_list = [(random.randrange(0, 255), random.randrange(0, 255), random.randrange(0, 255)) for _ in range(30)]

# Unbreakable block settings
unbreakable_block_list = [pygame.Rect(10 + 120 * i, 30, 100, 50) for i in range(10)]
unbreakable_block_color = pygame.Color(255, 0, 0)

# Bonus block color
bonus_block_color = pygame.Color(0, 255, 0)  # Green color for bonus blocks

# Game over Screen
losefont = pygame.font.SysFont('comicsansms', 40)
losetext = losefont.render('Game Over', True, (255, 255, 255))
losetextRect = losetext.get_rect()
losetextRect.center = (W // 2, H // 2)

# Win Screen
winfont = pygame.font.SysFont('comicsansms', 40)
wintext = losefont.render('You win yay', True, (0, 0, 0))
wintextRect = wintext.get_rect()
wintextRect.center = (W // 2, H // 2)

# Time variables
time_elapsed = 0
time_increment = 500  # Time increment for speed increase and paddle shrinkage (in milliseconds)

bonus_blocks = create_bonus_bricks()  # Initialize bonus blocks

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill(bg)

    # Drawing unbreakable blocks
    [pygame.draw.rect(screen, unbreakable_block_color, block) for block in unbreakable_block_list]

    # Drawing blocks
    for color, block in enumerate(block_list):
        pygame.draw.rect(screen, color_list[color], block)

    # Drawing bonus blocks
    for bonus_block in bonus_blocks:
        pygame.draw.rect(screen, bonus_block_color, bonus_block)

    pygame.draw.rect(screen, pygame.Color(255, 255, 255), paddle)
    pygame.draw.circle(screen, pygame.Color(255, 0, 0), ball.center, ballRadius)

    # Ball movement
    ball.x += int(ballSpeed * dx)
    ball.y += int(ballSpeed * dy)

    # Collision left 
    if ball.centerx < ballRadius or ball.centerx > W - ballRadius:
        dx = -dx
    # Collision top
    if ball.centery < ballRadius + 50: 
        dy = -dy
    # Collision with paddle
    if ball.colliderect(paddle) and dy > 0:
        dx, dy = detect_collision(dx, dy, ball, paddle)

    # Collision with bonus blocks
    bonus_block_collision = detect_bonus_collision(ball, bonus_blocks)
    if bonus_block_collision:
        dx, dy = detect_collision(dx, dy, ball, bonus_block_collision)
        bonus_blocks.remove(bonus_block_collision)
        collision_sound.play()
        increase_ball_speed()
        paddleW += 10  # Increase width of paddle
        paddle = pygame.Rect(paddle.x, paddle.y, paddleW, paddleH)  # Update paddle rect

    # Collision blocks
    hitIndex = ball.collidelist(block_list)

    if hitIndex != -1:
        hitRect = block_list.pop(hitIndex)
        hitColor = color_list.pop(hitIndex)
        dx, dy = detect_collision(dx, dy, ball, hitRect)
        game_score += 1
        collision_sound.play()
        increase_ball_speed()  # Call the function to increase ball speed

    # Game score
    game_score_text = game_score_fonts.render(f'Your game score is: {game_score}', True, (255, 255, 255))
    screen.blit(game_score_text, game_score_rect)

    # Win/lose screens
    if ball.bottom > H:
        screen.fill((0, 0, 0))
        screen.blit(losetext, losetextRect)
    elif not len(block_list):
        screen.fill((255,255, 255))
        screen.blit(wintext, wintextRect)

    # Paddle Control
    key = pygame.key.get_pressed()
    if key[pygame.K_LEFT] and paddle.left > 0:
        paddle.left -= paddleSpeed
    if key[pygame.K_RIGHT] and paddle.right < W:
        paddle.right += paddleSpeed

    # Paddle shrinking over time
    time_elapsed += clock.get_rawtime()
    if time_elapsed >= time_increment:
        time_elapsed = 0
        shrink_paddle()

    pygame.display.flip()
    clock.tick(FPS)
