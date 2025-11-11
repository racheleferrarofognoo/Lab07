from model.museoDTO import Museo
from database.DB_connect import ConnessioneDB

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
            cursor = cnx.cursor(dictionary=True)
            cursor.execute("SELECT * FROM museo")
            result = cursor.fetchall()
            cursor.close()
            cnx.close()
            return result
        except Exception as e:
            print(e)

