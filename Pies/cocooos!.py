import cocos
from cocos.actions import *
from pyglet.window import key
from collections import defaultdict
from cocos.mapcolliders import RectMapCollider
from cocos.scene import Scene
import cocos.collision_model as cm
import cocos.euclid as eu

cocos.director.director.init(caption='C2d', width=700, height=700, resizable=True)


class Actor(cocos.sprite.Sprite):
        def __init__(self, x, y, color):
                super(Actor, self).__init__('spaceship01.png', color=color, scale=0.20)
                self.position = pos = eu.Vector2(x, y)
                self.cshape = cm.CircleShape(pos, self.width / 2)


class ActorN(cocos.sprite.Sprite):
        def __init__(self, x, y):
                super(ActorN, self).__init__('ufo.png', scale=0.20)
                self.position = pos = eu.Vector2(x, y)
                self.cshape = cm.CircleShape(pos, self.width / 2)


class BackLayer(cocos.layer.ScrollableLayer):
        def __init__(self):
                super(BackLayer, self).__init__()
                self.bg = cocos.sprite.Sprite('planet.jpg', position=(500, 500))
                self.add(self.bg)


class MainLayer(cocos.layer.ScrollableLayer):
        is_event_handler = True

        def __init__(self):
                super(MainLayer, self).__init__()
                self.player = Actor(400, 240, color=(255, 255, 255))
                self.add(self.player)

                for pos in [(540, 380), (100, 380)]:
                        self.add(ActorN(pos[0], pos[1]))

                        cell = self.player.width * 1.25
                        self.collman = cm.CollisionManagerGrid(0, 640, 0, 480, cell, cell)

                #self.player.scale = 0.25
                #self.player.position = (355, 500)
                self.speed = 500
                self.pressed = defaultdict(int)
                self.schedule(self.update)

        def on_key_press(self, k, m):
                self.pressed[k] = 1
                print('Pressed', key.symbol_string(k))

        def on_key_release(self, k, m):
                self.pressed[k] = 0
                print('Released', key.symbol_string(k))
                self.player.do(RotateTo(0, 1))

        def update(self, dt):

                self.collman.clear()
                for _, node in self.children:
                        self.collman.add(node)
                for other in self.collman.iter_colliding(self.player):
                        self.remove(other)

                x = self.pressed[key.RIGHT] - self.pressed[key.LEFT]
                y = self.pressed[key.UP] - self.pressed[key.DOWN]

                if x == 1:

                        mr_r = AccelDeccel(MoveBy((10, 0), 30 * self.pressed[x])) | RotateBy(10, 2)
                        self.player.do(mr_r)
                        if self.pressed[key.SPACE]:
                                self.player.do(Jump(0, x * 150, 1, 0.15))

                if x == -1:

                        mr_l = AccelDeccel(MoveBy((-10, 0), 30 * self.pressed[(-x)])) | RotateBy(-10, 2)
                        self.player.do(mr_l)
                        if self.pressed[key.SPACE]:
                                self.player.do(Jump(0, x * 150, 1, 0.15))

                if y == 1:

                        mr_up = AccelDeccel(MoveBy((0, 10), 30 * self.pressed[y]))
                        self.player.do(mr_up)
                        if self.pressed[key.SPACE]:
                                self.player.do(Jump(y * 150, 0, 1, 0.15))

                if y == -1:

                        mr_down = AccelDeccel(MoveBy((0, -10), 30 * self.pressed[(-y)]))
                        self.player.do(mr_down)
                        if self.pressed[key.SPACE]:
                                self.player.do(Jump(y * 150, 0, 1, 0.15))

                #w, h = cocos.director.director.get_window_size()
                #xp, yp = self.player.position

                # if (xp > w):
                        #xp = w - 5

                # elif (xp < 0):
                        #xp = 5

                #self.player.position = eu.Vector2(xp, yp)

                scroll.set_focus(self.player.position[0], self.player.position[1])

                self.player.cshape.center = self.player.position

                # if x != 0 or y != 0:

                        #pos = self.player.position
                        #new_x = pos[0] + self.speed * x * dt
                        #new_y = pos[1] + self.speed * y * dt
                        #self.player.position = (new_x, new_y)


if __name__ == '__main__':

        mlayer = MainLayer()
        blayer = BackLayer()

        scroll = cocos.layer.ScrollingManager()
        scroll.add(blayer)
        scroll.add(mlayer)

        MyScene = cocos.scene.Scene()
        MyScene.add(mlayer, 1)
        MyScene.add(blayer, 0)

        cocos.director.director.run(MyScene)
