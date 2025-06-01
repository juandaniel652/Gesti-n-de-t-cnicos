import customtkinter as ctk

class PantallaFormulario (ctk.CTkFrame) :

    def __init__(self, master, callback_guardar = None) :

        super().__init__(master)

        self.pack(padx = 20, pady = 20, fill = "both", expand = True)

        self.callback_guardar = callback_guardar  # función que se llamará desde main

        ctk.CTkLabel(self, text="Formulario de Cliente", font=ctk.CTkFont(size=18, weight="bold")).pack(pady=10)

        #Entradas

        self.entrada_nombre = ctk.CTkEntry(self, placeholder_text="Nombre del cliente")

        self.entrada_direccion = ctk.CTkEntry(self, placeholder_text="Dirección")

        self.seleccion_tipo_servicio = ctk.CTkComboBox(self, values=["Instalación", "Reparación", "Mantenimiento", "Seleccione el servicio"], state = "readonly")
        self.seleccion_tipo_servicio.set("Seleccione el servicio")
        
        self.seleccion_ticket = ctk.CTkComboBox(self, values=["Sí", "No"], state = "readonly")
        self.seleccion_ticket.set("¿Tiene ticket?")
        
        self.boton_guardar = ctk.CTkButton(self, text="Continuar", command=self.enviar_formulario)

        #Ubicación

        lista_entradas = [self.entrada_nombre, self.entrada_direccion, 
                        self.seleccion_tipo_servicio, self.seleccion_ticket]

        for indice, entrada in enumerate (lista_entradas) : 

            entrada.pack(pady = 5, fill = "x")

        self.boton_guardar.pack(pady = 15)
        

    def enviar_formulario(self) :

        datos = {
            "nombre": self.entrada_nombre.get(),
            "direccion": self.entrada_direccion.get(),
            "servicio": self.seleccion_tipo_servicio.get(),
            "ticket": self.seleccion_ticket.get()
        }

        consulta_ticket = self.seleccion_ticket.get() 

        if consulta_ticket == "No" :

            return consulta_ticket