from database.DB_connect import ConnessioneDB
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
            cnx = ConnessioneDB().get_connection()
            cursor = cnx.cursor(dictionary = True)
            cursor.execute("SELECT * FROM artefatto")
            risultati = cursor.fetchall()
            cursor.close()
            cnx.close()
            return risultati
        except Exception as e:
            print(e)



