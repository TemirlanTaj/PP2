import pygame  # Import the pygame library

pygame.init()  # Initialize pygame

# Set up the window size
WIDTH = 800
HEIGHT = 600
screen = pygame.display.set_mode((WIDTH, HEIGHT))

# Create a base layer to store drawings
base_layer = pygame.Surface((WIDTH, HEIGHT))
base_layer.fill((0, 0, 0))  # Fill with white color

# Define colors
colors = {
    "red": (255, 0, 0),
    "blue": (0, 0, 255),
    "black": (0, 0, 0),
    "green": (0, 255, 0)
}

current_color = colors["red"]  # Default drawing color is red

clock = pygame.time.Clock()
LMBpressed = False  # Flag to track left mouse button press
THICKNESS = 5  # Line thickness

# Eraser settings
ERASER_SIZE = 20  # Initial eraser size

# Mouse coordinates
curr_x = curr_y = prev_x = prev_y = 0

draw_mode = "rectangle"  # Default drawing mode

# Function to calculate rectangle dimensions
def calculate_rect(x1, y1, x2, y2):
    return pygame.Rect(min(x1, x2), min(y1, y2), abs(x1 - x2), abs(y1 - y2))

# Function to calculate circle center and radius
def calculate_circle(x1, y1, x2, y2):
    radius = int(((x2 - x1) * 2 + (y2 - y1) * 2) ** 0.5)
    return (x1, y1), radius

# Function to draw an equilateral triangle
def draw_equilateral_triangle(surface, color, start, end, width):
    x1, y1 = start
    x2, y2 = end
    side = abs(x2 - x1)
    height = int((3 ** 0.5 / 2) * side)
    point1 = (x1, y1)
    point2 = (x1 + side, y1)
    point3 = (x1 + side // 2, y1 - height if y2 < y1 else y1 + height)
    pygame.draw.polygon(surface, color, [point1, point2, point3], width)

# Function to draw a right triangle
def draw_right_triangle(surface, color, start, end, width):
    x1, y1 = start
    x2, y2 = end
    point1 = (x1, y1)
    point2 = (x2, y2)
    point3 = (x1, y2)
    pygame.draw.polygon(surface, color, [point1, point2, point3], width)

# Function to draw a rhombus
def draw_rhombus(surface, color, start, end, width):
    x1, y1 = start
    x2, y2 = end
    cx = (x1 + x2) // 2
    cy = (y1 + y2) // 2
    dx = abs(x2 - x1) // 2
    dy = abs(y2 - y1) // 2
    points = [(cx, y1), (x2, cy), (cx, y2), (x1, cy)]
    pygame.draw.polygon(surface, color, points, width)

# Function to draw a square
def draw_square(surface, color, start, end, width):
    x1, y1 = start
    x2, y2 = end
    side = min(abs(x2 - x1), abs(y2 - y1))
    rect = pygame.Rect(x1, y1, side, side)
    if x2 < x1: rect.x = x1 - side
    if y2 < y1: rect.y = y1 - side
    pygame.draw.rect(surface, color, rect, width)

running = True
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False  # Close the window
        
        if event.type == pygame.MOUSEBUTTONDOWN and event.button == 1:
            LMBpressed = True
            prev_x, prev_y = event.pos  # Store the starting point

        if event.type == pygame.MOUSEMOTION:
            if LMBpressed:
                curr_x, curr_y = event.pos
                screen.blit(base_layer, (0, 0))  # Restore previous drawings

                # Determine which shape to draw
                if draw_mode == "rectangle":
                    pygame.draw.rect(screen, current_color, calculate_rect(prev_x, prev_y, curr_x, curr_y), THICKNESS)
                elif draw_mode == "circle":
                    center, radius = calculate_circle(prev_x, prev_y, curr_x, curr_y)
                    pygame.draw.circle(screen, current_color, center, radius, THICKNESS)
                elif draw_mode == "line":
                    pygame.draw.line(screen, current_color, (prev_x, prev_y), (curr_x, curr_y), THICKNESS)
                elif draw_mode == "square":
                    draw_square(screen, current_color, (prev_x, prev_y), (curr_x, curr_y), THICKNESS)
                elif draw_mode == "right_triangle":
                    draw_right_triangle(screen, current_color, (prev_x, prev_y), (curr_x, curr_y), THICKNESS)
                elif draw_mode == "equilateral_triangle":
                    draw_equilateral_triangle(screen, current_color, (prev_x, prev_y), (curr_x, curr_y), THICKNESS)
                elif draw_mode == "rhombus":
                    draw_rhombus(screen, current_color, (prev_x, prev_y), (curr_x, curr_y), THICKNESS)

        if event.type == pygame.MOUSEBUTTONUP and event.button == 1:
            LMBpressed = False
            curr_x, curr_y = event.pos

            # Save the drawn shape to the base layer
            base_layer.blit(screen, (0, 0))

        if event.type == pygame.KEYDOWN:
            # Change line thickness
            if event.key == pygame.K_EQUALS:
                THICKNESS += 1
            if event.key == pygame.K_MINUS:
                THICKNESS = max(1, THICKNESS - 1)

            # Adjust eraser size
            if event.key == pygame.K_LEFTBRACKET:
                ERASER_SIZE = max(5, ERASER_SIZE - 5)
            if event.key == pygame.K_RIGHTBRACKET:
                ERASER_SIZE += 5

            # Switch between shapes
            if event.key == pygame.K_r:
                draw_mode = "rectangle"
            if event.key == pygame.K_c:
                draw_mode = "circle"
            if event.key == pygame.K_l:
                draw_mode = "line"
            if event.key == pygame.K_e:
                screen.fill((0, 0, 0))
            if event.key == pygame.K_q:
                draw_mode = "square"
            if event.key == pygame.K_t:
                draw_mode = "right_triangle"
            if event.key == pygame.K_s:
                draw_mode = "equilateral_triangle"
            if event.key == pygame.K_b:
                draw_mode = "rhombus"

            # Switch colors
            if event.key == pygame.K_1:
                current_color = colors["red"]
            if event.key == pygame.K_2:
                current_color = colors["blue"]
            if event.key == pygame.K_3:
                current_color = colors["black"]
            if event.key == pygame.K_4:
                current_color = colors["green"]

    pygame.display.flip()  # Update the screen
    clock.tick(60)  # Limit FPS to 60

pygame.quit()  # Exit pygame