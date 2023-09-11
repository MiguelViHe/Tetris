from enum import Enum
import keyboard


class Movement(Enum):
    DOWN = 1
    RIGHT = 2
    LEFT = 3
    ROTATE = 4


def tetris():
    screen = [
        ["🔳", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
        ["🔳", "🔳", "🔳", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
        ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
        ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
        ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
        ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
        ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
        ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
        ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
        ["🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲", "🔲"],
    ]

    piece_position = 0

    print_screen(screen)

    while True:
        event = keyboard.read_event()
        if event.name == "esc":
            break
        elif event.event_type == keyboard.KEY_DOWN:
            match event.name:
                case "flecha abajo":
                    (screen, piece_position) = move_piece(screen, Movement.DOWN)
                case "flecha izquierda":
                    (screen, piece_position) = move_piece(screen, Movement.LEFT)
                case "flecha derecha":
                    (screen, piece_position) = move_piece(screen, Movement.RIGHT)
                case "space":
                    (screen, piece_position) = move_piece(
                        screen, Movement.ROTATE, piece_position
                    )


def move_piece(screen: list, movement: Movement, piece_position=0) -> list:
    new_screen = [["🔲"] * 10 for _ in range(10)]

    new_piece_position = 0
    rotation_item = 0
    rotations = [
        [(0, 1), (-1, 0), (0, -1), (1, -2)],
        [(0, 2), (1, 1), (-1, 1), (-2, 0)],
        [(0, 1), (1, 0), (2, -1), (1, -2)],
        [(1, 1), (0, 0), (-2, 0), (-1, -1)],
    ]

    for row_index, row in enumerate(screen):
        for column_index, item in enumerate(row):
            if item == "🔳":
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
                            row_index + rotations[piece_position][rotation_item][0]
                        )
                        new_column_index = (
                            column_index + rotations[piece_position][rotation_item][1]
                        )
                        rotation_item += 1

                if new_row_index > 9 or new_column_index > 9 or new_column_index < 0:
                    print("\nNo se puede realizar el movimiento")
                    return (screen, piece_position)
                else:
                    new_screen[new_row_index][new_column_index] = "🔳"

    if movement == Movement.ROTATE:
        new_piece_position = (piece_position + 1) % 4
    print_screen(new_screen)
    return (new_screen, new_piece_position)


def print_screen(screen: list):
    print("\nPantalla Tetris:\n")
    for row in screen:
        print("".join(row))


tetris()
