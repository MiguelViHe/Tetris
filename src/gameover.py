import curses
from typing import Any
from src.printer import print_scores_table
from src.score import save_score


def game_over_screen(stdscr: curses.window, score: int) -> None:
	"""Muestra la pantalla de game over y pide el nombre del jugador."""
	stdscr.clear()
	stdscr.addstr(5, 10, f"GAME OVER -- Score = {score}")
	stdscr.addstr(7, 10, "Introduce tu nombre: ")
	stdscr.refresh()

	curses.echo()
	usuario_bytes = stdscr.getstr(7, 32, 20)  # leer hasta 20 caracteres
	usuario = usuario_bytes.decode("utf-8").strip()
	curses.noecho()

	save_score(usuario, score)
	stdscr.clear()
	lines = print_scores_table(stdscr)

	stdscr.addstr(lines + 1, 0, "Pulsa una tecla para salir...")
	stdscr.refresh()
	stdscr.getch()
