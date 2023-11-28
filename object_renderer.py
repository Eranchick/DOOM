import pygame as pg
from settings import *

class ObjectRenderer:
    def __init__(self, game):
        self.game = game
        self.screen = game.screen
        self.wall_textures = self.load_wall_textures()
        self.sky_image = self.get_texture('resources/textures/sky.png', (WIDTH, HALF_HEIGHT))
        self.sky_offset = 0
        self.blood_screen = self.get_texture('resources/textures/blood_screen.png', RES)
        self.digit_size = int((HEIGHT / (15 * SCREEN_RES_SCALE)) * SCREEN_RES_SCALE)
        self.digit_images = [self.get_texture(f'resources/textures/digits/{i}.png', [self.digit_size] * 2)
                             for i in range(12)]  # keys 0-9 is nums, 10 is %, 11 is -
        self.digits = dict(zip(map(str, range(12)), self.digit_images))
        self.game_over_image = self.get_texture('resources/textures/game_over.png', RES)
        self.win_image = self.get_texture('resources/textures/win.png', RES)
        self.arial_font = None


    def draw(self):
        self.draw_background()
        self.render_game_object()
        self.draw_ui()

    def draw_ui(self):
        self.draw_back()
        self.draw_player_armor()
        self.draw_player_health()
        self.draw_ammo()

    def win(self):
        self.screen.blit(self.win_image, (0, 0))

    def game_over(self):
        self.screen.blit(self.game_over_image, (0, 0))

    def draw_player_health(self):
        health = str(self.game.player.health)
        for i, char in enumerate(health):
            self.screen.blit(self.digits[char], (i * self.digit_size + 450 * SCREEN_RES_SCALE, HEIGHT - self.digit_size - (77 * SCREEN_RES_SCALE)))
        self.screen.blit(self.digits['10'], ((i + 1) * self.digit_size + 450 * SCREEN_RES_SCALE, HEIGHT - self.digit_size - (77 * SCREEN_RES_SCALE)))

    def draw_player_armor(self):
        armor = str(self.game.player.armor)
        for i, char in enumerate(armor):
            self.screen.blit(self.digits[char],
                             (i * self.digit_size + 1000 * SCREEN_RES_SCALE, HEIGHT - self.digit_size - (77 * SCREEN_RES_SCALE)))
        self.screen.blit(self.digits['10'],
                         ((i + 1) * self.digit_size + 1000 * SCREEN_RES_SCALE, HEIGHT - self.digit_size - (77 * SCREEN_RES_SCALE)))

    def draw_back(self):
        pass

    def draw_debug(self):
        pass

    def draw_ammo(self):
        ammo = str(self.game.weapon.ammo)
        for i, char in enumerate(ammo):
            if char == '-':
                char = '11'
            self.screen.blit(self.digits[char],
                             (i * self.digit_size + 50, HEIGHT - self.digit_size - (77 * SCREEN_RES_SCALE)))

    def player_damage(self):
        self.screen.blit(self.blood_screen, (0, 0))

    def draw_background(self):
        self.sky_offset = (self.sky_offset + 4.5 * self.game.player.rel) % WIDTH
        self.screen.blit(self.sky_image, (-self.sky_offset, 0))
        self.screen.blit(self.sky_image, (-self.sky_offset + WIDTH, 0))
        # floor
        pg.draw.rect(self.screen, FLOOR_COLOR, (0, HALF_HEIGHT, WIDTH, HEIGHT))

    def render_game_object(self):
        list_objects = sorted(self.game.raycasting.objects_to_render, key=lambda t: t[0], reverse=True)
        for depth, image, pos in list_objects:
            self.screen.blit(image, pos)

    @staticmethod
    def get_texture(path, res=(TEXTURE_SIZE, TEXTURE_SIZE)):
        texture = pg.image.load(path).convert_alpha()
        return pg.transform.scale(texture, res)

    def load_wall_textures(self):
        return {
            1: self.get_texture('resources/textures/1.png'),
            2: self.get_texture('resources/textures/2.png'),
            3: self.get_texture('resources/textures/3.png'),
            4: self.get_texture('resources/textures/4.png'),
            5: self.get_texture('resources/textures/5.png'),
        }
