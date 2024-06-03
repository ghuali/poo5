import sqlite3

class Db:
    def conectar(name:str)-> sqlite3.Connection:
        return sqlite3.connect(name,isolation_level=None)


    @staticmethod
    def cerras(con: sqlite3.Connection):
        con.close