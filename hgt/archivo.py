class Archivo:
    
# Para coger del .txt que guarda la lista de tareas y de eventos
    
    def __init__(self, nombre):
        self.nombre = nombre

    def leer(self):
        try:
            leer = open(self.nombre, 'rt')
        except FileNotFoundError:
            return ''
        with leer:
            return leer.readline()
    

    def escribir(self, contenido):
        try:
            write = open(self.nombre, 'wt')
        except:
            raise Exception('Error')
        
        with write:
            write.write(contenido)
            return True
