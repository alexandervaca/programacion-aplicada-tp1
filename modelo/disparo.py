from participante import Participante

class Disparo(Participante):
    puntoX = 0.0
    puntoY = 0.0

    def __init__(self):
        print('Disparo __init__')

    def __str__(self):
        return 'Disparo:: puntoX:' + str(self.puntoX) + ', puntoY: ' + str(self.puntoY) 


    pass