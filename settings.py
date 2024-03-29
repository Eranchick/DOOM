import math
from screeninfo import get_monitors

SCREEN_RES_SCALE = 0.5  # scaleing screen res (0 < N <= 1)

# calculating screen res
scr = str(get_monitors()[0])[7:]  # getting monitor info

# width
scr_width_index = scr.index('width=') + 6  # getting index of width 1st digit
scr_width_index_last = scr[scr_width_index:].index(',') + scr_width_index  # getting index of width last digit
print(scr, scr[scr_width_index:scr_width_index_last])  # debug info about width
print(scr_width_index, scr_width_index_last)  # debug info about width
WIDTH = int(scr[scr_width_index:scr_width_index_last])  # width var

# height
scr_height_index = scr.index('height=') + 7  # getting index of height 1st digit
scr_height_index_last = scr[scr_height_index:].index(',') + scr_height_index  # getting index of height last digit
print(scr, scr[scr_height_index:scr_height_index_last])  # debug info about height
print(scr_height_index, scr_height_index_last)  # debug info about height
HEIGHT = int(scr[scr_height_index:scr_height_index_last])  # height var

# scaling res
WIDTH *= SCREEN_RES_SCALE
HEIGHT *= SCREEN_RES_SCALE

WIDTH, HEIGHT = int(WIDTH), int(HEIGHT)

# game settings
RES = WIDTH, HEIGHT
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 60

PLAYER_POS = 8.5, 1.5  # player
PLAYER_ANGLE = math.pi / 2
PLAYER_SPEED = 0.004
PLAYER_ROT_SPEED = 0.002
PLAYER_SIZE_SCALE = 60
PLAYER_MAX_HEALTH = 100

MOUSE_SENSITIVITY = 0.0001125
MOUSE_MAX_REL = 40
MOUSE_BORDER_LEFT = 100
MOUSE_BORDER_RIGHT = WIDTH - MOUSE_BORDER_LEFT

FLOOR_COLOR = (30, 30, 30)

FOV = math.pi / 3  # ray-casting
HALF_FOV = FOV / 2
NUM_RAYS = WIDTH // 2
HALF_NUM_RAYS = NUM_RAYS // 2
DELTA_ANGLE = FOV / NUM_RAYS
MAX_DEPTH = 20

SCREEN_DIST = HALF_WIDTH / math.tan(HALF_FOV)
SCALE = WIDTH // NUM_RAYS

TEXTURE_SIZE = 256
HALF_TEXTURE_SIZE = TEXTURE_SIZE // 2
