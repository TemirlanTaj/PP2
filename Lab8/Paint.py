import pygame

pygame.init()

WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))
base_layer = pygame.Surface((WIDTH, HEIGHT))
base_layer.fill((0, 0, 0))

colors = {
    "red": (255, 0, 0),
    "blue": (0, 0, 255),
    "black": (0, 0, 0),
    "green": (0, 255, 0)
}

colorWHITE = (255, 255, 255)
current_color = colors["red"]

clock = pygame.time.Clock()
LMBpressed = False
THICKNESS = 5

curr_x = 0
curr_y = 0
prev_x = 0
prev_y = 0

draw_mode = "rectangle"

def calculate_rect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

def calculate_circle(x1, y1, x2, y2):
    radius = int(((x2 - x1) * 2 + (y2 - y1) * 2) ** 0.5)
    return (x1, y1), radius

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            LMBpressed = True
            prev_x, prev_y = event.pos

        if event.type == pygame.MOUSEMOTION:
            if LMBpressed:
                curr_x, curr_y = event.pos
                screen.blit(base_layer, (0, 0))

                if draw_mode == "rectangle":
                    pygame.draw.rect(screen, current_color, calculate_rect(prev_x, prev_y, curr_x, curr_y), THICKNESS)
                elif draw_mode == "circle":
                    center, radius = calculate_circle(prev_x, prev_y, curr_x, curr_y)
                    pygame.draw.circle(screen, current_color, center, radius, THICKNESS)
                elif draw_mode == "line":
                    pygame.draw.line(screen, current_color, (prev_x, prev_y), (curr_x, curr_y), THICKNESS)

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            LMBpressed = False
            curr_x, curr_y = event.pos

            if draw_mode == "rectangle":
                pygame.draw.rect(screen, current_color, calculate_rect(prev_x, prev_y, curr_x, curr_y), THICKNESS)
            elif draw_mode == "circle":
                center, radius = calculate_circle(prev_x, prev_y, curr_x, curr_y)
                pygame.draw.circle(screen, current_color, center, radius, THICKNESS)
            elif draw_mode == "line":
                pygame.draw.line(screen, current_color, (prev_x, prev_y), (curr_x, curr_y), THICKNESS)

            base_layer.blit(screen, (0, 0))

        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_EQUALS:
                THICKNESS += 1
            if event.key == pygame.K_MINUS:
                THICKNESS -= 1
            if event.key == pygame.K_r:
                draw_mode = "rectangle"
            if event.key == pygame.K_c:
                draw_mode = "cirlce"
            if event.key == pygame.K_l:
                draw_mode = "line"
            if event.key == pygame.K_e:
                screen.fill((0,0,0))
            if event.key == pygame.K_1:
                current_color = colors["red"]
            if event.key == pygame.K_2:
                current_color = colors["blue"]
            if event.key == pygame.K_3:
                current_color = colors["black"]
            if event.key == pygame.K_4:
                current_color = colors["green"]

    pygame.display.flip()
    clock.tick(60)

pygame.quit()
