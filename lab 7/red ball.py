import pygame
import sys

pygame.init()

w = 1080
h = 720

WHITE = (255, 255, 255)
RED = (255, 0, 0)

screen = pygame.display.set_mode((w, h))
pygame.display.set_caption("red ball")

clock = pygame.time.Clock()
FPS = 60

x = w // 2
y = h // 2
speed = 20
radius = 25

left = right = up = down = False

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_LEFT:
                left = True
            elif event.key == pygame.K_RIGHT:
                right = True
            elif event.key == pygame.K_UP:
                up = True
            elif event.key == pygame.K_DOWN:
                down = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_LEFT:
                left = False
            elif event.key == pygame.K_RIGHT:
                right = False
            elif event.key == pygame.K_UP:
                up = False
            elif event.key == pygame.K_DOWN:
                down = False

    if left:
        x -= speed
    elif right:
        x += speed
    if up:
        y -= speed
    elif down:
        y += speed

    if x - radius < 0:
        x = radius
    elif x + radius > w:
        x = w - radius
    if y - radius < 0:
        y = radius
    elif y + radius > h:
        y = h - radius

    screen.fill(WHITE)
    pygame.draw.circle(screen, RED, (x, y), radius)
    pygame.display.update()
    clock.tick(FPS)
    