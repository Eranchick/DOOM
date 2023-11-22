from sprite_object import *


class Weapon(AnimatedSprite):
    def __init__(self, game, path='resources/sprites/weapon/'):
        self.game = game
        self.path = path
        self.root_path = self.path
        self.weapon_index = 0  # index in self.weapons list
        self.weapons = ('shotgun', 'chainsaw')  # all weapons of game
        self.weapons_inventory = ['shotgun', 'chainsaw']

        self.weapons_max_attack_dist = {'shotgun':20, 'chainsaw': 4}  # max attack distance
        self.weapons_damage = {'shotgun': 50, 'chainsaw': 7500}  # damage
        self.weapons_scale = {'shotgun': 0.4, 'chainsaw': 0.6}  # scale
        self.weapons_animation_time = {'shotgun': 90, 'chainsaw': 90}  # animation time

        self.weapons_index_letters = self.weapons_inventory[self.weapon_index]  # weapon index like 'shotgun', not 0

        self.scale = self.weapons_scale[self.weapons_index_letters]
        self.damage = self.weapons_damage[self.weapons_index_letters]
        self.animation_time = self.weapons_animation_time[self.weapons_index_letters]
        path = 'resources/sprites/weapon/'
        super().__init__(game=game, path=path + self.weapons[self.weapon_index] + '/0.png', scale=self.scale,
                         animation_time=self.animation_time)
        self.images = deque(
            [pg.transform.smoothscale(img, (self.image.get_width() * self.scale, self.image.get_height() * self.scale))
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

                self.update_weapon()

            elif event.button == 5:
                if self.weapon_index != 0:
                    self.weapon_index -= 1
                else:
                    self.weapon_index = len(self.weapons_inventory) - 1

                self.update_weapon()

    def update_weapon(self):  # change weapon if mousewheel move
        self.weapons_index_letters = self.weapons_inventory[self.weapon_index]

        self.scale = self.weapons_scale[self.weapons_index_letters]
        self.damage = self.weapons_damage[self.weapons_index_letters]
        self.animation_time = self.weapons_animation_time[self.weapons_index_letters]
        path = 'resources/sprites/weapon/'
        super().__init__(self.game, path=path + self.weapons[self.weapon_index] + '/0.png', scale=self.scale,
                         animation_time=self.animation_time)
        self.images = deque(
            [pg.transform.smoothscale(img, (self.image.get_width() * self.scale, self.image.get_height() * self.scale))
             for img in self.images])

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
                           HEIGHT - self.images[0].get_height() + 15 + math.sin(pg.time.get_ticks() / 600) * 15)
        self.game.screen.blit(self.images[0], self.weapon_pos)

    def update(self):
        self.check_animation_time()
        self.animate_shot()
