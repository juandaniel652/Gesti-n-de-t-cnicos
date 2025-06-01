import customtkinter as ctk
import calendar
from datetime import datetime
import locale

locale.setlocale(locale.LC_TIME, 'es_ES.utf8')


class PantallaCalendario (ctk.CTkFrame) :

    def __init__(self, master, callback_agenda) :

        super().__init__(master)

        self.callback_agenda = callback_agenda

        marco_seleccion = ctk.CTkFrame(master, fg_color = "#f0f0f0")

        self.master = master

        self.fecha_actual = datetime.today().replace(day = 1)

        self.dia_seleccionado = None

        #Botones y etiquetas

        self.boton_anterior = ctk.CTkButton(marco_seleccion, text = "←", width = 40, command = self.retroceder_mes)

        self.etiqueta_mes = ctk.CTkLabel(master, text = "", font = ("Arial", 20, "bold"))

        meses = [calendar.month_name[mes].capitalize() for mes in range(1, 13)]
        self.cambio_de_mes = ctk.CTkComboBox(marco_seleccion, values = meses, state = "readonly", command = self.cambiar_mes)

        anios = [str(anio) for anio in range(datetime.today().year, datetime.today().year + 10)]
        self.cambio_de_anio = ctk.CTkComboBox(marco_seleccion, values = anios, state = "readonly", command = self.cambiar_anio)

        self.boton_siguiente = ctk.CTkButton(marco_seleccion, text = "→", width = 40, command = self.avanzar_mes)

        self.marco_calendario = ctk.CTkFrame(master)

        self.etiqueta_dia = ctk.CTkLabel(master, text = "", font = ("Arial", 16))

        #Ubicación

        marcos_y_etiquetas = [marco_seleccion, self.etiqueta_dia, self.etiqueta_mes, self.marco_calendario]
        botones_y_cambios = [self.boton_anterior, self.cambio_de_mes, self.cambio_de_anio, self.boton_siguiente]
        
        ubicacion_pady = [(0, 10), (10, 5), (10, 5), 10]
        ubicacion_padx = [5, 10, 10, 5]

        for indice, marcos in enumerate (marcos_y_etiquetas) :

            marcos.pack(pady = ubicacion_pady[indice])

        for indice, botones in enumerate (botones_y_cambios) : 

            botones.pack(side = "left", padx = ubicacion_padx[indice])
        
        self.actualizar_selectores()
        self.mostrar_calendario()


    def actualizar_selectores (self) :

        mes_nombre = self.fecha_actual.strftime("%B").capitalize()
        self.cambio_de_mes.set(mes_nombre)
        self.cambio_de_anio.set(str(self.fecha_actual.year))
        self.etiqueta_mes.configure(text = f"{mes_nombre} {self.fecha_actual.year}")


    def cambiar_mes (self, valor) :

        meses = [calendar.month_name[mes].capitalize() for mes in range(1, 13)]

        if valor in meses :

            nuevo_mes = meses.index(valor) + 1
            self.fecha_actual = self.fecha_actual.replace(month = nuevo_mes)
            self.mostrar_calendario()


    def cambiar_anio(self, valor) :

        self.fecha_actual = self.fecha_actual.replace(year = int(valor))
        self.mostrar_calendario()


    def avanzar_mes (self) : 

        año = self.fecha_actual.year
        mes = self.fecha_actual.month + 1

        if mes > 12 :

            mes = 1
            año += 1

        self.fecha_actual = self.fecha_actual.replace(year = año, month = mes)
        self.mostrar_calendario()


    def retroceder_mes(self) :

        anio = self.fecha_actual.year
        mes = self.fecha_actual.month - 1

        if mes < 1 :
            mes = 12
            anio -= 1

        self.fecha_actual = self.fecha_actual.replace(year = anio, month = mes)
        self.mostrar_calendario()
 

    def mostrar_calendario (self) :

        for widget in self.marco_calendario.winfo_children() :

            widget.destroy()

        self.actualizar_selectores()
        mes = self.fecha_actual.month
        anio = self.fecha_actual.year

        dias_semana = ["Lun", "Mar", "Mié", "Jue", "Vie", "Sáb", "Dom"]

        for indice, dia in enumerate(dias_semana) :

            ctk.CTkLabel(self.marco_calendario, text = dia, font=("Arial", 18, "bold")).grid(row = 0, column = indice)

        calendario_mes = calendar.Calendar(firstweekday = 0).monthdayscalendar(anio, mes)

        for fila, semana in enumerate (calendario_mes, start = 1) :

            for columna, dia in enumerate (semana) :

                if dia == 0 :

                    continue

                botones_dias = ctk.CTkButton(
                    self.marco_calendario,
                    text = str(dia),
                    font = ("Arial", 18, "italic"),
                    fg_color = "#f5f6f6",
                    text_color = "black",
                    width = 50,
                    height = 50,
                    corner_radius = 50,
                    command = lambda d = dia: self.seleccionar_dia(d)
                )

                botones_dias.grid(row = fila, column = columna, padx = 3, pady = 3)


    def seleccionar_dia(self, dia) :

        fecha_seleccionada = self.fecha_actual.replace(day = dia)
        self.callback_agenda(fecha_seleccionada)