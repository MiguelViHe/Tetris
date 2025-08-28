from enum import Enum

from src.pieces import Piece
from src.printer import draw_screen
from src.score import calculate_score
from src.constants import BOARD_WIDTH, BOARD_HEIGHT
import copy

class Movement(Enum):
	DOWN = 1
	RIGHT = 2
	LEFT = 3
	ROTATE = 4
	
def clean_rows(screen: list) -> tuple[list, int]:
	completed_rows = 0
	screen_cleaned = []
	block_elem = lambda element: element == "🔳"
	for row in screen:
		if all(block_elem(item) for item in row):
			screen_cleaned.insert(0, ["⬜️"] * BOARD_WIDTH)
			completed_rows += 1
		else:
			screen_cleaned.append(row)
	return (screen_cleaned, completed_rows)

def print_piece(screen: list, piece: Piece) -> tuple[list, Piece]:
	is_blocked = lambda item: item == "🔳"
	for position in piece.initial_position:
		if is_blocked(screen[position[0]][position[1]]):
			piece.floor = True
		screen[position[0]][position[1]] = piece.color
	return (screen, piece)


def block_piece(screen: list) -> list:
	for row_index, row in enumerate(screen):
		for column_index, item in enumerate(row):
			if item != "⬜️" and item != "🔳":
				screen[row_index][column_index] = "🔳"
	return screen

def move_piece(
	screen: list, aux_screen: list, movement: Movement, piece: Piece, score: int, stdscr
) -> tuple[list, Piece, int]:
	new_screen = [row[:] for row in aux_screen]
	rotation_item = 0

	for row_index, row in enumerate(screen):
		for column_index, item in enumerate(row):
			if item == piece.color:
				new_row_index = 0
				new_column_index = 0
				match movement:
					case Movement.DOWN:
						new_row_index = row_index + 1
						new_column_index = column_index
					case Movement.RIGHT:
						new_row_index = row_index
						new_column_index = column_index + 1
					case Movement.LEFT:
						new_row_index = row_index
						new_column_index = column_index - 1
					case Movement.ROTATE:
						new_row_index = (
							row_index
							+ piece.rotations[piece.piece_position][rotation_item][0]
						)
						new_column_index = (
							column_index
							+ piece.rotations[piece.piece_position][rotation_item][1]
						)
						rotation_item += 1
				if (
					new_column_index > BOARD_WIDTH - 1
					or new_column_index < 0
					or (
						movement != Movement.DOWN
						and aux_screen[new_row_index][new_column_index] == "🔳"
					)
				):
					return (screen, piece, score)
				elif (
					movement == Movement.DOWN
					and not piece.floor
					and (
						new_row_index > BOARD_HEIGHT - 1
						or aux_screen[new_row_index][new_column_index] == "🔳"
					)
				):
					piece.floor = True
					(cleaned_scr, completed_rows) = clean_rows(block_piece(screen))
					return (cleaned_scr, piece, calculate_score(completed_rows, score))
				else:
					new_screen[new_row_index][new_column_index] = piece.color

	if movement == Movement.ROTATE:
		piece.piece_position = (piece.piece_position + 1) % 4
	draw_screen(stdscr, new_screen, score)

	return (new_screen, piece, score)