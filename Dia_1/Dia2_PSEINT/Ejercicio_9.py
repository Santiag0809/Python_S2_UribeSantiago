# # Algoritmo que reciba un numero y de la tabla de multiplicar de dicho numero
n = int(input("Bienvenido, digite su numero para realizar la tabla"))
for i in range(1,11):
    resultado= n*i 
    print(n, "x", i, "=",resultado)