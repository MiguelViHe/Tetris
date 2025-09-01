from enum import Enum

BOARD_WIDTH = 10
BOARD_HEIGHT = 15
MAX_NAME_LENGTH = 20
INITIAL_SPEED = 1.0

class Movement(Enum):
	DOWN = 1
	RIGHT = 2
	LEFT = 3
	ROTATE = 4