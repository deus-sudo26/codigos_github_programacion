#region CALCULOS
def cambiar_horas_minutos(horas:int):
    minutos = horas * 60
    return minutos
def calcular_presupuesto_hora(presupuesto:int, horas:int):
    presupuesto_hora = presupuesto / horas
    return presupuesto_hora
def calcular_dias_juego_largo(horas:int):
    dias_de_juego = (200 / horas)
    return dias_de_juego
def calcular_mayor(lista):
    mayor = lista[0]
    for i in range(0, len(lista), 1):
        if lista[i] > mayor:
            mayor = lista[i]
    return mayor
def calcular_promedio(dividendo:int, divisor:int) :
    promedio = dividendo / divisor
    return promedio
def calcular_porcentaje(cantidad_parcial, cantidad_total ):
    porcentaje = cantidad_parcial * 100 / cantidad_total
    return porcentaje

def contar_generos(lista_usuarios,cantidad_generos):
    for genero in cantidad_generos:
      cantidad_generos[genero] = 0
    for usuario in lista_usuarios:
      genero = usuario["genero"]
      if genero in cantidad_generos:
        cantidad_generos[genero] += 1
def obtener_genero_mas_elegido(cantidad_generos):
    genero_mas_elegido = ""
    mayor = -1
    for genero in cantidad_generos:
        if cantidad_generos[genero] > mayor:
            mayor = cantidad_generos[genero]
            genero_mas_elegido = genero
        elif cantidad_generos[genero] == mayor:
            genero_mas_elegido += " "+genero
    return genero_mas_elegido
def calcular_total_generos(cantidad_generos):
    total = 0
    for genero in cantidad_generos:
        total += cantidad_generos[genero]
    return total 