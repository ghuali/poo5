
Digitos = ['1','2','3','4','5','6','7','8','9']

class Utilidadstring:
    
    @staticmethod
    def contarDigitos(cadena:str) -> int:
        contador = 0
        for car in range(0,len(cadena)):
            if cadena[car] in Digitos:
                contador += 1

        return contador
    


if __name__ == '__main__':
    print(Utilidadstring.contarDigitos("Le digo hola ella me dice goodbye1"))