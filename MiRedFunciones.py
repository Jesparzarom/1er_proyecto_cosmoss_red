#IMPORTAR EN EL MÓDULO PRINCIPAL __MAIN__

from datetime import datetime as fecha
from tabulate import tabulate as tab
from tqdm import tqdm
from time import sleep


# Separadores visuales de datos en el intérprete. Hacen el programa más amigable.
def separador(n):
    if n == 1:
        print('***********************************************************************************************')
    else:
        print('-----------------------------------------------------------------------------------------------')


# Portada
def portada():
    print()
    separador(1)
    print("""                                              
              *                                                           *
              *            ▒█▀▀█ █▀▀█ █▀▀  █▀▄▀█ █▀▀█ █▀▀ █▀▀             *
              *            ▒█░░░ █░░█ ▀▀█  █░▀░█ █░░█ ▀▀█ ▀▀█             *    
              *            ▒█▄▄█ ▀▀▀▀ ▀▀▀  ▀░░░▀ ▀▀▀▀ ▀▀▀ ▀▀▀             *
    """)
    separador(1)
    print()


"""Para establecer un perfil, el programa le pedirá al usuario:
nombre, año de nacimiento, sexo, estatura, país, ciudad y mail. 
Estos datos seran almacenados en funciones para posteriormente asociarlos con una variable global"""


def ingreso_nombre():
    print()
    print('--------------------------------')
    print('a) Nuevo usuario')
    print('b) Iniciar sesión con mi usuario')
    iniciar = input(' Ingresa una opción ► ')
    print('--------------------------------')
    print()
    rein = True
    while rein == True:
        if iniciar == 'a':
            nombre = input("ingresa un nombre de usuario para comenzar el ► ")
            print()
            rein = False
            return nombre
            
        elif iniciar == 'b':
            nombre = input("ingresa tú usuario ► ")
            print()
            rein = False
            return nombre

        else:
            rein = True
          
        
            


def bienvenida(nombre):
    print()
    separador(1)
    print("****** Hola ", nombre, ", ¡te damos la bienvenida a COSMOSS!   (>‿◠)✌ ********")
    separador(1)
    print()


# Año de nacimiento del usuario.
# Se utiliza este dato para estimar la edad de la persona. Se almacena en la variable "edad"
def ingreso_edad():
    anio = int(input("¿En que año naciste? ► "))
    edad = 2022 - anio - 1
    separador(2)
    return edad


# Sexo del usuario. Se almacena en la variable "sexo".
def ingreso_sexo():
    sexo = input("¿cúal es tu sexo/género? ► ")
    separador(2)
    return sexo


# Estatura en metros. Se asigna la entrada a la variable "estatura"
def ingreso_estatura():
    estatura = float(input("¿Cuánto mides? (dímelo en metros). ► "))
    separador(2)
    return estatura


# País del usuario almacenado en la variable "pais"
def ingreso_pais():
    pais = input("Muy bien. Cuéntame... ¿en que país vives?. ► ")
    separador(2)
    return pais


# Ciudad del usuario almacenada en la variable "ciudad"
def ingreso_ciudad():
    ciudad = input("¿Y tu ciudad? ► ")
    separador(2)
    return ciudad


# Amigos del usuario en una variable tipo "int"
def nro_amigos():
    amigos = int(input("¿Cuántos amigos tienes? ► "))
    separador(2)
    return amigos


def sobre_mi():
    print()
    separador(2)
    descripcion = input("¡Escribe una descripción de tí! ► ")
    separador(2)
    print()
    return descripcion


def barra(nombre):
        for i in tqdm(nombre, ncols= 100, desc= ("Progreso"), unit=""):
            sleep(0.1)


# Tabla organizada de datos de perfil con el módulo "tabúlate"
def datos(nombre, edad, sexo, estatura, ciudad, pais, amigos, descripcion,):
    tabla = [[" ", " "], ['USUARIO', nombre], ['EDAD', f'{edad} años'],
             ["SEXO", sexo], ["ESTATURA", f"{estatura} mts"], ["CIUDAD", ciudad],
             ["PAIS", pais], [" ", " "], ["AMIGOS", amigos]]
    print(tab(tabla,
              headers=['SOBRE MÍ:', f'{descripcion[0:75]} \n{descripcion[75:150]}'],
              tablefmt="fancy_grid"))

    
def posteo1(nombre):
    print()
    mensaje = input('Escribe tu mensaje ► ')
    print()
    print()
    print(nombre, 'dice:')
    posteo = [[mensaje]]
    print(tab(posteo, tablefmt="fancy_grid"))
    print("Publicado el", fecha.today().strftime('%d-%m-%Y  a las %H:%M  hrs.'))
    print()    


def posteo2(nombre):
    print()
    mensaje = input(" ¿Qué quieres postear? ► ")
    print()
    nombre_amigo = input("Ingresa el nombre de tu amigo/amiga ► ")
    print()
    print(nombre, 'dice:')
    posteo_2 = [[f"@ {nombre_amigo}, {mensaje}"]]
    print(tab(posteo_2, tablefmt="fancy_grid"))
    print("Publicado el", fecha.today().strftime('%d-%m-%Y  a las %H:%M  hrs.'))
    print()
    print()
    
    
def menu_general():    
    separador(2)
    print("Acciones disponibles:")
    print("  1. Escribir un mensaje público")
    print("  2. Escribir un mensaje para amigos")
    print("  3. Mostrar los datos de perfil")
    print("  4. Actualizar el perfil de usuario")
    print("  0. Salir")
    opcion = int(input("Ingresa una opción: ► "))
    separador(2)
    while opcion < 0 or opcion > 4:
        print("Opción no válida. Inténtalo otra vez. ► ")
        opcion = int(input("Ingresa una opción: "))
    return opcion
 
def sub_menu():
    separador(2)
    print("¿Qué dato deseas modificar? (Para volver pulsa 'g' ):")
    print("a) Nombre")
    print("b) Sexo")
    print("c) Edad")
    print("d) Estatura")
    print("e) País y Ciudad")
    print("f) Descripción")
    print("g) Volver al menú principal")
    modif = input('Ingresa una opción: ► ')
    separador(2)
    return modif    
    
    
def mensajes():
    print()
    mensaje = input('¿Que quieres postear? ► ')
    return mensaje
        

def posteo(nombre, nombre_amigo, mensaje):
    if nombre_amigo == None:
        print()
        print()
        print(nombre, 'dice:')
        posteo = [[mensaje]]
        print(tab(posteo, tablefmt="fancy_grid"))
        print("Publicado el", fecha.today().strftime('%d-%m-%Y  a las %H:%M  hrs.'))
        print()    

    else:
        print()
        print()
        print(nombre, 'dice:')
        posteo_2 = [[f"@ {nombre_amigo}, {mensaje}"]]
        print(tab(posteo_2, tablefmt="fancy_grid"))
        print("Publicado el", fecha.today().strftime('%d-%m-%Y  a las %H:%M  hrs.'))
        print()


def espacio():
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()
    print()