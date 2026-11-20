import customtkinter as ctk
import numpy as np

from matplotlib.figure import Figure
from matplotlib.colors import LinearSegmentedColormap
from matplotlib.backends.backend_tkagg import FigureCanvasTkAgg

class HeatMapMaker(ctk.CTkFrame):
    def __init__(self, master, handler):
        super().__init__(master)
        # Création de la figure.
        self.figure = Figure(figsize=(7, 7))

        # Création des axes du graphique.
        self.ax = self.figure.add_subplot(111)

        # Intégration du graphique dans CustomTkinter.
        self.canvas = FigureCanvasTkAgg(self.figure, master=self)
        self.canvas.get_tk_widget().pack(fill="both", expand=True)

        # DataHandler
        self.handler = handler
        self.create_heatmap()

    def create_heatmap(self):
        # Effacer ancien graphique.
        # self.ax.clear()

        testarr = np.random.randint(0, 15, size=(7, 24))

        # Intensité couleurs.
        colors = ["#264653", "#2A9D8F", "#E9C46A", "#F4A261", "#E76F51"]
        custom_cmap = LinearSegmentedColormap.from_list("custom_gradient", colors)
        
        im = self.ax.imshow(testarr, cmap=custom_cmap)

        # Créer la barre de couleurs de fréquences.
        cbar = self.figure.colorbar(im, ax=self.ax, orientation="horizontal")
        cbar.set_label("Fréquence des collisions")

        # Titre du graphique et des axes.
        self.ax.set_title("Fréquence d'accidents à chaque journée en 24 heures")
        self.ax.set_xlabel("Heures de la journée")
        self.ax.set_ylabel("Journées de la semaine")

        # Noms des journées.
        n_journees = ["Lundi", "Mardi", "Mercredi", "Jeudi", "Vendredi", "Samedi", "Dimanche"]

        # Titre des lignes et des colonnes.
        self.ax.set_xticks(range(24))
        self.ax.set_yticks(range(len(n_journees)), labels=n_journees)

        # Ajouter le texte de numéro de fréquences dans chaque case.
        for i in range(len(n_journees)):
            for j in range(24):
                self.ax.text(j, i, testarr[i, j], ha="center", va="center", color="w")

    def update_heatmap(self):
        self.create_heatmap()
