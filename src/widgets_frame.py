from tkinter import Frame, IntVar, BooleanVar, Label, Scale, Checkbutton, HORIZONTAL

class WidgetsFrame(Frame):
    def __init__(self, parent, *args, **kwargs):
        Frame.__init__(self, parent, *args, **kwargs)

        self.gravity = IntVar(value=1)
        self.fps = IntVar(value=30)

        self.mass1 = IntVar(value=5)
        self.mass2 = IntVar(value=5)

        self.length1 = IntVar(value=100)
        self.length2 = IntVar(value=100)

        self.bg_color_r = IntVar(value=255)
        self.bg_color_g = IntVar(value=255)
        self.bg_color_b = IntVar(value=255)

        self.dots_color_r = IntVar(value=0)
        self.dots_color_g = IntVar(value=0)
        self.dots_color_b = IntVar(value=0)

        self.trail1_color_r = IntVar(value=255)
        self.trail1_color_g = IntVar(value=0)
        self.trail1_color_b = IntVar(value=0)

        self.trail2_color_r = IntVar(value=0)
        self.trail2_color_g = IntVar(value=255)
        self.trail2_color_b = IntVar(value=0)

        self.joints_color_r = IntVar(value=133)
        self.joints_color_g = IntVar(value=133)
        self.joints_color_b = IntVar(value=133)

        self.use_fade1 = BooleanVar(value=True)
        self.make_fade_bold1 = BooleanVar(value=True)

        self.use_fade2 = BooleanVar(value=True)
        self.make_fade_bold2 = BooleanVar(value=True)

        self.fade_length1 = IntVar(value=20)
        self.fade_length2 = IntVar(value=20)

        self.__set_widgets()

        for i in range(4):
            self.grid_columnconfigure(i, weight=1)


    def __set_widgets(self):
        Label(self, text='Gravity').grid(row=0, column=0)
        Scale(self, from_=1, to=20, orient=HORIZONTAL, variable=self.gravity).grid(row=0, column=1)

        Label(self, text='FPS').grid(row=0, column=2)
        Scale(self, from_=1, to=144, orient=HORIZONTAL, variable=self.fps).grid(row=0, column=3)

        Label(self, text='Mass 1').grid(row=1, column=0)
        Scale(self, from_=1, to=20, orient=HORIZONTAL, variable=self.mass1).grid(row=1, column=1)

        Label(self, text='Mass 2').grid(row=1, column=2)
        Scale(self, from_=1, to=20, orient=HORIZONTAL, variable=self.mass2).grid(row=1, column=3)

        Label(self, text='Length 1').grid(row=2, column=0)
        Scale(self, from_=20, to=200, orient=HORIZONTAL, variable=self.length1).grid(row=2, column=1)

        Label(self, text='Length 2').grid(row=2, column=2)
        Scale(self, from_=20, to=200, orient=HORIZONTAL, variable=self.length2).grid(row=2, column=3)

        Label(self, text='Background color').grid(row=3, column=0)
        Scale(self, from_=0, to=255, orient=HORIZONTAL, variable=self.bg_color_r).grid(row=3, column=1)
        Scale(self, from_=0, to=255, orient=HORIZONTAL, variable=self.bg_color_g).grid(row=3, column=2)
        Scale(self, from_=0, to=255, orient=HORIZONTAL, variable=self.bg_color_b).grid(row=3, column=3)

        Label(self, text='Dots color').grid(row=4, column=0)
        Scale(self, from_=0, to=255, orient=HORIZONTAL, variable=self.dots_color_r).grid(row=4, column=1)
        Scale(self, from_=0, to=255, orient=HORIZONTAL, variable=self.dots_color_g).grid(row=4, column=2)
        Scale(self, from_=0, to=255, orient=HORIZONTAL, variable=self.dots_color_b).grid(row=4, column=3)

        Label(self, text='Trail 1 color').grid(row=5, column=0)
        Scale(self, from_=0, to=255, orient=HORIZONTAL, variable=self.trail1_color_r).grid(row=5, column=1)
        Scale(self, from_=0, to=255, orient=HORIZONTAL, variable=self.trail1_color_g).grid(row=5, column=2)
        Scale(self, from_=0, to=255, orient=HORIZONTAL, variable=self.trail1_color_b).grid(row=5, column=3)

        Label(self, text='Trail 2 color').grid(row=6, column=0)
        Scale(self, from_=0, to=255, orient=HORIZONTAL, variable=self.trail2_color_r).grid(row=6, column=1)
        Scale(self, from_=0, to=255, orient=HORIZONTAL, variable=self.trail2_color_g).grid(row=6, column=2)
        Scale(self, from_=0, to=255, orient=HORIZONTAL, variable=self.trail2_color_b).grid(row=6, column=3)

        Label(self, text='Joints color').grid(row=7, column=0)
        Scale(self, from_=0, to=255, orient=HORIZONTAL, variable=self.joints_color_r).grid(row=7, column=1)
        Scale(self, from_=0, to=255, orient=HORIZONTAL, variable=self.joints_color_g).grid(row=7, column=2)
        Scale(self, from_=0, to=255, orient=HORIZONTAL, variable=self.joints_color_b).grid(row=7, column=3)

        Label(self, text='1st joint fading').grid(row=8, column=0)
        Checkbutton(self, text='Use fade', variable=self.use_fade1).grid(row=8, column=1)
        Checkbutton(self, text='Make fade bold', variable=self.make_fade_bold1).grid(row=8, column=2)
        Scale(self, label='Length', from_=2, to=50, orient=HORIZONTAL, variable=self.fade_length1).grid(row=8, column=3)

        Label(self, text='2nd joint fading').grid(row=9, column=0)
        Checkbutton(self, text='Use fade', variable=self.use_fade2).grid(row=9, column=1)
        Checkbutton(self, text='Make fade bold', variable=self.make_fade_bold2).grid(row=9, column=2)
        Scale(self, label='Length', from_=2, to=50, orient=HORIZONTAL, variable=self.fade_length2).grid(row=9, column=3)
