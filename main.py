import re
import json
import os

def clear_console():
    '''
    limpia la consola esperando una tecla
    '''
    _ = input("Press a key to continue...")
    os.system("cls")

def imprimir_menu():
    '''
    imprime el menu de opciones
    '''
    print("\n1. Mostrar la lista de todos los jugadores del Dream Team")
    print("2. Escoger indice y mostrar estadisticas completas")
    print("3. Guardar en un archivo ('csv') opcion anterior")
    print("4. Buscar los logros de un jugador")
    print("5. Promedio de puntos por partido del Dream Team (Nombres Ascendentes)")
    print("6. Pertenece al Salon de la Fama del Baloncesto?") 
    print("7. Jugador con la mayor cantidad de rebotes totales")
    print("8. Jugador con el mayor porcentaje de tiros de campo")
    print("9. Jugador con la mayor cantidad de asistencias totales")
    print("10. Jugadores con mas promedio de puntos por partido que N...")
    print("11. Jugadores con mas promedio de rebotes por partido que N...")
    print("12. Jugadores con mas promedio de asistencias por partido que N...")
    print("13. Jugador con la mayor cantidad de robos totales")
    print("14. Jugador con la mayor cantidad de bloqueos totales")
    print("15. Jugadores con mas '%' de tiros libres por partido que N...")
    print("16. Promedio de puntos por partido del Dream Team excluyendo el peor"
                                                                        "promdio")
    print("17. Jugador con mas logros obtenidos")
    print("18. Jugadores con mas '%' de tiros triples por partido que N...")
    print("19. Jugador con la mayor cantidad de temporadas jugadas")
    print("20. Jugadores con mas '%' de tiros de campo por partido que N...")
    print ("0. Salir")

def validar_opcion():
    '''
    valido la opcion ingresada por el usuario para interactuar con el menu
    :return: retorno la palabra validada
    '''
    imprimir_menu()
    result = -1
    result = input("Ingrese opcion:\n")
    if result.isdigit():
        result = int(result)
        if result >= 0 and result < 21:
            return result
        else:
            print("------------------------------------------------------")
            print("\n           opcion incorrecta")
            print("\n------------------------------------------------------")
    else:
        validar_opcion()   

def leer_archivo(nombre_archivo:str):
    '''
    Levanto un archivo json
    :param nombre_archivo: direccion del archivo a levantar
    :return: una lista con el contenido
    '''
    lista = []
    with open( nombre_archivo, "r", encoding="utf-8") as archivo:
        dict = json.load(archivo)
        lista = dict["jugadores"]

    return lista
        
def normalize_string(txt:str):
    '''
    normalizo un str quitando los '_' y capitalizandolo
    :param txt: string a normalizar
    :return: string normalizado
    '''
    txt = txt.replace("_", " ").capitalize()
    return txt

def print_stats_indice(indice: int, lista_jugadores:list):
    '''
    imprimo los logros de un jugador de la lista segun el indice
    :param indice: indice del jugador a imprimir
    :param lista_jugador: lista de jugadores
    :param return: 1 si logro printear los logros
    '''
    if not lista_jugadores:
        print("Lista vacia")
    else:  
        if indice < 0 and indice > len(lista_jugadores):
            print("Indice incorrecto")
        else:
            print("Estos son las estadisticas de {0}:".format(lista_jugadores[indice]["nombre"]))
            for key, value in lista_jugadores[indice]["estadisticas"].items():          
                print("{0}: {1}".format(normalize_string(key), value))
            return 1
        
def print_logros(jugador:dict):
    '''
    imprimo los logros de un jugador
    :param jugador: jugador a imprimir
    :param return: nada
    '''
    if not jugador:
        print("Jugador no existe")
    else:
        print("Estos son las estadisticas de {0}:".format(jugador["nombre"]))
        for key, value in jugador["estadisticas"].items():          
            print("{0}: {1}".format(normalize_string(key), value))

def print_jugador_indice(lista_jugadores:list):
    '''
    imprimo una lista de juagdores con sus indices 
    :param lista_jugadores: lista de jugadores
    '''
    indice = 0
    if not lista_jugadores:
        print("Lista vacia")
    else:
        print("Indice | jugador:")
        for player in lista_jugadores:
            print("{0} -> {1}".format(indice, player["nombre"]))
            indice +=1

def show_name_and_pos(lista_jugadores:list):
    '''
    imprimo una lista de jugadores con sus posiciones
    :param lista_jugadorres: lista de jugadores
    '''
    if not lista_jugadores:
        print("Lista vacia")
    else:
        print("Lista del Dream Team:\n")
        for player in lista_jugadores:
            print("Nombre: {0} - Posición: {1}".format(player["nombre"], player["posicion"]))

