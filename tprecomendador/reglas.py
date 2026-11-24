from colorama import *
from calculos import *
#region REGLAS
def comparar(valor_usuario, operador, valor_regla):
    bandera = False
    if operador == "==":
        bandera = valor_usuario == valor_regla
    elif operador == ">":
        bandera =  valor_usuario > valor_regla
    elif operador == "<":
        bandera = valor_usuario < valor_regla
    elif operador == ">=":
        bandera = valor_usuario >= valor_regla
    elif operador == "<=":
        bandera = valor_usuario <= valor_regla
    elif operador == "in":
        bandera = valor_usuario in valor_regla
    elif operador == "not in":
        bandera = valor_usuario not in valor_regla
    elif operador == "!=":
        bandera = valor_usuario != valor_regla
    return bandera

def exportar_reglasv2(usuario, reglas):
  usuario["recomendaciones"] = []
  for regla in reglas:
    cumple = True
    for llave_usuario, operador, valor in regla["condiciones"]:
      if comparar(usuario[llave_usuario], operador, valor) == False:
        cumple = False
        break
    if cumple:
      usuario["recomendaciones"].append(regla["texto"])
  return len(usuario["recomendaciones"])

def evaluar_condicion(usuario,juego,condiciones):
  cumple = True
  for llave_usuario,comparador,llave_juego in condiciones:
      if llave_juego in juego:
        valor_juego = juego[llave_juego]
      else:
        valor_juego = llave_juego
      if llave_usuario in usuario:
        valor_usuario = usuario[llave_usuario]
      else:
        valor_usuario = llave_usuario
        
      if comparar(valor_usuario,comparador,valor_juego) == False:
        cumple = False
        break
  return cumple

def exportar_puntosv2(usuario, reglas_videojuegos,juegos,genero):
      for juego_evaluar in juegos[genero].values(): #diccionarios con las caracteristicas de los juegos
        puntos = 0
        for regla in reglas_videojuegos:
          cumple = evaluar_condicion(usuario,juego_evaluar,regla["condiciones"])    
          if cumple:
            puntos += regla["puntos"]
            if "segunda_regla" in regla:
              if evaluar_condicion(usuario,juego_evaluar,regla["segunda_regla"]):
                puntos += regla["segundo_puntaje"]
          
        juego_evaluar["score"] = puntos
              
def cargar_puntuacionv2(usuario:dict , juegos: dict,reglas_videojuegos):
    for genero in juegos:
        if usuario["genero"] == genero:
          exportar_puntosv2(usuario,reglas_videojuegos,juegos,genero)

# def cargar_puntos_por_juego(juegos,usuario,genero):
#   for juego in juegos[genero]:
#         puntos_juego = 0
#         datos = juegos[genero][juego]
#         if usuario["edad"] >= datos["edad_recomendada"] and usuario["modalidad"] in datos["modalidad"] and usuario["dificultad"] == datos["dificultad"]:
#                 puntos_juego += 10
#         elif usuario["modalidad"] in datos["modalidad"]:
#             puntos_juego += 4
#         if usuario["plataforma"] == datos["plataforma"]:
#             puntos_juego += 5
#             if usuario["capacidad_almacenamiento_disponible"] >= datos["almacenamiento_minimo"]:
#                 puntos_juego += 2
#         if usuario["experiencia"] == datos["experiencia_requerida"] and usuario["dificultad"] == datos["dificultad"]:
#             puntos_juego += 4
#         elif usuario["experiencia"] == "Amateur" and datos["dificultad"] == "Dificil":
#             puntos_juego -= 4
#         if usuario["modalidad"] not in datos["modalidad"]:
#             puntos_juego -= 2
#         if usuario["minutos_disponibles_al_dia"] < datos["duracion"]["Minutos_recomendados"]:
#             puntos_juego -= 1
#         else:
#             puntos_juego += 2
#         if usuario["preferencia_duracion_juego"] in datos["duracion"]:
#             puntos_juego += 3
#         if usuario["presupuesto_disponible"] < datos["presupuesto_minimo"] or usuario["dificultad"] != datos["dificultad"]:
#             if usuario["experiencia"] == "Amateur":
#                 puntos_juego -= 2
#             else:
#                 puntos_juego -= 1
#         if usuario["capacidad_almacenamiento_disponible"] > datos["almacenamiento_minimo"]:
#             puntos_juego += 4
#         else:
#             puntos_juego -=2
#         datos["score"] = puntos_juego
    

def cargar_juegos_a_una_lista(juegos):
  lista_auxiliar = []
  for juego in juegos:
    lista_auxiliar.append(juego)
  return lista_auxiliar

def ordenar_puntuacion(juegos):
  lista_auxiliar = cargar_juegos_a_una_lista(juegos)
  for i in range(len(lista_auxiliar)-1):
    for j in range(i+1,len(lista_auxiliar)):
      if juegos[lista_auxiliar[i]]["score"] < juegos[lista_auxiliar[j]]["score"]:
        auxiliar = lista_auxiliar[i]
        lista_auxiliar[i] = lista_auxiliar[j]
        lista_auxiliar[j] =auxiliar
  return lista_auxiliar

def determinar_ranking(juegos_en_genero, lista_rank):
  ranking = {}
  puesto = 1
  for juego in lista_rank:
    puntos = juegos_en_genero[juego]["score"]
    if puntos >= 15:
        mensaje = "Excelente recomendación"
    elif puntos >= 10:
        mensaje = "Buena recomendación"
    elif puntos > 0:
        mensaje = "Recomendación regular"
    else:
        mensaje = "Mala opcion."
    ranking[puesto] = {
        "juego": juego,
        "puntos": puntos,
        "mensaje": mensaje
    }
    puesto += 1
  return ranking
