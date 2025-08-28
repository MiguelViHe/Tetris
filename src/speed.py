from src.constants import INITIAL_SPEED

def calc_speed(score: int) -> float:
	# cada 10 puntos se baja 0.1 desde 1.0
	speed = INITIAL_SPEED - (score // 10) * 0.1
	# límite inferior
	return max(speed, 0.1)