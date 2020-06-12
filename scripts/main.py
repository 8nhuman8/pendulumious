import pygame
import tkinter as tk

from math import sin, cos, pi
from random import randrange
from os import environ
from platform import system

from utils import first_acceleration, second_acceleration


WIDTH, HEIGTH = 500, 500


root = tk.Tk()
root.title('Pendulumious')
root.resizable(False, False)

embed = tk.Frame(root, width=WIDTH, height=HEIGTH)
embed.pack(side=tk.LEFT)
#embed.grid(row=0, column=0, rowspan=5, columnspan=3)

#parameters = tk.Frame(root, width=500, height=500)
#parameters.pack()

tk.Label(root, text='gravity').pack(side=tk.LEFT, anchor='nw')
gravity = tk.Entry(width=10)
gravity.insert(tk.END, '1')
gravity.pack(side=tk.LEFT, anchor='nw')


environ['SDL_WINDOWID'] = str(embed.winfo_id())
if system == 'Windows':
    environ['SDL_VIDEODRIVER'] = 'windib'


pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGTH))
clock = pygame.time.Clock()


BLACK = (0, 0, 0)
WHITE = (255, 255, 255)
GRAY = (133, 133, 133)
RED = (255, 0, 0)
GREEN = (0, 255, 0)

GRAVITY = 1
MASS1, MASS2 = 4, 5
LENGTH1, LENGTH2 = 100, 100
ORIGIN = (WIDTH // 2, HEIGTH // 3)

add_offset = lambda x, y: (x + ORIGIN[0], ORIGIN[1] - y)

angle1, angle2 = randrange(0, 10), randrange(0, 10)
anglular_velocity1, angular_velocity2 = 0, 0
scatter1, scatter2 = [], []
running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False

    angular_acceleration1 = first_acceleration(
        GRAVITY,
        MASS1, MASS2,
        LENGTH1, LENGTH2,
        angle1, angle2,
        anglular_velocity1, angular_velocity2
    )
    angular_acceleration2 = second_acceleration(
        GRAVITY,
        MASS1, MASS2,
        LENGTH1, LENGTH2,
        angle1, angle2,
        anglular_velocity1, angular_velocity2
    )

    x1 = int(LENGTH1 * sin(angle1))
    y1 = int(-LENGTH1 * cos(angle1))

    x2 = int(x1 + LENGTH2 * sin(angle2))
    y2 = int(y1 - LENGTH2 * cos(angle2))

    scatter1.append(add_offset(x1, y1))
    scatter2.append(add_offset(x2, y2))


    screen.fill(GRAY)

    pygame.draw.aalines(
        screen, WHITE, False, [
            ORIGIN,
            add_offset(x1, y1),
            add_offset(x2, y2)
        ]
    )

    if len(scatter1) > 1:
        pygame.draw.aalines(screen, RED, False, scatter1)
    if len(scatter2) > 1:
        pygame.draw.aalines(screen, GREEN, False, scatter2)

    pygame.draw.circle(screen, BLACK, ORIGIN, 5)
    pygame.draw.circle(screen, BLACK, add_offset(x1, y1), MASS1)
    pygame.draw.circle(screen, BLACK, add_offset(x2, y2), MASS2)


    pygame.display.flip()
    clock.tick(30)
    root.update()


    anglular_velocity1 += angular_acceleration1
    angular_velocity2 += angular_acceleration2

    angle1 += anglular_velocity1
    angle2 += angular_velocity2


pygame.quit()
quit()
