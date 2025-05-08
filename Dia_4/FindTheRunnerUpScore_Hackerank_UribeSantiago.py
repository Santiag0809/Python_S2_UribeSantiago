# Algoritmo que encuentra el segundo puntaje más alto de una carrera
n = int(input("Bienvenido, ingrese la cantidad de participantes: "))
arr = list(map(int, input("Ingrese los puntajes de los participantes separados por espacios: ").split()))
primero = segundo = -101  

for num in arr:
    if num > primero:
        segundo = primero
        primero = num
    elif primero > num > segundo:
        segundo = num

print("El segundo puntaje más alto es:", segundo)