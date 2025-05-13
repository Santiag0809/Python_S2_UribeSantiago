# Algoritmo que imprima el cuadrado de un numero desde 0 hasta n 
num = int(input("Bienvenido,ingrese un numero "))

for i in range(num):
    print(i**2, end=" ")

imprimir = ""
for i in range(num):
    imprimir += str( i**2) + " "
print (imprimir)

