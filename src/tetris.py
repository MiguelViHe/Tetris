import curses
import random
import copy
import time
from src.constants import BOARD_HEIGHT, BOARD_WIDTH
from src.pieces import Piece
from src.piece_actions import print_piece, move_piece, Movement
from src.printer import draw_screen
from src.gameover import game_over_screen
from src.speed import calc_speed

def tetris_curses(stdscr):
	curses.curs_set(0)
	stdscr.nodelay(True)  # getch() no bloquea asi el juego sigue corriendo cuando añada el temporizador
	stdscr.clear()

	score = 0
	game_over = False
	screen = [["⬜️"] * BOARD_WIDTH for _ in range(BOARD_HEIGHT)]

	while not game_over:
		new_piece = Piece(random.randint(1, 7))
		aux_screen = copy.deepcopy(screen)
		(screen, new_piece) = print_piece(screen, new_piece)
		if new_piece.floor:
			game_over = True
		draw_screen(stdscr, screen, score)
		last_drop_time = time.time()
		while not new_piece.floor:
			key = stdscr.getch()
			if key == ord('q'):  # salir con 'q'
				game_over = True
				break
			elif key == curses.KEY_DOWN:
				screen, new_piece, score = move_piece(screen, aux_screen, Movement.DOWN, new_piece, score, stdscr)
			elif key == curses.KEY_LEFT:
				screen, new_piece, score = move_piece(screen, aux_screen, Movement.LEFT, new_piece, score, stdscr)
			elif key == curses.KEY_RIGHT:
				screen, new_piece, score = move_piece(screen, aux_screen, Movement.RIGHT, new_piece, score, stdscr)
			elif key == ord(' '):
				screen, new_piece, score = move_piece(screen, aux_screen, Movement.ROTATE, new_piece, score, stdscr)
			# caida automatica
			drop_interval = calc_speed(score)
			if time.time() - last_drop_time > drop_interval:
				screen, new_piece, score = move_piece(screen, aux_screen, Movement.DOWN, new_piece, score, stdscr)
				last_drop_time = time.time()
	stdscr.nodelay(False)
	game_over_screen(stdscr, score, key)
# ===================== LLAMADA FINAL =====================
if __name__ == "__main__":
	curses.wrapper(tetris_curses)