from .persona import Persona


class Jugador(Persona):
    def __init__(self, apellido, nombre, cedula, sexo, categoria, foto):
        super().__init__(apellido, nombre, cedula, sexo)
        self.categoria = categoria
        self.foto = foto
        self.tarjetas_amarillas = 0
        self.suspendido = False

    def recibir_tarjeta_amarilla(self):
        if not self.suspendido:
            self.tarjetas_amarillas += 1
            if self.tarjetas_amarillas >= 2:
                self.suspendido = True
                print(f"{self.nombre} {self.apellido} ha sido suspendido por acumulación de tarjetas amarillas.")

    def recibir_tarjeta_roja(self):
        self.suspendido = True
        print(f"{self.nombre} {self.apellido} ha sido suspendido por recibir una tarjeta roja.")

    def __str__(self):
        suspension_estado = "Suspendido" if self.suspendido else "Activo"
        return f"{self.nombre} {self.apellido} ({suspension_estado})"
