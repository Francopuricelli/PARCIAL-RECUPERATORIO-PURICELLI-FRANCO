from random import *
import json
def promediar_coleccion(lista,campo): 
    """saca el promedio de una coleccion

    Args:
        lista (_type_): ingresa lista a promediar
        campo (_type_): ingresa campo a promediar

    Returns:
        _type_: devuelve el promedio del campo establecido en float
    """
    suma = 0
    total_iteraciones = 0
    for personaje in lista:
        total_iteraciones += 1
        suma += float(personaje[campo])
        

    return suma / total_iteraciones

def mapear_lista(funcion,lista):
    """mapea una lista

    Args:
        funcion (_type_): _description_
        lista (_type_): _description_

    Returns:
        _type_: retorna una lista con las keys mapeadas anteriormente
    """
    lista_retorno = []
    for el in lista:
        lista_retorno.append(funcion(el))
    return lista_retorno


def filtrar_lista(funcion,lista):
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


def calcular_mayor_campo_nombre(lista,campo,campo2): #campo 2 printea cualquier valor
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

def calcular_menor_campo_nombre(lista,campo,campo2):
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
    nombre_minimo = lista[0]
    minimo = lista[0]
    for diccionarios in lista:
        if float(diccionarios[campo]) <= float(minimo[campo]):
            minimo = diccionarios
            nombre_minimo = diccionarios[campo2]
        
    return nombre_minimo

def contador_lista(lista,campo):
    campo = {}
    for el in lista:
        campo[el] = 0

    for el in lista:
        for i in campo:
            if el == i:
                campo[el] += 1

    return campo




def promediar_coleccion(lista,campo): 
    """saca el promedio de una coleccion

    Args:
        lista (_type_): ingresa lista a promediar
        campo (_type_): ingresa campo a promediar

    Returns:
        _type_: devuelve el promedio del campo establecido en float
    """
    suma = 0
    total_iteraciones = 0
    for personaje in lista:
        total_iteraciones += 1
        suma += float(personaje[campo])
        promedio = suma / total_iteraciones

    return promedio




def swap_lista(lista:list,i:int,j:int):
    """swapea lugares

    Args:
        lista (list): _description_
        i (int): _description_
        j (int): _description_
    """
    aux = lista[i]
    lista[i] = lista[j]
    lista [j] = aux



def ordenar_lista_doble(lista, campo1, campo2):
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
    
    

def mostrar_ciclistas_tabla(lista:list):
    """muestras los ciclistas de la coleccion

    Args:
        lista (list): recibe una lista de diccionarios y los  muestra las claves del campo solicitado
    """
    if isinstance(lista,list):

        tam = len(lista)
        print("                      LISTA DE CICLISTAS")
        print("ID     Nombre            Tipo        Tiempo")
        print("------------------------------------------------------------------------")
        for ciclista in lista:
            print(f"{ciclista["id_bike"]}    {ciclista["nombre"]:15}    {ciclista["tipo"]:10}    {ciclista["tiempo"]}")
    else:
        raise ValueError("No se ingreso ninguna lista")


def menu():
    
    print("   MENU DE OPCIONES")
    print("1- Cargar CSV")
    print("2- Imprimir lista de bicicletas")
    print("3- Imprimir lista de bicicletas con  tiempos asignados")
    print("4- Informar ganador")
    print("5- filtrar por tipo de bicicleta")
    print("6- Mostrar promedio por tipo")
    print("7- Mostrar posiciones")
    print("8- Guardar posiciones en un .JSON")
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

def cargar_archivo_csv(nombre_archivo,lista):
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
            bicicleta= {}
            linea = linea.strip("\n").split(",")

            id_bike, nombre, tipo, tiempo = linea
            bicicleta["id_bike"] = int(id_bike)
            bicicleta["nombre"] = nombre
            bicicleta["tipo"] = tipo
            bicicleta["tiempo"] = int(tiempo)

            lista.append(bicicleta)
    return lista


def cargar_datos_random(lista,campo) -> list:
    """carga datos random a un campo ingresado.

    Args:
        lista (_type_): _description_
        campo (_type_): _description_

    Returns:
        list: _description_
    """
    lista_tiempos = mapear_lista(lambda tiempo : tiempo[campo],lista)
    for value in range(len(lista_tiempos)):
        lista_tiempos[value] = random.randint(50,120)
        lista[value][campo] = lista_tiempos[value]
    return lista

def crear_archivo_tipo_csv(lista:list):
    """crea un archivo de tipo .CSV filtrando por tipo.

    Args:
        lista (list): _description_
    """
    type_bike = input("Ingrese el tipo de bicicleta: ")
    while type_bike != "BMX" and type_bike != "PLAYERA" and type_bike != "MTB" and type_bike != "PASEO":
        type_bike = input("Ingrese un tipo de bicicleta valido: ")
    lista_tipo = (filtrar_lista(lambda bike: bike["tipo"] == type_bike, lista))
    
    with open(get_path_actual(type_bike + ".csv"), "w", encoding="utf-8") as archivo:
        encabezado = ",".join(list(lista[0].keys())) + "\n"
        archivo.write(encabezado)
        for i in range(len(lista_tipo)):
            lista_cargada = ",".join(lista_tipo[i]) + "\n"

        for persona in lista_tipo:
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

def crear_archivo_json(lista):
    """crea un archivo .JSON

    Args:
        lista (_type_): _description_
    """
    nombre_archivo = input("ingrese el nombre del archivo a asignar")
    with open(get_path_actual(nombre_archivo +".json"), "w", encoding="utf-8") as archivo:
        json.dump(lista, archivo,indent = 2)