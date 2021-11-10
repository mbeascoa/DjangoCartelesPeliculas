import cx_Oracle


class Pelicula:
    def __init__(self):
        self.connection = cx_Oracle.connect("system", "Tardes", "localhost/XE")

    def devolverdato(self):
        cursor = self.connection.cursor()
        dato=''
        try:
            cursor.execute("SELECT TITULO , FOTO   FROM PELICULAS ")

        except self.connection.Error as error:
            print("Error: ", error)

        return cursor
