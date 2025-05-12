# Algoritmo que lea 4 valores enteros x,y,z n que representan las dimensiones de un cuboide y el numero que se excluye
# Por cada i generar valores posibles de 0 hasta x
# Por cada i genera los valores de j que va desde 0 hasta y 
# Por cada combinacion de i y j genera los valores de k que va desde 0 hasta z
# Por ultimo solo se imprimara los reultados de i + j + k que no sean iguales a n
# La lista se imprimira en orden de menor a mayor
x = int(input("Ingrese el valor de x: "))
y = int(input("Ingrese el valor de y: "))
z = int(input("Ingrese el valor de z: "))
n = int(input("Ingrese el valor de n: "))
resultado = [[i, j, k] 
             for i in range(x + 1) 
             for j in range(y + 1) 
             for k in range(z + 1) 
             if i + j + k != n]
print(resultado)