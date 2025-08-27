import curses
import random
import copy
from src.pieces import Piece
from src.piece_actions import print_piece, move_piece, Movement
from src.printer import draw_screen
from src.gameover import game_over_screen

# def tetris():
#     score = 0
#     game_over = False
#     screen = [
#         ["⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️"],
#         ["⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️"],
#         ["⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️"],
#         ["⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️"],
#         ["⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️"],
#         ["⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️"],
#         ["⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️"],
#         ["⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️"],
#         ["⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️"],
#         ["⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️"],
#     ]

#     while not game_over:
#         new_piece = Piece(random.randint(1, 7))
#         aux_screen = copy.deepcopy(screen)
#         (screen, new_piece) = print_piece(screen, new_piece)
#         if new_piece.floor == True:
#             game_over = True
#         print_screen(screen)
#         print(f"Score = {score}")

#         while new_piece.floor == False:
#             event = keyboard.read_event()
#             if event.name == "esc":
#                 game_over = True
#                 break
#             elif event.event_type == keyboard.KEY_DOWN:
#                 match event.name:
#                     case "flecha abajo":
#                         (screen, new_piece, score) = move_piece(
#                             screen, aux_screen, Movement.DOWN, new_piece, score
#                         )
#                     case "flecha izquierda":
#                         (screen, new_piece, score) = move_piece(
#                             screen, aux_screen, Movement.LEFT, new_piece, score
#                         )
#                     case "flecha derecha":
#                         (screen, new_piece, score) = move_piece(
#                             screen, aux_screen, Movement.RIGHT, new_piece, score
#                         )
#                     case "space":
#                         (screen, new_piece, score) = move_piece(
#                             screen, aux_screen, Movement.ROTATE, new_piece, score
#                         )

#     print(f"\nGAME OVER -- Score = {score}")
#     usuario = input("Introduce tu nombre: ")
#     save_score(usuario, score)
#     print_scores_table()

# tetris()

def tetris_curses(stdscr):
	curses.curs_set(0)
	stdscr.nodelay(True)  # getch() no bloquea
	stdscr.clear()

	score = 0
	game_over = False
	screen = [["⬜️"] * 10 for _ in range(10)]  # pantalla 10x10

	while not game_over:
		new_piece = Piece(random.randint(1, 7))
		aux_screen = copy.deepcopy(screen)
		(screen, new_piece) = print_piece(screen, new_piece)
		if new_piece.floor:
			game_over = True

		draw_screen(stdscr, screen, score)
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
	stdscr.nodelay(False)
	game_over_screen(stdscr, score)
# ===================== LLAMADA FINAL =====================
if __name__ == "__main__":
	curses.wrapper(tetris_curses)