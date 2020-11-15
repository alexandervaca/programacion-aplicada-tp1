import math

#Clase Participante
class Participante:
    numero = 0
    nombre = ''
    apellido = ''
    edad = 0
    sexo = ''
    
    #constructor
    def __init__(self, numero, nombre, apellido, edad, sexo):
        self.numero = numero
        self.nombre = nombre
        self.apellido = apellido
        self.edad = edad
        self.sexo = sexo

    def __str__(self):
        cadena = 'Participante:: numero: ' + str(self.numero) 
        cadena += ', nombre y apellido: ' + self.nombre + ' ' + self.apellido
        cadena += ', edad: ' + str(self.edad) + ', sexo: ' + self.sexo
        return cadena
    pass

#Clase Disparo que hereda de Participante
class Disparo(Participante):
    disp1 = 0
    disp2 = 0
    disp3 = 0
    mejorDisp = 0.0
    promedioDisp = 0.0

    #constructor
    def __init__(self, disp1, disp2, disp3, participante):
        self.numero = participante.numero
        self.nombre = participante.nombre
        self.apellido = participante.apellido
        self.edad = participante.edad
        self.sexo = participante.sexo
        self.disp1 = disp1
        self.disp2 = disp2
        self.disp3 = disp3
        self.mejorDisp = min(disp1, disp2, disp3)
        self.promedioDisp = round((self.disp1 + self.disp2 + self.disp3) / 3, 2)

    def __str__(self):
        participanteStr = Participante.__str__(self)
        disparos = 'Disparos: ' + str(self.disp1) + ' ' + str(self.disp2) + ' ' + str(self.disp3)
        disparosText = 'Mejor: ' + str(self.mejorDisp) + ' promedio: ' + str(self.promedioDisp)
        return str(participanteStr + '\n') + disparos + '\n' + disparosText
    pass

#calcula la distancia al origen con los puntos x,Y
class CalculadorDisparo:

    def calcular(self, puntoX, puntoY):
        return round(math.sqrt(math.pow(puntoX, 2) + math.pow(puntoY, 2)), 2)
    pass

#Clase Concurso que contiene los disparos
class Concurso:
    disparos = []

    #constructor
    def __init__(self):
        print('Concurso __init__')

    def agregarDisparo(self, disparo):
        self.disparos.append(disparo)

    def mostrarRegistros(self):
        for disparo in self.disparos:
            print(disparo)

    #los 3 primeros
    def mostrarPodio(self):
        # TODO
        for disparo in self.disparos:
            print(disparo)

    def mostrarUltimo(self):
        # TODO
        ultimo = None
        for disparo in self.disparos:
            ultimo = disparo
        print(ultimo)

    def cantidadParticipantes(self):
        return self.disparos.__len__()

    def mostrarParticipantesPorEdad(self):
        # TODO ordenado por edad
        for disparo in self.disparos:
            print(disparo)

    def promedioDisparos(self):
        total = 0.0
        for disparo in self.disparos:
            #print(disparo)
            total += disparo
        return total / self.disparos.__len__()

    def guardarCSV(self):
        for disparo in self.disparos:
            print(disparo)

    pass