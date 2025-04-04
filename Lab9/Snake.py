# class Person:
#     def __init__(self, name, age):
#         print("init inr")
#         self.name = name
#         self.age = age
#         print(self.name, self. age)



# peple = Person("mark", 27)

# print(type("str") == str)

# s = [1,2,3,4]
# temp = s[::-1]
# print(temp)

# print(s == temp)

# import random
# res=[]
# for i in range(100):
#     res.append(random.randint(1, 21))
# res.sort()
# print(res)

# class Point():
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y
#     def show(self):
#         print(f'x coordinate: {self.x}, y coordinate: {self.y}')
#     def dist(p1, p2):
#         return ( (p1.x - p2.x)**2 + (p1.y - p2.y)**2 ) ** 0.5
    
# tochka1 = Point(1,2)
# tochka2 = Point(4,5)

# tochka1.show()
# tochka2.show()
# print(tochka1.dist(tochka2))


# def divisibleBy3and4(num):
#     start = 0
#     while start <= num:
#         if start % 3 == 0 and start % 4 == 0:
#             yield start
#         start += 1

# N = int(input())

# listOfNums = divisibleBy3and4(N)

# print(listOfNums)

# for i in listOfNums:
#    print(i)

# print(len("================================================================================"))
# print(len("                                                 "))
# print(len("           "))
# print(len("--------------------------------------------------"))
# print(len("--------------------"))
# print(len("topology/pod-1/node-201/sys/phys-[eth1/36]"))



#     # for atrib in jsonDict["imdata"][i]:
#     #     print(jsonDict["imdata"][atrib]["ad"])

# import re

# text_to_match = "John's John email is john.doe@example.com, and his Johnbackup is johndoe123@work.net."

# pattern = 'John' # our regex

# result = re.match(pattern, text_to_match)

# print(result) # match object

# print(result.group()) # print the match as a string

# import re

# txt = "hellllllo planet"

# #Search for a sequence that starts with "he", followed by 0 or more  (any) characters, and an "o":

# x = re.findall("he.*o", txt)

# from datetime import *

# d1 = date.today() - timedelta(1)
# d2 = date.today()
# d3 = date.today() + timedelta(1)

# print(type(d1))

# import os

# path = r"C:\Users\Hp\Desktop\PP2\Lab6\dir_and_files"

# everything = os.scandir(path)
# files = []
# dirs = []

# for i in everything:
#     if i.is_file():
#         files.append(i.name)
#     elif i.is_dir():
#         dirs.append(i.name)

# print(f"Files: {files}")
# print(f"Dirs: {dirs}")
# print(f"All: {dirs + files}")

# import os

# path = r"C:\Users\Hp\Desktop\PP2\Lab6\dir_and_files\4.txt"
# fileContent = open(path)

# # print(fileContent.readlines())

# linesList = list(fileContent)
# print(linesList)
# print('Length:', len(linesList))import sys, pygame
# import pygame
# pygame.init()


# #allow to load needed music
# def choice(order):
#     if order == 0:
#         return pygame.mixer.music.load("recources/music0.mp3")
#     elif order == 1:
#         return pygame.mixer.music.load("recources/music1.mp3")
#     elif order == 2:
#         return pygame.mixer.music.load("recources/music2.mp3")
#     elif order == 3:
#         return pygame.mixer.music.load("recources/music3.mp3")


# screen = pygame.display.set_mode((800,600))
# running = True
# order = 0
# changing = True#Check changes in music

# #allow to use commands smoothly without repeating too many
# clock = pygame.time.Clock()
# Fps = 7

# while running:
#     if changing:
#         choice(order)
#         changing = False
#         flag1 = True#used to check is it played firstly or not


#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False

#     #allow to get pressed keys
#     pressed_keys = pygame.key.get_pressed()
#     if pressed_keys[pygame.K_UP]:
#         if flag1:
#             pygame.mixer.music.play(0)
#         else:
#             pygame.mixer.music.unpause()#used to continue listening in paused place
#             flag1 = True
#     if pressed_keys[pygame.K_DOWN]:
#         pygame.mixer.music.pause()
#         flag1=False
#     if pressed_keys[pygame.K_RIGHT]:
#        if order == 3:
#            order-=4
#        order+=1
#        changing = True
#     if pressed_keys[pygame.K_LEFT]:
#         if order == 0:
#             order+=4 
#         order-=1
#         changing = True


#     pygame.display.update()
#     clock.tick(Fps) 
#     print(order)

#     # keyPressed = pygame.key.get_pressed()
#     # if keyPressed[pygame.K_UP]:
#     #     sound += 1
#     # if keyPressed[pygame.K_DOWN]:
#     #     sound -= 1
#     # if keyPressed[pygame.K_SPACE]:
#     #     playing = not playing

# colorGRAY = (128,128,128)
# colorWHITE = (0,0,0)
# colorRED = (255,0,0)
# colorYELLOW = (255,255,0)
# colorGREEN = (0,255,0)
# import pygame
# import random

# pygame.init()

# WIDTH = 600
# HEIGHT = 600

# screen = pygame.display.set_mode((WIDTH, HEIGHT))

# CELL = 30

# def draw_grid():
#     for i in range(HEIGHT // CELL):
#         for j in range(WIDTH // CELL):
#             pygame.draw.rect(screen, colorGRAY, (i * CELL, j * CELL, CELL, CELL), 1)

