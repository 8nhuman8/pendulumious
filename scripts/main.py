import pygame
from math import sin, cos, pi
from utils import first_acceleration, \
                  second_acceleration


pygame.init()

width, height = 500, 500

pygame.display.set_caption('Pendulumious')

screen = pygame.display.set_mode((width, height))
clock = pygame.time.Clock()

BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (133, 133, 133)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

gravity = 1
mass1, mass2 = 10, 10
length1, length2 = 100, 100
angle1, angle2 = pi/2, pi/2
anglular_velocity1, angular_velocity2 = 0, 0

scatter1, scatter2 = [], []

ORIGIN = (width // 2, height // 3)
add_offset = lambda x, y: (x + ORIGIN[0], ORIGIN[1] - y)

running = True


while running:
    pygame.display.flip()
    clock.tick(60)

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    screen.fill(WHITE)

    angular_acceleration1 = first_acceleration(
        gravity,
        mass1, mass2,
        length1, length2,
        angle1, angle2,
        anglular_velocity1, angular_velocity2
    )
    angular_acceleration2 = second_acceleration(
        gravity,
        mass1, mass2,
        length1, length2,
        angle1, angle2,
        anglular_velocity1, angular_velocity2
    )

    x1 = int(length1 * sin(angle1))
    y1 = int(-length1 * cos(angle1))

    x2 = int(x1 + length2 * sin(angle2))
    y2 = int(y1 - length2 * cos(angle2))

    scatter1.append(add_offset(x1, y1))
    scatter2.append(add_offset(x2, y2))

    pygame.draw.aalines(screen, GRAY, False, [ORIGIN, add_offset(x1, y1), add_offset(x2, y2)])

    if len(scatter1) > 1:
        pygame.draw.aalines(screen, RED, False, scatter1)
    if len(scatter2) > 1:
        pygame.draw.aalines(screen, GREEN, False, scatter2)

    pygame.draw.circle(screen, BLACK, ORIGIN, 5)
    pygame.draw.circle(screen, BLACK, add_offset(x1, y1), mass1)
    pygame.draw.circle(screen, BLACK, add_offset(x2, y2), mass2)

    anglular_velocity1 += angular_acceleration1
    angular_velocity2 += angular_acceleration2

    angle1 += anglular_velocity1
    angle2 += angular_velocity2


pygame.quit()
quit()
