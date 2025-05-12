# Encontrar el promedio de un estudiante en una lista de estudiantes y sus notas
n = int(input())  
estudiantes = []     
for i in range(n):
        datos = input().split()  
        nombre = datos[0]
        notas = [float(nota) for nota in datos[1:]]  
        estudiantes.append((nombre, notas))     
query_name = input().strip()    
for nombre, notas in estudiantes:
        if nombre == query_name:
            promedio = sum(notas) / len(notas)
            print(f"{promedio:.2f}") 
