from deportes.jugador import Jugador
from deportes.equipo import Equipo
from deportes.liga import Liga
from deportes.muerte_subita import MuerteSubita
from tabulate import tabulate


def ingresar_jugadores(equipo):
    num_jugadores = int(input(f"¿Cuántos jugadores tiene el equipo {equipo.nombre_equipo}? "))
    for i in range(num_jugadores):
        print(f"\nIngrese los datos del jugador {i + 1}:")
        apellido = input("Apellido: ")
        nombre = input("Nombre: ")
        cedula = input("Cédula: ")
        sexo = input("Sexo (True para masculino, False para femenino): ").strip().lower() == 'true'
        categoria = input("Categoría: ")
        foto = input("Foto (opcional, puede dejarse en blanco): ")
        jugador = Jugador(apellido=apellido, nombre=nombre, cedula=cedula, sexo=sexo, categoria=categoria, foto=foto)
        equipo.agregar_jugador(jugador)


def main():

    print("Ingrese los datos del primer equipo:")
    barrio1 = input("Barrio: ")
    color_uniforme1 = input("Color del uniforme: ")
    genero1 = input("Género (True para masculino, False para femenino): ").strip().lower() == 'true'
    nombre_equipo1 = input("Nombre del equipo: ")

    equipo1 = Equipo(barrio=barrio1, color_uniforme=color_uniforme1, genero=genero1, nombre_equipo=nombre_equipo1)
    ingresar_jugadores(equipo1)

    print("\nIngrese los datos del segundo equipo:")
    barrio2 = input("Barrio: ")
    color_uniforme2 = input("Color del uniforme: ")
    genero2 = input("Género (True para masculino, False para femenino): ").strip().lower() == 'true'
    nombre_equipo2 = input("Nombre del equipo: ")

    equipo2 = Equipo(barrio=barrio2, color_uniforme=color_uniforme2, genero=genero2, nombre_equipo=nombre_equipo2)
    ingresar_jugadores(equipo2)

    liga = Liga(jornadas=[])
    muerte_subita = MuerteSubita(rondas=[])

    goles_equipo1 = int(input(f"\nIngrese los goles del {equipo1.nombre_equipo}: "))
    goles_equipo2 = int(input(f"Ingrese los goles del {equipo2.nombre_equipo}: "))

    if goles_equipo1 > goles_equipo2:
        resultado = f"Ganador: {equipo1.nombre_equipo}"
    elif goles_equipo1 < goles_equipo2:
        resultado = f"Ganador: {equipo2.nombre_equipo}"
    else:
        resultado = "Empate"

    datos = [
        ["Equipo", "Goles"],
        [equipo1.nombre_equipo, goles_equipo1],
        [equipo2.nombre_equipo, goles_equipo2]
    ]

    print("\nEstadísticas del Partido:")
    print(tabulate(datos, headers="firstrow", tablefmt="grid"))

    print("\nResultado del Partido:")
    print(resultado)

    print(f"\nDatos del primer equipo ({equipo1.nombre_equipo}):")
    for jugador in equipo1.jugadores:
        print(f"Jugador: {jugador.nombre} {jugador.apellido}")

    print(f"\nDatos del segundo equipo ({equipo2.nombre_equipo}):")
    for jugador in equipo2.jugadores:
        print(f"Jugador: {jugador.nombre} {jugador.apellido}")


if __name__ == "__main__":
    main()

