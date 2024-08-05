
from deportes.jugador import Jugador
from deportes.equipo import Equipo
from deportes.liga import Liga
from deportes.muerte_subita import MuerteSubita

def main():

    jugador1 = Jugador(apellido="Perez", nombre="Juan", cedula="1234567890", sexo=True, categoria="Senior", foto=None)
    jugador2 = Jugador(apellido="Gomez", nombre="Pedro", cedula="0987654321", sexo=True, categoria="Senior", foto=None)

    equipo = Equipo(barrio="Centro", color_uniforme="Rojo", genero=True, nombre_equipo="Los Tigres")

    liga = Liga(jornadas=[])
    
    muerte_subita = MuerteSubita(rondas=[])
    
    # Ejemplo de uso
    print(f"Jugador 1: {jugador1.nombre} {jugador1.apellido}")
    print(f"Jugador 2: {jugador2.nombre} {jugador2.apellido}")
    print(f"Equipo: {equipo.nombre_equipo}")
    print("Liga y Muerte Súbita creados.")

if __name__ == "__main__":
    main()
