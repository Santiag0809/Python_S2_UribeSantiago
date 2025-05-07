# # Algoritmo para calcular el factorial de un número
# # Se pide un número al usuario
n = int(input("Ingresa un número: "))
# # # Se inicializa la variable factorial en 1
factorial = 1
# # Se calcula el factorial utilizando un bucle for
for i in range(1, n + 1):
    # # Se multiplica el número actual por el factorial acumulado
    factorial *= i
# # # Se imprime el resultado
print("El factorial de:", n, "es:", factorial)