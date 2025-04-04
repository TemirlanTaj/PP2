import pygame
import random
import time
pygame.init()

#all the colors we need
colorRed   = (255, 0, 0)
colorGreen = (0, 255, 0)
colorBlack = (0, 0, 0)

Width = 400 #constant variable
Height = 600 #constant variable
moveSpeed = 5 #speed of the sprite
score = 0 #total score

#fonts and game over text
font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)
game_over = font.render("Game Over", True, colorBlack)

background = pygame.image.load("resources/AnimatedStreet.png") #load background

screen = pygame.display.set_mode((400,600)) #our screen

#in all classes we use pygame sprite as parent class
class Enemy(pygame.sprite.Sprite):
      def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("resources/Enemy.png")
        self.rect = self.image.get_rect()
        self.rect.center = (random.randint(40,Width-40), 0)

      def move(self):
        global score
        global moveSpeed
        self.rect.move_ip(0,moveSpeed)
        if (self.rect.bottom > 600):
            moveSpeed += 0.75 #move speed increases with the amount of enemy hitting tho bottom
            score += 1
            self.rect.top = 0
            self.rect.center = (random.randint(40, Width - 40), 0)


class Player(pygame.sprite.Sprite):
    def __init__(self):
        super().__init__() 
        self.image = pygame.image.load("resources/Player.png")
        self.rect = self.image.get_rect()
        self.rect.center = (160, 520)
       
    def move(self):
        pressed_keys = pygame.key.get_pressed() #firstly we get all pressed keys
        
        if self.rect.left > 0: #then we move the car and do nothing if it thouches the borders
              if pressed_keys[pygame.K_LEFT]:
                  self.rect.move_ip(-5, 0)
        if self.rect.right < Width:        
              if pressed_keys[pygame.K_RIGHT]:
                  self.rect.move_ip(5, 0)

#initialize objects         
player = Player()
enemy = Enemy()

#group them
enemies = pygame.sprite.Group()
enemies.add(enemy)
all_sprites = pygame.sprite.Group()
all_sprites.add(player)
all_sprites.add(enemy)

running = True
clock = pygame.time.Clock()
FPS = 60

while running:
    #cycles through all events 
    for event in pygame.event.get():      
        if event.type == pygame.QUIT:
            running = False

    #add background and score in the left corner
    screen.blit(background, (0,0))
    scores = font_small.render(str(score), True, colorBlack)
    screen.blit(scores, (10,10))

    #Moves and Re-draws all Sprites
    for entity in all_sprites:
        entity.move()
        screen.blit(entity.image, entity.rect)
        

    #To be run if collision occurs between Player and Enemy
    if pygame.sprite.spritecollideany(player, enemies):
          pygame.mixer.Sound('resources/crash.wav').play()
          time.sleep(1)
                   
          screen.fill(colorRed)
          screen.blit(game_over, (30,175))
          screen.blit(font.render(f"Your score: {score}", True, colorBlack), (0, 275))
          
          pygame.display.update()
          for entity in all_sprites:
                entity.kill() 
          time.sleep(2)
          running = False

    pygame.display.update()
    clock.tick(FPS)