from modelo.participante import Participante

print('***************************')
print('* Programa Tiro al Blanco *')
print('***************************')
print()

participante1 = Participante()
participante1.nroParticipante = 20
participante1.nombre = 'Alex'
participante1.apellido = 'Vaca'
participante1.edad = 36
participante1.sexo = 'M'

print(str(participante1))
