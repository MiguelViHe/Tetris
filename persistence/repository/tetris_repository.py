from pathlib import Path
import sqlite3
from typing import List, Tuple


class TetrisRepository:
	def __init__(self) -> None:
		# Ruta absoluta a la base de datos, relativa a la raíz del proyecto
		base_path = Path(__file__).resolve().parents[2]
		db_path = base_path / "data" / "tetrisBBDD.db"
		self.conexion = sqlite3.connect(db_path)

	def get_scores(self) -> List[Tuple[str, int]]:
		"""Devuelve la lista de puntuaciones ordenadas de mayor a menor."""
		cursor = self.conexion.cursor()
		cursor.execute(
			"SELECT name, score FROM Scores ORDER BY score DESC",
		)
		scores = cursor.fetchall()
		cursor.close()
		return scores

	def score_register(self, usuario: str, score: int) -> None:
		"""Registra la puntuación de un usuario en la base de datos."""
		cursor = self.conexion.cursor()
		cursor.execute(
			"INSERT INTO Scores (name, score) VALUES (?, ?)",
			(usuario, score),
		)
		self.conexion.commit()
		cursor.close()

	def __del__(self) -> None:
		if hasattr(self, "conexion") and self.conexion:
			self.conexion.close()
