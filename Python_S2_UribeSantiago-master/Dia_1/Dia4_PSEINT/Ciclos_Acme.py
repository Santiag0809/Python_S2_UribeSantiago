# La empresa Acme nos ha contratado para hacer la nómina de sus empleados.
# El algoritmo debe pedir el nombre del empleado y sus horas trabajadas.
# Al final mostrará cuánto se le pagará al empleado descontando el 4% de salud y el 4% de pensión.
# También mostrará el que más gana y el que menos gana,
# el promedio del salario bruto y neto de todos los empleados,
# y el total del salario bruto y neto.

numEmpleados = int(input("¿De cuántos empleados desea realizar la nómina? "))
nomina = []

for i in range(numEmpleados):
    nombre = input("Ingrese el nombre del empleado " + str(i + 1) + ": ")
    horasTrabajadas = int(input("Ingrese las horas trabajadas por " + nombre + ": "))
    valorHora = 20000
    salarioBruto = horasTrabajadas * valorHora
    descuentoSaludYPension = salarioBruto * 0.08  # 4% de salud y 4% de pensión
    salarioNeto = salarioBruto - descuentoSaludYPension

    nomina.append((nombre, horasTrabajadas, salarioBruto, descuentoSaludYPension, salarioNeto))

mayorSalario = nomina[0]
menorSalario = nomina[0]

for empleado in nomina:
    if empleado[4] > mayorSalario[4]:
        mayorSalario = empleado
    if empleado[4] < menorSalario[4]:
        menorSalario = empleado
totalBruto = 0
totalNeto = 0

for empleado in nomina:
    totalBruto += empleado[2]
    totalNeto += empleado[4]

promedioBruto = totalBruto / numEmpleados
promedioNeto = totalNeto / numEmpleados

print("El empleado con mayor salario neto es:", mayorSalario[0], "con $", mayorSalario[4])
print("El empleado con menor salario neto es:", menorSalario[0], "con $", menorSalario[4])
print("Total de salarios brutos: $", totalBruto)
print("Total de salarios netos: $", totalNeto)
print("Promedio de salarios brutos: $", promedioBruto)
print("Promedio de salarios netos: $", promedioNeto)


