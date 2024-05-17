class Tarea:
#Tarea que pide en atributos id,estado,tarea desc y utilizar "CRUD" que es read update y delete
    def __init__(self,estado:bool,id:int,tarea:str,file) -> None:
        self.id = id
        self.estado = estado
        self.tarea = tarea
        self.file = file
        try:
            self.i = open(self.file, "r+")
        except Exception:
            self.i = open(self.file, "w+")
    
    def read(self):
        return(self.i.readlines())


    def update(self,newest,newid,newtarea):
        self.i.write(newest)
        self.i.write(newid)
        self.i.write(newtarea)

    def delete(self,file):
        pass




