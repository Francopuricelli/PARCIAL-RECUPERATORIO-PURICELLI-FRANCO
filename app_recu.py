from app_functions import *

lista = []

flag_archivo = False
while True:
    limpiar_pantalla()
    match menu():
        case "1":
            nombre_archivo = input("ingrese el nombre del archivo .CSV a cargar: ")
            if nombre_archivo != "nombre del ARCHIVO (REEMPLAZAR)":
                nombre_archivo = input("ingrese un archivo existente!")
            flag_archivo = True
            print("Archivo cargardo con exito!")
        case "2":
            if flag_archivo == False:
                print("No hay un archivo cargado")
            else:
                try:
                    pass #rellenar
                except:
                    raise ValueError("ese archivo no existe")
        case "3":
            if flag_archivo == False:
                print("No hay un archivo cargado")
            else:
                try:
                    pass #rellenar
                except:
                    raise ValueError("No hay un archivo cargado")
        case "4":
            if flag_archivo == False:
                print("No hay un archivo cargado")
            else:
                try:
                    pass #rellenar
                except:
                    raise ValueError("No hay un archivo cargado")
                
        case "5":
            if flag_archivo == False:
                print("No hay un archivo cargado")
            else:
                try:
                    pass #rellenar
                except:
                    raise ValueError("No hay un archivo cargado")
                
        case "6":
            if flag_archivo == False:
                print("No hay un archivo cargado")
            else:
                try:
                    pass #rellenar
                except:
                    raise ValueError("No hay un archivo cargado")
                
        case "7":
            if flag_archivo == False:
                print("no hay archivo cargado")
            else:
                try:
                    pass #rellenar
                except:
                    raise ValueError("No hay un archivo cargado")

        case "8":
            if flag_archivo == False:
                print("no hay archivo cargado")
            else:
                try:
                    pass #rellenar
                except:
                    raise ValueError("No hay un archivo cargado")
            
        case "9":
            if salir() == "no":
                menu()
            else:
                break

    pausar()