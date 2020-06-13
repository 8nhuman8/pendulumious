import pygame
import tkinter as tk

from math import sin, cos, pi
from random import randrange
from os import environ
from platform import system

from utils import first_acceleration, second_acceleration


WIDTH, HEIGTH = 500, 500
ORIGIN = (WIDTH // 2, HEIGTH // 3)
add_offset = lambda x, y: (x + ORIGIN[0], ORIGIN[1] - y)


root = tk.Tk()
root.title('Pendulumious')
root.resizable(False, False)

embed = tk.Frame(root, width=WIDTH, height=HEIGTH)
embed.grid(row=0, column=0)

parameters = tk.Frame(root, width=400, height=500)
parameters.grid(row=0, column=1)
parameters.grid_propagate(False)

tk.Label(parameters, text='Gravity').grid(row=0, column=0)
gravity_entry = tk.Scale(parameters, from_=1, to=20, orient=tk.HORIZONTAL)
gravity_entry.grid(row=0, column=1)
gravity_entry.set(1)

tk.Label(parameters, text='FPS').grid(row=0, column=2)
fps_entry = tk.Scale(parameters, from_=1, to=144, orient=tk.HORIZONTAL)
fps_entry.grid(row=0, column=3)
fps_entry.set(30)

tk.Label(parameters, text='Mass 1').grid(row=1, column=0)
mass1_entry = tk.Scale(parameters, from_=1, to=20, orient=tk.HORIZONTAL)
mass1_entry.grid(row=1, column=1)
mass1_entry.set(5)

tk.Label(parameters, text='Mass 2').grid(row=1, column=2)
mass2_entry = tk.Scale(parameters, from_=1, to=20, orient=tk.HORIZONTAL)
mass2_entry.grid(row=1, column=3)
mass2_entry.set(5)

tk.Label(parameters, text='Length 1').grid(row=2, column=0)
length1_entry = tk.Scale(parameters, from_=50, to=200, orient=tk.HORIZONTAL)
length1_entry.grid(row=2, column=1)
length1_entry.set(100)

tk.Label(parameters, text='Length 2').grid(row=2, column=2)
length2_entry = tk.Scale(parameters, from_=50, to=200, orient=tk.HORIZONTAL)
length2_entry.grid(row=2, column=3)
length2_entry.set(100)

tk.Label(parameters, text='Background color').grid(row=3, column=0)
bg_color_r_entry = tk.Scale(parameters, from_=0, to=255, orient=tk.HORIZONTAL)
bg_color_r_entry.grid(row=3, column=1)
bg_color_r_entry.set(133)
bg_color_g_entry = tk.Scale(parameters, from_=0, to=255, orient=tk.HORIZONTAL)
bg_color_g_entry.grid(row=3, column=2)
bg_color_g_entry.set(133)
bg_color_b_entry = tk.Scale(parameters, from_=0, to=255, orient=tk.HORIZONTAL)
bg_color_b_entry.grid(row=3, column=3)
bg_color_b_entry.set(133)

tk.Label(parameters, text='Dots color').grid(row=4, column=0)
dots_color_r_entry = tk.Scale(parameters, from_=0, to=255, orient=tk.HORIZONTAL)
dots_color_r_entry.grid(row=4, column=1)
dots_color_r_entry.set(0)
dots_color_g_entry = tk.Scale(parameters, from_=0, to=255, orient=tk.HORIZONTAL)
dots_color_g_entry.grid(row=4, column=2)
dots_color_g_entry.set(0)
dots_color_b_entry = tk.Scale(parameters, from_=0, to=255, orient=tk.HORIZONTAL)
dots_color_b_entry.grid(row=4, column=3)
dots_color_b_entry.set(0)

tk.Label(parameters, text='Trail 1 color').grid(row=5, column=0)
trail1_color_r_entry = tk.Scale(parameters, from_=0, to=255, orient=tk.HORIZONTAL)
trail1_color_r_entry.grid(row=5, column=1)
trail1_color_r_entry.set(255)
trail1_color_g_entry = tk.Scale(parameters, from_=0, to=255, orient=tk.HORIZONTAL)
trail1_color_g_entry.grid(row=5, column=2)
trail1_color_g_entry.set(0)
trail1_color_b_entry = tk.Scale(parameters, from_=0, to=255, orient=tk.HORIZONTAL)
trail1_color_b_entry.grid(row=5, column=3)
trail1_color_b_entry.set(0)

tk.Label(parameters, text='Trail 2 color').grid(row=6, column=0)
trail2_color_r_entry = tk.Scale(parameters, from_=0, to=255, orient=tk.HORIZONTAL)
trail2_color_r_entry.grid(row=6, column=1)
trail2_color_r_entry.set(0)
trail2_color_g_entry = tk.Scale(parameters, from_=0, to=255, orient=tk.HORIZONTAL)
trail2_color_g_entry.grid(row=6, column=2)
trail2_color_g_entry.set(255)
trail2_color_b_entry = tk.Scale(parameters, from_=0, to=255, orient=tk.HORIZONTAL)
trail2_color_b_entry.grid(row=6, column=3)
trail2_color_b_entry.set(0)

for i in range(4):
    parameters.grid_columnconfigure(i, weight=1)


environ['SDL_WINDOWID'] = str(embed.winfo_id())
if system == 'Windows':
    environ['SDL_VIDEODRIVER'] = 'windib'


pygame.init()

screen = pygame.display.set_mode((WIDTH, HEIGTH))
clock = pygame.time.Clock()


gravity = None
mass1, mass2 = None, None
length1, length2 = None, None

angle1, angle2 = randrange(0, 10), randrange(0, 10)
anglular_velocity1, angular_velocity2 = 0, 0
trail1, trail2 = [], []
running = True


while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False


    gravity = gravity_entry.get()
    fps = fps_entry.get()
    mass1 = mass1_entry.get()
    mass2 = mass2_entry.get()
    length1 = length1_entry.get()
    length2 = length2_entry.get()
    bg_color = (
        bg_color_r_entry.get(),
        bg_color_g_entry.get(),
        bg_color_b_entry.get()
    )
    dots_color = (
        dots_color_r_entry.get(),
        dots_color_g_entry.get(),
        dots_color_b_entry.get()
    )
    trail1_color = (
        trail1_color_r_entry.get(),
        trail1_color_g_entry.get(),
        trail1_color_b_entry.get()
    )
    trail2_color = (
        trail2_color_r_entry.get(),
        trail2_color_g_entry.get(),
        trail2_color_b_entry.get()
    )

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

    trail1.append(add_offset(x1, y1))
    trail2.append(add_offset(x2, y2))


    screen.fill(bg_color)

    pygame.draw.aalines(
        screen, WHITE, False, [
            ORIGIN,
            add_offset(x1, y1),
            add_offset(x2, y2)
        ]
    )

    if len(trail1) > 1:
        pygame.draw.aalines(screen, trail1_color, False, trail1)
    if len(trail2) > 1:
        pygame.draw.aalines(screen, trail2_color, False, trail2)

    pygame.draw.circle(screen, dots_color, ORIGIN, 5)
    pygame.draw.circle(screen, dots_color, add_offset(x1, y1), mass1)
    pygame.draw.circle(screen, dots_color, add_offset(x2, y2), mass2)


    pygame.display.flip()
    clock.tick(fps)
    root.update()


    anglular_velocity1 += angular_acceleration1
    angular_velocity2 += angular_acceleration2

    angle1 += anglular_velocity1
    angle2 += angular_velocity2


pygame.quit()
quit()
