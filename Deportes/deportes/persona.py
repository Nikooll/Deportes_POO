class Persona:
    def __init__(self, apellido, nombre, cedula, sexo):
        self.apellido = apellido
        self.nombre = nombre
        self.cedula = cedula
        self.sexo = sexo

    def __str__(self):
        return f"{self.nombre} {self.apellido}"