def keys_stats(lista_jugadores:list):
    '''
    creo una lista con las keys del diccionario 'estadisticas'
    :param lista_jugadores: lista de jugadores
    :return: lista con las keys
    '''
    flag = False
    list_keys = []
    for player in lista_jugadores:
        if flag == False:
            for key in player["estadisticas"].keys():
                list_keys.append(normalize_string(key))
                flag = True
    return list_keys

def keys_player(lista_jugadores:list):
    '''
    creo una lista con las keys 'nombre' y 'posicion'
    :param lista_jugadores: lista de jugadores
    :return: lista con las keys
    '''
    flag = False
    list_keys = []
    for player in lista_jugadores:
        if flag == False:
            for key in player.keys():
                list_keys.append(normalize_string(key))
                flag = True
    return list_keys[:-2]

def find_player_by_name(name:str, lista_jugadores:list):
    '''
    encuentra un jugador por el nombre ingresado
    :param name: nombre a buscar
    :param lista_jugadores: lista de jugadores a evaluar
    :return: diccionario del jugador
    '''
    name = name.lower().capitalize()
    pattern = rf"^{name}"
    for player in lista_jugadores:
        if re.search(pattern, player["nombre"]):
            return player
    else: print("No se encontro {0}".format(name))

        
def show_mames_stats(lista_jugadores:list, estadistica:str):
    '''
    creo una lista con los nombres y una estadistica deseada
    :param lista_jugadores: lista de jugadores
    :param estadistica: estadistica a mostrar
    :return: lista de jugadores y estadistica
    '''
    lista = []
    if not lista_jugadores: 
        return None      
    else:       
        for player in lista_jugadores:                
            lista.append(("nombre: {0}, {1}: {2}".format(player["nombre"],
                                        normalize_string(estadistica), 
                                        player["estadisticas"][estadistica])))
        return lista
    
def sort_list_by_key(lista_og:list, key:str, mayor_menor:str ="mayor"):
    '''
    hago una copia y ordeno una lista segun key y orden ingresados
    :param mayor_menor: para ordenar de forma ascendente o descendente
    :param key: key a evaluar
    :param lista_og: lista a ordenar
    :return: lista ordenada   
    '''
    if not lista_og:
        return None
    else:
        lista_copy = lista_og 
        rango_a = len(lista_og)
        flag_swap = True

        while(flag_swap):
            flag_swap = False
            rango_a = rango_a - 1
            for indice_A in range(rango_a):
                if  mayor_menor == "mayor" and lista_copy[indice_A][key] < lista_copy[indice_A+1][key] \
                    or mayor_menor == "menor" and lista_copy[indice_A][key] > lista_copy[indice_A+1][key]:
                    lista_copy[indice_A],lista_copy[indice_A+1] = lista_copy[indice_A+1],lista_copy[indice_A]
                    flag_swap = True

        return lista_copy

def sort_list_by_stat(lista_og:list, key:str, mayor_menor:str ="mayor"):
    '''
    hago una copia y ordeno una lista segun key de estadistica y orden ingresados
    :param mayor_menor: para ordenar de forma ascendente o descendente
    :param key: key a evaluar
    :param lista_og: lista a ordenar
    :return: lista ordenada   
    '''
    if not lista_og:
        return None
    else:           
        lista_copy = lista_og 
        rango_a = len(lista_og)
        flag_swap = True

        while(flag_swap):
            flag_swap = False
            rango_a = rango_a - 1
            for indice_A in range(rango_a):
                if  mayor_menor == "mayor" and lista_copy[indice_A]["estadisticas"][key] < \
                    lista_copy[indice_A+1]["estadisticas"][key] \
                    or mayor_menor == "menor" and lista_copy[indice_A]["estadisticas"][key] > \
                    lista_copy[indice_A+1]["estadisticas"][key]:
                    lista_copy[indice_A],lista_copy[indice_A+1] = \
                    lista_copy[indice_A+1],lista_copy[indice_A]
                    flag_swap = True

        return lista_copy
    
def average_stat(lista_jugadores:list, stat:str):
    '''
    calculo el promedio de una estadistica
    :param lista_jugadores: lista de jugadores
    :param stat: estadistica a calcular
    :return: promedio de la estadistica
    '''
    if not lista_jugadores:
        return None 
    else:
        total = 0.0
        for player in lista_jugadores:
            total += player["estadisticas"][stat]

        average = total / len(lista_jugadores)

        return "{:.2f}".format(average)
     
