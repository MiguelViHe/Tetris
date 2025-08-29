from typing import Any
from persistence.repository.tetris_repository import TetrisRepository
from src.speed import calc_speed
from src.constants import BOARD_WIDTH as BW, BOARD_HEIGHT as BH

def draw_screen(stdscr: Any, screen: Any, score: int) -> None:
	stdscr.clear()  # limpia toda la pantalla

	# Tamaño de la terminal
	max_y, max_x = stdscr.getmaxyx()
	cell_width = 2  # el emoji ocupa 2 columnas
	board_width = BW * cell_width
	board_height = BH

	if max_y < board_height + 6 or max_x < board_width + 20:
		stdscr.addstr(0, 0, "La ventana es demasiado pequeña. Por favor, ajústala.")
		stdscr.refresh()
		return

	y_offset = (max_y - board_height) // 2
	x_offset = (max_x - board_width) // 2
	
	# Dibujar borde superior
	stdscr.addstr(y_offset - 1, x_offset - 1, "┌" + "─" * board_width + "┐")

	for i, row in enumerate(screen):
		line = "".join(row)
		stdscr.addstr(y_offset + i, x_offset - 1, f"│{line}│")

	# Dibujar borde inferior
	stdscr.addstr(y_offset + board_height, x_offset - 1, "└" + "─" * board_width + "┘")

	# Pintar la info debajo del tablero
	stdscr.addstr(y_offset + BH + 1, x_offset, f"Score = {score}")
	stdscr.addstr(y_offset + BH + 2, x_offset, f"Speed = {calc_speed(score):.1f} seg")
	stdscr.refresh()  # refresca la pantalla para mostrar los cambios

def print_scores_table(stdscr: Any) -> int:
	"""
	Muestra en pantalla la tabla de puntuaciones usando curses.
	
	Args:
		stdscr: ventana principal de curses donde se imprimen los textos.
	"""
	managedb = TetrisRepository()
	scores = managedb.get_scores()
	stdscr.addstr(0, 0, "------ Scores ------")
	for i, (usuario, score) in enumerate(scores, start=1):
		stdscr.addstr(i, 0, f"{usuario}: {score}")
	stdscr.addstr(len(scores) + 1, 0, "--------------------")
	stdscr.refresh()
	return len(scores) + 2  # devuelve la cantidad de líneas impresas
