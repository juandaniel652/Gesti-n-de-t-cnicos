# widgets/turno_card.py
import customtkinter as ctk

class TurnoCard(ctk.CTkFrame):
    def __init__(self, master, turno):
        super().__init__(master, corner_radius=5)
        if turno:
            self.configure(fg_color="#0052cc")  # azul oscuro
            ctk.CTkLabel(self, text=f"N° {turno['id']}\n{turno['cliente']}", font=("Arial", 12), text_color="white").pack(padx=4, pady=4)
        else:
            self.configure(fg_color="#a0f3a0")  # verde claro
            ctk.CTkLabel(self, text="+", font=("Arial", 20), text_color="black").pack(padx=4, pady=4)
