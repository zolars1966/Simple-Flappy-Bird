from math import *
from decimal import Decimal
from pygame import time as pgtime
import numpy as np
import sys


# global references
W_SCALE = 80
try:
    SIZE = WIDTH, HEIGHT = int(sys.argv[1]), int(sys.argv[2])
except IndexError:
    SIZE = WIDTH, HEIGHT = 9 * W_SCALE, 16 * W_SCALE

H_SIZE = H_WIDTH, H_HEIGHT = WIDTH / 2, HEIGHT / 2
M_DELTA_TIME = 100 / 6
N_DELTA_TIME = M_DELTA_TIME * 1000000
DELTA_TIME = M_DELTA_TIME / 1000
FPS = 60
FPS_DT = 1000 / FPS if FPS else 0
g = 9.81 * (HEIGHT / 3)
dt = Decimal(M_DELTA_TIME) / 1000
