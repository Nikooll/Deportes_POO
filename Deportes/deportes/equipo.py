class Equipo:
    def __init__(self, barrio, color_uniforme, genero, nombre_equipo):
        self.barrio = barrio
        self.color_uniforme = color_uniforme
        self.genero = genero
        self.nombre_equipo = nombre_equipo
        self.jugadores = []

    def agregar_jugador(self, jugador):
        self.jugadores.append(jugador)

    def __str__(self):
        return self.nombre_equipo