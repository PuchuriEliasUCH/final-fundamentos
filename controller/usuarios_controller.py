import sys
from pathlib import Path
sys.path.append(str(Path(__file__).resolve().parent.parent))
from utils.json_manager import read_data

def listar_usuarios():
    return read_data()['trabajadores']

def listar_areas():
    return read_data()['areas']

def buscar_por_area():
    pass

def buscar_por_nombre():
    pass

