import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from utils.json_manager import read_data, write_json
from models.administrador import Usuario
from models.area import Area

def crear_usuario(usuario = Usuario):
    data = read_data()

    data['trabajadores'].append({
        'codigo': usuario.codigo,
        'nombre': usuario.nombre.title(),
        'apellido': usuario.apellido.title(),
        'area': usuario.area,
        'numero' : usuario.numero,
        'correo': usuario.correo,
        'activo': usuario.activo
    })

    write_json(data)

    


def editar_usuario():
    pass

def eliminar_usuario(codigo):
    data = read_data()
    usuario = next((x for x in data['trabajadores'] if x['codigo'] == codigo), None)
    if usuario is None: 
        print(f"El usuario no existe")
    else:
        usuario['activo'] = False
        write_json(data)
        print("El usuario fue eliminado correctamente")

def crear_area(area = str):
    data = read_data()

    data['areas'].append({
        'id': data['areas'][-1]['id'] + 1,
        'nombre': area.title(),
        'activo': True
    })

    write_json(data)

def editar_area():
    pass

def eliminar_area():
    pass