import customtkinter as ctk
from interfaz.pantalla_formulario import PantallaFormulario
from interfaz.pantalla_calendario import PantallaCalendario
from interfaz.pantalla_turnos import PantallaTurnos

class App (ctk.CTk) :

    def __init__ (self) :

        super().__init__()
        self.title("Gestor de Turnos")
        self.geometry("500x500")
        self.minsize(800, 600)

        self.pestanas = ctk.CTkTabview (self)
        self.pestanas.pack(fill = "both", expand = True)

        self.pestana_consulta = self.pestanas.add("Consulta")
        self.pestana_calendario = self.pestanas.add("Calendario")
        self.pestana_turnos = self.pestanas.add("Agenda")

        pantalla_formulario = PantallaFormulario(self.pestana_consulta)
        pantalla_agenda = PantallaTurnos(self.pestana_turnos)

        def actualizar_agenda(fecha_seleccionada) :

            self.pestanas.set("Agenda")
            pantalla_agenda.mostrar_turnos_para_fecha(fecha_seleccionada)

        PantallaCalendario(self.pestana_calendario, callback_agenda = actualizar_agenda)


if __name__ == "__main__" :

    ctk.set_appearance_mode("light")  
    ctk.set_default_color_theme("blue")
    app = App()
    app.mainloop()