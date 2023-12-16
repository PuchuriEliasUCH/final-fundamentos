from tabulate import tabulate
import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from utils.json_manager import read_data

# Creamos una lista con aquellos trabajadores activos
trabajadores = list(filter(lambda x: x['activo'] == True, read_data()['trabajadores']))
# Creamos una lista con aquellas areas activas
areas = list(filter(lambda x: x['activo'] == True, read_data()['areas']))

for i in trabajadores:
    i['area'] = areas[i['area'] - 1]['nombre']


def listar_usuarios():
    print(tabulate(trabajadores, headers="keys", tablefmt='pretty'))

def listar_areas():
    for area in areas:
        print(f"{area['id']} - {area['nombre']}")

def buscar_por_area(area = int):
    data = read_data()['trabajadores']
    return list(filter(lambda x: x['area'] == area, data))

def buscar_por_nombre(nombre = str):
    resultados = list(filter(lambda x: nombre.lower() in x['nombre'].lower(), trabajadores))
    
    if resultados != []:
        for resultado in resultados:
            print(f"""==== {resultado['codigo']} ====
nombre: {resultado['nombre']} {resultado['apellido']}
area: {resultado['area']}
número: {resultado['numero']}
correo: {resultado['correo']}
""")
    else:
        print("No hay resultados para su busqueda")

    
def funcion_de_fer():
    print("🐿️🐿️")

funcion_de_fer()