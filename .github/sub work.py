import pygame
import math

# Initialize pygame
pygame.init()

# Constants
WIDTH, HEIGHT = 600, 600
FPS = 60
CENTER = (WIDTH // 2, HEIGHT // 2)
RADIUS = 200
NUM_CARS = 8

# Colors
WHITE = (0,0,0)
BLACK = (0,0,0)
RED = (0,0,0)
BLUE = (0,0,0)
LIME = (0,0,0)

#Setup display
screen = pygame.display.set_mode((WIDTH, HEIGHT))
pygame.display.set_caption("Rotating Ferris Wheel")
clock = pygame.time.Clock()
angle = 0 # Initial angle

running = True
while running:
    screen.fill(LIME)

# Draw wheel circle
pygame.draw.circle(screen, BLACK, CENTER, RADIUS, 3)

# Draw central hub
pygame.draw.circle(screen, BLUE, CENTER, 10)

# Update car positions
for i in range(NUM_CARS):
    car_angle = angle + (i* (360/NUM_CARS)) # Distribute cars evenly
    radian_angle = math.radians(car_angle)
    car_x = CENTER[0] + RADIUS * math.cos(radian_angle)
    car_y = CENTER[1] + RADIUS * math.sin(radian_angle)
    # Draw passenger car
    pygame.draw.circle(screen, RED, (int(car_x), int(car_y)), 15)

# Update display
pygame.display.flip()

# Increment angle for rotation
angle += 1 # Adjust speed of rotation if needed

# Handle events
for event in pygame.event.get():
    if event.type == pygame.QUIT:
        running = False

clock.tick(FPS)