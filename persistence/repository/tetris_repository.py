import sqlite3
from contextlib import contextmanager

class TetrisRepository:
	def __init__(self, db_path: str = "data/tetrisBBDD.db"):
		self.db_path = db_path

	@contextmanager
	def _get_connection(self):
		"""Context manager que abre y cierra la conexión automáticamente."""
		conn = sqlite3.connect(self.db_path)
		try:
			yield conn
		finally:
			conn.close()

	def get_scores(self):
		with self._get_connection() as conn:
			cursor = conn.cursor()
			cursor.execute(
				"SELECT name, score FROM Scores ORDER BY score DESC"
			)
			scores = cursor.fetchall()
			cursor.close()
		return scores

	def score_register(self, usuario: str, score: int):
		with self._get_connection() as conn:
			cursor = conn.cursor()
			cursor.execute(
				"INSERT INTO Scores (name, score) VALUES (?, ?)",
				(usuario, score)
			)
			conn.commit()
			cursor.close()
