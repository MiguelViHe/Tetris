from enum import Enum
import keyboard
import random
import copy
from pieces import Piece


class Movement(Enum):
    DOWN = 1
    RIGHT = 2
    LEFT = 3
    ROTATE = 4


def print_piece(screen: list, piece: Piece) -> list:
    for position in piece.initial_position:
        screen[position[0]][position[1]] = piece.color
    return screen


def print_screen(screen: list):
    print("\nPantalla Tetris:\n")
    for row in screen:
        print("".join(row))


def block_piece(screen: list) -> list:
    for row_index, row in enumerate(screen):
        for column_index, item in enumerate(row):
            if item != "⬜️" and item != "🔳":
                screen[row_index][column_index] = "🔳"
    return screen


def clean_rows(screen: list) -> list:
    screen_cleaned = []
    block_elem = lambda element: element == "🔳"
    for row in screen:
        if all(block_elem(item) for item in row):
            screen_cleaned.insert(0, ["⬜️"] * 10)
        else:
            screen_cleaned.append(row)
    return screen_cleaned


def move_piece(
    screen: list, aux_screen: list, movement: Movement, piece: Piece
) -> (list, Piece):
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
                    return (screen, piece)
                elif (
                    movement == Movement.DOWN
                    and not piece.floor
                    and (
                        new_row_index > 9
                        or aux_screen[new_row_index][new_column_index] == "🔳"
                    )
                ):
                    piece.floor = True
                    return (clean_rows(block_piece(screen)), piece)
                else:
                    new_screen[new_row_index][new_column_index] = piece.color

    if movement == Movement.ROTATE:
        piece.piece_position = (piece.piece_position + 1) % 4
    print_screen(new_screen)
    return (new_screen, piece)


def tetris():
    screen = [
        ["⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️"],
        ["⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️"],
        ["⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️"],
        ["⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️"],
        ["⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️"],
        ["⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️"],
        ["⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️"],
        ["⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️"],
        ["⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️"],
        ["⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️", "⬜️"],
    ]
    while True:
        new_piece = Piece(random.randint(1, 7))
        aux_screen = copy.deepcopy(screen)
        screen = print_piece(screen, new_piece)
        print_screen(screen)

        while new_piece.floor == False:
            event = keyboard.read_event()
            if event.name == "esc":
                break
            elif event.event_type == keyboard.KEY_DOWN:
                match event.name:
                    case "flecha abajo":
                        (screen, new_piece) = move_piece(
                            screen, aux_screen, Movement.DOWN, new_piece
                        )
                    case "flecha izquierda":
                        (screen, new_piece) = move_piece(
                            screen, aux_screen, Movement.LEFT, new_piece
                        )
                    case "flecha derecha":
                        (screen, new_piece) = move_piece(
                            screen, aux_screen, Movement.RIGHT, new_piece
                        )
                    case "space":
                        (screen, new_piece) = move_piece(
                            screen, aux_screen, Movement.ROTATE, new_piece
                        )


tetris()
