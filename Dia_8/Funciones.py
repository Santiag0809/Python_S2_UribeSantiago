def ingresar_telefonos():
    telefonos = []
    cant_numeros = int(input("¿Cuántos números de teléfono tienes?: "))
    for t in range(cant_numeros):
        print("--- Teléfono #" + str(t + 1) + " ---")
        codigo = int(input("Ingrese el código de su teléfono: "))
        numero = int(input("Ingrese el número de su teléfono: "))
        tipo = input("¿Es su numero personal o trabajo?: ").lower()
        if tipo != "personal":
            tipo = "trabajo"
        telefonos.append({"codigo": codigo, "numero": numero, "tipo": tipo})
    return telefonos


def actualizar_persona(persona, modo):
    if modo == "todo":
        persona["nombre"] = input("Ingrese el nuevo nombre: ")
        persona["apellido"] = input("Ingrese el nuevo apellido: ")
        persona["edad"] = int(input("Ingrese la nueva edad: "))
        persona["ciudad"] = input("Ingrese la nueva ciudad: ")
        persona["telefonos"] = ingresar_telefonos()
    elif modo == "telefonos":
        for b, tel in enumerate(persona["telefonos"]):
            print(f"--- Teléfono #{b+1} ---")
            tel["codigo"] = int(input("Nuevo código: "))
            tel["numero"] = int(input("Nuevo número: "))
            tipo = input("¿Es su número personal o trabajo?: ").lower()
            if tipo != "personal":
                tipo = "trabajo"
            tel["tipo"] = tipo
    elif modo == "nombre":
        persona["nombre"] = input("Nuevo nombre: ")
    elif modo == "apellido":
        persona["apellido"] = input("Nuevo apellido: ")
    elif modo == "edad":
        persona["edad"] = int(input("Nueva edad: "))
    elif modo == "ciudad":
        persona["ciudad"] = input("Nueva ciudad: ")
    return persona
