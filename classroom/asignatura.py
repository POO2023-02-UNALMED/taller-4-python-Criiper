class Asignatura:

    def __init__(self, nombre, salon = None):
        self._nombre = nombre
        if salon != None:
            self._salon = salon
        else:
            self._salon = "remoto"

    def __str__(self):
         return self._nombre + " " + self._salon
