"""
Settings
"""
from struct import Struct

WIDTH = 640
HEIGHT = 480
FRAMERATE = 24
HTTP_PORT = 8082
CAMERA_WS_PORT = 8084
SENSORS_WS_PORT = 8085
COLOR = u'#444'
JSMPEG_MAGIC = b'jsmp'
JSMPEG_HEADER = Struct('>4sHH')
VFLIP = False
HFLIP = False

DISTANCE_SENSORS = [
    {
        'i2c_address': 0x2B,
        'shutdown_pin': 23
    },
    {
        'i2c_address': 0x2A,
        'shutdown_pin': 24
    },
]

MOTION_SENSORS = [
    {'pin': 14},
    {'pin': 4},
]
