from tarea import Tarea

class Evento(Tarea):
    def __init__(self, fechaInicio: str, fechaFinal: str, horaInicio: float, horaFinal:float) -> None:
        super().__init__(fechaInicio, fechaFinal,  horaInicio, horaFinal)
# Tener de atributos de fecha de inicio,hora inicio,fecha final,hora final y utilizar "CRUD" que es read update y delete


    def read(self):
        pass


    def update(self):
        pass

    def delete(self):
        pass
