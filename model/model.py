from database.museo_DAO import MuseoDAO
from database.artefatto_DAO import ArtefattoDAO

'''
    MODELLO: 
    - Rappresenta la struttura dati
    - Si occupa di gestire lo stato dell'applicazione
    - Si occupa di interrogare il DAO (chiama i metodi di MuseoDAO e ArtefattoDAO)
'''

class Model:
    def __init__(self):
        self._museo_dao = MuseoDAO()
        self._artefatto_dao = ArtefattoDAO()

    # --- ARTEFATTI ---
    def get_artefatti_filtrati(self, museo:str, epoca:str):
        """Restituisce la lista di tutti gli artefatti filtrati per museo e/o epoca (filtri opzionali)."""
        # TODO
        risultati_filtrati = []
        lista_DAO_artefatti = self._artefatto_dao.get_artefatto()
        for artefatto in lista_DAO_artefatti:
            if (museo == "Nessun filtro" or artefatto["museo_nome"] == museo) and (epoca == "Nessun filtro" or artefatto["epoca"] == epoca):
                risultati_filtrati.append(artefatto)
        return risultati_filtrati


    def get_epoche(self):
        """Restituisce la lista di tutte le epoche."""
        # TODO
        risultati = []
        lista_artefatti = self._artefatto_dao.get_artefatto()
        for artefatto in lista_artefatti:
            risultati.append(artefatto.epoca)
        epoche = ["Nessun filtro"] + sorted(risultati)
        return epoche

    # --- MUSEI ---
    def get_musei(self):
        """ Restituisce la lista di tutti i musei."""
        # TODO
        risultati = []
        lista_musei = self._museo_dao.get_museo()
        for museo in lista_musei:
            risultati.append(museo.nome)
        musei = ["Nessun filtro"] + sorted(risultati)
        return musei


