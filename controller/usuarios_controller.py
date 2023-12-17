from tabulate import tabulate
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from utils.json_manager import trabajadores, read_data

trabajadores = trabajadores()
areas = list(filter(lambda x: x['activo'] == True, read_data()['areas']))

for i in trabajadores:
    i['area'] = areas[i['area'] - 1]['nombre']


def listar_usuarios():
    print(tabulate(trabajadores, headers="keys", tablefmt='pretty'))

def listar_areas():
    print(tabulate(areas, headers="keys", tablefmt='pretty'))

def buscar_por_area(area = str):
    resultados = list(filter(lambda x: area.lower() in x['area'].lower(), trabajadores))
    print(tabulate(resultados, headers="keys", tablefmt='pretty'))

def buscar_por_nombre(nombre = str):
    resultados = list(filter(lambda x: nombre.lower() in x['nombre'].lower(), trabajadores))
    
    if resultados != []:
        print(tabulate(resultados, headers="keys", tablefmt='pretty'))
    else:
        print("No hay resultados para su busqueda")

    
def funcion_de_fer():
    print("🐿️🐿️")

funcion_de_fer()