def print_player_max_stat(player:dict, stat:str):
    '''
    imprime el jugador con el formato maxima estadistica
    :param player: diccionario del jugador
    :param stat: estadistica a imprimir
    :return: nada
    ''' 
    print("El jugador con mas {0} es: \n".format(normalize_string(stat)))
    print("Nombre: {0} -> {1}: {2}".format(player["nombre"],
                            normalize_string(stat), player["estadisticas"][stat]))

def print_player_above_average(lista_jugadores:list, stat:str, average:float,pos:bool = False):
    '''
    imprimo los jugadores que superan el promedio ingresado
    :param lista_jugadores: lista de jugadores
    :param stat: estadistica a ser evaluada
    :param average: promedio a superar
    :param pos: imprimir posicion 
    :return: nada
    '''
    print("Los jugadores que superan los: {0} {1} son: ".format(average, 
                                                    normalize_string(stat)))
    
    for player in lista_jugadores:                   
        if player ["estadisticas"][stat] > average and pos == False:
            print("Nombre: {0} -> {1}: {2}".format(player["nombre"],
            normalize_string(stat), player["estadisticas"][stat]))
        else:
            if player ["estadisticas"][stat] > average and pos == True:
                print("Nombre: {0} ({1})-> {2}: {3}".format(player["nombre"],
                player["posicion"], normalize_string(stat), player["estadisticas"][stat]))

def sort_by_logros(lista_og:list, mayor_menor:str = "mayor"):
    '''
    creo una lista segun la cantidad de logros obetenidos
    :param lista_og: lista a ordenar
    :param mayor_menor: para ordenar de forma ascendente o descendente
    :return: lista ordenada
    '''
    if not lista_og:
        return None
    else:           
        lista_copy = lista_og 
        rango_a = len(lista_og)
        flag_swap = True

        while(flag_swap):
            flag_swap = False
            rango_a = rango_a - 1
            for indice_A in range(rango_a):
                if  mayor_menor == "mayor" and len(lista_copy[indice_A]["logros"]) < \
                    len(lista_copy[indice_A]["logros"]) \
                    or mayor_menor == "menor" and len(lista_copy[indice_A]["logros"]) > \
                    len(lista_copy[indice_A]["logros"]):
                    lista_copy[indice_A],lista_copy[indice_A+1] = \
                    lista_copy[indice_A+1],lista_copy[indice_A]
                    flag_swap = True

        return lista_copy
    
def member_HOF(player:dict):
    '''
    confirmo si el jugador forma parte del salon de la fama
    :param player: diccionario del jugador
    :return: nada
    '''
    if not player:
        return None
    else:
        flag = False
        hof = "Miembro del Salon de la Fama del Baloncesto"
        for logro in player["logros"]:
            if logro == hof:
                print("el jugador {0} es un: {1}".format(player["nombre"], hof))         
                flag = True
        if flag == False:
            print("el jugador {0} no es un: {1}".format(player["nombre"], hof))     

def save_file(name_file:str, lista_jugadores:list, i:int):
    '''
    creo un archivo csv con las estadisticas con el 
    indice del jugador de la opcion 2
    :param name_file: nombre del archivo
    :param lista_jugadores: lista de jugadores
    :param i: indice del jugador
    :return: nada
    '''
    lista_keys_estadisticas = keys_stats(player_list)   
    lista_keys_player = keys_player(player_list)
            
    for element in lista_keys_estadisticas:
        lista_keys_player.append(element)

    encabezado = ""
    encabezado = ", ".join((lista_keys_player))
    with open(name_file, "w+") as file:
        file.write(encabezado)
        file.write("\n")
        list_values = lista_jugadores[i]["nombre"],lista_jugadores[i]["posicion"]
        for element in list_values:
            result = file.write(str(element))
            file.write(", ")
        for element in lista_jugadores[i]["estadisticas"].values():
            result = file.write(str(element))
            file.write(", ")
        file.write("\n")
    if result == 0:
        print("Error al crear el archivo: {}".format(name_file))
        return False 
    else:
        print("Se creo el archivo: ", name_file)
        return True
    

flag_op_2 = False            
player_list = leer_archivo("D:\programacion 1\parcial_00\dt.json")
indice_selected = ""

