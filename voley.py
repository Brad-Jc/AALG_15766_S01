import random

class equipo:
    def __init__(self, nombre):
        self.nombre = nombre
        self.partidosganados = 0
        self.partidosperdidos = 0
        self.setganados = 0

def puntos():
    return random.randint(10, 28)

def puntosextras():
    return random.randint(0, 6)

def registraset(ganador, equipo1, equipo2):
    if ganador == 1:
        equipo1.setganados += 1
    else:
        equipo2.setganados += 1

def jugarset(equipo1, equipo2):
    puntos1 = puntos()
    puntos2 = puntos()

    while True:
        if puntos1 >= 25 and puntos1 > puntos2:
            registraset(1, equipo1, equipo2)
            break
        elif puntos2 >= 25 and puntos2 > puntos1:
            registraset(2, equipo1, equipo2)
            break
        else:
            puntos1 += puntosextras()
            puntos2 += puntosextras()

def jugarpartido(equipo1, equipo2):
    equipo1.setganados = 0
    equipo2.setganados = 0

    while equipo1.setganados < 3 and equipo2.setganados < 3:
        jugarset(equipo1, equipo2)

    if equipo1.setganados == 3:
        equipo1.partidosganados += 1
        equipo2.partidosperdidos += 1
        print(f"{equipo1.nombre} ganó el partido")
    else:
        equipo2.partidosganados += 1
        equipo1.partidosperdidos += 1
        print(f"{equipo2.nombre} ganó el partido")

def resultadotorneo(equipo1, equipo2):
    print("\n    RESULTADO FINAL    ")
    print(f"{equipo1.nombre} - Ganados: {equipo1.partidosganados}, Perdidos: {equipo1.partidosperdidos}")
    print(f"{equipo2.nombre} - Ganados: {equipo2.partidosganados}, Perdidos: {equipo2.partidosperdidos}")

def main():
    nombre1 = input("Nombre del equipo 1: ")
    nombre2 = input("Nombre del equipo 2: ")

    equipo1 = equipo(nombre1)
    equipo2 = equipo(nombre2)

    try:
        cantidad = int(input("¿Cuantos partidos deben jugar?: "))
    except ValueError:
        print("Error")
        return

    for i in range(cantidad):
        print(f"\n   Partido {i+1}   ")
        jugarpartido(equipo1, equipo2)

    resultadotorneo(equipo1, equipo2)

if __name__ == "__main__":
    main()