import math
import screeninfo

# calculating screen res
scr = str(screeninfo.get_monitors()[0])[7:]  # getting monitor info
   # width
scr_width_index = scr.index('width=') + 6  # getting index of width 1st digit
scr_width_index_last = scr[scr_width_index:].index(',') + scr_width_index  # getting index of width last digit
print(scr, scr[scr_width_index:scr_width_index_last])  # debug info about width
print(scr_width_index, scr_width_index_last)  # debug info about width
scr_width = int(scr[scr_width_index:scr_width_index_last])  # width var

    # height
scr_height_index = scr.index('height=') + 7  # getting index of height 1st digit
scr_height_index_last = scr[scr_height_index:].index(',') + scr_height_index  # getting index of heighth last digit
print(scr, scr[scr_height_index:scr_height_index_last])  # debug info about height
print(scr_height_index, scr_height_index_last)  # debug info about height
scr_height = int(scr[scr_height_index:scr_height_index_last])  # height var

# game settings
RES = WIDTH, HEIGHT = scr_width, scr_height
HALF_WIDTH = WIDTH // 2
HALF_HEIGHT = HEIGHT // 2
FPS = 0

PLAYER_POS = 1.5, 5  # mini_map
PLAYER_ANGLE = 0
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
