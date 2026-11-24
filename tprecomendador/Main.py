from entradas2 import *
from Diccionario_reglas import *
from mostrar import *
from reglas import *
from juegos import *
from Listas_lista_personas import *
import json
import os
if not os.path.exists("datos_usuarios.json"): 
  with open("datos_usuarios.json","w",encoding="utf-8") as archivo:
    json.dump([],archivo)
def main():
  mostrar_indice()
  cantidad_consultas = 0
  suma_scores_mejor = 0
  while True:
    opciones = ["\n1.Cargar datos y preferencias de usuario","2.Mostrar recomendaciones",
               "3.Mostrar estadisticas","4.Listar usuarios registrados",
               "5.Ampliar datos de mi consulta","6.Mostrar por nombre","7.Salir\n"]
    mostrar_menu(opciones)
    opcion = pedir_int_validar("Ingresa una opcion de la lista: ","Opcion incorrecta",1,7,10)
    match opcion:
      case 1:
        usuario_nuevo = cargar_usuario(lista_modalidades,lista_plataformas,lista_generos,lista_dificultades,lista_nivel_experiencia,lista_duracion,lista_duracion_horas)
        if usuario_nuevo != None:
          with open("datos_usuarios.json","r",encoding= "utf-8") as archivo:
            lista_usuariosjson = json.load(archivo)
          usuario = usuario_nuevo
          lista_usuarios.append(usuario)
          genero = usuario["genero"]
          recomendaciones_consulta = exportar_reglasv2(usuario,reglas_recomendaciones)
          lista_usuariosjson.append(usuario)
          with open("datos_usuarios.json", "w", encoding="utf-8") as archivo:
            json.dump(lista_usuariosjson, archivo, ensure_ascii=False, indent=4) 
          # with open("datos_usuario.json", "r", encoding="utf-8") as archivo:
          #   usuariosjson = json.load(archivo)
          #   for usuariojson in usuariosjson:
          #     mostrar_un_usuario(usuariojson)

        else:
          print("Error al cargar el usuario...")
      case 2: 
        if len(lista_usuarios) != 0:
          cantidad_consultas += 1
          cargar_puntuacionv2(usuario,videojuegos,reglas_videojuegos)
          lista_rank = ordenar_puntuacion(videojuegos[genero])
          mostrar_primer_salida(usuario,lista_rank,videojuegos[genero],recomendaciones_consulta)
          suma_scores_mejor += videojuegos[genero][lista_rank[0]]["score"]
        else:
          print("\nPrimero debes cargar tus datos y preferencias :) ...")
      case 3:
        if len(lista_usuarios) != 0 and cantidad_consultas != 0:
          contar_generos(lista_usuarios,cantidad_generos)
          promedio_scores_mejor = calcular_promedio(suma_scores_mejor,cantidad_consultas)
          mostrar_segunda_salida(cantidad_consultas,promedio_scores_mejor,cantidad_generos)
          genero_mas_elegido = obtener_genero_mas_elegido(cantidad_generos)
          mostrar_graficov2(cantidad_generos,genero_mas_elegido)
        else:
          print("\nNo se han cargado datos a la base de datos o no has realizado consultas.")
        
      case 4:
        if len(lista_usuariosjson) != 0:
          mostrar_usuarios(lista_usuariosjson)
        else:
          print("No hay usuario registrado...")
      case 5:
        if len(lista_usuarios) != 0 or cantidad_consultas != 0:
          mostrar_todos_los_datos(usuario,videojuegos,genero,reglas_videojuegos)
        else:
          print("\nLos datos de usuario estan vacios.")
      case 6:
        if len(lista_usuarios) != 0:
          nombre_buscado = pedir_nombre("Ingresa el nombre que quieres buscar: ")
          filtrar_por_nombre(nombre_buscado,lista_usuarios)
        else:
          print("No hay usuarios...")
      case 7:
        break


if __name__ == "__main__":
  main()