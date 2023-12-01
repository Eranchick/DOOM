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
        self.in_level_ui = self.get_texture('resources/textures/UI/HealAmAr.png', (WIDTH, HEIGHT))

    def update(self):
        self.draw_ui()

    def draw_ui(self):
        self.draw_back()
        self.draw_player_armor()
        self.draw_player_health()
        self.draw_ammo()

    def draw_back(self):
        self.screen.blit(self.in_level_ui, (0, 0))

    def draw_ammo(self):
        ammo = str(self.game.weapon.ammo)
        for i, char in enumerate(ammo):
            if char == '-':
                char = '11'
            self.screen.blit(self.digits[char],
                             (i * self.digit_size + (WIDTH * 0.06625), HEIGHT - self.digit_size - (77 * SCREEN_RES_SCALE)))

    def draw_player_health(self):
        health = str(self.game.player.health)
        for i, char in enumerate(health):
            self.screen.blit(self.digits[char], (i * self.digit_size + WIDTH * 0.28125, HEIGHT - self.digit_size - (77 * SCREEN_RES_SCALE)))
        self.screen.blit(self.digits['10'], ((i + 1) * self.digit_size + WIDTH * 0.28125, HEIGHT - self.digit_size - (77 * SCREEN_RES_SCALE)))

    def draw_player_armor(self):
        armor = str(self.game.player.armor)
        for i, char in enumerate(armor):
            self.screen.blit(self.digits[char],
                             (i * self.digit_size + WIDTH * 0.61, HEIGHT - self.digit_size - (77 * SCREEN_RES_SCALE)))
        self.screen.blit(self.digits['10'],
                         ((i + 1) * self.digit_size + WIDTH * 0.61, HEIGHT - self.digit_size - (77 * SCREEN_RES_SCALE)))

    @staticmethod
    def get_texture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)
