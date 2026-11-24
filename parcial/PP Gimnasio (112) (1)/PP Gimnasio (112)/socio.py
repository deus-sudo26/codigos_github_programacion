from funciones import *


def mostrar_socios(nombres, apellidos, ids_socios, edades, planes):
    for i in range(0,len(nombres),1):
        print(nombres[i],apellidos[i], ids_socios[i],edades[i],planes[i])

    


def cargar_socio(nombres, apellidos, ids_socios, edades, planes,mensaje_input):
    print(mensaje_input)
    nombre = get_string("Nombre: ")
    apellido = get_string("Apellido: ")
    id_socio = get_int("Ingresa tu ID: ")
    edad = get_int("ingresa tu edad: ")
    edad = validate_int(edad, "ingresa tu edad", "dato invalido,ingresa un valor entre 16 a 70", 16, 70, 10)
    plan = get_string("Tipo de plan: ")
    

    nombres.append(nombre)
    apellidos.append(apellido)
    ids_socios.append(id_socio)
    edades.append(edad)
    planes.append(plan)

    
    


def buscar_socio(id_buscado, nombres, apellidos, ids_socios, edades, planes):
    encontrado = True
    for i in range(0,len(ids_socios,1)):
        if id_buscado == ids_socios[i]:
            print("Resultado encontrado:")
            print(f"{nombres[i]} {apellidos[i]}, edad {edades[i]},{planes[i]} " )
        else:
            encontrado = False
    if encontrado == False:
        print("No se encontro el id.")
    



def ordenar_por_apellido(ids_socios, nombres, apellidos, edades, planes):
    pass



def calcular_recaudacion(valor_planes_activos, planes_activos,planes_socios):
    """Calculo de la recaudacion por plan activo

    Args:
        valor_planes_activos (int): valores de cada plan
        planes_activos (str): son los planes activos que se pueden elegir
        planes_socios (str):son los planes de cada socio

    Returns:
        devuelve una lista paralela con el valor total de la recaudacion por plan respecto a la cantidad de tipos de planes. 
    """
    contadores_planes = contar_planes(planes_socios,planes_activos)
    recaudacion_plan = []
    for i in range(0,len(planes_activos),1):
        valor = valor_planes_activos[i] * contadores_planes[i]
        recaudacion_plan.append(valor)
    return recaudacion_plan 

def mostrar_recaudacion_por_plan(planes_activos,planes_socios,valor_planes_activos):
    """Mostrar los planes, las cantidades que tiene inscripto cada plan y la recaudacion total de cada uno.

    Args:
        planes_activos (str): los planes habilitados
        planes_socios (str): el plan de cada socio
        valor_planes_activos (int): el valor de cada tipo de plan
    """
    contadores_planes = contar_planes(planes_socios, planes_activos)
    for i in range(0,len(planes_activos)):
        recaudacion_plan = calcular_recaudacion(valor_planes_activos, planes_activos, planes_socios)
        print(f"cantidad de {planes_activos[i]}: {contadores_planes[i]} de planes = ${recaudacion_plan[i]} pesos")

def calculo_porcentaje(valor_parcial,valor_total):
    porcentaje = valor_parcial * 100 / valor_total
    return porcentaje

def calcular_porcentaje_por_plan(planes_socios, valor_planes_activos, planes_activos):
    contadores_planes = contar_planes(planes_socios=planes_socios, planes_activos=planes_activos)
    recaudacion_plan = calcular_recaudacion(valor_planes_activos,planes_activos,planes_socios)
    acumulador = 0
    for i in range(0,len(contadores_planes),1):
        acumulador += recaudacion_plan[i]
    for j in range(0,len(contadores_planes),1):
        porcentaje = calculo_porcentaje(recaudacion_plan[j],acumulador)

        print(f"El porcentaje de recaudacion de {planes_activos[j]} , es {porcentaje} %")




