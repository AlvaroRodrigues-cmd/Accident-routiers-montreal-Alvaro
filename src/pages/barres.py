import customtkinter as ctk
import tkinter as tk

from graphes.bar_maker import BarMaker

class Barres(ctk.CTkFrame):
    def __init__(self, master, handler, **kwargs):
        super().__init__(master, **kwargs)
        # DataHandler
        self.handler = handler

        # Créer la page du graphique de barrres.
        self.creer_page_graphique_bar()

    def creer_page_graphique_bar(self):
        # Créer et insérer le graphique de barres.
        barres_y = 0.35
        self.barres_graphe = BarMaker(self, self.handler)
        self.barres_graphe.place(relx=0.6, rely=barres_y, anchor="center", relwidth=0.75, relheight=0.7)

        # Options pout les dropdowns.
        options_annees = ["2012","2013","2014","2015","2016","2017","2018","2019","2020","2021"]
        options_type = ["Tout","Nombre de morts", "Nombre de blessés graves", "Nombre de blessés légers",
                "Nombre total de victimes", "Nombre de victimes piétons", "Nombre de victimes moto", "Nombre de victimes vélo"]

        # Conversion de string à tk.StringVar des options.
        self.selection_annees_bar = tk.StringVar(value = options_annees[0])
        self.selection_type = tk.StringVar(value= options_type[0])

        # Création du prèmier bouton dropdown (années).
        menuDeroulant_y = barres_y - 0.26 
        menuDeroulantGraphique = ctk.CTkOptionMenu(self, variable=self.selection_annees_bar, values=options_annees, command=self.actualiser_barres, font=("Arial", 13), corner_radius=8, height=36)
        menuDeroulantGraphique.place(relx=0.025, rely=menuDeroulant_y, anchor="nw", relwidth=0.2)

        # Titre du bouton 1.
        TitreMenuDeroulantGraphique = ctk.CTkLabel(self, text="Année", font=("Arial", 16, "bold"), text_color="black", fg_color="transparent")
        TitreMenuDeroulantGraphique.place(relx=0.125, rely=menuDeroulant_y - 0.025, anchor="center")

        # Création du déuxieme bouton dropdown (types de victimes).
        menuDeroulant2_y = menuDeroulant_y + 0.15
        menuDeroulantGraphique2 = ctk.CTkOptionMenu(self, variable=self.selection_type, values=options_type, command=self.actualiser_barres, font=("Arial", 13), corner_radius=8, height=36)
        menuDeroulantGraphique2.place(relx=0.025, rely=menuDeroulant2_y, anchor="nw", relwidth=0.2)

        # Titre du bouton 2.
        TitreMenuDeroulantGraphique2 = ctk.CTkLabel(self, text="Type de victime", font=("Arial", 16, "bold"), text_color="black", fg_color="transparent")
        TitreMenuDeroulantGraphique2.place(relx=0.125, rely= menuDeroulant2_y - 0.025, anchor="center")

        # Encadré des statistiques
        self.stats_frame = ctk.CTkFrame(self, fg_color="white", border_width=1, border_color="#D9DEE5", corner_radius=12)
        self.stats_frame.place(relx=0.025, rely=0.60, anchor="nw", relwidth=0.3, relheight=0.35)

        # Titre de l'encadré
        self.titre_stats = ctk.CTkLabel(self.stats_frame, text="Résumé statistique", font=("Arial", 20, "bold"), text_color="black")
        self.titre_stats.pack(pady=(12, 8))

        # Texte des statistiques
        self.texte_stats = ctk.CTkLabel(self.stats_frame, text="Chargez un fichier CSV", font=("Arial", 18), text_color="black", justify="left", anchor="w")
        self.texte_stats.pack(fill="x", padx=12, pady=8)

    def actualiser_barres(self, value=None):
        # Actualiser le graphique à barres avec les sélections.
        self.barres_graphe.update_bar(
            self.selection_annees_bar.get(),
            self.selection_type.get(),
            self.texte_stats
        )