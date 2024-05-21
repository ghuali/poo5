from hgt.listatarea import ListaTareas
from hgt.archivo import Archivo
import pytest
import os

FILENAME = 'archivo.txt'
DATA    = 'False,1,"Dibujar un pato"' + ListaTareas.LIMITCHAR + 'True,2,"Matar a Dios"'

@pytest.fixture
def fichero():
    return Archivo(FILENAME)

def test_ficheroLeer(fichero):
    os.remove(FILENAME)
    assert fichero.leer() == ''

def test_ficheroEscribir(fichero):
    assert fichero.escribir(DATA) == True

def test_ficheroLeer2(fichero):
    assert fichero.leer() == DATA

def test_ficheroListaTareas(fichero):
    lista = ListaTareas()
    lista.load(fichero.leer())
    assert lista.read() == DATA