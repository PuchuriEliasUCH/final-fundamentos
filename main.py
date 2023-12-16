import click
from controller import usuarios_controller, administrador_controller
from models.usuario import Usuario


@click.group()
def main():
    pass


@main.command()
def usuarios():
    usuarios_controller.listar_usuarios()

@main.command()
def areas():
    usuarios_controller.listar_areas()

@main.command()
@click.option('--filtro', 
              prompt = 'Parte del nombre', 
              help = "Introducir una parte del nombre para ver resultados de busqueda",
              type = str)
@click.pass_context
def buscar_por_nombre(context, filtro):
    if not filtro:
        context.fail("Debe ingresar almenos la inicial de la persona que quiere buscar")
    else:
        usuarios_controller.buscar_por_nombre(filtro)

# print(usuarios_controller.buscar_por_area(3))

@main.command()
@click.option('--codigo', prompt = 'Código', help = "Introducir código", type = int)
@click.option('--nombre', prompt = 'Nombre', help = "Introducir nombre", type = str)
@click.option('--apellido', prompt = 'Apellido', help = "Introducir apellido", type = str)
@click.option('--area', prompt = 'Área', help = "Introducir área", type = int)
@click.option('--numero', prompt = 'Número', help = "Introducir número", type = int)
@click.option('--correo', prompt = 'Correo', help = "Introducir correo", type = str)
@click.pass_context
def crear(context, codigo, nombre, apellido, area, numero, correo):
    if not codigo or not nombre or not apellido or not area or not numero or not correo:
        context.fail("Los datos solicitados son obligatorios")
    else:
        usuario = Usuario(codigo, nombre, apellido, area, numero, correo)
        administrador_controller.crear_usuario(usuario)
        print(f"Se registró correctamente a {usuario.nombre}")


# crear(1,'fernanda', 'beltran', 2, '987654321', 'fer@gmail.com', 'asdasdasd')
    
if __name__ == '__main__':
    main()