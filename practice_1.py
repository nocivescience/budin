from manim import *
class Budin(Dot):
    def __init__(self, **kwargs):
        super().__init__(**kwargs)
        
class BudinScene(Scene):
    def construct(self):
        budin = Budin()
        
        self.play(Create(budin))
        self.wait()