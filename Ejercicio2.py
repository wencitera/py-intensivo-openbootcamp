
class Persona:
    nombre=''
    telefono=''
    def __init__(self, nombre, telefono):
        self.nombre = nombre
        self.telefono = telefono


def crear_persona():
    nombre = input('Ingrese nombre: \n')
    telefono = input('Ingrese telefono: \n')
    return Persona(nombre, telefono)


def listar_personas(personas):
    for persona in personas:
        print(f'{persona.nombre} {persona.telefono}')

    input('\nAprente enter para salir \n')


def buscar_persona(personas):
    persona_filtradas = []
    nombre = input('Ingrese el nombre de la persona: \n')
    for persona in personas:
        if str(persona.nombre).__contains__(nombre):
            persona_filtradas.append(persona)

    listar_personas(persona_filtradas)


def main():
    personas=[]
    opciones= {
        1: lambda: personas.append(crear_persona()),
        2: lambda: buscar_persona(personas),
        3: lambda: listar_personas(personas),
        0: lambda: print('Adios!')
    }
    opcion = 1
    while opcion != 0:
        print(f'''Seleccione una opcion: 
                \n1- Cargar persona
                \n2- Buscar persona
                \n3- Listar personas
                \n\n0- Salir''')
        
        opcion = int(input())

        opciones.get(opcion, lambda: print('Opcion no valida'))()


if __name__ == '__main__':
    main()