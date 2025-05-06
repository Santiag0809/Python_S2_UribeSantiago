# Diccionario de menú para RAPPID BURGUERS
menu = {
    "pan": {
        "centeno": 1000,
        "avena": 1500
    },
    "carne": {
        "250g": 5000,
        "300g": 7000
    },
    "pollo": {
        "250g": 4500,
        "350g": 5500
    },
    "pollo_desmechado": {
        "250g": 6500,
        "350g": 7500
    },
    "tocineta": {
        "1_lonja": 1500,
        "2_lonjas": 2500
    },
    "papa": {
        "a_la_francesa": 5000,
        "en_cascos": 6000
    },
    "bebida": {
        "gaseosa": 5000,
        "cerveza": 8000,
        "naranjada": 9000
    }
}
def hamburguesa():
    total = 0
    print("\n=== Personaliza tu hamburguesa ===")

    pan = input("Tipo de pan (centeno/avena): ").lower()
    total += menu["pan"][pan]

    proteina_tipo = input("¿Qué proteína deseas? (carne/pollo/pollo_desmechado): ").lower()
    if proteina_tipo == "carne":
        cantidad = input("Cantidad de carne (250g/300g): ")
        total += menu["carne"][cantidad]
    elif proteina_tipo == "pollo":
        cantidad = input("Cantidad de pollo (250g/350g): ")
        total += menu["pollo"][cantidad]
    elif proteina_tipo == "pollo_desmechado":
        cantidad = input("Cantidad de pollo desmechado (250g/350g): ")
        total += menu["pollo_desmechado"][cantidad]
    tocineta = input("Tocineta (1_lonja/2_lonjas/ninguna): ").lower()
    if tocineta != "ninguna":
        total += menu["tocineta"][tocineta]
    papa = input("Tipo de papa (a_la_francesa/en_cascos/ninguna): ").lower()
    if papa != "ninguna":
        total += menu["papa"][papa]
    bebida = input("Bebida (gaseosa/cerveza/naranjada/ninguna): ").lower()
    if bebida != "ninguna":
        total += menu["bebida"][bebida]
    return total
def realizar_pedido():
    total_general = 0
    n = int(input("¿Cuántas hamburguesas deseas personalizar?: "))

    for i in range(n):
        print(f"\n--- Hamburguesa {i + 1} ---")
        total_hamburguesa = hamburguesa()
        total_general += total_hamburguesa

    servicio = total_general * 0.10
    total_pagar = total_general + servicio

    print(f"\nSubtotal: ${total_general}")
    print(f"Servicio (10%): ${servicio}")
    print(f"Total a pagar: ${total_pagar}")
realizar_pedido()

