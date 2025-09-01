
from src.constants import BOARD_WIDTH, BOARD_HEIGHT, Movement

# Verifica si el movimiento de la pieza colisiona con otras piezas o los bordes. En los movimientos laterales
# o en la rotación, devuelve True si hay colisión.
def movement_collides(aux_screen: list, movement: Movement, new_row_index: int, new_column_index: int) -> bool:
	if (
		((movement == Movement.RIGHT or movement == Movement.LEFT)
		and (new_column_index > BOARD_WIDTH - 1
		or new_column_index < 0
		or aux_screen[new_row_index][new_column_index] == "🔳"))
		or
		(movement == Movement.ROTATE
		and (new_row_index > BOARD_HEIGHT - 1
		or new_column_index > BOARD_WIDTH - 1 or new_column_index < 0
		or aux_screen[new_row_index][new_column_index] == "🔳"))
	):
		return True
	return False