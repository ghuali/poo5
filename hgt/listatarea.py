from hgt.tarea import Tarea

class ListaTareas:
    LIMITCHAR = "|&&|"
    def __init__(self) -> None:
        self.tareaitas = []

    def agregar(self, tarea:Tarea):
        self.tareaitas.append(tarea)
        
# Guardar una los valores de tarea en una lista y utilizar "CRUD" que es read  y delete



    def read(self):
        result = ""
        for tarea in self.tareaitas:
            result += tarea
            if tarea != self.tareaitas[-1]:
                result += self.LIMITCHAR

        return result

    def load(self, data:str):
        tareas = data.split(self.LIMITCHAR)
        for tarea in tareas:
            self.tareaitas.append(tarea)

    def update(self, latarea:Tarea, estado:bool,id:int,tarea:str):
        for x in self.tareaitas:
            if x == latarea:
                x.update(estado,id,tarea)
                break


    def delete(self,tarea:Tarea):
        for x in self.tareaitas:
            if x == tarea:
                x.delete()
                break

    def __str__(self):
        return self.read()
    
    def __len__(self):
        return  self.tareaitas.__len__()
    
    def __getitem__(self, index):
        return self.tareaitas[index]
    
    def __setitem__(self, index, value):
        self.tareaitas[index] = value

    def __delitem__(self, index):
        del self.tareaitas[index]

    def __iter__(self):
        return self.tareaitas.__iter__()
    
    def __next__(self):
        return self.tareaitas.__next__()
    
    def __contains__(self, item):
        return item in self.tareaitas
    
    def __eq__(self, other):
        return self.tareaitas == other.tareaitas
    
    def __ne__(self, other):
        return self.tareaitas != other.tareitas        
