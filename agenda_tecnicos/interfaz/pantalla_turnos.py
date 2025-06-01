import customtkinter as ctk
from datetime import datetime, timedelta

class PantallaTurnos (ctk.CTkFrame) :

    def __init__(self, master) :

        super().__init__(master)

        self.pack(fill = "both", expand = True) 

        self.label_titulo = ctk.CTkLabel(self, text = "Agenda", font = ctk.CTkFont(size = 18, weight = "bold"))
        self.frame_turnos = ctk.CTkScrollableFrame(self, width = 500, height = 400)

        self.label_titulo.pack(pady = 10)
        self.frame_turnos.pack(padx = 10, pady=10, fill = "both", expand = True)


    def mostrar_turnos_para_fecha (self, fecha) :

        # Limpiar turnos anteriores
        for widget in self.frame_turnos.winfo_children() :

            widget.destroy()

        self.label_titulo.configure(text = fecha.strftime("Agenda para el %d de %B de %Y").capitalize())

        hora_inicio = datetime.strptime("08:00", "%H:%M")
        hora_fin = datetime.strptime("12:00", "%H:%M")
        intervalo = timedelta(minutes = 15)

        ctk.CTkLabel(self.frame_turnos, text = "Turnos disponibles:", font = ctk.CTkFont(size = 14)).pack(pady = 5)

        hora_actual = hora_inicio

        while hora_actual < hora_fin :

            hora_str = hora_actual.strftime("%H:%M")
            ctk.CTkLabel(self.frame_turnos, text = f"{hora_str} - Disponible").pack(anchor="w", padx=10, pady=2)
            hora_actual += intervalo
