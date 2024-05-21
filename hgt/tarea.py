class Tarea:
#Tarea que pide en atributos id,estado,tarea desc y utilizar "CRUD" que es read update y delete
    def __init__(self,estado:bool,id:int,tarea:str) -> None:
        self.id = id
        self.estado = estado
        self.tarea = tarea


    
    def read(self):
        return self.estado,self.id,self.tarea


    def update(self,estado,id,tarea):
        self.id = id
        self.estado = estado
        self.tarea = tarea


    def delete(self):
        self.id = None
        self.estado = None
        self.tarea = None




