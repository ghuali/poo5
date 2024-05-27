from examenRepaso.perusoma import Persona

class Jugador(Persona):
    def __init__(self, nombre,deporte) -> None:
        super().__init__(nombre)
        self.deporte = deporte


    def read(self):
        return super().read() + ',' + self.deporte