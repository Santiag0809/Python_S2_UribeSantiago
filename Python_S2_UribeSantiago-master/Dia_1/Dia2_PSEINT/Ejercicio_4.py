# Algoritmo para determinar si un número es primo 
n = int(input("Ingresa un número: "))
if n <= 1:
    print(n, "no es un número primo")
else:
    for i in range(2, n):
        if n % i == 0:
            print(n, "no es un número primo")
            break
    else:
        print(n, "es un número primo")