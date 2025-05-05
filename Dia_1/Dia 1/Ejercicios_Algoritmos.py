# # Algoritmo sumar dos numeros
print ("Bienvenido.Digite 2 numeros a sumar")
num1 = int(input())
num2 = int(input())
resultado = num1 + num2
print ("La suma de los dos numeros es: ", resultado)

# # Algoritmo hayar el mayor de 3 numeros
print (" Bienvenido. Digite 3 numeros a comparar")
numero1 = int(input())
numero2 = int(input())
numero3 = int(input())

mayor = max(numero1, numero2, numero3)
print ("El mayor de los 3 numeros es: ", mayor)

# # Algoritmo para calcular el factorial de un numero
print ("Bienvenido. Digite un numero para calcular su factorial")
num = int(input())
factorial = 1
for i in range(1, num + 1):
    factorial = factorial*i
print ("El factorial de ", num, " es: ", factorial)

# # Algoritmo para saber si un numero es primo o no
print ("Bienvenido. Digite un numero para saber si es primo")
numerito = int(input())
if numerito < 1:
    print ("El numerito no es primito")
else  :
    for i in range(2, numerito):
        if numerito % i == 0:
            print ("El numerito no es primito")
            break
    else:
        print("El numerito si es primito")

# # Algoritmo para convertir grados celcius a fahrenheit
print ("Bienvenido. Digite los grados celcius a convertir a fahrenheit")
celcius = int(input())
fahrenheit = (celcius * 9/5) + 32
print ("Los grados fahrenheit son: ", fahrenheit)

# # Algoritmo para saber si un numero es par o impar
print ("Bienvenido. Digite un numero para saber si es par o impar")
n = int(input())
if n % 2 == 0:
    print ("El numero es par")
else:
    print ("El numero es impar")

 # # Algoritmo para hayar el area de un triangulo
print ("Bienvenido. Digite la base y la altura del triangulo")
base = int(input())
altura = int(input())
area = (base * altura) / 2
print ("El area del triangulo es: ", area)

# # Algoritmo para generar la serie fibonacci
print ("Bienvenido. Digite el numero de terminos a hacer en la serie fibonacci")
n = int(input())
a, b = 0, 1
print ("La serie fibonacci es: ", end=" ")
for i in range(n):
    print(a, end=" ")
    a, b = b, a + b
print()

# # Algoritmo para generar una tabla de multiplicar
print ("Bienvenido. Digite el numero en el que vamosa hacer su tablita de multiplicar")
nu = int(input())
print ("La tabla de multiplicar del ", nu, " es: ")
for i in range(1, 11):
    print (nu, " x ", i, " = ", nu * i)

# # Algoritmo para hayar el promedio de una lista de numeros
print ("Bienvenido. Digite de cuanto sera su lista")
n = int(input())
numeros = []
for i in range(n):
  num = int(input(f"Digite el numero # {i + 1}: "))
  numeros.append(num)
promedio = sum(numeros) / len(numeros)
print ("El promedio de la lista es: ", promedio)

# # Algoritmo par hayar el area de un circulo
print ("Bienvenido. Digite el radio del circulo")
radio = int(input())
area = 3.1416 * (radio ** 2)
print ("El area del circulo es: ", area)