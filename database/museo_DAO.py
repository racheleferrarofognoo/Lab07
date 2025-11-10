from database.DB_connect import ConnessioneDB
from model.museoDTO import Museo
from DB_connect import ConnessioneDB

"""
    Museo DAO
    Gestisce le operazioni di accesso al database relative ai musei (Effettua le Query).
"""

class MuseoDAO:
    def __init__(self):
        pass

    # TODO
    def get_museo(self):
        try:
            cnx = ConnessioneDB.get_connection()
            cursor = cnx.cursor(dictionary = True)
            cursor.execute("SELECT * FROM museo")
            rows = cursor.fetchall()
            risultati = []
            for row in rows:
                museo = Museo(row["id"],row["nome"],row["tipologia"])
                risultati.append(museo)
            cursor.close()
            cnx.close()
            return risultati
        except Exception as e:
            return []


