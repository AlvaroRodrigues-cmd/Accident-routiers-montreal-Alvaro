import customtkinter as ctk
from app import MainApplication

# Créer et ouvrir la fênetre de l'application.        
if __name__ == "__main__":
    ctk.set_appearance_mode("system")
    ctk.set_default_color_theme("blue")
    app = MainApplication()
    app.mainloop()