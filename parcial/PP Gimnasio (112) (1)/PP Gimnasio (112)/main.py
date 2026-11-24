
from funciones import *
from data_storage import *
from socio import *

def main():
    lista_opciones = [
        "Cargar socio",
        "Mostrar socios",
        "Buscar socio por ID",
        "Ordenar socios por Apellido",
        "Recaudacion por plan",
        "Calcular porcentaje por plan",
        "Salir"
    ]

    planes_activos = [
        "Musculacion",
        "Funcional",
        "Pileta",
        "Full"
    ]
    valores_planes_activos = [
        19000,
        15000,
        23000, 
        50000
    ]

    while True:
        opcion = elegir_opcion(lista_opciones)
        match opcion:
            case 1:
                print("Vamos a cargar tus datos")
                cargar_socio(nombres,apellidos,ids_socios,edades,planes, "ingresa tus datos a continuacion.")


                pass
            case 2:
                mostrar_socios(nombres,apellidos,ids_socios,edades,planes)
                pass
            case 3:
                id_buscado = get_int("ingresa el id que deseas buscar: ")
                buscar_socio(id_buscado,nombres,apellidos,ids_socios,edades,planes)

            case 4:
                pass
            case 5:
                
                mostrar_recaudacion_por_plan(planes_activos,planes,valores_planes_activos)


                
            case 6:
                calcular_porcentaje_por_plan(planes_socios=planes,valor_planes_activos=valores_planes_activos,planes_activos=planes_activos)
                pass
            case 7:
                print("finalizacion del programa...")
                break

        
        


if __name__ == "__main__":
    main()