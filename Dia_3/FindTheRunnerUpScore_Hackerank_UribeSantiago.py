# Algoritmo que encuentra el segundo puntaje más alto de una carrera 
num = int(input("Bienvenido, ingrese la cantidad de participantes: "))
puntajes = []

for i in range(num):
    puntaje = float(input("Ingrese el puntaje del participante: "))
    puntajes.append(puntaje)

puntajes_ordenados = sorted(puntajes)
puntaje_maximo = puntajes_ordenados[-1]

for i in range(len(puntajes_ordenados) - 2, -1, -1):
   
    if puntajes_ordenados[i] < puntaje_maximo:
        puntaje_segundo_maximo = puntajes_ordenados[i]
        break

print("El segundo puntaje más alto es:", puntaje_segundo_maximo)