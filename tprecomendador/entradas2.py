from mostrar import *
from calculos import *
#region pedir datos
def pedir_str(mensaje:str)-> str:
    str = input(mensaje).capitalize()
    return str
def pedir_int(mensaje:str):
    entero = input(mensaje)
    return entero
def pedir_nombre(mensaje:str)->str:
    nombre = input(mensaje).strip().capitalize()
    nombre = validar_nombre(nombre, mensaje)
    return nombre
#endregion
#region validaciones
def validar_nombre(nombre:str, mensaje:str):
    while len(nombre) < 3 or len(nombre) > 30 or validar_numero_en_nombre(nombre) == False:
        print("Error, ingresa un nombre hasta 30 caracteres y sin numeros.")
        nombre = input(mensaje).strip().capitalize()
    return nombre
def validar_numero_en_nombre(nombre:str):
    bandera = True
    for i in range(0,len(nombre),1):
        if nombre[i] >= "0" and nombre[i] <= "9":
            bandera = False
            break
    return bandera
  
def determinar_digitos(numero):
  bandera = True
  for digito in numero:
        if digito < "0" or digito > "9":
          bandera = False
          break
  return bandera
def validar_int_v2(numero,mensaje:str,mensaje_error:str,minimo:int,maximo:int,reintentos:int)-> int|None:
  intentos = 0
  while True:
    bandera = True
    if numero == "":
      bandera = False
    else:
      bandera = determinar_digitos(numero)
    if bandera == True:
      numero = int(numero)
      if minimo <= numero <= maximo:
        break        
    print(mensaje_error)
    intentos += 1
    if intentos == reintentos:
      print("Superaste los intentos...")
      numero = None
      break
    numero = pedir_int(mensaje)
  return numero
def comparar_dato_lista(lista,dato_validar):
  bandera = False
  for i in range(0,len(lista),1):
         if dato_validar == lista[i]:
            bandera = True
            break
  return bandera
  
def validar_str_en_lista(mensaje_input:str, dato_validar:str, lista:list, mensaje_error:str)-> str:
    bandera = False
    while bandera == False:
        bandera = comparar_dato_lista(lista,dato_validar)
        if bandera == False:
            mostrar_mensaje(mensaje_error)
            mostrar_mensaje(mensaje_input)
            mostrar_lista(lista)
            dato_validar = pedir_str("...:").capitalize()
    return dato_validar
#endregion
#region ENTRADA Y VALIDACION
def pedir_dato_validar(mensaje_input:str, lista:list, mensaje_error:str)-> str:
    mostrar_mensaje(mensaje_input)
    mostrar_lista(lista)
    dato = pedir_str("...: ")
    dato = validar_str_en_lista(mensaje_input, dato, lista, mensaje_error)
    return dato

def pedir_dato_duracion(mensaje_input:str, lista1:list, lista2:list, mensaje_error:str)-> str:
    mostrar_mensaje(mensaje_input)
    mostrar_duracion_tiempo(lista1, lista2)
    dato = pedir_str("...:")
    dato = validar_str_en_lista(mensaje_input, dato, lista1, mensaje_error)
    return dato

def pedir_int_validar(mensaje_input:str, mensaje_error:str, minimo:int, maximo:int, reintentos:int)-> int|None:
    entero = pedir_int(mensaje_input)
    entero = validar_int_v2(entero, mensaje_input, mensaje_error, minimo, maximo, reintentos)
    return entero
#endregion
def cargar_usuario(lista_modalidades,lista_plataformas,lista_generos,lista_dificultades,lista_nivel_experiencia,lista_duracion,lista_duracion_horas):
  usuario = {}
  carga_correcta = True
  usuario["nombre"] = pedir_nombre("Primero, Cómo te llamas?(minimo 3 caracteres): ")
  usuario["genero"] = pedir_dato_validar("\nMuy bien, dentro de esta lista de generos,elige el que mas te guste.\n",lista_generos,"\nEl genero no se encontró")
  usuario["plataforma"] = pedir_dato_validar("\n¿Con cual plataforma cuentas para jugar?\n",lista_plataformas,"\nPlataforma no encontrada " )
  usuario["modalidad"] = pedir_dato_validar("\nComo quieres jugar?\n",lista_modalidades, "\nModalidad no encontrada ")  
  if usuario["modalidad"] == "Solo" :      
      usuario["cantidad_jugadores"] = 1
  else:
      usuario["cantidad_jugadores"] = pedir_int("\nCuantos jugadores van a ser?(Hasta 10 jugadores): ")
      usuario["cantidad_jugadores"] = validar_int_v2(usuario["cantidad_jugadores"],"\nCuantos jugadores van a ser?","\nDato invalido,vuelve a intentar",1,10,10)
      if usuario["cantidad_jugadores"] == None:
        carga_correcta = False
  usuario["dificultad"] = pedir_dato_validar("\nElige tu nivel de dificultad: ",lista_dificultades,"\nDificultad no encontrada ")
  mostrar_mensaje("\nPerfecto, pasaremos a datos personales para una experiencia mas personalizada.")      
  usuario["edad"] = pedir_int_validar("\nIngresa tu edad: ","\nDebes tener 10 años o más, ingresa nuevamente",10, 80, 10)
  if usuario["edad"] == None:
    carga_correcta = False
  usuario["tiempo_disponible_al_dia"] = pedir_int("\nTiempo disponible al dia en horas(1hs a 24hs): ")
  usuario["tiempo_disponible_al_dia"] = validar_int_v2(usuario["tiempo_disponible_al_dia"], "\nIngresa nuevamente: ", "\nError al ingresar el dato", 1, 24,10)
  if usuario["tiempo_disponible_al_dia"] == None:
    carga_correcta = False
  usuario["experiencia"] = pedir_dato_validar("\nHas jugado antes? como te consideras en el gaming?: ",lista_nivel_experiencia,"\nNo hemos encontrado tu nivel...")
  usuario["preferencia_duracion_juego"] = pedir_dato_duracion("\nComo quieres que sea el juego?\n",lista_duracion, lista_duracion_horas, "\nError al ingresar dato...")
  usuario["capacidad_almacenamiento_disponible"] = pedir_int_validar("\n¿Cuantos GB libres tenes para instalar el juego?: ","\nTiene que ser entre 4GB a 2000GB.", 4, 2000, 10)
  if usuario["capacidad_almacenamiento_disponible"] == None:
    carga_correcta = False
  usuario["presupuesto_disponible"] = pedir_int_validar("\nCuanto dinero tenes disponible para gastar en el juego(pesos)?: ","\nError en el rango, de $3000 a $500000. ", 3000, 500000,10)
  if usuario["presupuesto_disponible"] == None:
    carga_correcta = False
  if carga_correcta:
    usuario["minutos_disponibles_al_dia"] = cambiar_horas_minutos(usuario["tiempo_disponible_al_dia"])
    usuario["presupuesto_por_hora_libre"] = calcular_presupuesto_hora(usuario["presupuesto_disponible"], usuario["tiempo_disponible_al_dia"])
    usuario["dias_para_completar"] = calcular_dias_juego_largo(usuario["tiempo_disponible_al_dia"])# dias que tardaria en terminar un juego largo  
  else:
    usuario = None
  return usuario