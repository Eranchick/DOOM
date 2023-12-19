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

        self.face_size = int((HEIGHT / (15 * SCREEN_RES_SCALE)) * SCREEN_RES_SCALE)

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
        closest_npc_pos = (9999 + self.game.player.pos[0], 9999 + self.game.player.pos[1])
        for npc in self.game.object_handler.npc_list:
            dist = math.sqrt(abs(npc.x - self.game.player.x) ** 2 + abs(npc.y - self.game.player.y) ** 2)
            if dist <= 15:
                closest_npc_pos = npc.x, npc.y
        health_index = (health - 1) // 20
        face_index = 0
        if health > 80:
            img = self.get_texture(f'resources/textures/UI/doomguy_face/{health_index}/{face_index}.png', (self.face_size))
            self.screen.blit(img,
                             (HALF_WIDTH,
                              HEIGHT - self.face_size - (60 * SCREEN_RES_SCALE)))

    @staticmethod
    def get_texture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)
