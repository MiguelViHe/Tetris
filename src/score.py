from persistence.repository.tetris_repository import TetrisRepository

SCORES = [0, 1, 1.25, 1.5, 1.75]

def calculate_score(rows: int, score: int) -> int:
	return rows * SCORES[rows] + score


def save_score(usuario: str, score: int):
	managedb = TetrisRepository()
	managedb.score_register(usuario, score)