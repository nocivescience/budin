from manim import *
import itertools as it
class PracticeScene(Scene):
    def construct(self):
        vector = rotate_vector(RIGHT, PI/4)
        vector2 = rotate_vector(RIGHT, PI/2)
        dot= Dot().move_to(vector)
        dot2= dot.copy().move_to(vector2)
        self.play(Create(dot))
        self.play(Create(dot2))
        self.wait()

class PracticeScene2(Scene):
    diccionario={
        'a': 0,
    }
    def construct(self):
        dot = Dot().add_updater(self.getting_moves)
        path = TracedPath(dot.get_center)
        self.add(dot, path)
        self.wait(2)
    def getting_moves(self, mob, dt):
        self.diccionario['a'] += dt*2
        position = rotate_vector(3*RIGHT, 2*PI+self.diccionario['a'])
        mob.move_to(position- self.diccionario['a']*RIGHT)
        return mob

class VibratingScene(Scene):
    def construct(self):
        dot = Dot()
        random_time = [np.random.random() for _ in range(10)]
        color= interpolate_color(BLUE, RED, 10)
        print(color)
        self.play(
            *it.chain(*[
                (dot.animate.scale(escala).set_color(color[i]),)
                for i, escala in enumerate(random_time)
            ]),
        )
        self.wait()