# def draw_grid_chess():
#     colors = [colorWHITE, colorGRAY]

#     for i in range(HEIGHT // CELL):
#         for j in range(WIDTH // CELL):
#             pygame.draw.rect(screen, colors[(i + j) % 2], (i * CELL, j * CELL, CELL, CELL))

# class Point:
#     def __init__(self, x, y):
#         self.x = x
#         self.y = y

#     def __str__(self):
#         return f"{self.x}, {self.y}"

# class Snake:
#     def __init__(self):
#         self.body = [Point(10, 11), Point(10, 12), Point(10, 13)]
#         self.dx = 1
#         self.dy = 0

#     def move(self):
#         for i in range(len(self.body) - 1, 0, -1):
#             print("move")
#             print(f" x: {self.body[i].x} -> {self.body[i-1].x}")
#             print(f" y: {self.body[i].y} -> {self.body[i-1].y}")
#             self.body[i].x = self.body[i - 1].x
#             self.body[i].y = self.body[i - 1].y

#         self.body[0].x += self.dx
#         self.body[0].y += self.dy

#         # checks the right border
#         if self.body[0].x > WIDTH // CELL - 1:
#             self.body[0].x = 0
#         # checks the left border
#         if self.body[0].x < 0:
#             self.body[0].x = WIDTH // CELL - 1
#         # checks the bottom border
#         if self.body[0].y > HEIGHT // CELL - 1:
#             self.body[0].y = 0
#         # checks the top border
#         if self.body[0].y < 0:
#             self.body[0].y = HEIGHT // CELL - 1


#     def draw(self):
#         head = self.body[0]
#         pygame.draw.rect(screen, colorRED, (head.x * CELL, head.y * CELL, CELL, CELL))
#         for segment in self.body[1:]:
#             pygame.draw.rect(screen, colorYELLOW, (segment.x * CELL, segment.y * CELL, CELL, CELL))

#     def check_collision(self, food):
#         head = self.body[0]
#         if head.x == food.pos.x and head.y == food.pos.y:
#             print("Got food!")
#             self.body.append(Point(head.x, head.y))
#             food.generate_random_pos()

# class Food:
#     def __init__(self):
#         self.pos = Point(9, 9)

#     def draw(self):
#         pygame.draw.rect(screen, colorGREEN, (self.pos.x * CELL, self.pos.y * CELL, CELL, CELL))

#     def generate_random_pos(self):
#         self.pos.x = random.randint(0, WIDTH // CELL - 1)
#         self.pos.y = random.randint(0, HEIGHT // CELL - 1)


# FPS = 5
# clock = pygame.time.Clock()

# food = Food()
# snake = Snake()

# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_RIGHT:
#                 snake.dx = 1
#                 snake.dy = 0
#             elif event.key == pygame.K_LEFT:
#                 snake.dx = -1
#                 snake.dy = 0
#             elif event.key == pygame.K_DOWN:
#                 snake.dx = 0
#                 snake.dy = 1
#             elif event.key == pygame.K_UP:
#                 snake.dx = 0
#                 snake.dy = -1

#     screen.fill((255,255,255))

#     draw_grid()

#     snake.move()
#     snake.check_collision(food)

#     snake.draw()
#     food.draw()

#     pygame.display.flip()
#     clock.tick(FPS)

# pygame.quit()

# import pygame

# pygame.init()

# WIDTH = 800
# HEIGHT = 600
# screen = pygame.display.set_mode((WIDTH, HEIGHT))
# base_layer = pygame.Surface((WIDTH, HEIGHT))

# colorRED = (255, 0, 0)
# colorBLUE = (0, 0, 255)
# colorWHITE = (255, 255, 255)
# colorBLACK = (0, 0, 0)

# clock = pygame.time.Clock()
# LMBpressed = False
# THICKNESS = 5

# curr_x = 0
# curr_y = 0
# prev_x = 0
# prev_y = 0

# def calculate_rect(x1, y1, x2, y2):
#     return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

# running = True
# while running:
#     for event in pygame.event.get():
#         if event.type == pygame.QUIT:
#             running = False
        
#         if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
#             print("LMB pressed!")
#             LMBpressed = True
#             prev_x, prev_y = event.pos

#         if event.type == pygame.MOUSEMOTION:
#             print("Position of the mouse:", event.pos)
#             if LMBpressed:
#                 curr_x, curr_y = event.pos
#                 screen.blit(base_layer, (0, 0))
#                 pygame.draw.rect(screen, colorRED, calculate_rect(prev_x, prev_y, curr_x, curr_y), THICKNESS)
        
#         if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
#             print("LMB released!")
#             LMBpressed = False
#             curr_x, curr_y = event.pos
#             pygame.draw.rect(screen, colorRED, calculate_rect(prev_x, prev_y, curr_x, curr_y), THICKNESS)
#             base_layer.blit(screen, (0, 0))

#         if event.type == pygame.KEYDOWN:
#             if event.key == pygame.K_EQUALS:
#                 print("Increased thickness")
#                 THICKNESS += 1
#             if event.key == pygame.K_MINUS:
#                 print("Reduced thickness")
#                 THICKNESS -= 1

#     pygame.display.flip()
#     clock.tick(60)

# pygame.quit()

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
