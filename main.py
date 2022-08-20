# Módulos importados:
import os
import MiRedFunciones as funcion

# Primer bucle (principal): Regresa al principio, en dónde se selecciona si se es nuevo usuario o no
bucle: bool = True
while bucle:

    funcion.portada()  # Portada COSMOSS

    # Ingresar nombre de usuario (Nuevo o registrado)
    nombre = funcion.ingreso_nombre()
    funcion.bienvenida(nombre)  # Este es un mensaje de bienvenida

    # Busca archivo con nombre de usuario almacenado.
    if os.path.isfile(nombre + ".user"):
        print("Leyendo datos de usuario", nombre, "desde archivo.")
        print()
        # Barra de progreso
        funcion.barra(nombre)
        print()
        # Si encuentra archivo, lo abre en modo lectura con las variables indicadas.
        archivo_usuario = open(nombre + ".user", "r")
        nombre = archivo_usuario.readline()
        edad = int(archivo_usuario.readline())
        sexo = archivo_usuario.readline()
        estatura = float(archivo_usuario.readline())
        pais = archivo_usuario.readline()
        ciudad = archivo_usuario.readline()
        amigos = int(archivo_usuario.readline())
        descripcion = archivo_usuario.readline()
        # Una vez que hemos leído los datos del usuario, no olvidarnos de cerrar el archivo
        archivo_usuario.close()
        print(' Hola de nuevo', nombre, '¡Aquí tienes tu perfil!')

    else:
        # En caso que el usuario no exista, consultamos por sus datos.
        print(f'{nombre}, sos un nuevo usuario: ¡vamos a completar tu perfil! ')
        edad = funcion.ingreso_edad()
        sexo = funcion.ingreso_sexo()
        estatura = funcion.ingreso_estatura()
        pais = funcion.ingreso_pais()
        ciudad = funcion.ingreso_ciudad()
        amigos = funcion.nro_amigos()
        descripcion = funcion.sobre_mi()
        print()
        funcion.barra(nombre)
        print()
        print()
        print('¡Muy bien, ya tenemos listo tu perfil!')
        print()
        funcion.separador(1)
        print("Gracias por la información. Esperamos que disfrutes con COSMOSS")
        funcion.separador(1)
        print()

    # Imprime una tabla de perfil de usuario formateada con el módulo <<tabulate>>
    funcion.datos(nombre, edad, sexo, estatura, ciudad, pais, amigos, descripcion)

    opcion = 1
    # Segundo bucle: Opciones del menú general.
    while opcion != 0:
        opcion = funcion.menu_general()

        # Código para la opción 1. Publicar un mensaje.
        if opcion == 1:
            mensaje = funcion.mensajes()
            funcion.posteo(nombre, None, mensaje)

        # Código para la opción 2. Publicar un mensaje etiquetando a una persona.
        elif opcion == 2:
            mensaje = funcion.mensajes()
            nombre_amigo = input("Ingresa el nombre de tu amigo/amiga ► ")
            funcion.posteo(nombre, nombre_amigo, mensaje)

        # Código para la opción 3. Publicar los datos del perfil del usuario.
        elif opcion == 3:
            funcion.datos(nombre, edad, sexo, estatura, ciudad, pais, amigos, descripcion)

        # Código para la opción 4. Actualizar los datos del perfil del usuario.
        elif opcion == 4:
            seguir = True

            # Tercer bucle: Opciones del sub menú de modificaciones.
            while seguir:
                modif = funcion.sub_menu()

                # Modificar nombre.
                if modif == 'a' or modif == 'nombre':
                    nombre = input('Ingresa tu nuevo usuario ► ')  # Ingreso nuevo nombre de usuario
                    print()
                    print(f'{nombre}, ¡tu nombre ha sido actualizado!')
                    print()

                # Modificar sexo / género.
                elif modif == 'b' or modif == 'sexo':
                    sexo = funcion.ingreso_sexo()
                    print()
                    print(f'{nombre}, ¡tu sexo/género ha sido actualizado!')
                    print()

                # Modificar edad.
                elif modif == 'c' or modif == 'edad':
                    edad = funcion.ingreso_edad()
                    print()
                    print(f'{nombre}, ¡tu edad ha sido actualizada!')
                    print()

                # Modificar estatura.
                elif modif == 'd' or modif == 'estatura':
                    estatura = funcion.ingreso_estatura()
                    print()
                    print(f'{nombre}, ¡tu estatura ha sido actualizada!')
                    print()

                # Modificar país y ciudad.
                elif modif == 'e' or modif == 'país' or modif == 'pais y ciudad':
                    pais = funcion.ingreso_pais()
                    ciudad = funcion.ingreso_ciudad()
                    print()
                    print(f'{nombre}, ¡tu localización ha sido actualizada!')
                    print()

                # Modificar descripción
                elif modif == 'f' or modif == 'descripción':
                    descripcion = funcion.sobre_mi()
                    print()
                    print(f'{nombre}, ¡tu perfil ha sido actualizado!')
                    print()

                # Salir del sub-menú de modificaciones.
                elif modif == 'g' or modif == 'salir':
                    seguir = False

                # en caso de que no coincida ninguna opcion.    
                else:
                    seguir = True
                    print()
                    funcion.separador(2)
                    print(" ¡¡¡Esa no es una opción válida!!!")
                    funcion.separador(2)
                    print()

            # Tabla de datos.
            funcion.datos(nombre, edad, sexo, estatura, ciudad, pais, amigos, descripcion)
            print()

            """ Para la opcion salir: si el usuario es nuevo se guardan sus datos en un archivo con su
            nombre de usuario. Si el usuario ya existe y no se cambia ningún dato, se queda el archivo
            sin modificaciones. Si el usuario modifica un dato, se guardan esas modificaciones."""

        elif opcion == 0:
            print("Has decidido salir. Guardando perfil en ", nombre + ".user")
            funcion.barra(nombre)
            funcion.generarUsuario(
                                   nombre, edad, sexo, 
                                   estatura, pais, ciudad, amigos, descripcion
                                   )
            print("Archivo", nombre + ".user", "guardado")

    # Despedida al usuario
    funcion.separador(1)
    print("                     Gracias por usar COSMOSS. ¡Hasta pronto!")
    print("""                              (>‿◠)✌ ᶜʰᵃᵘᵘᵘᵘᵘᵘ      """)
    funcion.separador(1)
    funcion.espacio()

bucle = True

