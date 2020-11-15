class Concurso:
    disparos = []

    def agregarDisparo(self, disparo):
        self.disparos.append(disparo)

    def mostrarRegistros(self):
        # TODO terminar
        for disparo in self.disparos:
            print(disparo)

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

    def mostrarParticipantes(self):
        # TODO ordenado por edad
        for disparo in self.disparos:
            print(disparo)

    def promedioDisparos(self):
        total = 0.0
        for disparo in self.disparos:
            print(disparo)
            total += 0#disparo.
        return total / self.disparos.__len__()

    def guardarCSV(self):
        for disparo in self.disparos:
            print(disparo)

    pass