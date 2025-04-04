import pygame
import random
import time
pygame.init()

width = 600
height = 600
cell = 40

screen = pygame.display.set_mode((width, height))

colorRed = (255,0,0) #rgb
colorYellow = (255,255,0)
color_gray_white = ((0,0,0), (128,128,128))
colorGreen = (0,255,0)
colorBlue = (0,0,255)
colorBlack = (255,255,255)

font = pygame.font.SysFont("Verdana", 60)
font_small = pygame.font.SysFont("Verdana", 20)

def draw_grid_walls():
    for i in range(width // cell):
        for j in range(height // cell):
            pygame.draw.rect(screen, color_gray_white[(i + j) % 2 - 1], (i * cell, j * cell, cell, cell))
            if j == 0:
                pygame.draw.line(screen, colorRed, (0, j * cell), (width, j * cell))
            elif j == width // cell - 1:
                pygame.draw.line(screen, colorRed, (0, (j+1) * cell - 1), (width, (j+1) * cell - 1))
        if i == 0:
            pygame.draw.line(screen, colorRed, (i * cell, 0), (i * cell, width))
        elif i == width // cell - 1:
            pygame.draw.line(screen, colorRed, ((i+1) * cell - 1, 0), ((i + 1) * cell - 1, width))

def game_over():
    font = pygame.font.SysFont("Verdana", 60)
    game_over_text = font.render("Game Over", True, colorRed)
    screen.blit(game_over_text, (145, 250))
    global snake
    snake.dx = 0
    snake.dy = 0

class Point:
    def __init__(self, x, y):
        self.x = x
        self.y = y

class Snake:
    def __init__(self):
        self.body = [Point(10,10), Point(10,11), Point(10,12)]
        self.dx = 0
        self.dy = -1
        self.level = 1

    def check_collision_food(self, food, level):
        head = self.body[0]
        global food_count
        global FPS
        if head.x == food.collection[0].x and head.y == food.collection[0].y:
            for i in range(food.weight):
                self.body.append(Point(head.x, head.y))
            food.generate_random_pos(level)
            food.weight = random.randint(1,3)
            food_count += 1
            if food_count % 4 == 0:
                FPS += 2
                level += 1
                foods.append(Food())



    def drawSnake(self):
        head = self.body[0]
        pygame.draw.rect(screen, colorRed, (head.x * cell, head.y * cell, cell, cell))
        for i in range(1, len(self.body)):
            pygame.draw.rect(screen, colorYellow, (self.body[i].x * cell, self.body[i].y * cell, cell, cell))

    def move(self):
        for part in range(len(self.body) - 1, 0, -1):
            self.body[part].x = self.body[part - 1].x
            self.body[part].y = self.body[part - 1].y
        self.body[0].x += self.dx
        self.body[0].y += self.dy

        for i in range(1, len(self.body) - 1):
            if i == self.body[0]:
                game_over()

        # checks the right border
        if self.body[0].x > width // cell:
            game_over()
        # checks the left border
        if self.body[0].x < 0:
            game_over()
        # checks the bottom border
        if self.body[0].y > height // cell:
            game_over()
        # checks the top border
        if self.body[0].y < 0:
            game_over() 

class Food:
    def __init__(self):
        self.collection = [Point(random.randint(0, width // cell - 1), random.randint(0, height // cell - 1))]
        self.weight = random.randint(1,3)

    def draw(self):
        for point in self.collection:
            pygame.draw.rect(screen, colorGreen, (point.x * cell, point.y * cell, cell, cell))
            screen.blit(font_small.render(str(self.weight), True, colorRed), (point.x * cell + 15, point.y * cell + 6))

    def generate_random_pos(self, level):
        self.collection = [Point(random.randint(0, width // cell - 1), random.randint(0, height // cell - 1)) for _ in range(level)]

running = True
clock = pygame.time.Clock()
FPS = 5

snake = Snake()
foods = [Food()]
food_count = 0
level = 1

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_RIGHT and snake.dx != -1:
                snake.dx = 1
                snake.dy = 0
            elif event.key == pygame.K_LEFT and snake.dx != 1:
                snake.dx = -1
                snake.dy = 0
            elif event.key == pygame.K_DOWN and snake.dy != -1:
                snake.dx = 0
                snake.dy = 1
            elif event.key == pygame.K_UP and snake.dy != 1:
                snake.dx = 0
                snake.dy = -1

    draw_grid_walls()

    snake.drawSnake()
    for i in foods:
        snake.check_collision_food(i, level)
        i.draw()

    snake.move()

    scores = font_small.render(str(food_count), True, colorRed)
    levels = font_small.render(str(level), True, colorRed)
    screen.blit(scores, (10,10))
    screen.blit(levels, (30,10))


    pygame.display.flip()
    clock.tick(FPS)
