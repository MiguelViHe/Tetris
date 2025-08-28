import curses
from typing import Any
from src.printer import print_scores_table
from src.score import save_score
from src.constants import MAX_NAME_LENGTH as MNL


# def game_over_screen(stdscr: curses.window, score: int, key: int) -> None:
# 	"""Muestra la pantalla de game over y pide el nombre del jugador."""
# 	if key != ord('q'):
# 		stdscr.clear()
# 		stdscr.addstr(5, 10, f"GAME OVER -- Score = {score}")
# 		stdscr.addstr(7, 10, "Introduce tu nombre: ")
# 		stdscr.refresh()

# 		curses.echo()
# 		while True:
# 			usuario_bytes = stdscr.getstr(7, 32, MNL)  # leer hasta 20 caracteres
# 			usuario = usuario_bytes.decode("utf-8").strip()
# 			if len(usuario) >= 3:
# 				break
# 			stdscr.clear()
# 			stdscr.addstr(5, 10, f"GAME OVER -- Score = {score}")
# 			stdscr.addstr(7, 10, "Nombre demasiado corto. Intenta de nuevo: ")
# 			stdscr.addstr(8, 10, "Introduce tu nombre: ")
# 		curses.noecho()

# 		save_score(usuario, score)
# 		stdscr.clear()
# 		lines = print_scores_table(stdscr)

# 		stdscr.addstr(lines + 1, 0, "Pulsa una tecla para salir...")
# 		stdscr.refresh()
# 		stdscr.getch()

def game_over_screen(stdscr: curses.window, score: int, key: int) -> None:
	"""Muestra la pantalla de game over y pide el nombre del jugador."""
	if key == ord('q'):
		return

	curses.echo()
	height, width = stdscr.getmaxyx()

	while True:
		stdscr.clear()

		# Calcular posiciones centradas
		title = "=== GAME OVER ==="
		score_msg = f"Tu puntuación: {score}"
		prompt = "Introduce tu nombre (mínimo 3 letras):"

		stdscr.addstr(height // 2 - 2, (width - len(title)) // 2, title, curses.A_BOLD)
		stdscr.addstr(height // 2, (width - len(score_msg)) // 2, score_msg)
		stdscr.addstr(height // 2 + 2, (width - len(prompt)) // 2, prompt)

		stdscr.refresh()

		# Pedir nombre (entrada centrada)
		usuario_bytes = stdscr.getstr(height // 2 + 3, (width // 2) - 10, 20)
		usuario = usuario_bytes.decode("utf-8").strip()

		if len(usuario) >= 3:
			break
		else:
			error_msg = "❌ Nombre demasiado corto, intenta de nuevo..."
			stdscr.addstr(height // 2 + 5, (width - len(error_msg)) // 2, error_msg, curses.A_BOLD)
			stdscr.refresh()
			curses.napms(1200)  # pequeña pausa antes de reintentar

	curses.noecho()

	# Guardar puntuación
	save_score(usuario, score)

	# Mostrar ranking
	stdscr.clear()
	lines = print_scores_table(stdscr)

	stdscr.addstr(lines + 2, (width - 30) // 2, "Pulsa cualquier tecla para salir...")
	stdscr.refresh()
	stdscr.getch()

