import customtkinter as ctk
import tkinter as tk

from graphes.heatmap_maker import HeatMapMaker

class CarteThermique(ctk.CTkFrame):
    def __init__(self, master, handler, **kwargs):
        super().__init__(master, **kwargs)

        # DataHandler
        self.handler = handler

        # Créer la page de la carte thermique.
        self.create_carte_page()

    def create_carte_page(self):
        # Créer la carte thermique.
        carte_y = 0.3
        carte = HeatMapMaker(self, self.handler)
        carte.place(relx=0.625, rely=carte_y, anchor="center", relwidth=0.75, relheight=0.7)

        # Liste des statistiques disponibles.
        options_annees = ["2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021"]
        options_mois = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"]

        # Variable pour le choix de la statistique.
        self.selection_annee = tk.StringVar(value=options_annees[0])
        self.selection_mois = tk.StringVar(value=options_mois[0])

        # Menu déroulant d'années.
        menuAnnees_y = carte_y - 0.05
        menuAnnees = ctk.CTkOptionMenu(self, variable=self.selection_annee, values=options_annees, command=None, font=("Arial", 13), corner_radius=8, height=36)
        menuAnnees.place(relx=0.025, rely=menuAnnees_y, anchor="nw", relwidth=0.2)

        # Label du menu déroulant d'années.
        titreAnnees = ctk.CTkLabel(self, text="Choix d'année", font=("Arial", 16, "bold"), text_color="black", fg_color="transparent")
        titreAnnees.place(relx=0.125, rely=menuAnnees_y - 0.025, anchor="center")

        # Menu déroulant des mois.
        menuMois_y = menuAnnees_y + 0.15
        menuMois = ctk.CTkOptionMenu(self, variable=self.selection_mois, values=options_mois, command=None, font=("Arial", 13), corner_radius=8, height=36)
        menuMois.place(relx=0.025, rely=menuMois_y, anchor="nw", relwidth=0.2)

        # Label du menu déroulant de mois.
        titreMois = ctk.CTkLabel(self, text="Choix de mois", font=("Arial", 16, "bold"), text_color="black", fg_color="transparent")
        titreMois.place(relx=0.125, rely=menuMois_y - 0.025, anchor="center")



