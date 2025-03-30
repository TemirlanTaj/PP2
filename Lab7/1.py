import pygame

pygame.init()

running = True

clock_inner = pygame.time.Clock()
FPS = 1

clock = pygame.image.load(r"C:\Users\Hp\Desktop\PP2\Lab7\recources\clock.png") #getting the images
clockRect = clock.get_rect()
min_hand = pygame.image.load(r"C:\Users\Hp\Desktop\PP2\Lab7\recources\min_hand.png")
sec_hand = pygame.image.load(r"C:\Users\Hp\Desktop\PP2\Lab7\recources\sec_hand.png")


screen = pygame.display.set_mode((clockRect.width, clockRect.height))

min_angle = -50
sec_angle = 60
timer_sec = 0

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
    
    screen.blit(clock, (0,0))
    
    
    sec_hand_rot = pygame.transform.rotate(sec_hand, sec_angle)
    sec_hand_rect = sec_hand_rot.get_rect(center = (clockRect.width // 2, clockRect.height // 2))
    

    min_hand_rot = pygame.transform.rotate(min_hand, min_angle)
    min_hand_rect = min_hand_rot.get_rect(center = (clockRect.width // 2, clockRect.height // 2))

    screen.blit(sec_hand_rot, sec_hand_rect)
    screen.blit(min_hand_rot, min_hand_rect)
    

    timer_sec += 1
    sec_angle -= 360/60
    if timer_sec == 60:
        timer_sec = 0
        min_angle -= 360/60

    
    pygame.display.flip()
    clock_inner.tick(FPS)
    