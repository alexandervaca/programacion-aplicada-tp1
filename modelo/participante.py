class Participante:
    nroParticipante = 0
    nombre = ''
    apellido = ''
    edad = 0
    sexo = 'N'
    
    # def __init__(self):
    #     print('Participante __init__')

    def __str__(self):
        cadena = 'Participante:: nroParticipante: ' + str(self.nroParticipante) 
        cadena += ', nombre y apellido: ' + str(self.nombre) + ' ' + str(self.apellido)
        cadena += ', edad: ' + str(self.edad) + ', sexo: ' + str(self.sexo)
        return cadena

    pass