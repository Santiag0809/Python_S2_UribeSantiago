# Algoritmo que imprima una secuencia de numeros desde 1 hasta n
num = int(input("Bienvenido,ingrese un numero "))
imprimir = " "
for i in range(1, num + 1):
    imprimir += str(i) + " "
print(imprimir)