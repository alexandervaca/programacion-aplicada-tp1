import math
import csv

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

    def agregarDisparo(self, disparo):
        self.disparos.append(disparo)

    def mostrarRegistros(self):
        for disparo in self.disparos:
            print(str(disparo))

    #podio con los 3 primeros
    def mostrarPodio(self):
        participantesPodio = self.disparos
        for i in range(len(participantesPodio)-1):
            for k in range(len(participantesPodio)-1-i):
                if participantesPodio[ k ].mejorDisp > participantesPodio[ k+1 ].mejorDisp:
                    participantesPodio[ k ],participantesPodio[ k+1 ] = participantesPodio[ k+1 ],participantesPodio[ k ]
        
        if participantesPodio.__len__() >= 3:
            print('Nro 1: ' + str(participantesPodio[0]))
            print('Nro 2: ' + str(participantesPodio[1]))
            print('Nro 3: ' + str(participantesPodio[2]))
        if participantesPodio.__len__() == 2:
            print('Nro 1: ' + str(participantesPodio[0]))
            print('Nro 2: ' + str(participantesPodio[1]))
        if participantesPodio.__len__() == 1:
            print('Nro 1: ' + str(participantesPodio[0]))
        if participantesPodio.__len__() == 0:
            print('Sin participantes.')

    def mostrarUltimo(self):
        ultimoPart = None
        ultimoPuntaje = 0.0
        for disparo in self.disparos:
            peorDisparo = max(disparo.disp1, disparo.disp2, disparo.disp3)
            if ultimoPuntaje < peorDisparo:
                ultimoPuntaje = peorDisparo
                ultimoPart = disparo
        
        return ultimoPart.nombre + ' ' + ultimoPart.apellido + ' ' + str(ultimoPart)

    def cantidadParticipantes(self):
        return self.disparos.__len__()

    def mostrarParticipantesPorEdad(self):
        participantesPorEdad = self.disparos
        for i in range(len(participantesPorEdad)-1):
            for k in range(len(participantesPorEdad)-1-i):
                if participantesPorEdad[ k ].edad < participantesPorEdad[ k+1 ].edad:
                    participantesPorEdad[ k ],participantesPorEdad[ k+1 ] = participantesPorEdad[ k+1 ],participantesPorEdad[ k ]
        
        #imprime participantes ordenados por edad
        for participante in participantesPorEdad:
          print(str(participante))

    #retorna el promedio de todos los mejores disparos
    def promedioDisparos(self):
        promedioTotal = 0.0
        for disparo in self.disparos:
            promedioTotal += disparo.mejorDisp
        return promedioTotal / self.disparos.__len__()

    def guardarCSV(self):
        # abre archivo csv en modo escritura 'w' 
        archivo = open('torneo.csv', 'w', newline ='')
        # escribe en el archivo cabecera y filas de registros
        with archivo:
            header = ['Nro Part','Nombre','Apellido','Edad','Sexo','Disp1','Disp2','Disp3','MejorDisp','PromDisp']
            writer = csv.DictWriter(archivo, fieldnames = header)
            writer.writeheader()

            for disparo in self.disparos:
                disparoCSV = {
                  'Nro Part': disparo.numero, 
                  'Nombre': disparo.nombre, 
                  'Apellido': disparo.apellido, 
                  'Edad': disparo.edad, 
                  'Sexo': disparo.sexo,
                  'Disp1': disparo.disp1,
                  'Disp2': disparo.disp2,
                  'Disp3': disparo.disp3,
                  'MejorDisp': disparo.mejorDisp,
                  'PromDisp': disparo.promedioDisp
                }
                writer.writerow(disparoCSV)
            
            archivo.close()

        print('Los datos del torneo se guardaron en el archivo: torneo.csv')
    
    pass