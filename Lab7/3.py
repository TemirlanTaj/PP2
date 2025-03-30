import pygame

pygame.init()

WIDTH = 1100
HEIGHT = 700
screen = pygame.display.set_mode((WIDTH, HEIGHT))
colorRed = (200, 0, 0) #RGB - red
colorWhite = (255, 255, 255) #RGB - white
circle_radius = 25

circle_x = WIDTH // 2
circle_y = HEIGHT // 2

move_speed = 20
def calibration(border, radius, cord): # корректирует координаты, убирает отклонениe
    if cord > border - radius: #если касатся крайнего бордера
        cord = border - radius
    elif cord < 0 + radius: #если касается бордера = 0
        cord = 0 + radius
    return cord


running = True
is_white = True

clock = pygame.time.Clock()
FPS = 60

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_SPACE:
                is_white = not is_white
            if event.key == pygame.K_MINUS:
                move_speed -= 1
            if event.key == pygame.K_EQUALS:
                move_speed += 1
    
    pressedKey = pygame.key.get_pressed()
    if pressedKey[pygame.K_UP] and circle_y > circle_radius:
        circle_y -= move_speed
        circle_y = calibration(HEIGHT, circle_radius, circle_y)
    if pressedKey[pygame.K_DOWN] and circle_y < HEIGHT - circle_radius:
        circle_y += move_speed
        circle_y = calibration(HEIGHT, circle_radius, circle_y)
    if pressedKey[pygame.K_LEFT] and circle_x > circle_radius:
        circle_x -= move_speed
        circle_x = calibration(WIDTH, circle_radius, circle_x)
    if pressedKey[pygame.K_RIGHT] and circle_x < WIDTH - circle_radius:
        circle_x += move_speed
        circle_x = calibration(WIDTH, circle_radius, circle_x)



    if is_white:
        screen.fill(colorWhite)
        pygame.draw.circle(screen, colorRed, (circle_x, circle_y), circle_radius)
    else:
        screen.fill(colorRed)
        pygame.draw.circle(screen, colorWhite, (circle_x, circle_y), circle_radius)

    # print(circle_x, circle_y, move_speed) # для тестирования координат

    pygame.display.flip()
    clock.tick(FPS)