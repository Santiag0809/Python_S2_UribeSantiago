# Usando diccionarios y listas creamos un programa que almacene los datos
# de i personas y los imprima en pantalla
# El programa debe pedir el nombre, apellido y edad, codigo de celular, numero celular y ciudad de nacimiento
# Además, según el código celular, este dirá si es un número personal o de trabajo de cada persona

diccionario1 = {
    "id": "1",
    "nombre": "Pedro",
    "apellido": "Gómez",
    "edad": 25,
    "ciudad": "Barichara",
    "telefonos": [
        {"codigo": 57, "numero": 3023019865, "tipo": "trabajo"},
        {"codigo": 1, "numero": 3983054625, "tipo": "personal"}
    ]
}
diccionario2 = {
    "id": "2",
    "nombre": "Corpus",
    "apellido": "Bejarano",
    "edad": 27,
    "ciudad": "Bucaramanga",
    "telefonos": [
        {"codigo": 58, "numero": 2323057565, "tipo": "trabajo"},
        {"codigo": 22, "numero": 6857493658, "tipo": "personal"}
    ]
}

personas = []
personas.append(diccionario1)
personas.append(diccionario2)


boleanito = True
while boleanito == True:
    print("#################")
    print("#### Librería de personas ####")
    print("#################")
    print("1. Crear Persona")
    print("2. Mostrar todas las personas")
    print("3. Mostrar a una persona individual")
    print("4. Actualizar a una persona en específico")
    print("5. Eliminar a una persona en específico")
    print("6. Cerrar programa")
    opcionUsuario = int(input("Escoja una opción (Numérica):"))

    if opcionUsuario == 1:
        print("#################")
        print("#### Crear Persona ####")
        print("#################")
        cantidad = int(input("¿Cuántas personas quieres ingresar?: "))
        for i in range(cantidad):
            print("")
            print("--- Persona #" + str(i + 1) + " ---")
            telefonos = []
            cant_numeros = int(input("¿Cuántos números de teléfono tienes?: "))
            for t in range(cant_numeros):
                print("--- Teléfono #" + str(t + 1) + " ---")
                codigo = int(input("Ingrese el código de su teléfono: "))
                numero = int(input("Ingrese el número de su teléfono: "))
                tipo = input("¿Es su numero personal o trabajo?:").lower
                if tipo != "personal":
                    tipo = "trabajo" 
                telefonos.append({"codigo": codigo, "numero": numero, "tipo": tipo})
                id_usado=[int(p["id"])for p in personas]
                idnuevo = 1 
                while idnuevo in id_usado:
                    idnuevo+=1

            persona = {
                "id": idnuevo,
                "nombre": input("Ingrese su nombre: "),
                "apellido": input("Ingrese su apellido: "),
                "edad": int(input("Ingrese su edad: ")),
                "telefonos": telefonos,
                "ciudad": input("Ingrese su ciudad de nacimiento: ")
            }

            personas.append(persona)

    elif opcionUsuario == 2:
        print("#################")
        print("#### Lista de Personas ####")
        print("#################")
        for h in range(len(personas)):
            print("#################")
            print("#### Persona #", h + 1, " ####")
            print("#################")
            print("ID:", personas[h]["id"])
            print("Nombre:", personas[h]["nombre"])
            print("Apellido:", personas[h]["apellido"])
            print("Edad:", personas[h]["edad"])
            print("Ciudad:", personas[h]["ciudad"])
            for profe in range(len(personas[h]["telefonos"])):
                print("---------------------------")
                print("Teléfono#", profe + 1, ":")
                print("#### - Código:", personas[h]["telefonos"][profe]["codigo"])
                print("#### - Número:", personas[h]["telefonos"][profe]["numero"])
                if personas[h]["telefonos"][profe]["tipo"] == "personal":
                    print("#### - Tipo: Es su número Personal")
                else:
                    print("#### - Tipo: Es su número de Trabajo")
                print("---------------------------")

    elif opcionUsuario == 3:
        print("#################")
        print("#################")
        idPersonita = input("Ingrese el id de la persona que desea ver: ")
        id_encontrado = None
        for persona in personas:
            if persona["id"] == idPersonita:
                id_encontrado = persona
                break

        if id_encontrado:
            print("#################")
            print("#### Datos de la persona ####")
            print("#################")
            print("ID:", id_encontrado["id"])
            print("Nombre:", id_encontrado["nombre"])
            print("Apellido:", id_encontrado["apellido"])
            print("Edad:", id_encontrado["edad"])
            print("Ciudad:", id_encontrado["ciudad"])
            for profe in range(len(id_encontrado["telefonos"])):
                print("---------------------------")
                print("Teléfono#", profe + 1, ":")
                print("#### - Código:", id_encontrado["telefonos"][profe]["codigo"])
                print("#### - Número:", id_encontrado["telefonos"][profe]["numero"])
                if id_encontrado["telefonos"][profe]["tipo"] == "personal":
                    print("#### - Tipo: Es su número Personal")
                else:
                    print("#### - Tipo: Es su número de Trabajo")
                print("---------------------------")
        else:
            print("No se encontró ninguna persona con el ID ingresado.")
            

    elif opcionUsuario == 4:
        print("#################")
        print("#### Actualizar Persona ####")
        print("#################")
        idPersonita = input("Ingrese el id de la persona que desea actualizar: ")
        for j in range(len(personas)):
            if personas[j]["id"] == idPersonita:
                print("ID:", personas[j]["id"])
                print("Nombre:", personas[j]["nombre"])
                print("Apellido:", personas[j]["apellido"])
                print("Edad:", personas[j]["edad"])
                print("Ciudad:", personas[j]["ciudad"])

                personas[j]["nombre"] = input("Ingrese el nuevo nombre: ")
                personas[j]["apellido"] = input("Ingrese el nuevo apellido: ")
                personas[j]["edad"] = int(input("Ingrese la nueva edad: "))
                personas[j]["ciudad"] = input("Ingrese la nueva ciudad: ")

                for profe in range(len(personas[j]["telefonos"])):
                    print("---------------------------")
                    print("Teléfono#", profe + 1, ":")
                    print("#### - Código:", personas[j]["telefonos"][profe]["codigo"])
                    print("#### - Número:", personas[j]["telefonos"][profe]["numero"])
                    if personas[j]["telefonos"][profe]["tipo"] == "personal":
                        print("#### - Tipo: Es su número Personal")
                    else:
                        print("#### - Tipo: Es su número de Trabajo")
                    print("---------------------------")
                break

    elif opcionUsuario == 5:
        print("#################")
        print("#### Eliminar Persona ####")
        print("#################")
        idsocio = input("Ingrese el id de la persona que desea eliminar: ")
        encontrada = False
        for l in range(len(personas)):
            if personas[l]["id"] == idsocio:
                del personas[l]
                print("Persona eliminada con éxito.")
                encontrada = True
                break
        if not encontrada:
            print("No se encontró ninguna persona con ese ID.")

    elif opcionUsuario == 6:
        print("Cerrando programa...")
        boleanito = False