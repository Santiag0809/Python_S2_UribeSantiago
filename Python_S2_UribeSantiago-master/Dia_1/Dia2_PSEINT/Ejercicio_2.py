# # ALgoritmo para hayar el mayor de tres numeros
a = int(input("Ingrese su primer numero a comparar"))
b = int(input("Ingrese su segundo numero a comparar"))
c = int(input("Ingrese su tercer numero a comparar"))
if a>b and a>c:
    mayor=a 
elif b>a and b>c:
    mayor=b 
else:
    mayor=c 
print("El numero mayor es ",mayor)
