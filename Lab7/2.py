import pygame
pygame.init()
screen = pygame.display.set_mode((800, 600))

music_list = (r"resources\music0.mp3",
              r"resources\music1.mp3",
              r"resources\music2.mp3",
              r"resources\music3.mp3")

order = 0
sound = 50
playing = False

running = True
pygame.mixer.music.load(music_list[order])
pygame.mixer.music.play(0)
pygame.mixer.music.pause()


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                sound += 5
                pygame.mixer.music.set_volume(sound / 100)
            if event.key == pygame.K_DOWN:
                sound -= 5
                pygame.mixer.music.set_volume(sound / 100)
            if event.key == pygame.K_SPACE:
                playing = not playing
                if playing:
                    pygame.mixer.music.unpause()
                else:
                    pygame.mixer.music.pause()
            if event.key == pygame.K_RIGHT:
                order += 1
                if order > 3:
                    order = 0
                pygame.mixer.music.load(music_list[order])
                if playing:
                    pygame.mixer.music.play(0)
                else:
                    pygame.mixer.music.play(0)
                    pygame.mixer.music.pause()
                
            if event.key == pygame.K_LEFT:
                order -= 1
                if order < 0:
                    order = 3
                pygame.mixer.music.load(music_list[order])
                if playing:
                    pygame.mixer.music.play(0)
                else:
                    pygame.mixer.music.play(0)
                    pygame.mixer.music.pause()

    if sound > 100:
        sound = 100
    elif sound < 0:
        sound = 0
    if order > 3:
        order = 0
    elif order < 0:
        order = 3

    print(sound, playing, order)
    pygame.display.flip()

