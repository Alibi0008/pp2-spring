import pygame
import sys

def play_music(file, start_pos=0):
    pygame.mixer.music.load(file)
    pygame.mixer.music.play(start=start_pos)

def stop_music():
    pygame.mixer.music.stop()

def next_track():
    global current_index, music_files
    current_index = (current_index + 1) % len(music_files)
    play_music(music_files[current_index])

def previous_track():
    global current_index, music_files
    current_index = (current_index - 1) % len(music_files)
    play_music(music_files[current_index])


pygame.init()
pygame.mixer.init()

screen = pygame.display.set_mode((200, 200))
pygame.display.set_caption('Music Player')

global current_index, music_files
music_files = ['Sia_Snowman.mp3', 'La La La.mp3', 'Shape of You.mp3']
current_index = 0

music_playing = False
music_position = 0

while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()

        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                if not music_playing:
                    play_music(music_files[current_index], start_pos=music_position)
                    music_playing = True
                else:
                    music_position = pygame.mixer.music.get_pos() / 1000
                    stop_music()
                    music_playing = False
            elif event.key == pygame.K_RIGHT:
                next_track()
            elif event.key == pygame.K_LEFT:
                previous_track()

    pygame.display.update()
