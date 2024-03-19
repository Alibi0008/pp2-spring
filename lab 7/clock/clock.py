import pygame
import sys
import time
import math

pygame.init()

screen_width = 600
screen_height = 600
screen = pygame.display.set_mode((screen_width, screen_height))
pygame.display.set_caption("Mickey Clock")

left_hand_image = pygame.image.load("clock/leftarm.png")
right_hand_image = pygame.image.load("clock/rightarm.png")
clock_face_image = pygame.image.load("clock/mainclock.png")

def rotate(image, angle, center):
    rotated_image = pygame.transform.rotate(image, angle)
    new_rect = rotated_image.get_rect(center=center)
    return rotated_image, new_rect

def scale_image(image, width, height):
    return pygame.transform.scale(image, (width, height))

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

    clock_face_scaled = pygame.transform.scale(clock_face_image, (screen_width, screen_height))

    screen.blit(clock_face_scaled, (0, 0))

    current_time = time.localtime()
    seconds_angle = -6 * current_time.tm_sec
    minutes_angle = -6 * current_time.tm_min - (current_time.tm_sec / 10)

    center_x = clock_face_scaled.get_width() // 2
    center_y = clock_face_scaled.get_height() // 2

    seconds_hand_width = 45
    seconds_hand_height = 450
    minutes_hand_width = 600
    minutes_hand_height = 600
    left_hand_scaled = scale_image(left_hand_image, seconds_hand_width, seconds_hand_height)
    right_hand_scaled = scale_image(right_hand_image, minutes_hand_width, minutes_hand_height)

    seconds_hand_length = max(left_hand_scaled.get_width(), left_hand_scaled.get_height()) // 2
    minutes_hand_length = max(right_hand_scaled.get_width(), right_hand_scaled.get_height()) // 2

    seconds_hand_x = center_x
    seconds_hand_y = center_y

    minutes_hand_x = center_x
    minutes_hand_y = center_y

    left_hand_rotated, left_hand_rect = rotate(left_hand_scaled, seconds_angle, (seconds_hand_x, seconds_hand_y))
    right_hand_rotated, right_hand_rect = rotate(right_hand_scaled, minutes_angle, (minutes_hand_x, minutes_hand_y))

    screen.blit(left_hand_rotated, left_hand_rect)
    screen.blit(right_hand_rotated, right_hand_rect)

    pygame.display.flip()

    pygame.time.delay(1000)