while(True):
    
    option = validar_opcion()
    match(option):

        case 0:
            print("Hasta la proxima capo, maestro, mastodonte")
            break

        
        case 1:
            show_name_and_pos(player_list)  
            

        case 2:
            print_jugador_indice(player_list)
            indice_selected = input("seleccione un indice...\n")
            indice_selected = int(indice_selected)
            change = print_stats_indice(indice_selected, player_list)
            if change == 1:
                flag_op_2 = True
            

        case 3:
            if flag_op_2 == False:
                print("\n------------------------------------------------------")
                print("Primero ingresa a la opcion #2")
                print("\n------------------------------------------------------")
            else:
                save_file("jugador_{0}.csv".
                        format(player_list[indice_selected]["nombre"]),
                        player_list, indice_selected)
           

        case 4:
            player_name = input("Ingrese el nombre del jugador:...\n")
            player = find_player_by_name(player_name, player_list)
            print_logros(player)
            

        case 5:
            list_sort_by_name = sort_list_by_key(player_list,"nombre")
            retorno = show_mames_stats(list_sort_by_name, "promedio_puntos_por_partido")
            if retorno != None:
                for elemento in retorno:
                    print(elemento)
            else:
                print("ocurrio un error")
            

        case 6:
            player_name = input("Ingrese el nombre del jugador:...\n")
            player = find_player_by_name(player_name, player_list)
            member_HOF(player)


        case 7:
            stat = "rebotes_totales"
            retorno = sort_list_by_stat(player_list, stat)
            if retorno != None :
                print_player_max_stat(retorno[0], stat)
                

        case 8:
            stat = "porcentaje_tiros_de_campo"
            retorno = sort_list_by_stat(player_list, stat)
            if retorno != None :
                print_player_max_stat(retorno[0], stat)
                
        
        case 9:
            stat = "asistencias_totales"
            retorno = sort_list_by_stat(player_list, stat)
            if retorno != None :
                print_player_max_stat(retorno[0], stat)
                

        case 10:
            stat = "promedio_puntos_por_partido"
            more_than = float(input("Ingrese los puntos a superar\n")) 
            average = average_stat(player_list,stat)
            if average != None:
                print_player_above_average(player_list, stat, more_than)
            
        
        case 11:
            stat = "promedio_rebotes_por_partido"
            more_than = float(input("Ingrese los rebotes a superar\n"))                
            average = average_stat(player_list,stat)
            if average != None:
                print_player_above_average(player_list, stat, more_than)
            
            
        case 12:
            stat = "promedio_asistencias_por_partido"
            more_than = float(input("Ingrese las asistencias a superar\n"))         
            average = average_stat(player_list,stat)
            if average != None:
                print_player_above_average(player_list, stat, more_than)
            

        case 13:
            stat = "robos_totales"
            retorno = sort_list_by_stat(player_list, stat)
            if retorno != None :
                print_player_max_stat(retorno[0], stat)
            

        case 14:
            stat = "bloqueos_totales"
            retorno = sort_list_by_stat(player_list, stat)          
            if retorno != None :
               print_player_max_stat(retorno[0], stat) 
            
        
        case 15:
            stat = "porcentaje_tiros_libres"
            more_than = float(input("Ingrese el '%' de tiros libres a superar\n")) 
            average = average_stat(player_list, stat)
            if average != None:
                print_player_above_average(player_list, stat, more_than)
            
        
        case 16:
            stat = "promedio_puntos_por_partido"
            list_sorted_point_p_match = sort_list_by_stat(player_list, stat)
            print("\nEl {0} de los jugadores del Dream Team excluyendo el peor"
                  " promedio es: {1}".format(normalize_string(stat),
                                    average_stat(list_sorted_point_p_match[:-1],
                                                stat)))
            
        case 17:
            list_sorted_by_logros = sort_by_logros(player_list)
            print("El jugador con mas logros es: {0} con: {1}".
                  format(list_sorted_by_logros[0]["nombre"],
                        len(list_sorted_by_logros[0]["logros"])))
            
        case 18:
            stat = "porcentaje_tiros_triples"
            more_than = float(input("Ingrese el '%' de tiros triples a superar\n")) 
            average = average_stat(player_list, stat)
            if average != None:
                print_player_above_average(player_list, stat, more_than)
            
        case 19:
            stat = "temporadas"
            retorno = sort_list_by_stat(player_list, stat)
            if retorno != None :
                print_player_max_stat(retorno[0], stat)
            
        case 20:
            stat = "porcentaje_tiros_de_campo"
            more_than = float(input("Ingrese el '%' de tiros de campo a superar\n")) 
            list_sorted_by_pos = sort_list_by_key(player_list, "posicion")
            average = average_stat(list_sorted_by_pos, stat)
            if average != None:
                print_player_above_average(player_list, stat, more_than, True)

    clear_console()