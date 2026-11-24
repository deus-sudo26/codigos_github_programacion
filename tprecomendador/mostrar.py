from colorama import *
from reglas import *
def mostrar_mensaje(mensaje:str):
    print(mensaje)
def mostrar_lista(lista:list):
    for i in range(0,len(lista),1):
        print(lista[i] ,end= " / ")
def mostrar_menu(lista:list):
    for i in range(0,len(lista),1):
        print(lista[i])
def mostrar_duracion_tiempo(lista1:list, lista2:list):
    for i in range(0, len(lista2),1):
        print(f"{lista1[i]} Hasta {lista2[i]} horas en terminarlo")        
def mostrar_indice():
    print(f"""
        '''{Fore.RED}BIENVENIDO A LA BASE DE DATOS DE VIDEOJUEGOS'''{Style.RESET_ALL}
        TE AYUDAREMOS A ENCONTRAR UN JUEGO SEGUN TUS PREFERENCIAS.
        """)  
#region MOSTRAR
def mostrar_recomendacionesv2(usuario):
  for i in range(len(usuario["recomendaciones"])):
    print(f"{i+1}) {usuario["recomendaciones"][i]}")

def mostrar_primer_salida(usuario,lista_rank,diccionario_juegos_en_genero,recomendaciones_consulta):
    ranking = determinar_ranking(diccionario_juegos_en_genero,lista_rank)
    print("\n" + f"{Fore.CYAN}={Style.RESET_ALL}"*80 )
    print("\t"*3 + f"RESULTADO DE TU BÚSQUEDA PARA {usuario["nombre"]}")
    print(f"{Fore.CYAN}={Style.RESET_ALL}"*80)
    for i in range(len(lista_rank)):
      print(f"{i+1}° Puesto: {lista_rank[i]} (Puntaje: {diccionario_juegos_en_genero[lista_rank[i]]["score"]}) - {ranking[i+1]["mensaje"]}")
    print(f"{Fore.CYAN}={Style.RESET_ALL}" * 80)
    print(f"{Fore.YELLOW}RECOMENDACIONES PARA TU PERFIL ({recomendaciones_consulta}){Style.RESET_ALL}")
    mostrar_recomendacionesv2(usuario)
    print(f"{Fore.CYAN}={Style.RESET_ALL}" * 80)
  
def mostrar_segunda_salida(cantidad_de_consultas, promedio_scores_mejor,cantidad_generos):
    print(f"{Fore.CYAN}={Style.RESET_ALL}"*80)
    print(f"""{Fore.CYAN}======================================= ESTADISTICAS ================================{Style.RESET_ALL}
                CANTIDAD DE CONSULTAS: {cantidad_de_consultas}
                PROMEDIO DE PUNTOS DEL 1° PUESTO: {promedio_scores_mejor:.2f}
  {Fore.CYAN}====================================================================================={Style.RESET_ALL}""")
    print("La cantidad de registros de generos son:\n")
    mostrar_diccionario(cantidad_generos)
    print(f"{Fore.CYAN}={Style.RESET_ALL}"*80)
#endregion
def mostrar_diccionario(diccionario):
  for datos in diccionario:
    print(f"{datos:<20} : {diccionario[datos]}")

def mostrar_un_usuario(usuario):
    print(f"Nombre: {usuario["nombre"]:<30}\nEdad: {usuario["edad"]}\nGenero elegido: {usuario["genero"]}\n ")

def detallar_usuario(usuario):
   print(f"Nombre: {usuario["nombre"]:<30}\nEdad: {usuario["edad"]}\nGenero elegido: {usuario["genero"]}\nPlataforma disponible: {usuario["plataforma"]}\nJuega: {usuario["modalidad"]}")
   print(f"Tu presupuesto: ${usuario["presupuesto_disponible"]}\nDificultad de preferencia: {usuario["dificultad"]}")
   
def mostrar_usuarios(usuarios):
    for usuario in usuarios:
        mostrar_un_usuario(usuario)
    print("=" * 50)

def mostrar_todos_los_datos(usuario,videojuegos,genero,reglas_videojuegos):
    detallar_usuario(usuario)
    cargar_puntuacionv2(usuario,videojuegos,reglas_videojuegos)
    lista_rank = ordenar_puntuacion(videojuegos[genero])
    ranking = determinar_ranking(videojuegos[genero],lista_rank)
    mostrar_primer_salida(usuario,lista_rank,ranking,videojuegos[genero],usuario["recomendaciones"])


def mostrar_graficov2(cantidad_generos, genero_mas_elegido):
    print(f"\n      GENEROS ELEGIDOS (cada 🟩 = 10%)")
    total = calcular_total_generos(cantidad_generos)
    for genero in cantidad_generos:
        porcentaje_genero = calcular_porcentaje(cantidad_generos[genero],total)
        barra = ""
        for i in range(int(porcentaje_genero // 10)):
            if porcentaje_genero != 0:
                barra += "🟩"
                continue
            barra += "  "
        print(f"      {genero:<10}{barra:<22} {cantidad_generos[genero]} ({porcentaje_genero:.1f}%)")  
    print(f"\n      GENERO MAS ELEGIDO: {genero_mas_elegido}")

def filtrar_por_nombre(nombre_buscado,lista_usuarios):
  encontrado = False
  for usuario in lista_usuarios:
    if nombre_buscado == usuario["nombre"]:
      encontrado = True
      mostrar_un_usuario(usuario)
  if encontrado == False:
    print("No se ha encontrado ese usuario. ")
    
