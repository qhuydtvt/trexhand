from bases import vector2d

class GameObject:
    def __init__(self):
        self.position = vector2d.ZERO()
        self.screen_position = vector2d.ZERO()
        self.renderer = None
        self.active = True
        self.children = []

    def run(self, parent):
        if parent is not None:
            self.screen_position = parent.position.add(self.position)
        else:
            self.screen_position = self.position
        for child in self.children:
            if child.active:
                child.run(self)

    def render(self, qp, parent_position):
        draw_position = parent_position.add(self.position)
        if self.renderer is not None:
            self.renderer.render(qp, draw_position)
        for child in self.children:
            if child.active:
                child.render(qp, draw_position)

game_objects = []

def game_object_count():
    return len(game_objects)

def recycle(t):
    for game_object in game_objects:
        if not game_object.active and type(game_object) == t:
            game_object.active = True
            return game_object
    new_game_object = t()
    game_objects.append(new_game_object)
    return new_game_object

def add_game_object(new_game_object):
    game_objects.append(new_game_object)

def render_all(qp):
    for game_object in game_objects:
        if game_object.active:
            game_object.render(qp, vector2d.ZERO())

def run_all():
    for game_object in game_objects:
        if game_object.active:
            game_object.run(None)
