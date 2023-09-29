import sqlite3


class TetrisRepository:
    def __init__(self):
        self.conexion = sqlite3.connect("BBDD/tetrisBBDD.db")

    def getScores(self):
        cursor = self.conexion.cursor()
        cursor.execute(
            "SELECT name, score FROM Scores ORDER BY score DESC",
        )
        list = cursor.fetchall()
        cursor.close()
        return list

    def scoreRegister(self, usuario, score):
        cursor = self.conexion.cursor()
        cursor.execute(
            "INSERT INTO Scores (name, score) VALUES (?, ?)",
            (usuario, score),
        )
        self.conexion.commit()
        cursor.close()

    def __del__(self):
        self.conexion.close()

    """
    def guardar_partida(self, nom_usu, points, voypor):
        cursor = self.conexion.cursor()
        cursor.execute(
            "UPDATE Usuarios SET puntuacion = ?, guardado = ? WHERE nombre_usu = ?",
            (points, voypor, nom_usu),
        )
        self.conexion.commit()
        cursor.close()

    def partida_nueva(self):
        cursor = self.conexion.cursor()
        cursor.execute(
            "SELECT tbooklet.id_frase, tbooklet.libro, tbooklet.lista, tbooklet.par, tbooklet.castellano, tbooklet.inglés, tbooklet.alt_ingles, dificultad.dificultad,"
            " dificultad.color_fondo, dificultad.color_texto FROM tbooklet INNER JOIN dificultad"
            " ON tbooklet.libro = dificultad.id"
        )
        listafrases = cursor.fetchall()
        cursor.close()
        return listafrases

    def cargar_partida(self, id_frase):
        cursor = self.conexion.cursor()
        cursor.execute(
            "SELECT tbooklet.id_frase, tbooklet.libro, tbooklet.lista, tbooklet.par,  tbooklet.castellano, tbooklet.inglés, tbooklet.alt_ingles, dificultad.dificultad,"
            " dificultad.color_fondo, dificultad.color_texto FROM tbooklet INNER JOIN dificultad"
            " ON tbooklet.libro = dificultad.id WHERE id_frase >= ? ORDER BY id_frase",
            (id_frase,),
        )
        listafrases = cursor.fetchall()
        cursor.close()
        return listafrases
"""
