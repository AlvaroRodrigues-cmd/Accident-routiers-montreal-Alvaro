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
        carte_y = 0.35
        self.carte = HeatMapMaker(self, self.handler)
        self.carte.place(relx=0.6, rely=carte_y, anchor="center", relwidth=0.75, relheight=0.7)

        # Liste des statistiques disponibles.
        options_annees = ["2012", "2013", "2014", "2015", "2016", "2017", "2018", "2019", "2020", "2021"]
        options_mois = ["Janvier", "Février", "Mars", "Avril", "Mai", "Juin", "Juillet", "Août", "Septembre", "Octobre", "Novembre", "Décembre"]
        options_type = ["Nombre de collisions", "Nombre de morts", "Nombre de blessés graves", "Nombre de blessés légers",
                        "Nombre total de victimes", "Nombre de victimes piétons", "Nombre de victimes moto", "Nombre de victimes vélo"]

        # Variable pour le choix de la statistique.
        self.selection_annee = tk.StringVar(value=options_annees[0])
        self.selection_mois = tk.StringVar(value=options_mois[0])
        self.selection_type = tk.StringVar(value=options_type[0])

        # Menu déroulant d'années.
        menuAnnees_y = carte_y - 0.26
        menuAnnees = ctk.CTkOptionMenu(self, variable=self.selection_annee, values=options_annees, command=self.actualiser_carte, font=("Arial", 13), corner_radius=8, height=36)
        menuAnnees.place(relx=0.025, rely=menuAnnees_y, anchor="nw", relwidth=0.2)

        # Label du menu déroulant d'années.
        titreAnnees = ctk.CTkLabel(self, text="Choix d'année", font=("Arial", 16, "bold"), text_color="black", fg_color="transparent")
        titreAnnees.place(relx=0.125, rely=menuAnnees_y - 0.025, anchor="center")

        # Menu déroulant des mois.
        menuMois_y = menuAnnees_y + 0.15
        menuMois = ctk.CTkOptionMenu(self, variable=self.selection_mois, values=options_mois, command=self.actualiser_carte, font=("Arial", 13), corner_radius=8, height=36)
        menuMois.place(relx=0.025, rely=menuMois_y, anchor="nw", relwidth=0.2)

        # Label du menu déroulant de mois.
        titreMois = ctk.CTkLabel(self, text="Choix de mois", font=("Arial", 16, "bold"), text_color="black", fg_color="transparent")
        titreMois.place(relx=0.125, rely=menuMois_y - 0.025, anchor="center")

        # Menu déroulant de victimes.
        menuType_y = menuMois_y + 0.15
        menuType = ctk.CTkOptionMenu(self, variable=self.selection_type, values=options_type, command=self.actualiser_carte, font=("Arial", 13), corner_radius=8, height=36)
        menuType.place(relx=0.025, rely=menuType_y, anchor="nw", relwidth=0.2)

        # Label du menu déroulant de victimes.
        titreType = ctk.CTkLabel(self, text="Choix de type", font=("Arial", 16, "bold"), text_color="black", fg_color="transparent")
        titreType.place(relx=0.125, rely=menuType_y - 0.025, anchor="center")

        # Encadré des statistiques
        self.stats_frame = ctk.CTkFrame(self, fg_color="white", border_width=1, border_color="#D9DEE5", corner_radius=12)
        self.stats_frame.place(relx=0.025, rely=0.65, anchor="nw", relwidth=0.24, relheight=0.31)

        # Titre de l'encadré
        self.titre_stats = ctk.CTkLabel(self.stats_frame, text="Résumé statistique", font=("Arial", 16, "bold"), text_color="black")
        self.titre_stats.pack(pady=(12, 8))

        # Texte des statistiques
        self.texte_stats = ctk.CTkLabel(self.stats_frame, text="Chargez un fichier CSV", font=("Arial", 13), text_color="black", justify="left", anchor="w")
        self.texte_stats.pack(fill="x", padx=12, pady=8)

    def actualiser_carte(self, value=None):
        # Actualiser la carte thermique avec les sélections
        self.carte.update_heatmap(
            self.selection_annee.get(),
            self.selection_mois.get(),
            self.selection_type.get()
        )

