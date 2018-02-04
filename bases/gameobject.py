from bases import vector2d

class GameObject:
    def __init__(self):
        self.position = vector2d.ZERO
        self.renderer = None

    def run(self):
        pass

    def render(self, qp):
        if self.renderer is not None:
            self.renderer.render(qp, self.position)

game_objects = []

def add_game_object(new_game_object):
    game_objects.append(new_game_object)

def render_all(qp):
    for game_object in game_objects:
        game_object.render(qp)

def run_all():
    for game_object in game_objects:
        game_object.run()
