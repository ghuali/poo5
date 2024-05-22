from tarea import Tarea

class Evento(Tarea):
    def __init__(self, fechaInicio: str, fechaFinal: str, horaInicio: float, horaFinal:float) -> None:
        Tarea.__init__(estado,id,tarea)
        # Tener de atributos de fecha de inicio,hora inicio,fecha final,hora final y utilizar "CRUD" que es read update y delete
        self.fechaInicio = fechaInicio
        self.fechaFinal = fechaFinal
        self.horaInicio = horaInicio
        self.horaFinal = horaFinal
        self.estado = estado


    def read(self):
        self.fechaInicio = fechaInicio
        self.fechaFinal = fechaFinal
        self.horaInicio = horaInicio
        self.horaFinal = horaFinal


    def update(self):
        pass

    def delete(self):
        pass
