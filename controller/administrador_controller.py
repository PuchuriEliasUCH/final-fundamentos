import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from utils.json_manager import read_data, write_json
from models.administrador import Usuario

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

def eliminar_usuario():
    pass

def crear_area():
    pass

def editar_area():
    pass

def eliminar_area():
    pass