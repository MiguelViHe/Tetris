from typing import Any
from persistence.repository.tetris_repository import TetrisRepository
from src.speed import calc_speed

def draw_screen(stdscr: Any, screen: Any, score: int) -> None:
	stdscr.clear()  # limpia toda la pantalla
	stdscr.addstr(0, 0, "Pantalla Tetris:\n")
	for i, row in enumerate(screen):
		stdscr.addstr(i + 1, 0, "".join(row))
	stdscr.addstr(len(screen) + 2, 0, f"Score = {score}")
	stdscr.addstr(len(screen) + 3, 0, f"Speed = {calc_speed(score):.1f} seg")
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
