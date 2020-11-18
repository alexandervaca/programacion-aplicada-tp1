from modelo import Participante
from modelo import Disparo
from modelo import CalculadorDisparo
from modelo import Concurso

print('***************************')
print('* Programa Tiro al Blanco *')
print('***************************')

concurso = Concurso()
opcion = 's'
while (opcion == 's' or opcion == 'S'):
    
    print('Datos del participante')
    numero = int(input('Ingrese numero de partipante: '))
    nombre = input('Ingrese nombre: ')
    apellido = input('Ingrese apellido: ')
    edad = int(input('Ingrese edad: '))
    sexo = input('Ingrese sexo (F o M): ')

    print('Disparo nro 1')
    d1_X = int(input('Ingrese coordenada X de disparo 1: '))
    d1_Y = int(input('Ingrese coordenada Y de disparo 1: '))
    calculador = CalculadorDisparo()
    d1 = calculador.calcular(d1_X, d1_Y)

    print('Disparo nro 2')
    d2_X = int(input('Ingrese coordenada X de disparo 2: '))
    d2_Y = int(input('Ingrese coordenada Y de disparo 2: '))
    d2 = calculador.calcular(d2_X, d2_Y)

    print('Disparo nro 3')
    d3_X = int(input('Ingrese coordenada X de disparo 3: '))
    d3_Y = int(input('Ingrese coordenada Y de disparo 3: '))
    d3 = calculador.calcular(d3_X, d3_Y)

    disparo = Disparo(d1, d2, d3, Participante(numero, nombre, apellido, edad, sexo))
    concurso.agregarDisparo(disparo)

    opcion = input('Desea seguir ingresando participantes (S/N)? ')


print('\n')
print('Registros:')
concurso.mostrarRegistros()
print('\n')
print('Podio:')
concurso.mostrarPodio()
print('\n')
print('Ultimo participante:')
print(concurso.mostrarUltimo())
print('\n')
print('Cantidad de participantes: ' + str(concurso.cantidadParticipantes()))
print('\n')
print('Participantes ordenados por edad:')
concurso.mostrarParticipantesPorEdad()
print('\n')
print('Promedio de todos los disparos: ' + str(concurso.promedioDisparos()))
print('\n')
concurso.guardarCSV()
print('\n')
print('* Fin de programa *')
