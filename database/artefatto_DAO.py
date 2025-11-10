from DB_connect import ConnessioneDB
"""
    ARTEFATTO DAO
    Gestisce le operazioni di accesso al database relative agli artefatti (Effettua le Query).
"""

class ArtefattoDAO:
    def __init__(self):
        pass

    # TODO
    def get_artefatto(self):
        try:
            cnx = ConnessioneDB.get_connection()
            cursor = cnx.cursor()
            cursor.execute("SELECT * FROM artefatto")
            rows = cursor.fetchall(dictionary = True)
            risultati = []
            cursor.close()
            cnx.close()
            for row in rows:
                risultati.append(row)
            return risultati
        except Exception as e:
            print(e)



