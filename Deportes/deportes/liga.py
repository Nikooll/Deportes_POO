class Liga:
    def __init__(self, jornadas):
        self.jornadas = jornadas

    def __str__(self):
        return f"Liga con {len(self.jornadas)} jornadas"
