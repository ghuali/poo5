from tarea import Tarea

class Evento(Tarea):
    def __init__(self, fechaInicio: str, fechaFinal: str, horaInicio: str, horaFinal:str) -> None:
        
        # Tener de atributos de fecha de inicio,hora inicio,fecha final,hora final y utilizar "CRUD" que es read update y delete
        self.fechaInicio = fechaInicio
        self.fechaFinal = fechaFinal
        self.horaInicio = horaInicio
        self.horaFinal = horaFinal
        


    def read(self):
        return super().read(),self.fechaInicio,self.fechaFinal,self.horaInicio,self.horaFinal


    def update(self,fechaInicio,fechaFinal,horaInicio,horaFinal):
        super().update()
        self.fechaInicio = fechaInicio
        self.fechaFinal = fechaFinal
        self.horaInicio = horaInicio
        self.horaFinal = horaFinal

    def delete(self):
        super().delete()
        self.fechaInicio = None
        self.fechaFinal = None
        self.horaInicio = None
        self.horaFinal = None

