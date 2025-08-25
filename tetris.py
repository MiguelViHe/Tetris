from enum import Enum
import curses
import random
import copy
from pieces import Piece
from persistence.repository.tetris_repository import TetrisRepository


class Movement(Enum):
    DOWN = 1
    RIGHT = 2
    LEFT = 3
    ROTATE = 4


SCORES = [0, 1, 1.25, 1.5, 1.75]


def print_piece(screen: list, piece: Piece) -> tuple[list, Piece]:
    is_blocked = lambda item: item == "🔳"
    for position in piece.initial_position:
        if is_blocked(screen[position[0]][position[1]]):
            piece.floor = True
        screen[position[0]][position[1]] = piece.color
    return (screen, piece)


# def print_screen(screen: list):
#     print("\nPantalla Tetris:\n")
#     for row in screen:
#         print("".join(row))

def draw_screen(stdscr, screen, score):
    stdscr.clear()  # limpia toda la pantalla
    stdscr.addstr(0, 0, "Pantalla Tetris:\n")
    for i, row in enumerate(screen):
        stdscr.addstr(i + 1, 0, "".join(row))
    stdscr.addstr(len(screen) + 2, 0, f"Score = {score}")
    stdscr.refresh()  # refresca la pantalla para mostrar los cambios


def block_piece(screen: list) -> list:
    for row_index, row in enumerate(screen):
        for column_index, item in enumerate(row):
            if item != "⬜️" and item != "🔳":
                screen[row_index][column_index] = "🔳"
    return screen


def clean_rows(screen: list) -> tuple[list, int]:
    completed_rows = 0
    screen_cleaned = []
    block_elem = lambda element: element == "🔳"
    for row in screen:
        if all(block_elem(item) for item in row):
            screen_cleaned.insert(0, ["⬜️"] * 10)
            completed_rows += 1
        else:
            screen_cleaned.append(row)
    return (screen_cleaned, completed_rows)


def calculate_score(rows: int, score: int) -> int:
    return rows * SCORES[rows] + score


def save_score(usuario: str, score: int):
    managedb = TetrisRepository()
    managedb.scoreRegister(usuario, score)


def print_scores_table():
    managedb = TetrisRepository()
    list = managedb.getScores()
    print("------ Scores ------")
    for usuario, score in list:
        print(f"{usuario}: {score}")
    print("--------------------")


def move_piece(
    screen: list, aux_screen: list, movement: Movement, piece: Piece, score: int, stdscr
) -> tuple[list, Piece, int]:
    new_screen = copy.deepcopy(aux_screen)
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
                    new_column_index > 9
                    or new_column_index < 0
                    or (
                        movement != Movement.DOWN
                        and aux_screen[new_row_index][new_column_index] == "🔳"
                    )
                ):
                    print("\nNo se puede realizar el movimiento")
                    return (screen, piece, score)
                elif (
                    movement == Movement.DOWN
                    and not piece.floor
                    and (
                        new_row_index > 9
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

    print(f"\nGAME OVER -- Score = {score}")
    usuario = input("Introduce tu nombre: ")
    save_score(usuario, score)
    print_scores_table()

# ===================== LLAMADA FINAL =====================
if __name__ == "__main__":
    curses.wrapper(tetris_curses)