# Usando diccionarios y listas creamos un programa que almacene los datos
# de i personas y los imprima en pantalla
# El programa debe pedir el nombre, apellido y edad, codigo de celular, numero celular y ciudad de nacimiento
# Además, según el código celular, este dirá si es un número personal o de trabajo de cada persona

print("Bienvenido a la librería de personas")
personas = []

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
        for h in range(cantidad):
            print("")
            print("--- Persona #" + str(h + 1) + " ---")
            persona = {
                "id": input("Ingrese el id de usuario: "),
                "nombre": input("Ingrese su nombre: "),
                "apellido": input("Ingrese su apellido: "),
                "edad": int(input("Ingrese su edad: ")),
                "telefonos": [
                    {
                        "codigo": int(input("Ingrese el código de su teléfono: ")),
                        "numero": int(input("Ingrese el número de su teléfono: "))
                    }
                ],
                "ciudad": input("Ingrese su ciudad de nacimiento: ")
            }

            if persona["telefonos"][0]["codigo"] == 57:
                persona["telefonos"][0]["tipo"] = "trabajo"
            else:
                persona["telefonos"][0]["tipo"] = "personal"

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
        
        id_encontrado = "No hay socio con ese ID"
        for persona in personas:
            if persona["id"] == idPersonita:
                id_encontrado = persona
            else:
                print("No se encontró ninguna persona con el ID ingresado.")
                
        if id_encontrado != "No hay socio con ese ID":
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
        
    elif opcionUsuario == 4:
        print("#################")
        print("#### Actualizar Persona ####")
        print("#################")
        idPersonita = input("Ingrese el id de la persona que desea actualizar: ")
        
        for h in range(len(personas)):
            if personas[h]["id"] == idPersonita:
                print("ID:", personas[h]["id"])
                print("Nombre:", personas[h]["nombre"])
                print("Apellido:", personas[h]["apellido"])
                print("Edad:", personas[h]["edad"])
                print("Ciudad:", personas[h]["ciudad"])
                
                # Actualizar datos
                personas[h]["nombre"] = input("Ingrese el nuevo nombre: ")
                personas[h]["apellido"] = input("Ingrese el nuevo apellido: ")
                personas[h]["edad"] = int(input("Ingrese la nueva edad: "))
                personas[h]["ciudad"] = input("Ingrese la nueva ciudad: ")
                
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

    elif opcionUsuario == 5:
        print("#################")
        print("#### Eliminar Persona ####")
        print("#################")
        idsocio = input("Ingrese el id de la persona que desea eliminar: ")
        for l in range(len(personas)):
            if personas[l]["id"] == idsocio:
                del personas[l]
                print("Persona eliminada con éxito.")
        
        
    elif opcionUsuario == 6:
        print("Cerrando programa...")
        boleanito = False  