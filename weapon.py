from sprite_object import *
from settings import *


class Weapon(AnimatedSprite):
    def __init__(self, game, path='resources/sprites/weapon/'):
        self.to_update_weapon = False

        self.game = game
        self.path = path
        self.root_path = self.path
        self.weapon_index = 0  # index in self.weapons_inventory list
        self.weapons = ('hands', 'shotgun', 'chainsaw', '2-shotgun', 'bfg', 'gun', 'machinegun', 'plasmagun', 'rpg')  # all weapons of game
        self.weapons_inventory = ['hands', 'machinegun']

        self.weapons_max_attack_dist = {'shotgun': 20, 'chainsaw': 4, 'hands': 4, '2-shotgun': 20, 'bfg': 15, 'gun': 10, 'machinegun': 15, 'plasmagun': 17, 'rpg': 25}  # max attack distance
        self.weapons_damage = {'shotgun': 50, 'chainsaw': 150, 'hands': 20, '2-shotgun': 100, 'bfg': 600, 'gun': 30, 'machinegun': 10, 'plasmagun': 25, 'rpg': 75}  # damage
        self.weapons_scale = {'shotgun': 0.4, 'chainsaw': 4, 'hands': 4, '2-shotgun': 4, 'bfg': 4, 'gun': 4, 'machinegun': 4, 'plasmagun': 4, 'rpg': 4}  # scale
        self.weapons_animation_time = {'shotgun': 90, 'chainsaw': 90, 'hands': 120, '2-shotgun': 150, 'bfg': 180, 'gun': 90, 'machinegun': 15, 'plasmagun': 150, 'rpg': 90}  # animation time
        self.weapons_ammo = {'shotgun': 60, 'chainsaw': '-', 'hands': '-', '2-shotgun': 60, 'bfg': 10, 'gun': 40, 'machinegun': 300, 'plasmagun': 80, 'rpg': 20}  # ammo

        self.weapons_index_letters = self.weapons_inventory[self.weapon_index]  # weapon index like 'shotgun', not 0

        self.scale = self.weapons_scale[self.weapons_index_letters]
        self.damage = self.weapons_damage[self.weapons_index_letters]
        self.animation_time = self.weapons_animation_time[self.weapons_index_letters]
        self.ammo = self.weapons_ammo[self.weapons_index_letters]
        path = 'resources/sprites/weapon/'
        super().__init__(game=game, path=path + self.weapons_index_letters + '/0.png', scale=self.scale,
                         animation_time=self.animation_time)
        self.images = deque(
            [pg.transform.smoothscale(img, (self.image.get_width() * self.scale * SCREEN_RES_SCALE, self.image.get_height() * self.scale * SCREEN_RES_SCALE))
             for img in self.images])

        self.weapon_pos = (HALF_WIDTH - self.images[0].get_width() // 2, HEIGHT - self.images[0].get_height() - 300)
        self.reloading = False
        self.num_images = len(self.images)
        self.frame_counter = 0

    def check_weapon_change(self, event):
        if event.type == pg.MOUSEBUTTONDOWN:
            if event.button == 4:
                if self.weapon_index < len(self.weapons_inventory) - 1:
                    self.weapon_index += 1
                else:
                    self.weapon_index = 0

                self.to_update_weapon = True

            elif event.button == 5:
                if self.weapon_index != 0:
                    self.weapon_index -= 1
                else:
                    self.weapon_index = len(self.weapons_inventory) - 1

                self.to_update_weapon = True

    def update_weapon(self):  # change weapon if mousewheel move

        path = 'resources/sprites/weapon/'
        super().__init__(self.game, path=path + self.weapons_inventory[self.weapon_index] + '/0.png', scale=self.scale,
                         animation_time=self.animation_time)
        self.images = deque(
            [pg.transform.smoothscale(img, (self.image.get_width() * self.scale * SCREEN_RES_SCALE, self.image.get_height() * self.scale * SCREEN_RES_SCALE))
             for img in self.images])

        self.to_update_weapon = False

    def animate_shot(self):
        if self.reloading:
            self.game.player.shot = False
            if self.animation_trigger:
                self.images.rotate(-1)
                self.image = self.images[0]
                self.frame_counter += 1
                if self.frame_counter == self.num_images:
                    self.reloading = False
                    self.frame_counter = 0

    def draw(self):
        self.weapon_pos = (HALF_WIDTH - self.images[0].get_width() // 2,
                           HEIGHT - self.images[0].get_height() + 15 + float(math.sin(pg.time.get_ticks() / 600) * 15) * SCREEN_RES_SCALE - self.game.ui.in_level_ui_height)
        self.game.screen.blit(self.images[0], self.weapon_pos)

    def update(self):
        self.check_animation_time()
        self.animate_shot()

        self.weapons_index_letters = self.weapons_inventory[self.weapon_index]

        self.scale = self.weapons_scale[self.weapons_index_letters]
        self.damage = self.weapons_damage[self.weapons_index_letters]
        self.animation_time = self.weapons_animation_time[self.weapons_index_letters]
        self.ammo = self.weapons_ammo[self.weapons_index_letters]
        self.num_images = len(self.images)

        if self.to_update_weapon:
            self.update_weapon()
