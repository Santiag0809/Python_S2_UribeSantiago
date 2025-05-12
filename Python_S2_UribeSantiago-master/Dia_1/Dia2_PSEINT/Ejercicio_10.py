# # Algoritmo que pida un numero para hacer una lista y luego saque el promedio de los valores ingresados
n = int(input("Hola, bienvenido porfavor inserte la cantidad "))
totalnumeros = 0

for i in range (n):
    numeros = int(input("Ingrese las califaciones o numeros para su tabla "))
    totalnumeros= totalnumeros + numeros
promedio = totalnumeros / n
print ("El promedio de tus notas o numeros es ", promedio)