# Algoritmo que cree un menú personalizado con precios y opciones
# y que permita al usuario elegir una opción y calcular el total.

numHamburguesas = int(input("¿Cuántas hamburguesas desea? "))
totalPedido = 0

for i in range(numHamburguesas):
    print("Hamburguesa", i + 1)
    subtotal = 0

    tipoPan = input("¿Qué tipo de pan desea? (1. Centeno - $1000, 2. Avena - $1500): ")
    if tipoPan == "1":
        subtotal += 1000
    elif tipoPan == "2":
        subtotal += 1500

    tipoCarne = input("¿Cuánto de carne desea? (1. 250g - $5000, 2. 300g - $7000): ")
    if tipoCarne == "1":
        subtotal += 5000
    elif tipoCarne == "2":
        subtotal += 7000

    tipoPollo1 = input("¿Cuánto de pollo desea? (1. 250g - $4500, 2. 350g - $5500): ")
    if tipoPollo1 == "1":
        subtotal += 4500
    elif tipoPollo1 == "2":
        subtotal += 5500

    tipoPollo2 = input("¿Cuánto de pollo desmechado desea? (1. 250g - $6500, 2. 350g - $7500): ")
    if tipoPollo2 == "1":
        subtotal += 6500
    elif tipoPollo2 == "2":
        subtotal += 7500

    tocineta = input("¿Cuánto de tocineta desea? (1. Una lonja - $1500, 2. Dos lonjas - $2500): ")
    if tocineta == "1":
        subtotal += 1500
    elif tocineta == "2":
        subtotal += 2500

    tipoPapa = input("¿Qué tipo de papa desea? (1. Papas a la francesa - $5000, 2. Papas en cascos - $6000): ")
    if tipoPapa == "1":
        subtotal += 5000
    elif tipoPapa == "2":
        subtotal += 6000

    bebidas = input("¿Qué bebida desea? (1. Gaseosa - $5000, 2. Cerveza Club Colombia - $8000, 3. Naranjada - $9000): ")
    if bebidas == "1":
        subtotal += 5000
    elif bebidas == "2":
        subtotal += 8000
    elif bebidas == "3":
        subtotal += 9000

    totalPedido += subtotal 
    
servicio = totalPedido * 0.10
totalConServicio = totalPedido + servicio

print("Total sin servicio: $", totalPedido)
print("Servicio (10%): $", servicio)
print("Total a pagar: $", totalConServicio)

