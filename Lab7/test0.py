import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))

music_list = [r"resources\music0.mp3",
              r"resources\music1.mp3",
              r"resources\music2.mp3",
              r"resources\music3.mp3"]

order = 0
sound = 50
playing = False  # Start with music paused
running = True

# Initial music load
pygame.mixer.music.load(music_list[order])
pygame.mixer.music.set_volume(sound/100)

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                sound += 1
                pygame.mixer.music.set_volume(sound/100)
            elif event.key == pygame.K_DOWN:
                sound -= 1
                pygame.mixer.music.set_volume(sound/100)
            elif event.key == pygame.K_SPACE:
                if playing:
                    pygame.mixer.music.pause()
                else:
                    pygame.mixer.music.unpause()
                playing = not playing
            elif event.key == pygame.K_RIGHT:
                order += 1
                if order > 3:
                    order = 0
                pygame.mixer.music.load(music_list[order])
                pygame.mixer.music.play(-1)  # -1 means loop forever
                if not playing:
                    pygame.mixer.music.pause()
            elif event.key == pygame.K_LEFT:
                order -= 1
                if order < 0:
                    order = 3
                pygame.mixer.music.load(music_list[order])
                pygame.mixer.music.play(-1)
                if not playing:
                    pygame.mixer.music.pause()

    # Keep sound within bounds
    sound = max(0, min(100, sound))

    print(sound, playing, order)
    pygame.display.flip()

pygame.quit()