from hgt.listatarea import ListaTareas
import pytest

@pytest.fixture
def lista():
    return ListaTareas()

# Test de la clase ListaAlumnos
def test_listaTareas0(lista):
    assert len(lista) == 0

def test_listaTareas1(lista):
    lista.agregar('False,1,"Dibujar un pato"')
    assert len(lista) == 1

def test_listaTarea2(lista):
    lista.agregar('False,1,"Dibujar un pato"')
    lista.agregar('True,2,"Matar a Dios"')

    assert len(lista) == 2

    assert lista[0] == ('False,1,"Dibujar un pato"')
    assert lista[1] == ('True,2,"Matar a Dios"')

def test_listaTareaDelete(lista):
    lista.agregar('True,3,"Jugar a fortnite"')
    assert lista[0] == 'True,3,"Jugar a fortnite"'

    del lista[0]
    assert len(lista) == 0

    assert 'True,3,"Jugar a fortnite"' not in lista

def test_listaRead(lista):
    lista.agregar('False,1,"Dibujar un pato"')
    lista.agregar('True,2,"Matar a Dios"')

    assert lista.read() == 'False,1,"Dibujar un pato"' + lista.LIMITCHAR + 'True,2,"Matar a Dios"'

def test_listaLoad(lista):
    lista.load('False,1,"Dibujar un pato"' + lista.LIMITCHAR + 'True,2,"Matar a Dios"')
    assert len(lista) == 2

    assert lista[0] == 'False,1,"Dibujar un pato"'
    assert lista[1] == 'True,2,"Matar a Dios"'