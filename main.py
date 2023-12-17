from utils.validates import click, val_nombre, val_area, val_tel, val_codigo
from controller import usuarios_controller, administrador_controller
from models.usuario import Usuario
from models.area import Area


@click.group()
def main():
    pass

# Listar usuarios
@main.command()
def usuarios():
    usuarios_controller.listar_usuarios()

# Listas áreas
@main.command()
def areas():
    usuarios_controller.listar_areas()

# Buscar trabajadores por nombre
@main.command()
@click.option('--filtro', 
              prompt = 'nombre', 
              help = "Introducir una parte del nombre para ver resultados de busqueda",
              type = str)
@click.pass_context
def buscar_nombre(context, filtro):
    if not filtro:
        context.fail("Debe ingresar almenos la inicial de la persona a buscar")
    else:
        usuarios_controller.buscar_por_nombre(filtro)

# Buscar trabajadores por área de trabajo
@main.command()
@click.option("--filtro", prompt = 'area', 
              help = "Introducir una parte del area para ver resultados de busqueda",
              type = str)
@click.pass_context
def buscar_area(context, filtro):
    if not filtro:
        context.fail("Debe ingresar almenos la inicial del área a buscar")
    else:
        usuarios_controller.buscar_por_area(filtro)

# Registrar trabajador
@main.command()
@click.option('--codigo', prompt = 'Código', help = "Introducir código", type= click.UNPROCESSED, callback = val_codigo)
@click.option('--nombre', prompt = 'Nombre', help = "Introducir nombre", type = click.UNPROCESSED, callback = val_nombre)
@click.option('--apellido', prompt = 'Apellido', help = "Introducir apellido", type = click.UNPROCESSED, callback = val_nombre)
@click.option('--area', prompt = 'Área', help = "Introducir área", type = click.UNPROCESSED, callback = val_area)
@click.option('--telefono', prompt = 'Teléfono', help = "Introducir número de teléfono", type = click.UNPROCESSED, callback = val_tel)
@click.option('--correo', prompt = 'Correo', help = "Introducir correo", type = str)
@click.pass_context
def crear_usuario(context, codigo, nombre, apellido, area, telefono, correo):
    if not codigo or not nombre or not apellido or not area or not telefono or not correo:
        context.fail("Los datos solicitados son obligatorios")
    else:
        usuario = Usuario(codigo, nombre, apellido, area, telefono, correo)
        administrador_controller.crear_usuario(usuario)
        print(f"Se registró correctamente a {usuario.nombre}")


# Eliminar trabajador
@main.command()
@click.argument('codigo', type = int)
def eliminar_usuario(codigo):
    administrador_controller.eliminar_usuario(codigo)



# Registrar Area de trabajo
@main.command()
@click.option('--nombre', prompt = 'Nombre', help = "Introducir nombre del área", type = str)
@click.pass_context
def crear_area(context, nombre):
    if not nombre:
        context.fail("Los datos solicitados son obligatorios")
    else:
        administrador_controller.crear_area(nombre)
        click.echo(f"Se registró el área {nombre}")
    


if __name__ == '__main__':
    main()