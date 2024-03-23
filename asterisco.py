from manim import *
import itertools as it
class Example1Scene(Scene):
    def construct(self):
        circle = Circle()
        square = Square()
        self.play(Create(circle))
        self.play(Transform(circle, square))
        self.wait()
class Example2Scene(Scene):
    def construct(self):
        objetos = [Circle(), Square()]
        self.play(Transform(*objetos))
        self.wait()

# Sin usar *
class SinAsterisco(Scene):
    def construct(self):
        circulo = FadeIn(Circle())
        cuadrado = FadeIn(Square())
        triangulo = FadeIn(Triangle())
        self.play(circulo, cuadrado, triangulo)

# Usando *
class ConAsterisco(Scene):
    def construct(self):
        formas = [FadeIn(Circle()), FadeIn(Square()), FadeIn(Triangle())]
        self.play(*formas)

class VMobjectExample(Scene):
    def construct(self):
        path= VMobject()
        path.set_points_as_corners([LEFT,LEFT+UP,UP])
        self.play(Create(path))
        self.wait()

class VMobject2Example(Scene):
    def construct(self):
        path= VMobject()
        puntos = [LEFT, LEFT+UP, UP]
        path.set_points_as_corners(*[puntos])
        self.play(Create(path))
        self.wait()