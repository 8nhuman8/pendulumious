from math import sin, cos
from random import randrange
from os import environ
from platform import system
from tkinter import Tk, Frame, Button, SUNKEN, RAISED, W, E

from pygame import init, QUIT
from pygame import quit as pygame_quit
from pygame.event import get as get_events
from pygame.time import Clock
from pygame.display import set_mode, flip
from pygame.draw import aalines, circle, line, aaline

from utils import first_acceleration, second_acceleration
from widgets_frame import WidgetsFrame


WIDTH, HEIGTH = 500, 500

ORIGIN = (WIDTH // 2, HEIGTH // 3)
add_offset = lambda x, y: (x + ORIGIN[0], ORIGIN[1] - y)

pause = False
first_frame_will_be_shown = True
reset = False


root = Tk()
root.title('Pendulumious')
root.resizable(False, False)

embed = Frame(root, width=WIDTH, height=HEIGTH)
embed.grid(row=0, column=0)

widgets = WidgetsFrame(root, width=WIDTH, height=HEIGTH)
widgets.grid(row=0, column=1)
widgets.grid_propagate(False)

def pause_button_behavior():
    global pause

    if pause:
        pause_button.config(relief=RAISED)
    else:
        pause_button.config(relief=SUNKEN)

    pause = not pause

def reset_button_behavior():
    global reset
    reset = True

pause_button = Button(widgets, text='Pause', command=pause_button_behavior)
pause_button.config(relief=SUNKEN)
pause_button.grid(
    row=10, column=0,
    columnspan=2, sticky=W + E,
    padx=(10,), pady=(10,)
)

reset_button = Button(widgets, text='Reset', command=reset_button_behavior)
reset_button.grid(
    row=10, column=2,
    columnspan=2, sticky=W + E,
    padx=(10,), pady=(10,)
)


environ['SDL_WINDOWID'] = str(embed.winfo_id())
if system() == 'Windows':
    environ['SDL_VIDEODRIVER'] = 'windib'


init()

screen = set_mode((WIDTH, HEIGTH))
clock = Clock()


gravity = None
mass1, mass2 = None, None
length1, length2 = None, None

angle1, angle2 = randrange(0, 10), randrange(0, 10)
anglular_velocity1, angular_velocity2 = 0, 0
trail1, trail2 = [], []


running = True

def stop_running():
    global running
    running = False

root.protocol('WM_DELETE_WINDOW', stop_running)


while running:
    if reset:
        angle1, angle2 = randrange(0, 10), randrange(0, 10)
        anglular_velocity1, angular_velocity2 = 0, 0
        trail1, trail2 = [], []

        pause_button.config(relief=SUNKEN)
        first_frame_will_be_shown = True
        reset = False


    if not pause:
        for event in get_events():
            if event.type == QUIT:
                running = False


        gravity = widgets.gravity.get()
        fps = widgets.fps.get()

        mass1 = widgets.mass1.get()
        mass2 = widgets.mass2.get()

        length1 = widgets.length1.get()
        length2 = widgets.length2.get()

        bg_color = (
            widgets.bg_color_r.get(),
            widgets.bg_color_g.get(),
            widgets.bg_color_b.get()
        )
        dots_color = (
            widgets.dots_color_r.get(),
            widgets.dots_color_g.get(),
            widgets.dots_color_b.get()
        )
        trail1_color = (
            widgets.trail1_color_r.get(),
            widgets.trail1_color_g.get(),
            widgets.trail1_color_b.get()
        )
        trail2_color = (
            widgets.trail2_color_r.get(),
            widgets.trail2_color_g.get(),
            widgets.trail2_color_b.get()
        )
        joints_color = (
            widgets.joints_color_r.get(),
            widgets.joints_color_g.get(),
            widgets.joints_color_b.get()
        )

        use_fade1 = widgets.use_fade1.get()
        make_fade_bold1 = widgets.make_fade_bold1.get()

        use_fade2 = widgets.use_fade2.get()
        make_fade_bold2 = widgets.make_fade_bold2.get()

        fade_length1 = widgets.fade_length1.get()
        fade_length2 = widgets.fade_length2.get()

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

        aalines(
            screen, joints_color, False, [
                ORIGIN,
                add_offset(x1, y1),
                add_offset(x2, y2)
            ]
        )

        if len(trail1) > 1 and not use_fade1:
            aalines(screen, trail1_color, False, trail1)
        if len(trail2) > 1 and not use_fade2:
            aalines(screen, trail2_color, False, trail2)

        if use_fade1:
            while len(trail1) > fade_length1:
                trail1.pop(0)
            for i in range(len(trail1) - 1):

                r = widgets.trail1_color_r.get() + (len(trail1) - i) * 25
                g = widgets.trail1_color_g.get() + (len(trail1) - i) * 25
                b = widgets.trail1_color_b.get() + (len(trail1) - i) * 25

                if r > 255: r = 255
                if g > 255: g = 255
                if b > 255: b = 255

                start_position = (int(trail1[i][0]), int(trail1[i][1]))
                end_position = (int(trail1[i + 1][0]), int(trail1[i + 1][1]))

                if make_fade_bold1:
                    line(screen, (r, g, b), start_position, end_position, mass1)
                else:
                    aaline(screen, (r, g, b), start_position, end_position)

        if use_fade2:
            while len(trail2) > fade_length2:
                trail2.pop(0)
            for i in range(len(trail2) - 1):

                r = widgets.trail2_color_r.get() + (len(trail2) - i) * 25
                g = widgets.trail2_color_g.get() + (len(trail2) - i) * 25
                b = widgets.trail2_color_b.get() + (len(trail2) - i) * 25

                if r > 255: r = 255
                if g > 255: g = 255
                if b > 255: b = 255

                start_position = (int(trail2[i][0]), int(trail2[i][1]))
                end_position = (int(trail2[i + 1][0]), int(trail2[i + 1][1]))

                if make_fade_bold2:
                    line(screen, (r, g, b), start_position, end_position, mass2)
                else:
                    aaline(screen, (r, g, b), start_position, end_position)

        circle(screen, dots_color, ORIGIN, 5)
        circle(screen, dots_color, add_offset(x1, y1), mass1)
        circle(screen, dots_color, add_offset(x2, y2), mass2)


        flip()
        clock.tick(fps)


        anglular_velocity1 += angular_acceleration1
        angular_velocity2 += angular_acceleration2

        angle1 += anglular_velocity1
        angle2 += angular_velocity2


    if first_frame_will_be_shown:
        pause = True
    first_frame_will_be_shown = False


    root.update_idletasks()
    root.update()


pygame_quit()
quit()
