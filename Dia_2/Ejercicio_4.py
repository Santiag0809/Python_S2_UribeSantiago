# Algoritmo para determinar si un número es primo 
n = int(input("Ingresa un número: "))
if n <= 1:
    # Si el número es menor o igual a 1, no es primo
    print(n, "no es un número primo")
else:
    for i in range(2, n):
        if n % i == 0:
            # Si se encuentra un residuo diferente de 0, no es primo
            print(n, "no es un número primo")
            break
    else:
        # Si no se encuentra ningún divisor, es primo
        print(n, "es un número primo")