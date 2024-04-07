# Imports
import pygame, sys
from pygame.locals import *
import random, time

# Initializing pygame
pygame.init()

# Setting up FPS 
FPS = 60
FramePerSec = pygame.time.Clock()

# Creating colors
BLUE  = (0, 0, 255)
RED   = (255, 0, 0)
GREEN = (0, 255, 0)
BLACK = (0, 0, 0)
WHITE = (255, 255, 255)

# Other Variables for use in the program
SCREEN_WIDTH = 400
SCREEN_HEIGHT = 600
SPEED = 5
SCORE = 0
LEVEL = 1

# Setting up Fonts
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, BLACK)

background = pygame.image.load("lab 8/racer/images/AnimatedStreet.png")

# Create a white screen 
DISPLAYSURF = pygame.display.set_mode((400,600))
DISPLAYSURF.fill(WHITE)
pygame.display.set_caption("Racer")

# Define the Enemy class
class Enemy(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("lab 8/racer/images/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,SCREEN_WIDTH-40), 0)

    def move(self):
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Define the Player class
class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("lab 8/racer/images/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed()
        
        if self.rect.left > 0:
              if pressed_keys[K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < SCREEN_WIDTH:        
              if pressed_keys[K_RIGHT]:
                  self.rect.move_ip(5, 0)

# Define the Coin class
class Coin(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__()
        self.image = pygame.image.load("lab 8/racer/images/coin.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

    def move(self):
        self.rect.move_ip(0,SPEED)
        if (self.rect.bottom > 600):
            self.rect.top = 0
            self.rect.center = (random.randint(40, SCREEN_WIDTH - 40), 0)

# Setting up Sprites        
P1 = Player()
E1 = Enemy()
C1 = Coin()

# Creating Sprites Groups
enemies = pygame.sprite.Group()
enemies.add(E1)

coins = pygame.sprite.Group()
coins.add(C1)

all_sprites = pygame.sprite.Group()
all_sprites.add(P1)
all_sprites.add(E1)
all_sprites.add(C1)

# Adding a new User event 
INC_SPEED = pygame.USEREVENT + 1
pygame.time.set_timer(INC_SPEED, 1000)

# Start background music
pygame.mixer.music.load("lab 8/racer/sound/background.wav")
pygame.mixer.music.play(-1)

# Function to create a new coin
def create_coin():
    new_coin = Coin()  # Create a new instance of the Coin sprite
    coins.add(new_coin)  # Add the new coin sprite to the coin group

# Game Loop
while True:
    # Cycles through all events occurring
    for event in pygame.event.get():
        if event.type == QUIT:
            pygame.quit()
            sys.exit()

    # Draw background
    DISPLAYSURF.blit(background, (0,0))

    # Display score and level
    text = font_small.render("Score: " + str(SCORE) + "   Level: " + str(LEVEL), True, BLACK)
    DISPLAYSURF.blit(text, (10, 10))

    # Moves and Re-draws all Sprites
    for entity in all_sprites:
        entity.move()
        DISPLAYSURF.blit(entity.image, entity.rect)

    # Check for collision between player and coins
    if pygame.sprite.spritecollide(P1, coins, dokill=True):
        pygame.mixer.Sound('lab 8/racer/sound/catch.wav').play()
        SCORE += random.randint(1,3)
        # Generate a new coin
        new_coin = Coin()
        coins.add(new_coin)
        all_sprites.add(new_coin)

    # Increase level and speed
    if SCORE > LEVEL*5:
        LEVEL += 1
        SPEED += 0.5

    # Generate new coins periodically
    if pygame.time.get_ticks() % 2000 == 0:
        create_coin()

    # Check for collision between Player and Enemy
    if pygame.sprite.spritecollideany(P1, enemies):
        pygame.mixer.music.stop()  # Stop background music
        pygame.mixer.Sound('lab 8/racer/sound/crash.wav').play()
        time.sleep(1)

        # Display game over message
        DISPLAYSURF.fill(RED)
        DISPLAYSURF.blit(game_over, (30,220))

        pygame.display.update()
        for entity in all_sprites:
            entity.kill()  # Remove all sprites from the screen
        time.sleep(2)  # Pause for 2 seconds
        pygame.quit()  # Quit pygame
        sys.exit()  # Exit the program

    pygame.display.update()
    FramePerSec.tick(FPS)
