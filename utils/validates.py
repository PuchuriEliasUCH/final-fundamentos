import click
from .json_manager import read_data

def val_codigo(ctx, param, value):
    codigos = [x['codigo'] for x in read_data()['trabajadores']]
    
    try:
        value = int(value)
    except ValueError:
        raise click.BadParameter("Debes ingresar únicamente números")
    

    if value in codigos:
        raise click.BadParameter("Este usuario ya está registrado")
    
    return value

def val_nombre(ctx, param, value):
    if value.isalpha():
        return value
    
    raise click.BadParameter("Ingrese un nombre correcto")
    
def val_area(ctx, param, value):
    areas = [x['id'] for x in read_data()['areas']]
    
    try:
        value = int(value)
    except ValueError:
        raise click.BadParameter("Debes ingresar el número del área")
    
    if value not in areas:
        raise click.BadParameter("El área específicada no existe")
    
    return value

def val_tel(ctx, param, value):
    
    if not value.isdigit():
        raise click.BadParameter("Debe ingresar únicamente números")

    if len(value) != 9:
        raise click.BadParameter("Ingrese una telefóno correcto")

    return value
    
    
