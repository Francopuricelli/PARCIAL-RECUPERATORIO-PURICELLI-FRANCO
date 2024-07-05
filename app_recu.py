from app_functions import *

lista = []

flag_archivo = False
while True:
    limpiar_pantalla()
    match menu():
        case "1":
                nombre_archivo = input("ingrese el nombre del archivo .CSV a cargar: ")
                if nombre_archivo != "posts":
                    nombre_archivo = input("ingrese un archivo existente!")
                lista_usuarios = cargar_archivo_csv(nombre_archivo,lista)
                flag_archivo = True
                print("Archivo cargardo con exito!")
        case "2":
            if flag_archivo == False:
                print("No hay un archivo cargado")
            else:
                try:
                    mostrar_usuarios_tabla(cargar_archivo_csv("posts",lista))
                except:
                    raise ValueError("ese archivo no existe")
        case "3":
            if flag_archivo == False:
                print("No hay un archivo cargado")
            else:
                try:
                    datos_random(lista_usuarios)
                    mostrar_usuarios_tabla(lista_usuarios)
                    
                except:
                    raise ValueError("No hay un archivo cargado")
        case "4":
            if flag_archivo == False:
                print("No hay un archivo cargado")
            else:
                try:
                    crear_archivo_mejores_posts_csv(lista_usuarios)
                    print("archivo creado con exito!")
                except:
                    raise ValueError("No hay un archivo cargado")
                
        case "5":
            if flag_archivo == False:
                print("No hay un archivo cargado")
            else:
                try:
                    crear_archivo_haters_csv(lista_usuarios)
                    print("archivo creado con exito!")
                except:
                    raise ValueError("No hay un archivo cargado")
                
        case "6":
            if flag_archivo == False:
                print("No hay un archivo cargado")
            else:
                try:
                    promedio_followers = promediar_coleccion(lista_usuarios,"followers")
                    print(f"PROMEDIO FOLLOWERS \n {promedio_followers:.2f}")
                except:
                    raise ValueError("No hay un archivo cargado")
                
        case "7":
            if flag_archivo == False:
                print("no hay archivo cargado")
            else:
                try:
                    crear_archivo_json(lista_usuarios)
                except:
                    raise ValueError("No hay un archivo cargado")

        case "8":
            if flag_archivo == False:
                print("no hay archivo cargado")
            else:
                try:
                    user_mas_likeado_nombre = calcular_mayor_campo_nombre(lista_usuarios,"likes","user")
                    user_mas_likeado_likes = calcular_mayor_campo_nombre(lista_usuarios,"likes","likes")
                    print(f"MAS POPULAR---- \n Nombre: {user_mas_likeado_nombre} \t Likes: {user_mas_likeado_likes}")
                except:
                    raise ValueError("No hay un archivo cargado")
        case "9":
            if salir() == "no":
                menu()
            else:
                break

    pausar()