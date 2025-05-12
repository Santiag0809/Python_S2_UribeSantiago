# Algoritmo que dada una lista la organice y bote el segundo resultado mas bajo
cantidad = int(input())
estudiantes = []
contador = 0
while contador < cantidad:
    nombre = input()
    nota = float(input())
    estudiantes.append([nombre, nota])
    contador = contador + 1
