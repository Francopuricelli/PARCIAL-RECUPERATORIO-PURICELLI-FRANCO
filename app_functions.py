import random
import json

def validar_lista(lista:list):
    """valida que la lista no tenga ningun valor, ni que no sea de tipo list.

    Args:
        lista (_type_): _description_

    Raises:
        ValueError: _description_
        ValueError: _description_
    """
    if not isinstance(lista, list):
        raise ValueError("El argumento debe ser una lista.")
    if len(lista) == 0:
        raise ValueError("La lista no puede estar vacía.")


def promediar_coleccion(lista:list,campo): 
    """saca el promedio de una coleccion

    Args:
        lista (_type_): ingresa lista a promediar
        campo (_type_): ingresa campo a promediar

    Returns:
        _type_: devuelve el promedio del campo establecido en float
    """
    validar_lista(lista)
    suma = 0
    total_iteraciones = 0
    for personaje in lista:
        total_iteraciones += 1
        suma += float(personaje[campo])
        

    return suma / total_iteraciones

def mapear_lista(funcion,lista:list):
    """mapea una lista

    Args:
        funcion (_type_): _description_
        lista (_type_): _description_

    Returns:
        _type_: retorna una lista con las keys mapeadas anteriormente
    """
    validar_lista(lista)
    lista_retorno = []
    for el in lista:
        lista_retorno.append(funcion(el))
    return lista_retorno


def filtrar_lista(funcion,lista:list):
    """evalua el valor de una key

    Args:
        funcion (_type_): _description_
        lista (_type_): _description_

    Returns:
        _type_: retorna una lista con los valores filtrados
    """
    lista_retorno = []
    for el in lista:
        if funcion(el):
            lista_retorno.append(el)
    return lista_retorno


def calcular_mayor_campo_nombre(lista:list,campo,campo2): #campo 2 printea cualquier valor
    """Le asigna un valor al campo 1

    Args:
        lista (_type_): ingresa lista 
        campo (_type_): campo a comparar
        campo2 (_type_): valor a asociar al campo

    Raises:
        ValueError: _description_

    Returns:
        _type_: el nombre asociado al campo a comparar
    """
    
    if len(lista) == 0: 
        raise ValueError("no esta definido el mayor de una lista vacia")
    nombre_maximo = lista[0]
    maximo = lista[0]
    for diccionarios in lista:
        if float(diccionarios[campo]) >= float(maximo[campo]):
            maximo = diccionarios
            nombre_maximo = diccionarios[campo2]
        
    return nombre_maximo








def swap_lista(lista:list,i:int,j:int):
    """swapea lugares

    Args:
        lista (list): _description_
        i (int): _description_
        j (int): _description_
    """
    validar_lista(lista)
    aux = lista[i]
    lista[i] = lista[j]
    lista [j] = aux



def ordenar_lista_doble(lista:list, campo1:str, campo2:str):
    """ordena lista con doble parametro

    Args:
        lista (_type_): _description_
        campo1 (_type_): Separa el campo
        campo2 (_type_): campo a ordenar

    Raises:
        ValueError: _description_
    """
    if isinstance(lista,list):
            
            tam = len(lista)
            for i in range(tam - 1):
                for j in range(i + 1, tam):
                    if lista[i][campo1] == lista[j][campo1]:
                        if lista[i][campo2] > lista[j][campo2]:
                            swap_lista(lista, i, j)  
                    elif lista[i][campo1] > lista[j][campo1]:
                        swap_lista(lista,i,j)
    else:
        raise ValueError("No se ingreso ninguna lista")
    
    

def mostrar_usuarios_tabla(lista:list):
    """muestras los ciclistas de la coleccion

    Args:
        lista (list): recibe una lista de diccionarios y los  muestra las claves del campo solicitado
    """
    if isinstance(lista,list):

        tam = len(lista)
        print("                      LISTA DE CICLISTAS")
        print("ID     User           likes        dislikes       followers ")
        print("------------------------------------------------------------------------")
        for user in lista:
            print(f"{user["id_"]}    {user["user"]:15}    {user["likes"]:4}    {user["dislikes"]:4}   {user["followers"]:}") 
    else:
        raise ValueError("No se ingreso ninguna lista")


def menu():
    
    print("   MENU DE OPCIONES")
    print("1- Cargar CSV")
    print("2- Imprimir lista usuarios")
    print("3- Imprimir lista de usuarios con likes, dislikes y followers asignados")
    print("4- Mejores posts")
    print("5- Haters")
    print("6- Mostrar promedio de followers")
    print("7- Guardar datos por nombre ordenados en un archivo .JSON")
    print("8- Mas popular")
    print("9- Salir")

    return input("ingrese numero ")

