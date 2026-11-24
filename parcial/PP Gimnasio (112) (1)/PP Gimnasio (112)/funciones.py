def get_int(mensaje:str)-> int|None:
    numero = int(input(mensaje))
    return numero


def validate_int(numero,mensaje,mensaje_error,minimo,maximo,reintentos)-> int|None:
    intentos = 0
    while minimo > numero or numero > maximo:
        print(mensaje_error)
        numero = int(input(mensaje))
        intentos += 1
        if intentos == reintentos:
            break
    return numero


def get_string(mensaje:str)-> str|None:
    cadena = input(mensaje)
    return cadena

def elegir_opcion(lista)-> int:
    for i in range(0,len(lista),1):
        print(f"{i+1}. {lista[i]}")
    opcion = get_int("selecciona una opcion: ")
    return opcion

def contar_planes(planes_socios, planes_activos):
    contadores_planes = []

    for i in range(0,len(planes_activos)):
        contador = 0
        for j in range(0,len(planes_socios)):
            if planes_activos[i] == planes_socios[j]:
                contador += 1
        contadores_planes.append(contador)
    return contadores_planes




