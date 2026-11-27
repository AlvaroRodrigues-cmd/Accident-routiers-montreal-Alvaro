import customtkinter as ctk
import pandas as pd

from matplotlib.figure import Figure
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class HeatMapMaker(ctk.CTkFrame):
    def __init__(self, master, handler):
        super().__init__(master)
        # DataHandler
        self.handler = handler

        # Création de la figure.
        self.figure = Figure(figsize=(12, 6), dpi=100)
        self.ax = self.figure.add_subplot(111)

        # Barre de couleurs, initialement vide.
        self.colorbar = None

        # Intégration du graphique dans CustomTkinter.
        self.canvas = FigureCanvasTkAgg(self.figure, master=self)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)

        # Message de départ.
        self.afficher_message("Chargez un fichier CSV")

    def create_heatmap(self, pivot_table, params):
        # Effacer ancien carte thermique.
        self.ax.clear()

        # Créer la carte thermique à partir des données.
        im = self.ax.imshow(pivot_table.values, cmap="YlOrRd", aspect="auto")

        # Définir les heures sur l'axe horizontal.
        self.ax.set_xticks(range(24))
        self.ax.set_xticklabels(range(24))

        # Définir les jours sur l'axe vertical
        self.ax.set_yticks(
            range(7),
            labels=[
                "Lundi", "Mardi", "Mercredi",
                "Jeudi", "Vendredi", "Samedi", "Dimanche"
            ]
        )

        # Ajouter les titres des axes.
        self.ax.set_xlabel("Heure")
        self.ax.set_ylabel("Jour")

        # Ajouter le titre du graphique.
        self.ax.set_title(f"{params[0]} par jour et par heure au mois de {params[1]} en {params[2]}")

        # Créer la barre de couleurs une seule fois
        if self.colorbar is None:
            self.colorbar = self.figure.colorbar(
                im,
                ax=self.ax,
                orientation="horizontal"
            )
            self.colorbar.set_label("Fréquence des collisions")
        else:
            # Actualiser la barre de couleurs existante
            self.colorbar.update_normal(im)

        # Actualiser le graphique.
        self.canvas.draw_idle()

    def update_heatmap(self, annee, mois, type_victimes, texte_stats):
        # Si les données ne sont pas chargées, arrêter l'éxecution.
        if self.handler.df.empty:
            return

        # Dictionnaire associant les mois à leur numéro.
        mois_dict = {
            "Janvier": 1,
            "Février": 2,
            "Mars": 3,
            "Avril": 4,
            "Mai": 5,
            "Juin": 6,
            "Juillet": 7,
            "Août": 8,
            "Septembre": 9,
            "Octobre": 10,
            "Novembre": 11,
            "Décembre": 12
        }

        # Copier le DataFrame.
        resultat = self.handler.df.copy()

        # Garder seulement les accidents de l'année sélectionnée
        resultat = resultat[resultat["AN"] == int(annee)]

        # Transformer la date de l'accident en datetime.
        # Ensuite filtrer le DataFrame par mois.
        resultat["DT_ACCDN"] = pd.to_datetime(resultat["DT_ACCDN"]) 
        resultat = resultat[resultat["DT_ACCDN"].dt.month == mois_dict[mois]]

        # Extraire l'heure de chaque accident
        resultat["HEURE"] = pd.to_numeric(resultat["HEURE_ACCDN"].str[:2], errors="coerce")

        # Dico d'équivalence pour les noms de colonnes du DataFrame.
        colonnes = {
            "Nombre de morts": "NB_MORTS",
            "Nombre de blessés graves": "NB_BLESSES_GRAVES",
            "Nombre de blessés légers": "NB_BLESSES_LEGERS",
            "Nombre total de victimes": "NB_VICTIMES_TOTAL",
            "Nombre de victimes piétons": "NB_VICTIMES_PIETON",
            "Nombre de victimes moto": "NB_VICTIMES_MOTO",
            "Nombre de victimes vélo": "NB_VICTIMES_VELO"
        }

        # Déterminer la valeur à utiliser selon le choix de l'utilisateur.
        if type_victimes == "Nombre de collisions":
            # Chaque ligne représente une collision.
            resultat["VALEUR"] = 1
        else:
            # Récupérer la colonne correspondant au type sélectionné.
            resultat["VALEUR"] = resultat[colonnes[type_victimes]]

        # Créer un tableau croisé dynamique.
        # Les lignes représentent les jours.
        # Les colonnes représentent les heures.
        # Les valeurs sont additionnées.

        df_pivot = resultat.pivot_table(
            index="JR_SEMN_ACCDN",
            columns="HEURE",
            values="VALEUR",
            aggfunc="sum",
            fill_value=0
        )

        # Liste des jours de la semaine dans l'ordre.
        jours = ["LU", "MA", "ME", "JE", "VE", "SA", "DI"]

        # S'assurer que les 7 jours et les 24 heures sont présents.
        df_pivot = df_pivot.reindex(index=jours, columns=range(24), fill_value=0)

        # Nouveau texte de statistiques.
        texte = ("Total mois: \n\n"
                 "Total année: \n\n"
                 "Journée(s) record: ")

        # Réinitialiser le graphique.
        self.create_heatmap(df_pivot, (type_victimes, mois, annee))

        # Préparer les données pour l'exportation CSV
        self.handler.df_resultats = df_pivot.reset_index()

        # Préparer le graphique pour l'exportation PNG.
        self.handler.graph_resultat = self.figure

        # Changer le texte de statistiques.
        texte_stats.configure(text=texte)

    def afficher_message(self, message):
        # Effacer l'ancien graphique.
        self.ax.clear()

        # Si la barre de couleurs est visible, l'effacer.
        if self.colorbar is not None:
            self.colorbar.remove()
            self.colorbar = None

        # Créer le texte au millieu du graphique.
        self.ax.text(
            0.5,
            0.5,
            message,
            fontsize=16,
            ha='center',
            va='center', 
            transform=self.ax.transAxes
        )

        # Cacher le graphique vide.
        self.ax.axis("off")