def pausar():
    from os import system
    system("pause")

def salir():
    salir = input("desea salir? \n (si/no) ")
    return salir

def limpiar_pantalla():
    from os import system
    system("cls")

#---------------------------------------------------------------------------------------------#

def get_path_actual(nombre_archivo):
    import os
    directorio_actual = os.path.dirname(__file__)
    return os.path.join(directorio_actual, nombre_archivo)


def cargar_archivo_csv(nombre_archivo,lista:list):
    """ Carga un archivo .CSV

    Args:
        nombre_archivo (_type_): _description_
        lista (_type_): _description_

    Returns:
        _type_: me retorna el contenido del archivo en una lista.
    """
    
    with open(get_path_actual(nombre_archivo + ".csv"), "r", encoding="utf-8") as archivo :
        lista = []
        encabezado = archivo.readline().strip("\n").split(",")

        for linea in archivo.readlines():
            usuario= {}
            linea = linea.strip("\n").split(",")

            id_, user, likes, dislikes,followers = linea
            usuario["id_"] = int(id_)
            usuario["user"] = user
            usuario["likes"] = int(likes)
            usuario["dislikes"] = int(dislikes)
            usuario["followers"] = int(followers)

            lista.append(usuario)
    return lista




def crear_archivo_mejores_posts_csv(lista:list):
    """crea un archivo de tipo .CSV filtrando por tipo.

    Args:
        lista (list): _description_
    """
    
    nombre_archivo = input("ingrese el nombre que quiera asignarle al archivo")
    lista_likes = (filtrar_lista(lambda user: user["likes"] > 2000, lista))
    
    with open(get_path_actual(nombre_archivo + ".csv"), "w", encoding="utf-8") as archivo:
        encabezado = ",".join(list(lista[0].keys())) + "\n"
        archivo.write(encabezado)
        for i in range(len(lista_likes)):
            lista_cargada = ",".join(lista_likes[i]) + "\n"

        for persona in lista_likes:
            values = list(persona.values())
            lista_cargada = []
            for value in values:
                if isinstance(value,int):
                    lista_cargada.append(str(value))
                elif isinstance(value,float):
                    lista_cargada.append(str(value))
                else:
                    lista_cargada.append(value)
            linea = ",".join(lista_cargada) + "\n"
            archivo.write(linea)

#5
def crear_archivo_haters_csv(lista:list):
    """crea un archivo de tipo .CSV filtrando por tipo.

    Args:
        lista (list): _description_
    """
    
    nombre_archivo = input("ingrese el nombre que quiera asignarle al archivo")
    lista_haters = (filtrar_lista(lambda user: user["dislikes"] > user["likes"], lista))
    
    with open(get_path_actual(nombre_archivo + ".csv"), "w", encoding="utf-8") as archivo:
        encabezado = ",".join(list(lista[0].keys())) + "\n"
        archivo.write(encabezado)
        for i in range(len(lista_haters)):
            lista_cargada = ",".join(lista_haters[i]) + "\n"

        for persona in lista_haters:
            values = list(persona.values())
            lista_cargada = []
            for value in values:
                if isinstance(value,int):
                    lista_cargada.append(str(value))
                elif isinstance(value,float):
                    lista_cargada.append(str(value))
                else:
                    lista_cargada.append(value)
            linea = ",".join(lista_cargada) + "\n"
            archivo.write(linea)



    return lista
def cargar_datos_random(lista:list,campo,desde,hasta) -> list:
    """carga datos random a un campo ingresado.

    Args:
        lista (_type_): _description_
        campo (_type_): _description_

    Returns:
        list: _description_
    """
    validar_lista(lista)
    lista_tiempos = mapear_lista(lambda tiempo : tiempo[campo],lista)
    for value in range(len(lista_tiempos)):
        lista_tiempos[value] = random.randint(desde,hasta)
        lista[value][campo] = lista_tiempos[value]
    return lista


def crear_archivo_json(lista:list):
    
    """crea un archivo .JSON

    Args:
        lista (_type_): _description_
    """
    validar_lista(lista)
    ordenar_lista_doble(lista,"user","user")
    nombre_archivo = input("ingrese el nombre del archivo a asignar")
    with open(get_path_actual(nombre_archivo +".json"), "w", encoding="utf-8") as archivo:
        json.dump(lista, archivo,indent = 2)

def datos_random(lista:list):
    validar_lista(lista)
    cargar_datos_random(lista,"likes",500,3000)
    cargar_datos_random(lista,"dislikes",300,3500)
    cargar_datos_random(lista,"followers",10000,20000)

