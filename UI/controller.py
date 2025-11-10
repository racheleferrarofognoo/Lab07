import flet as ft

from UI import alert
from UI.view import View
from model.model import Modelfor
from model.model import Model
from alert import AlertManager
'''
    CONTROLLER:
    - Funziona da intermediario tra MODELLO e VIEW
    - Gestisce la logica del flusso dell'applicazione
'''

class Controller:
    def __init__(self, view: View, model: Model):
        self._model = model
        self._view = view
        self._alert = alert.AlertManager()

        # Variabili per memorizzare le selezioni correnti
        self.museo_selezionato = None
        self.epoca_selezionata = None

    # POPOLA DROPDOWN
    # TODO
    def popola_dropdown(self):
        #appendo al dropdown

        musei = self._model.get_musei()
        epoche = self._model.get_epoche()

        self._view._dd_filtro_musei.options.clear() #cancello la scelta precedente
        for museo in musei:
            self._view._dd_filtro_musei.options.append(museo)

        self._view._dd_filtro_epoca.options.clear()
        for epoca in epoche:
            self._view._dd_filtro_epoca.options.append(epoca)

        #poi riimposto i valori di default
        self._view._dd_filtro_musei.value = "Nessun filtro"
        self._view._dd_filtro_epoca.value = "Nessun filtro"

        self._view.update()


    # AZIONE: MOSTRA ARTEFATTI
    # TODO
    def mostra_artefatti(self):
        museo = self._view.dd_filtro_musei.value
        epoca = self._view.dd_filtro_epoca
        lista = self._model.get_artefatti_filtrati( museo, epoca)

        #svuoto la lista e la rinizializzo
        self._view.listview_artefatti.controls.clear()

        if len(lista) == 0:
            self._alert.show_alert("Errore, lista vuota!")
        else:
            for elemento in lista:
                nome = elemento["nome"]
                descrizione = elemento["descrizione"]




            self._view.listview_artefatti.controls.append(lista)




