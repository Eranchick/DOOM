import math

from settings import *
from pygame import *
from object_renderer import *

class UI:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.digit_size = int((HEIGHT / (15 * SCREEN_RES_SCALE)) * SCREEN_RES_SCALE)
        self.digit_images = [self.get_texture(f'resources/textures/digits/{i}.png', [self.digit_size] * 2)
                             for i in range(12)]  # keys 0-9 is nums, 10 is %, 11 is -
        self.digits = dict(zip(map(str, range(12)), self.digit_images))
        self.in_level_ui = self.get_texture('resources/textures/UI/in_level.png', (WIDTH, WIDTH / 11.636363636363))
        self.in_level_ui_height = self.in_level_ui.get_height()

        self.face_size = int((HEIGHT / (8 * SCREEN_RES_SCALE)) * SCREEN_RES_SCALE)

    def update(self):
        self.draw_ui()

    def draw_ui(self):
        # back
        self.screen.blit(self.in_level_ui, (0, HEIGHT - self.in_level_ui_height))

        # health
        health = str(self.game.player.health)
        for i, char in enumerate(health):
            self.screen.blit(self.digits[char], (
            i * self.digit_size + WIDTH * 0.26125, HEIGHT - self.digit_size - (60 * SCREEN_RES_SCALE)))
        self.screen.blit(self.digits['10'], (
        (i + 1) * self.digit_size + WIDTH * 0.26125, HEIGHT - self.digit_size - (60 * SCREEN_RES_SCALE)))

        # armor
        armor = str(self.game.player.armor)
        for i, char in enumerate(armor):
            self.screen.blit(self.digits[char],
                             (i * self.digit_size + WIDTH * 0.61, HEIGHT - self.digit_size - (60 * SCREEN_RES_SCALE)))
        self.screen.blit(self.digits['10'],
                         ((i + 1) * self.digit_size + WIDTH * 0.61, HEIGHT - self.digit_size - (60 * SCREEN_RES_SCALE)))

        # ammo
        ammo = str(self.game.weapon.ammo)
        for i, char in enumerate(ammo):
            if char == '-':
                char = '11'
            self.screen.blit(self.digits[char],
                             (i * self.digit_size + (WIDTH * 0.06625),
                              HEIGHT - self.digit_size - (60 * SCREEN_RES_SCALE)))

        # face
        self.face()

    def face(self):
        health = self.game.player.health
        angle = self.game.player.angle
        pos = self.game.player.pos
        p_forward = pos[0] + self.game.raycasting.straight_ox, pos[1] + self.game.raycasting.straight_oy
        closest_npc_pos = (9999 + self.game.player.pos[0], self.game.player.pos[1])
        npc_in_radius = False
        seeing_npc = False
        for npc in self.game.object_handler.npc_list:
            dist = math.sqrt(abs(npc.x - self.game.player.x) ** 2 + abs(npc.y - self.game.player.y) ** 2)
            if dist <= 15:
                closest_npc_pos = npc.x, npc.y
                npc_in_radius = True
                if seeing_npc != True:
                    seeing_npc = npc.ray_cast_value

        v2 = (pos[0] - p_forward[0], pos[1] - p_forward[1])
        v1 = (closest_npc_pos[0] - pos[0], closest_npc_pos[1] - pos[1])  # in development
        angle2 = math.atan2(v2[1], v2[0]) - math.atan2(v1[1], v1[0])
        if not npc_in_radius:
            face_index = 1
        elif seeing_npc and (angle2 <= HALF_FOV):
            face_index = 1
        else:
            face_index = 3

        health_index = (health - 1) // 20
        face_index = 1
        img = self.get_texture(f'resources/textures/UI/doomguy_face/{health_index}/{face_index}.png', (self.face_size, self.face_size))
        self.screen.blit(img,
                         (HALF_WIDTH - img.get_width() / 2,
                          HEIGHT - self.face_size - (12.5 * SCREEN_RES_SCALE)))

    @staticmethod
    def get_texture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)
